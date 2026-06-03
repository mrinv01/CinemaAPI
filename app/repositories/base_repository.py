from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, and_
from app.database import async_session_maker


class BaseRepository:
    model = None

    @classmethod
    async def get(cls, entity_id: int):
        async with async_session_maker() as session:
            return await session.get(cls.model, entity_id)

    @classmethod
    async def get_all(cls, *, offset: int = 0, limit: int = 100):
        async with async_session_maker() as session:
            stmt = select(cls.model).offset(offset).limit(limit)
            result = await session.scalars(stmt)
            return result.all()

    @classmethod
    async def create(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance

    @classmethod
    async def update(cls, filter_by, **values):
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    sqlalchemy_update(cls.model)
                    .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                    .values(**values)
                    .execution_options(synchronize_session="fetch")
                )
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result, result.rowcount

    @classmethod
    async def delete(cls, delete_all: bool = False, **filter_by):
        if not delete_all and not filter_by:
            raise ValueError("Необходимо указать хотя бы один параметр для удаления.")

        async with async_session_maker() as session:
            async with session.begin():
                query = sqlalchemy_delete(cls.model).filter_by(**filter_by)
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result.rowcount

    @classmethod
    async def delete_by_ids(cls, ids: list[int]) -> int:
        if not ids:
            raise ValueError("Список ID не может быть пустым.")

        async with async_session_maker() as session:
            async with session.begin():
                stmt = sqlalchemy_delete(cls.model).where(cls.model.id.in_(ids))
                result = await session.execute(stmt)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result.rowcount

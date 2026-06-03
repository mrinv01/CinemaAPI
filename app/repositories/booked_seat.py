from sqlalchemy import select

from app.database import async_session_maker
from app.models import booked_seat
from app.repositories.base import BaseRepository


class BookedSeatRepository(BaseRepository):
    model = booked_seat

    @classmethod
    async def get_by_showtime(cls, showtime_id: int):
        async with async_session_maker() as session:
            stmt = select(booked_seat).where(booked_seat.showtime_id == showtime_id)
            result = await session.scalars(stmt)
            return result.all()

    @classmethod
    async def get_by_seat(cls, seat_id: int):
        async with async_session_maker() as session:
            stmt = select(booked_seat).where(booked_seat.seat_id == seat_id)
            result = await session.scalars(stmt)
            return result.all()

    @classmethod
    async def get_by_showtime_and_seat(cls, showtime_id: int, seat_id: int):
        async with async_session_maker() as session:
            stmt = select(booked_seat).where(
                booked_seat.showtime_id == showtime_id,
                booked_seat.seat_id == seat_id,
            )
            result = await session.scalar(stmt)
            return result

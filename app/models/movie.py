from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk
from sqlalchemy.dialects.postgresql import JSONB

class Movie(Base):
    id: Mapped[int_pk]
    kp_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column( nullable=False)
    alternative_name: Mapped[str] = mapped_column( nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    movie_length: Mapped[int] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column( default=0, nullable=False)
    film_critics: Mapped[int] = mapped_column(default=0, nullable=False)
    good_reviews: Mapped[int] = mapped_column(default=0, nullable=False)
    bad_reviews: Mapped[int] = mapped_column(default=0, nullable=False)
    genres: Mapped[str] = mapped_column(nullable=False)
    countries: Mapped[str] = mapped_column(nullable=False)
    age_rating: Mapped[int] = mapped_column(nullable=False)
    short_description: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    poster: Mapped[str] = mapped_column(nullable=False)
    backdrop: Mapped[str] = mapped_column(nullable=False)
    logo: Mapped[str | None] = mapped_column(nullable=True)
    persons: Mapped[list[dict]] = mapped_column(JSONB, nullable=False)
    trailer: Mapped[str | None] = mapped_column(nullable=True)

    showtimes: Mapped[list["Showtime"]] = relationship(
        back_populates="movie",
        cascade="all, delete-orphan",
    )
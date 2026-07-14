from typing import Optional

from pydantic import Field

from app.schemas.common_schemas import ORMBaseModel, PositiveID


class MovieBase(ORMBaseModel):
    kp_id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=255)
    alternative_name: str = Field(max_length=255)
    type: str = Field(min_length=1, max_length=50)
    year: int = Field(ge=1888)
    movie_length: int = Field(gt=0)
    rating: float = Field(default=0, ge=0, le=10)
    film_critics: int = Field(default=0, ge=0)
    good_reviews: int = Field(default=0, ge=0)
    bad_reviews: int = Field(default=0, ge=0)
    genres: str = Field(min_length=1)
    countries: str = Field(min_length=1)
    age_rating: int = Field(ge=0, le=21)
    short_description: str = Field(min_length=1)
    description: str = Field(min_length=1)
    poster: str = Field(min_length=1)
    backdrop: str = Field(min_length=1)
    logo: Optional[str] = None
    persons: str = Field(min_length=1)
    trailer: Optional[str] = None


class MovieCreate(MovieBase):
   pass


class MovieUpdate(ORMBaseModel):
    kp_id: Optional[int] = Field(default=None, gt=0)
    name: Optional[str] = Field(default=None, min_length=1, max_length=255)
    alternative_name: Optional[str] = Field(default=None, max_length=255)
    type: Optional[str] = Field(default=None, min_length=1, max_length=50)
    year: Optional[int] = Field(default=None, ge=1888)
    movie_length: Optional[int] = Field(default=None, gt=0)
    rating: Optional[float] = Field(default=None, ge=0, le=10)
    film_critics: Optional[int] = Field(default=None, ge=0)
    good_reviews: Optional[int] = Field(default=None, ge=0)
    bad_reviews: Optional[int] = Field(default=None, ge=0)
    genres: Optional[str] = Field(default=None, min_length=1)
    countries: Optional[str] = Field(default=None, min_length=1)
    age_rating: Optional[int] = Field(default=None, ge=0, le=21)
    short_description: Optional[str] = Field(default=None, min_length=1)
    description: Optional[str] = Field(default=None, min_length=1)
    poster: Optional[str] = Field(default=None, min_length=1)
    backdrop: Optional[str] = Field(default=None, min_length=1)
    logo: Optional[str] = None
    persons: Optional[str] = Field(default=None, min_length=1)
    trailer: Optional[str] = None


class MovieRead(MovieBase):
    id: PositiveID

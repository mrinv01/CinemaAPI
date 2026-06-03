from datetime import datetime
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class ORMBaseModel(BaseModel):
    """Base class for schemas built from SQLAlchemy ORM objects."""

    model_config = ConfigDict(from_attributes=True)


PositiveID = Annotated[int, Field(gt=0)]
Money = Annotated[Decimal, Field(ge=0, max_digits=10, decimal_places=2)]
Timestamp = datetime

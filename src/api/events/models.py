"""Define the models and schemas for handling events in the API.

Includes:
- EventModel: The database model for events.
- EventCreateSchema: Schema for creating new events.
- EventUpdateSchema: Schema for updating existing events.
- EventListSchema: Schema for listing events.
"""

from __future__ import annotations

from sqlmodel import Field, SQLModel
from timescaledb import TimescaleModel


class EventModel(TimescaleModel, table=True):
    """Schema representing an event.

    Attributes
    ----------
    name : str | None
        The name of the event.
    description : str | None
        The description of the event.
    created_at : datetime
        The timestamp when the event was created.
    updated_at : datetime
        The timestamp when the event was last updated.

    """

    # id field is inherited from TimescaleModel (int | None)
    name: str = Field(index=True, nullable=False)
    description: str | None = Field(default=None)

    __chunk_time_interval__ = "INTERVAL 1 days"
    __drop_after__ = "INTERVAL 30 days"


class EventCreateSchema(SQLModel):
    """Schema for creating a new event.

    Attributes
    ----------
    name : str
        The name of the event.

    """

    name: str


class EventUpdateSchema(SQLModel):
    """Schema for updating an existing event.

    Attributes
    ----------
    description : str
        The new description of the event.

    """

    description: str


class EventListSchema(SQLModel):
    """Schema representing a list of events.

    Attributes
    ----------
    results : list[EventModel]
        The list of event objects.
    count : int
        The total number of events.

    """

    results: list[EventModel]
    count: int

"""Define the models and schemas for handling events in the API.

Includes:
- EventModel: The database model for events.
- EventCreateSchema: Schema for creating new events.
- EventUpdateSchema: Schema for updating existing events.
- EventListSchema: Schema for listing events.
"""

from __future__ import annotations

import uuid

from sqlmodel import Field, SQLModel


class EventModel(SQLModel, table=True):
    """Schema representing an event.

    Attributes
    ----------
    id : uuid.UUID
        The unique identifier of the event.

    """

    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)


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

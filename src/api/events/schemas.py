"""Schemas for event-related API endpoints.

This module defines Pydantic models for representing event data and lists of events.
"""

from __future__ import annotations

from pydantic import BaseModel


class EventSchema(BaseModel):
    """Schema representing an event.

    Attributes
    ----------
    id : int
        The unique identifier of the event.

    """

    id: int
    name: str | None = None
    description: str | None = None


class EventCreateSchema(BaseModel):
    """Schema for creating a new event.

    Attributes
    ----------
    name : str
        The name of the event.

    """

    name: str


class EventUpdateSchema(BaseModel):
    """Schema for updating an existing event.

    Attributes
    ----------
    description : str
        The new description of the event.

    """

    description: str


class EventListSchema(BaseModel):
    """Schema representing a list of events.

    Attributes
    ----------
    results : list[EventSchema]
        The list of event objects.
    count : int
        The total number of events.

    """

    results: list[EventSchema]
    count: int

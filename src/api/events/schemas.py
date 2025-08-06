"""Schemas for event-related API endpoints.

This module defines Pydantic models for representing event data and lists of events.
"""

from pydantic import BaseModel


class EventSchema(BaseModel):
    """Schema representing an event.

    Attributes
    ----------
    id : int
        The unique identifier of the event.

    """

    id: int


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

"""Routing for event-related API endpoints.

This module defines FastAPI routes for listing and retrieving events.
"""

from fastapi import APIRouter

from .schemas import EventListSchema, EventSchema

router = APIRouter()


@router.get("")
@router.get("/")
def read_events() -> EventListSchema:
    """Retrieve a list of all events.

    Returns
    -------
    EventListSchema
        A schema containing a list of event objects and the total count.

    """
    return EventListSchema(
        results=[
            EventSchema(id=1),
            EventSchema(id=2),
            EventSchema(id=3),
        ],
        count=3,
    )

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    """Retrieve a single event by its ID.

    Parameters
    ----------
    event_id : int
        The unique identifier of the event to retrieve.

    Returns
    -------
    EventSchema
        The event object corresponding to the given ID.

    """
    return EventSchema(id=event_id)

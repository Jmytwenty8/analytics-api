"""Routing for event-related API endpoints.

This module defines FastAPI routes for listing and retrieving events.
"""

from fastapi import APIRouter

from .models import EventCreateSchema, EventListSchema, EventModel

router = APIRouter()


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
            EventModel(id="1"),
            EventModel(id="2"),
            EventModel(id="3"),
        ],
        count=3,
    )


@router.get("/{event_id}")
def get_event(event_id: str) -> EventModel:
    """Retrieve a single event by its ID.

    Parameters
    ----------
    event_id : int
        The unique identifier of the event to retrieve.

    Returns
    -------
    EventModel
        The event object corresponding to the given ID.

    """
    return EventModel(id=event_id)


@router.post("/")
def create_event(payload: EventCreateSchema) -> EventModel:
    """Create a new event.

    Parameters
    ----------
    payload : EventCreateSchema
        The data for the new event.

    Returns
    -------
    EventModel
        The created event object.

    """
    # In a real application, you would save the event to a database here.
    data = payload.model_dump()
    return EventModel(id="42", **data)

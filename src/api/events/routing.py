"""Routing for event-related API endpoints.

This module defines FastAPI routes for listing and retrieving events.
"""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from api.db.session import get_session

from .models import EventCreateSchema, EventListSchema, EventModel

router = APIRouter()


@router.get("/")
def read_events(session: Annotated[Session, Depends(get_session)]) -> EventListSchema:
    """Retrieve a list of all events.

    Returns
    -------
    EventListSchema
        A schema containing a list of event objects and the total count.

    """
    statement = select(EventModel)
    results = session.exec(statement).all()
    return EventListSchema(
        results=list(results),
        count=len(results),
    )


@router.get("/{event_id}")
def get_event(event_id: uuid.UUID, session: Annotated[Session, Depends(get_session)]) -> EventModel:
    """Retrieve a single event by its ID.

    Parameters
    ----------
    event_id : uuid.UUID
        The unique identifier of the event to retrieve.
    session : Session
        The database session used for interacting with the database.

    Returns
    -------
    EventModel
        The event object corresponding to the given ID.

    """
    statement = select(EventModel).where(EventModel.id == event_id)

    return session.exec(statement).one()


@router.post("/")
def create_event(payload: EventCreateSchema, session: Annotated[Session, Depends(get_session)]) -> EventModel:
    """Create a new event.

    Parameters
    ----------
    payload : EventCreateSchema
        The data for the new event.
    session : Session
        The database session used for interacting with the database.

    Returns
    -------
    EventModel
        The created event object.

    """
    # In a real application, you would save the event to a database here.
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

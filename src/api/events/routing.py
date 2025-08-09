"""Routing for event-related API endpoints.

This module defines FastAPI routes for listing and retrieving events.
"""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from api.db.session import get_session

from .models import EventCreateSchema, EventListSchema, EventModel, EventUpdateSchema

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
    result = session.exec(statement).first()

    if not result:
        raise HTTPException(status_code=404, detail="Event not found")

    return result


@router.put("/{event_id}")
def update_event(
    event_id: uuid.UUID,
    payload: EventUpdateSchema,
    session: Annotated[Session, Depends(get_session)],
) -> EventModel:
    """Update an existing event.

    Parameters
    ----------
    event_id : uuid.UUID
        The unique identifier of the event to update.
    payload : EventUpdateSchema
        The new data for the event.
    session : Session
        The database session used for interacting with the database.

    Returns
    -------
    EventModel
        The updated event object.

    """
    statement = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(statement).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")

    for key, value in payload.model_dump().items():
        setattr(obj, key, value)

    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.delete("/{event_id}")
def delete_event(event_id: uuid.UUID, session: Annotated[Session, Depends(get_session)]) -> None:
    """Delete an event by its ID.

    Parameters
    ----------
    event_id : uuid.UUID
        The unique identifier of the event to delete.
    session : Session
        The database session used for interacting with the database.

    """
    statement = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(statement).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")

    session.delete(obj)
    session.commit()


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

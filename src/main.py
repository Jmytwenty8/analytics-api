"""Main entry point for the FastAPI REST API application.

This module initializes the FastAPI app, includes routers, and defines basic endpoints.
"""

from __future__ import annotations

from fastapi import FastAPI

from api.events import router as events_router

app = FastAPI(redirect_slashes=False)
app.include_router(events_router, prefix="/api/events", tags=["events"])


@app.get("/")
def read_root() -> dict:
    """Root endpoint returning a simple greeting.

    Returns
    -------
    dict
        A dictionary with a greeting message.

    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict:
    """Retrieve an item by its ID with an optional query parameter.

    Parameters
    ----------
    item_id : int
        The ID of the item to retrieve.
    q : str, optional
        An optional query string.

    Returns
    -------
    dict
        A dictionary containing the item ID, query parameter, and a message.

    """
    return {"item_id": item_id, "q": q, "message": "This is a sample FastAPI application."}

@app.get("/health-check")
def health_check() -> dict:
    """Health check endpoint.

    Returns
    -------
    dict
        A dictionary containing the health status of the application.

    """
    return {"status": "ok", "message": "The application is running smoothly."}

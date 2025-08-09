"""Main entry point for the FastAPI REST API application.

This module initializes the FastAPI app, includes routers, and defines basic endpoints.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError as FastAPIRequestValidationError
from fastapi.responses import JSONResponse

from api.db.session import init_db
from api.events import router as events_router

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan events."""
    init_db()
    yield
    # cleanup


app = FastAPI(
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
    openapi_url="/openapi.json",  # OpenAPI schema
    title="Analytics REST API",
    description="A REST API for managing analytics data.",
    version="1.0.0",
    lifespan=lifespan,
)
app.include_router(events_router, prefix="/api/events", tags=["events"])


@app.exception_handler(FastAPIRequestValidationError)
async def validation_exception_handler(_request: Request, exc: FastAPIRequestValidationError) -> JSONResponse:
    """Handle FastAPI request validation errors and return a JSON response.

    Parameters
    ----------
    request : Request
        The incoming HTTP request.
        The incoming HTTP request.
    exc : FastAPIRequestValidationError
        The validation error raised by FastAPI.

    Returns
    -------
    JSONResponse
        A JSON response with a 422 status code and error details.

    """
    # Extract the first error message, or provide a default
    error_msg = exc.errors()[0]["msg"] if exc.errors() else "Invalid input"
    return JSONResponse(
        status_code=422,
        content={"detail": error_msg},
    )


@app.get("/health-check")
def health_check() -> dict:
    """Health check endpoint.

    Returns
    -------
    dict
        A dictionary containing the health status of the application.

    """
    return {"status": "ok", "message": "The application is running smoothly."}

"""API package initialization and router collection."""
import importlib
import pkgutil

from fastapi import APIRouter


def get_all_routers() -> list[APIRouter]:
    """Retrieve all API routers dynamically from the routes package.

    This function scans the `app.api.routes` package for Python modules
    that define a `router` variable of type `APIRouter` and returns them.

    Returns:
        List[APIRouter]: List of APIRouter instances found in the routes package.

    """
    from app.api import routes

    routers: list[APIRouter] = []

    for _, module_name, is_pkg in pkgutil.iter_modules(routes.__path__):
        if is_pkg:
            continue

        module = importlib.import_module(f"{routes.__name__}.{module_name}")
        if hasattr(module, "router"):
            routers.append(module.router)

    return routers
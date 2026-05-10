"""Command-line interface (CLI) entry point for managing the application."""
import typer

app = typer.Typer()


@app.command()
def start(port: int = typer.Option(8000, "--port", "-p", help="Port to listen on"),
          host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host to listen on"),
          reload: bool | None = typer.Option(False, "--reload", "-r",
                                             help="Reload the server on file changes")):
    """Start the FastAPI server.

    Starts the FastAPI server with the specified host, port, and reload option.

    Args:
    port (int, optional): Port to listen on. Defaults to 8000.
    host (str, optional): Host to bind to. Defaults to "0.0.0.0".
    reload (bool, optional): Reload the server on file changes. Defaults to False

    """
    import uvicorn

    from app.main import app as fastapi_app

    typer.echo(f"Starting FastAPI server on http://{host}:{port}")
    uvicorn.run(fastapi_app, host=host, port=port, reload=reload)


if __name__ == "__main__":
    app()

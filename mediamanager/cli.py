from typing import Optional

import typer

from mediamanager import __app_name__, __version__

app = typer.Typer(name=__app_name__)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

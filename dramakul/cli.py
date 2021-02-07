import typer

from dramakul import name as package_name, description as package_description
from dramakul.gui import watch_gui, download_gui, config_gui

app = typer.Typer()


@app.callback()
def callback(log_level: str = typer.Option("info", help="Specifies the log level of the program (info, warning, debug, error).")):
    f"""
    {package_name} : {package_description}
    """


@app.command()
def watch(context: typer.Context):
    """
    Watch command.
    """
    watch_gui()


@app.command()
def download(context: typer.Context):
    """
    Download command.
    """
    download_gui()


@app.command()
def config(context: typer.Context):
    """
    Config command.
    """
    config_gui()

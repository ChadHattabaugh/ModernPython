#Third party 
import click
import requests

# System
import textwrap

# Local
from . import __version__, wikipedia

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of wikipeda",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language): 
    """The Modern python template"""
    data = wikipedia.random_page(language=language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))


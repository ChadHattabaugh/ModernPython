# src/modern_python/console.py
import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """The modern python project"""
    click.echo("Hello World!")
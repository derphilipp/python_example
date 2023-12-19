"""Command-line interface."""
import sys

import click
import ui


@click.command()
@click.version_option()
def main() -> None:
    """Python Example."""


if __name__ == "__main__":
    ui.main(sys.argv)

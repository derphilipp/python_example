"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Python Example."""


if __name__ == "__main__":
    main(prog_name="python_example")  # pragma: no cover

# Standard library imports.
import argparse

# Personal imports.
from backend.console import Console


# Entry point for when the package is ran as a script.
def main() -> None:
    # Create the parser.
    parser = argparse.ArgumentParser()
    # Add the --console argument.
    parser.add_argument('--console',
                        action='store_true',
                        help='Launch the geocalc console')
    # Parse the arguments.
    args = parser.parse_args()

    if args.console:
        # If --console was passed, launch the console interface.
        console = Console()
        console.run()

        # If no arguments were passed, run the GUI here.


if __name__ == '__main__':
    main()

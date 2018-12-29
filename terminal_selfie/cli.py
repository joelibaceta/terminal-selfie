"""This module contains a CLI interface"""

from . import selfier


def main():
    import argparse

    CLI_DESC = "It is a simple tool to take a selfie using terminal"
    EPILOG = ("\033[1;37mThanks for trying!\033[0m")

    PARSER = argparse.ArgumentParser(prog='terminal_selfie', description=CLI_DESC, epilog=EPILOG)
    ARGS = PARSER.parse_args()

    selfier.take_selfie()


if __name__ == '__main__':
    main()
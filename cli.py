"""This module contains a CLI interface"""
import main

def main():
    import argparse

    CLI_DESC = "It is a simple tool to take a selfie using terminal"
    EPILOG = ("\033[1;37mThanks for trying!\033[0m")

    PARSER = argparse.ArgumentParser(prog='terminal-selfie', description=CLI_DESC, epilog=EPILOG)
    ARGS = PARSER.parse_args()

    main.take_selfie()


if __name__ == '__main__':
    main()
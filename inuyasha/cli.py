from argparse import ArgumentParser
import sys

from inuyasha import __description__, __version__
from inuyasha.scaffold import main_scaffold


def main():
    # 命令行处理程序入口
    arg_parser = ArgumentParser(description=__description__)
    arg_parser.add_argument("-V", "--version", dest="version", action="store_true", help="show version")
    arg_parser.add_argument("-P", "--project", dest="version", action="store_true", help="Create an inuyasha test project")

    if sys.argv[1] in ["-V", "--version"]:
        print(f"{__version__}")
    elif sys.argv[1] in ["-h", "--help"]:
        arg_parser.print_help()
    elif sys.argv[1] in ["-P", "--project"]:
        arg_parser.print_help()
        main_scaffold()
    else:
        print(f"Unknown command: {sys.argv[1]}")
        arg_parser.print_help()
        sys.exit(0)

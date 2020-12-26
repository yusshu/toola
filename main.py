from cli.dispatcher import dispatch_command
from command.help_cmd import show_help
from command.base64_cmd import *
from command.exit_cmd import *


def main() -> None:

    log_separator()
    log('$a    Tool-A $f- $rUtility for me. Just a practice in Python')
    log_separator()
    show_help()
    log_separator()

    while True:
        command = prompt()
        dispatch_command(command)


if __name__ == '__main__':
    main()

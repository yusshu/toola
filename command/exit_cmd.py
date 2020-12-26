from cli.command import command
from cli.log import log


@command(['exit', 'quit', 'q'], "D-Don't leave me, O-Onee-chan")
def exit_command():
    log('$aBye!')
    exit(0)

from cli.log import *
from cli.command import *


@command(['help', '?'], 'Shows all the commands, and its usage')
def show_help():
    for name, spec in commands.items():
        log(f' $c| $a{name} $f- $r{spec.description}')
        if len(spec.aliases) > 0:
            log(f' $c\\\\_ $fAliases: [{", ".join(spec.aliases)}]')

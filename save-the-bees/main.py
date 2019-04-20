import click
import os
import crayons
from pathlib import Path
from bees_shell import SaveTheBees

@click.group()
@click.version_option()
def cli():
    '''
      Want to know how to save the bees?
      Open up the shell environment with the command:

      save-the-bees shell

      Enjoy!
    '''
    pass

@cli.command('setup')
    '''
      :setup:
      Setup
    '''
def setup():
    pass

@cli.command('shell')
def shell():
    SaveTheBees().cmdloop()


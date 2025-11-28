import sys
import importlib
import click


@click.group()
def cli():
    pass

@cli.command()
@click.argument('year', type=int)
@click.argument('day', type=int)
def init(year, day):
    from aoc.init import Init
    Init(year, day)


@cli.command()
@click.argument('year', type=int)
@click.argument('day')
@click.argument('input_suffix', required=False, default=None)
def run(year, day, input_suffix):
    module = importlib.import_module(f'solution.{year}.{day}')

    solution = module.Solution(input_suffix)
    solution.run()

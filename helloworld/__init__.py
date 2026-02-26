import click

@click.group()
def cli():
    pass

@cli.command()
def world():
    click.echo('Hello World!')

@cli.command()
def user():
    click.echo('Hello User!')


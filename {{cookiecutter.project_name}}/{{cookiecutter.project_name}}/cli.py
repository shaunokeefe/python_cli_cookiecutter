import click

from {{cookiecutter.project_name}} import example


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--option',
              default=10, type=click.IntRange(0, None),
              help="this is an example of an option")
@click.option('--flag', default=False, type=bool, is_flag=True,
              help="this is an example of a flag")
def run(path, option, flag):
    example()
    print "ran the command"


if __name__ == '__main__':
    run()

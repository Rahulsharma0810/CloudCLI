import click
from src.vm_instance import vm as vmops


@click.group()
def entry_point():
    """ CLI EntryPoint """
    pass


entry_point.add_command(vmops.list_instances_by_filter)

if __name__ == "__main__":
    entry_point()

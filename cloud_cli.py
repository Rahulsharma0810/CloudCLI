import click
from src.vm_instance.vm import ls_vm


@click.group()
def entry_point():
    pass

@entry_point.command()
@click.option('--proj', required=True, type=str,
              help='GCP Project ID', default = "")
@click.option('--filt', required=True, type=str,
              help='Name or regex of instance name', defualt = "")
# def ls_vm(proj, filt):
#     """List instances Based on filters"""
def list_vm(proj, filt):
    ls_vm(proj, filt)

entry_point.add_command(ls_vm)

if __name__ == "__main__":
    entry_point(default_map = {
        "list_vm":{
            "proj":
        }
    })

#coming in 2 minutes you can take control
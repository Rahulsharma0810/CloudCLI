# from googleapiclient import discovery
# from oauth2client.client import GoogleCredentials
import click
from src.list_instances_by_filter import list_instances_by_filter
from src.list_instances_by_filter import install_cmd


# @click.command()
# @click.option('linst', required=True, type=str,
#               help='GCP Project ID')

# @click.option('--project', required=True, type=str,
#               help='GCP Project ID')
# @click.option('--filter', required=True, type=str,
#               help='Name or regex of instance name')
# def main(project, filter):
#     list_instances_by_filter(project, filter)


# if __name__ == '__main__':
#     main()
# ListInstancesByFilter("wise-arch-107501",
#                       "(name eq 'honeywell')")
# PROJECT = "functionize-system"
# FILTER = "(name eq 'mysql-connector-demo')"


cli = click.CommandCollection(sources=[install_cmd])

if __name__ == '__main__':
    cli()
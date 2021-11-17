import json
from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import click
from src.list_instances_by_filter import list_instances_by_filter
credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@click.command()
@click.option('--project',
              help='GCP Project ID')
@click.option('--filter',
              help='Name or regex of instance name')
@click.option('--yes', is_flag=True, callback=abort_if_false, expose_value=False,
              prompt='Are you sure you want to stop mentioned Vms?')
def main(project, filter):
    list_instances_by_filter(project, filter)
    stopVM(project)


def stopVM(project):
    with open('resource.json', 'r') as File:
        response = json.load(File)
        File.close()
        for instances in response['response']:
            zone = instances['zone'].split('/')[-1]
            name = instances['name']
            print(name)
            print(zone)
            request = service.instances().stop(project=project, zone=zone, instance=name)
            response = request.execute()


if __name__ == '__main__':
    main()

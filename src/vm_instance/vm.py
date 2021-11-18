import json
from pprint import pprint
from googleapiclient import discovery
import click
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)


@click.command()
def ls_vm(proj, filt):
    """
    To list instances from a GCP project based on filters.
    ---

    Parameters:
        project: str: Project ID from GCP
        filter: str: Name or regex of instances

    Return: None
    """
    request = service.instances().aggregatedList(
        project=proj, filter=filt)
    with open('resource.json', 'w', encoding='utf-8') as file:
        # Create a key to initialize a dictionary of instances.
        json_key = {'response': []}
        while request is not None:
            response = request.execute()
            instance = response.get('items', {})
            for instance in instance.values():
                for instances in instance.get('instances', []):
                    json_key.get('response').append(instances)
            # Appending previous response on next request
            request = service.instances().aggregatedList_next(
                previous_request=request, previous_response=response)
        json.dump(json_key, file)


# proj = 'wise-arch-107501'
# filt = "name eq '^longlive-honeywell-proxy.*'"

# if __name__ == '__main__':
#     ls_vm(proj, filt)

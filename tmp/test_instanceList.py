from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'wise-arch-107501'  # TODO: Update placeholder value.

request = service.instances().aggregatedList(project=project)
while request is not None:
    response = request.execute()

    for name, instances_scoped_list in response['items'].items():
        # TODO: Change code below to process each (name, instances_scoped_list) item:
        pprint((name, instances_scoped_list))

    request = service.instances().aggregatedList_next(
        previous_request=request, previous_response=response)

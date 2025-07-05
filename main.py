from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()
subscription_id = "subscription-id"

client = ResourceManagementClient(credential, subscription_id)

for group in client.resource_groups.list():
    print(group.name)

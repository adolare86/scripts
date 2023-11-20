



import botocore.session
import requests

bucket_name='coderbytechallengesandbox'


# Specify the public bucket URL
bucket_url = 'https://coderbytechallengesandbox.s3.amazonaws.com/'

# Initialize a botocore session without credentials
session = botocore.session.Session()

# Create a client with the session
client = session.create_client('s3', config=botocore.client.Config(signature_version=botocore.UNSIGNED))

# List objects in the bucket
response = requests.get(bucket_url)

if response.status_code == 200:
    # Parse the XML response to get object names
    from xml.etree import ElementTree
    root = ElementTree.fromstring(response.content)
    for contents in root.iter('{http://s3.amazonaws.com/doc/2006-03-01/}Key'):
        print(contents.text)
else:
    print(f"Error: Unable to access the bucket. Status code {response.status_code}")

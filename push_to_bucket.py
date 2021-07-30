# pip install --upgrade google-cloud-storage
from google.cloud import storage


def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

def upload_to_bucket():
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('123-temp-bucket')
    object_file = bucket.blob('python-audio.mp3')
    # Name of the object in local file system
    object_file.upload_from_filename('audio.mp3')

if __name__ == '__main__':
    # list_buckets()
    upload_to_bucket()
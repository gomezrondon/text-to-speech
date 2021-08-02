# pip install --upgrade google-cloud-storage
from google.cloud import storage
import os


def list_buckets():
    """Lists all buckets."""
    storage_client = storage.Client()
    buckets = storage_client.list_buckets()
    for bucket in buckets:
        print(bucket.name)


def download_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    try:
        os.mkdir('tmp')
    except(FileExistsError):
        pass
    blob.download_to_filename("/tmp/"+destination_file_name)

    print(
        "Blob {} downloaded to file path {}. successfully ".format(
            source_blob_name, destination_file_name
        )
    )

def upload_to_bucket(bucket_name, source_file_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    object_file = bucket.blob(destination_file_name)
    # Name of the object in local file system
    object_file.upload_from_filename("/tmp/"+source_file_name)

if __name__ == '__main__':
    # list_buckets()
    # upload_to_bucket('<project-id>','audio.mp3' , 'python-audio.mp3' )
    download_file('<project-id>', 'python-text.txt', 'text.txt')
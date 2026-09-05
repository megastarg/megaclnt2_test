import os
import time
import threading
import boto3
import traceback
import urllib3
from dotenv import load_dotenv

# Suppress InsecureRequestWarning caused by verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables from .env file, overriding any existing bash variables
load_dotenv(override=True)

# Configuration: Expecting these environment variables in Heroku or .env
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
AWS_ENDPOINT_URL = os.environ.get('AWS_ENDPOINT_URL') # Used for free S3 alternatives like Cloudflare R2 or Backblaze B2

FILES_TO_SYNC = [
    'mydatabase.db',
    'saved_and_blocked.txt',
    'blocked.txt',
    'main2links.txt',
    'cookie.txt',
    'checkout.txt',
    'donotsave.txt'
]

FOLDERS_TO_SYNC = [
    'M_appliences_HKPK',
    'W_appliences_HKPK'
]

from botocore.config import Config

def get_s3_client():
    if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY or not AWS_BUCKET_NAME:
        return None
    kwargs = {
        'aws_access_key_id': AWS_ACCESS_KEY_ID,
        'aws_secret_access_key': AWS_SECRET_ACCESS_KEY,
        'region_name': AWS_REGION,
        'config': Config(signature_version='s3v4', s3={'addressing_style': 'virtual'}),
        'verify': False
    }
    if AWS_ENDPOINT_URL:
        kwargs['endpoint_url'] = AWS_ENDPOINT_URL
    return boto3.client('s3', **kwargs)

def upload_file(s3_client, file_path, object_name=None):
    if object_name is None:
        object_name = file_path
    if os.path.exists(file_path):
        try:
            print(f"Uploading {file_path}...")
            s3_client.upload_file(file_path, AWS_BUCKET_NAME, object_name)
            print(f"Successfully uploaded {file_path}!")
        except Exception as e:
            print(f"Error uploading {file_path}: {e}")

def sync_job():
    while True:
        try:
            s3_client = get_s3_client()
            if s3_client:
                print("Starting S3 Sync...")
                # Sync specific files
                for file_name in FILES_TO_SYNC:
                    upload_file(s3_client, file_name)
                
                # Sync folders
                for folder in FOLDERS_TO_SYNC:
                    if os.path.exists(folder) and os.path.isdir(folder):
                        for root, _, files in os.walk(folder):
                            for file in files:
                                local_path = os.path.join(root, file)
                                # The S3 object name should include the folder structure
                                object_name = local_path.replace(os.sep, '/') 
                                upload_file(s3_client, local_path, object_name)
                print("S3 Sync Completed.")
            else:
                print("AWS credentials not configured. Skipping S3 sync.")
        except Exception as e:
            print("Exception in S3 Sync Thread:")
            traceback.print_exc()
        
        # Wait 5 minutes before syncing again
        time.sleep(300)

def start_sync_thread():
    thread = threading.Thread(target=sync_job, daemon=True)
    thread.start()
    print("S3 background sync thread started.")

if __name__ == '__main__':
    # For testing manually
    sync_job()

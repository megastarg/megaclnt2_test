import os
import re
import requests
import psutil
import time
import boto3
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv(override=True)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
AWS_ENDPOINT_URL = os.environ.get('AWS_ENDPOINT_URL')

def seconds_elapsed():
    return time.time() - psutil.boot_time()

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds

def download(name):
    s3_downloaded = False
    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_BUCKET_NAME:
        try:
            from botocore.config import Config
            kwargs = {
                'aws_access_key_id': AWS_ACCESS_KEY_ID,
                'aws_secret_access_key': AWS_SECRET_ACCESS_KEY,
                'region_name': AWS_REGION,
                'config': Config(signature_version='s3v4', s3={'addressing_style': 'virtual'}),
                'verify': False
            }
            if AWS_ENDPOINT_URL:
                kwargs['endpoint_url'] = AWS_ENDPOINT_URL
            s3_client = boto3.client('s3', **kwargs)
            s3_client.download_file(AWS_BUCKET_NAME, name, name)
            print(f"Successfully downloaded {name} from S3.")
            s3_downloaded = True
        except Exception as e:
            print(f"Failed to download {name} from S3: {e}. Falling back to default URL...")

    if not s3_downloaded:
        url = "http://oracle1.lalkothi.tech/amz/flipkart/"+name
        try:
            response = requests.get(url).content
            if response != None and len(response)!=0 and response.find(b"/lander")==-1 and response.find(b"DOCTYPE")==-1:
                with open(name, 'wb') as f:
                    f.write(response)
                print(f"Successfully downloaded {name} from URL.")
        except Exception as e:
            print(f"Failed to download {name} from URL: {e}")
        
def start():
    download("mydatabase.db")
    download("saved_and_blocked.txt")
    download("blocked.txt")
    download("main2links.txt")
    download("cookie.txt")
    download("checkout.txt")
    download("donotsave.txt")
    print("All files downloaded")
if __name__ == '__main__':
    start()
#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.s3_bucket import S3Bucket
import random
import string


def generate_random_bucket_name(prefix="my-bucket-", length=8):
    """Generate a random bucket name with a prefix."""
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{prefix}{random_suffix}"


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Initialize AWS provider
        AwsProvider(self, "AWS", region="us-east-1")

        # Generate a random bucket name
        bucket_name = generate_random_bucket_name()

        # Create the S3 bucket with the random name
        S3Bucket(self, "my_bucket",
                bucket=bucket_name,
                tags={
                    "Environment": "dev",
                    "ManagedBy": "cdktf"
                })


app = App()
MyStack(app, "learn-cdktf-docker")

app.synth()

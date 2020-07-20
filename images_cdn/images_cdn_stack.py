from aws_cdk import core
from aws_cdk import aws_s3 as s3


class ImagesCdnStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, bucket_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        s3.Bucket(self, "images-cdn", bucket_name=bucket_name)

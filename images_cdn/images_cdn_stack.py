from aws_cdk import aws_s3 as s3
from aws_cdk import aws_cloudfront as cf
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_certificatemanager as acm
from aws_cdk import Stack
from constructs import Construct

class ImagesCdnStack(Stack):

    def __init__(self, scope: Construct, id: str, bucket_name: str, cf_id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, 
                            id=id,
                            bucket_name=bucket_name,
                            public_read_access=False,
                            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                            website_index_document="index.html"
                            )
        s3.BlockPublicAccess()
        cert = acm.Certificate(self, 
                        "Cert", 
                        domain_name=bucket_name,
                        validation=acm.CertificateValidation.from_dns()
                        )
        oai = cf.OriginAccessIdentity(self, "OriginAccess", comment=f"Origin Access Identity for the S3 bucket {bucket_name}")
        viewer_cert = cf.ViewerCertificate.from_acm_certificate(cert, 
                        aliases=[bucket_name] 
        )
        cf.CloudFrontWebDistribution(self, 
                                    id=cf_id,
                                    price_class=cf.PriceClass.PRICE_CLASS_200,
                                    origin_configs=[
                                        cf.SourceConfiguration(
                                            behaviors=[
                                                cf.Behavior(
                                                    is_default_behavior=True)
                                            ],
                                            s3_origin_source=cf.S3OriginConfig(
                                                s3_bucket_source=bucket,
                                                origin_access_identity=oai,
                                            ),
                                        )
                                    ],
                                    viewer_certificate=viewer_cert
        )
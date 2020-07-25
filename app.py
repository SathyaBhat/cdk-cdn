#!/usr/bin/env python3

from aws_cdk import core

from images_cdn.images_cdn_stack import ImagesCdnStack


app = core.App()
cdn = ImagesCdnStack(app, 
                    "images-cdn", 
                    env=core.Environment(region='us-east-1'),
                    bucket_name="images.sbhat.me")
core.Tag.add(cdn, "used_for", "Blog images")
core.Tag.add(cdn, "created_by", "sathyabhat")
app.synth()

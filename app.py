#!/usr/bin/env python3

from aws_cdk import core

from images_cdn.images_cdn_stack import ImagesCdnStack


app = core.App()
ImagesCdnStack(app, "images-cdn")

app.synth()

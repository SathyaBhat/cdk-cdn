#!/usr/bin/env python3

from aws_cdk import core

from images_cdn.images_cdn_stack import ImagesCdnStack


app = core.App()
images_cdn = ImagesCdnStack(app, 
                    id="images-cdn",
                    env=core.Environment(region='us-east-1'),
                    bucket_name="images.sbhat.me",
                    cf_id="cf_cdn")
core.Tag.add(images_cdn, "used_for", "Blog images")
core.Tag.add(images_cdn, "created_by", "sathyabhat")

cpgweds_cdn = ImagesCdnStack(app, 
                    id="cpgweds", 
                    env=core.Environment(region='us-east-1'),
                    bucket_name="joshenoy.weds.sathyabh.at",
                    cf_id="cpgweds_cf")
core.Tag.add(cpgweds_cdn, "used_for", "cpgweds.com site")
core.Tag.add(cpgweds_cdn, "created_by", "sathyabhat")

app.synth()

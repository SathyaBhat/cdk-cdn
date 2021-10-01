#!/usr/bin/env python3

from aws_cdk import core

from images_cdn.images_cdn_stack import ImagesCdnStack


app = core.App()
images_cdn = ImagesCdnStack(app, 
                    id="images-cdn",
                    env=core.Environment(region='us-east-1'),
                    bucket_name="images.sbhat.me",
                    cf_id="cf_cdn")
core.Tags.of(images_cdn).add("used_for", "Blog images")
core.Tags.of(images_cdn).add("created_by", "sathyabhat")

cpgweds_cdn = ImagesCdnStack(app, 
                    id="cpgweds", 
                    env=core.Environment(region='us-east-1'),
                    bucket_name="joshenoy.weds.sathyabh.at",
                    cf_id="cpgweds_cf")
core.Tags.of(cpgweds_cdn).add("used_for", "cpgweds.com site")
core.Tags.of(cpgweds_cdn).add("created_by", "sathyabhat")

all_images_cdn = ImagesCdnStack(app, 
                    id="all-images",
                    env=core.Environment(region='us-east-1'),
                    bucket_name="i.sathyabh.at",
                    cf_id="cf_cdn")

core.Tags.of(all_images_cdn).add("used_for", "Blog images")
core.Tags.of(all_images_cdn).add("created_by", "sathyabhat")


app.synth()

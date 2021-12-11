import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="images_cdn",
    version="1.0.0",

    description="Creates a S3 Bucket and CloudFront distribution with the bucket as origin to act as a CDN" ,
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Sathyajith Bhat",

    package_dir={"": "images_cdn"},
    packages=setuptools.find_packages(where="images_cdn"),

    install_requires=[
        "aws-cdk-lib==2.1.0",
        "constructs==10.0.9",
    ],
    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)

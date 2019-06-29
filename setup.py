import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PiHole-Panel",
    version="0.0.1",
    author="Dale Osm",
    author_email="webmster@daleosm.com",
    description="Python/GTK3 based Pi-hole Dashboard for stats and more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daleosm/PiHole-Panel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

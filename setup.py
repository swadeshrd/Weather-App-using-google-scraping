import os

from setuptools import find_packages, setup


def get_requirement(f):
    return open(os.path.join("requirements", f)).read().splitlines()


setup(
    name="weather-app",
    version="V1",
    author="Swadesh Ranjan Dash",
    description="weather app using bs4 package and google weather scrapping",
    packages=find_packages(where="weatherapp"),
    package_dir={"": "weatherapp"},
    include_package_data=True,
    install_requires=get_requirement("app.txt"),
)

from setuptools import find_packages, setup

setup(
    name="slack_components",
    install_requires=["pydantic>=1.10.6"],
    packages=find_packages(include=['slack_components']),
    version='0.1.0',
    description='This Library lets you build complex slack message for the slack API at ease',
    author='Quentin Delignon'
)
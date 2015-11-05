from pip.req import parse_requirements

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

links = []
requires = []
for item in parse_requirements('requirements.txt'):
    if item.url:
        links.append(str(item.url))
    if item.req:
        requires.append(str(item.req))


setup(
    name='ESengine',
    version="0.0.1",
    url='https://github.com/catholabs/ESengine',
    license='CATHO LICENSE',
    author="Catholabs",
    author_email="catholabs@catho.com",
    description='Elasticsearch models inspired on mongo engine ORM',
    long_description="Elasticsearch models inspired on mongo engine ORM",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    dependency_links=links
)
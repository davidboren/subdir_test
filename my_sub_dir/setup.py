try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fairapis',
    'author': 'fair',
    'url': 'https://www.github.com/davidboren/subdir_test',
    'download_url': 'https://www.github.com/davidboren/subdir_test',
    'author_email': 'marshallb@fair.com',
    'version': '0.0.0',
    'install_requires': [],
    'packages': find_packages(exclude=('tests', 'docs')),
    'scripts': [],
    'name': 'my_sub_dir'
}

setup(**config)

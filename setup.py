from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('requirements.txt') as requirements_file:
    REQUIREMENTS = requirements_file.read().split("\n")

setup_args = dict(
    name='plugp100',
    version='2.0-beta',
    description='Controller for TP-Link Tapo P100',
    long_description_content_type="text/markdown",
    long_description=README,
    license='GPL3',
    packages=find_packages(),
    author='@petretiandrea',
    author_email='petretiandrea@gmail.com',
    keywords=['Tapo', 'P100'],
    url='https://github.com/petretiandrea/plugp100',
    download_url='https://github.com/petretiandrea/plugp100'
)

install_requires = REQUIREMENTS

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
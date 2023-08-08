from setuptools import setup, find_packages
import re

# https://stackoverflow.com/a/7071358/353278
VERSIONFILE="snafu/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
if mo := re.search(VSRE, verstrline, re.M):
    verstr = mo[1]
else:
    raise RuntimeError(f"Unable to find version string in {VERSIONFILE}.")

setup(name='pysnafu',
      version=verstr,
      description='Generate semantic networks from fluency data',
      url='https://github.com/AusterweilLab/snafu-py',
      author='The Austerweil Lab at UW-Madison',
      author_email='jeffzemla@gmail.com',
      keywords=['fluency', 'networks','psychology','recall'],
      packages=['snafu'],
      include_package_data=True,
      install_requires=['numpy','networkx>=2.4','more_itertools'],
      python_requires='>=3.5',
      zip_safe=False,
      classifiers=[
            'Programming Language :: Python :: 3.5'
      ]
      )

import re
from distutils.core import setup

with open("requirements.txt", "r") as req:
    requirements = req.readlines()

version = ''
with open('mari/__init__.py') as f:
version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(name='mari',
      author='UVClay',
      author_email='clay@uvclay.com',
      version=version,
      license='WTFPL',
      description='a mostly useless bot for my clan',
      install_requires=req,
      packages=['mari'])
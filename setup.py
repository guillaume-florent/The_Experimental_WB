from setuptools import setup
import os

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                            "freecad", "the_experimental_workbench", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='The_Experimental_WB',
      version=str(__version__),
      packages=['freecad',
                'freecad.the_experimental_workbench'],
      maintainer="GF",
      maintainer_email="someemail@someprovider.com",
      url="https://github.com/guillaume-florent/The_Experimental_WB",
      description="template for a freecad extensions, installable with pip",
      install_requires=['numpy'],  # should be satisfied by FreeCAD's system dependencies already
      include_package_data=True)

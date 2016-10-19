from setuptools import setup

setup(name='brightway2-conda-installer',
      packages=['brightway2_conda_installer'],
      version='0.0.1',
      author="Adrian Haas",
      license=open('LICENSE.txt').read(),
      description='Installation of brightway2 and all of its dependencies in a new anaconda environment.',
      entry_points={
          'console_scripts': [
              'create_new_brightway2_env = brightway2_conda_installer.__main__:create_new_brightway2_env',
              'bw_env = brightway2_conda_installer.__main__:create_new_brightway2_env'
          ]
      },
      )
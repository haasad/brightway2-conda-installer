import sys
import subprocess
import tempfile

if not ('continuum' in sys.version.lower() or 'conda' in sys.version.lower()):
	raise RuntimeError('This script needs to be executed with the anaconda python distribution.')


def create_new_brightway2_env():

	name_str = 'name: {}\n'
	channels_str = "channels:\n\t- defaults\n\t- haasad\n\t- conda-forge\n\t"
	python_str = '\ndependencies:\n\t- python={}'

	conda_dependencies = ['pypardiso',
	                      'jupyter',
	                      'matplotlib',
	                      'flask',
	                      'lxml',
	                      'requests',
	                      'nose',
	                      'docopt',
	                      'xlsxwriter',
	                      'xlrd',
	                      'unidecode',
	                      'appdirs',
	                      'psutil',
	                      'unicodecsv',
	                      'wrapt',
	                      'whoosh',
						  'peewee',
						  'asteval',
						  'future',
						  'monotonic',
						  'fasteners']

	conda_dependencies_str = '\n\t- ' + '\n\t- '.join(conda_dependencies)

	pip_dependencies = ['brightway2',
	                    'bw2analyzer',
	                    'bw2calc',
	                    'bw2data',
	                    'bw2io',
	                    'bw2parameters',
	                    'bw2speedups',
	                    'eight']

	pip_dependencies_str = '\n\t- pip:\n\t\t- '+'\n\t\t- '.join(pip_dependencies)

	yaml_str = name_str + channels_str + python_str + conda_dependencies_str + pip_dependencies_str
	yaml_str = yaml_str.replace('\t', '    ')

	temp_yaml_file = tempfile.mktemp(suffix='.yml')

	env_name = input('Enter the name of your new environment: ')
	if not env_name:
		env_name = 'bw'
	py_ver = input('Enter the python version, one of (2.7, 3.4, 3.5): ')
	if not py_ver in {'2.7', '3.4', '3.5'}:
		py_ver = '3.5'

	with open(temp_yaml_file, 'w') as f:
	    f.write(yaml_str.format(env_name, py_ver))

	subprocess.call(['conda-env', 'create', '-f', temp_yaml_file])


if __name__ == "__main__":
    create_new_brightway2_env()

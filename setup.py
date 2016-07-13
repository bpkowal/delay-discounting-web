try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
	'description' : 'Delay Discounting',
	'author' : 'Benjamin Kowal',
	'url' : 'in progress...setting up account',
	'download_url' : 'https://github.com/bpkowal/delay-discounting-web',
	'author_email' : 'benjaminkowal9@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'scripts' : [],
	'name' : 'delay-discounting-web'
}

setup(**config)

#for additional requirements see Learn Python the Hard Way online text

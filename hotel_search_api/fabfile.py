import time
from fabric.api import local, settings, prefix


MODULES = ['scraper.scraperapi', 'hotel_search.hotel_search_server']

def test():
    for i in MODULES:
	with prefix('source env/bin/activate'):
        	#local('which python2')
        	local('python -m %s &' % i)	
    time.sleep(1)  # Waiting for services to complete start
    local('source env/bin/activate; python -m tests.scraperapi_test')
    for i in MODULES:
	with settings(warn_only=True):
        	local("kill -9 `ps -ax | grep -v grep | grep %s | awk '{print $1}'`" % i)

def setup():
    local('virtualenv env')
    local('source env/bin/activate; pip install -r requirements.txt')

def cleanup():
    local('rm -rf env')
    local("find . -name '*.pyc' -delete")

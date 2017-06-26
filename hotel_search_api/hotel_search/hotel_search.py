import json

from tornado import gen
from tornado.httpclient import AsyncHTTPClient


class hotelSearch(object):
    def __init__(self, config):
        self.config = config
	#print self.config
        self.providers = self.config['providers']
	#print self.providers
        self.urls = ['http://localhost:9000/scrapers/{}'.format(p) for p in self.providers]
	print self.urls

    @gen.coroutine
    def fetch_results(self):
	httpclient = AsyncHTTPClient()
        responses = yield [httpclient.fetch(u) for u in self.urls]
        responses = [json.loads(r.body.decode('utf-8', 'ignore')) for r in responses]
        sorted_results = yield self.merge_results(responses)
        raise gen.Return(json.dumps({"results": sorted_results}))

    @gen.coroutine
    def merge_results(self, responses):
        responses = [r['results'] for r in responses]
        # flatten the list
        responses = [r for provider_list in responses for r in provider_list]
	#print responses
        raise gen.Return(sorted(responses, key=lambda x: x['ecstasy']))

import os
import sys
import logging
from tornado import gen, ioloop, web

from hotel_search import hotelSearch

log = logging.getLogger('hotel-search')
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
log.setLevel(logging.DEBUG)

servers = { 'providers': ['orbitz','expedia','priceline','travelocity','hilton'],'port': 8000,'scraper_hostname':'localhost','scraper_port':9000}


class hotelSearchHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        serv = hotelSearch(servers)
        results = yield serv.fetch_results()
        self.write(str(results))


ROUTES = [(r"/hotels/search", hotelSearchHandler)]


def run():
    port = servers['port']
    application = web.Application(ROUTES, debug=True)
    application.listen(port)
    log.info("Started server at port {}".format(port))
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()

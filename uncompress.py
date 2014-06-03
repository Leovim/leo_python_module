# _*_coding:utf8_*_

from StringIO import StringIO
import urllib2
import gzip

class ContentEncodingProcessor(urllib2.BaseHandler):
    """A handler to add gzip capabilities to urllib2 requests """

    def uncompress_gzip(self, url):
        """ This checks if the content is gzipped and decompresses it. """
        request = urllib2.Request(url)
        request.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(request)
        if response.info().get('Content-Encoding') == 'gzip':
            print "the page is compressed."
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj = buf)
            data = f.read()
            return data
        else:
            print "the page is uncompressed."
            return response.read()

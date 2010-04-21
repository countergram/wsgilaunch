# Copyright 2010 Jason Stitt
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from optparse import OptionParser
from sys import exit, modules

# TODO add HTTP server
FLUP_SERVERS = ["ajp", "ajp_fork", "fcgi", "fcgi_fork", "scgi", "scgi_fork"]
PASTE_SERVERS = ['http']
SERVERS = PASTE_SERVERS + FLUP_SERVERS

def run(app, default_host='localhost', default_port=8080):
    usage = "usage: %prog <servertype> [options]\n"
    usage += "Server types: %s" % (", ".join(SERVERS))
    parser= OptionParser(usage=usage)
    parser.add_option('-H', '--host', dest='host', default=default_host,
        help='Hostname (default: %s)' % (default_host), metavar='HOSTNAME')
    parser.add_option('-p', '--port', dest='port', default=default_port,
        help='Port (default: %s)' % (default_port), metavar='PORT')
    # TODO
    # parser.add_option('-q', '--quiet', dest='quiet', default=False,
        # action="store_true", help='Suppress stdout and stderr')
    (options, args) = parser.parse_args()
    if len(args) != 1 or args[0] not in SERVERS:
        parser.print_usage()
        exit(1)
        
    try:
        port = int(options.port)
    except:
        print "Port must be an integer."
        exit(1)
    
    run_method = args[0]
    if run_method in FLUP_SERVERS:
        module_name = 'flup.server.' + run_method
        __import__(module_name)
        modules[module_name].WSGIServer(app, bindAddress=(options.host, port)).run()
        
    elif run_method == 'http':
        from paste import httpserver
        httpserver.serve(app, host=options.host, port=port, use_threadpool=True)
        
    else:
        parser.print_usage()
        exit(1)

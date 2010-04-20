from optparse import OptionParser
from sys import exit, modules

FLUP_SERVERS = ["ajp", "ajp_fork", "fcgi", "fcgi_fork", "scgi", "scgi_fork"]
SERVERS = FLUP_SERVERS

def run(app, default_host='localhost', default_port=8080):
    usage = "usage: %prog <servertype> [options]\n"
    usage += "Server types: %s" % (", ".join(SERVERS))
    parser= OptionParser(usage=usage)
    parser.add_option('-H', '--host', dest='host', default=default_host,
        help='Hostname (default: %s)' % (default_host), metavar='HOSTNAME')
    parser.add_option('-p', '--port', dest='port', default=default_port,
        help='Port (default: %s)' % (default_port), metavar='PORT')
    # parser.add_option('-q', '--quiet', dest='quiet', default=False,
        # action="store_true", help='Suppress stdout and stderr')
    (options, args) = parser.parse_args()
    args = ['fcgi']
    if len(args) != 1 or args[0] not in SERVERS:
        parser.print_usage()
        exit(1)
        
    try:
        port = int(options.port)
    except:
        print "Port must be an integer."
        exit(1)
    
    run_method = args[0]
    try:
        module_name = 'flup.server.' + run_method
        __import__(module_name)
        modules[module_name].WSGIServer(app, bindAddress=(options.host, port)).run()
        
    except ImportError:
        parser.print_usage()
        exit(1)
    
if __name__ == '__main__':
    def myapp(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return ['Hello World!\n']
    
    run(myapp)
    
`wsgilaunch`_ is a Python package that provides an easy way to run WSGI
web applications from the command line in a number of modes, including:

 * HTTP (threaded, paste.httpserver)
 * FastCGI (threaded or forked, flup)
 * SCGI (threaded or forked, flup)
 * AJP (threaded or forked, flup)

Small example of use
====================

The following executable script runs a WSGI app::

    from your.module import main_app
    from wsgilaunch import run
    if __name__ == '__main__':
        run(main_app)
        
The executable wsgilaunch_sample script is also installed with the package.
You can use it to see command-line usage and experiment with host and port
options. It contains a hello-world WSGI app.
    
Docs
====

Documentation is shipped with the source distribution and is available at
the `wsgilaunch`_ web page.

.. _`wsgilaunch`: http://countergram.com/open-source/wsgilaunch/

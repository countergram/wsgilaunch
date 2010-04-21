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

from distutils.core import setup

longdesc = """\
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
"""

VERSION = "0.1.0"

setup(
    name="wsgilaunch",
    version=VERSION,
    description="Command-line WSGI server launcher supporting http, fcgi, scgi",
    long_description=longdesc,
    author="Jason Stitt",
    author_email="js@jasonstitt.com",
    url="http://countergram.com/open-source/wsgilaunch/",
    download_url="http://cloud.github.com/downloads/countergram/wsgilaunch/wsgilaunch-%s.tar.gz" % VERSION,
    packages=['wsgilaunch'],
    provides=["wsgilaunch"],
    requires=[
        'flup (>= 1.0.0)',
        'Paste (>= 1.7.3)',
        ],
    scripts=[
        'scripts/wsgilaunch_sample',
        ],
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Topic :: Utilities',
          ],
    )


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
import os.path

longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

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


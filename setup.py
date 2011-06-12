from distutils.core import setup

setup(
    name = "lastfm-advanced-charts",
    version = "0.1",
    author = "Imanol Eizaguirre",
    author_email = "imanol@imanol.cc",
    description = "Accumulated scrobblings of a given LastFM account graph generator",
    download_url = "https://download.github.com/imanoleizaguirre-lastfm-advanced-charts-ef1ca10.tar.gz",
    url = "https://github.com/imanoleizaguirre/lastfm-advanced-charts",
    packages= ['lastfm-advanced-charts'],
    long_description="""\
LastFM Advanced Charts generates a customizable graph with the accumulated
scrobblings of a given lastfm account using Google Chart API.
""",
    classifiers=['Development Status :: 2 - Pre-Alpha',
                'Environment :: Web Environment',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Utilities']
)
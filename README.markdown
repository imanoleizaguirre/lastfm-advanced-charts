# LastFM Advanced Charts

LastFM Advanced Charts generates a customizable graph with the accumulated
scrobblings of a given lastfm account using [Google Chart API](http://code.google.com/apis/chart/)
during your lastfm account's timeline.

The main purpose of thus library is to play a little bit withlast.fm's API,
and building up graphs and stats that are really helpful for me and I haven't 
found at [build.last.fm](http://build.last.fm) other services...

This project was originaly developed for Google App Engine, and it's been migrated
to a stand-alone library.

# Dependencies

This library has some requirements listed above:

- [GChartWrapper](http://code.google.com/p/google-chartwrapper/)
- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
- [A LastFM API key](http://www.lastfm.es/api)

# Examples

This is a  [graph](http://chart.apis.google.com/chart?chxt=x,y&chd=t:0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.0,12.0,12.0,12.0,12.0,17.0,18.0,18.0,20.0,20.0,20.0,21.0,21.0,21.0,21.0,22.0,22.0,23.0,23.0,25.0,26.0,27.0,27.0,27.0,28.0,28.0,30.0,30.0,30.0,31.0,31.0,33.0,33.0,33.0,33.0,34.0,34.0,35.0,35.0,36.0,37.0,37.0,38.0,38.0,38.0,39.0,39.0,40.0,41.0,42.0,43.0,43.0,43.0,43.0,44.0,44.0,44.0,44.0,44.0,45.0,47.0,52.0,52.0,52.0,53.0,53.0,54.0,54.0,54.0,55.0,56.0,57.0,58.0,59.0,59.0,59.0,60.0,60.0,61.0,61.0,63.0,68.0,73.0,73.0,74.0,75.0,76.0,77.0,79.0,81.0,81.0,82.0,82.0,83.0,83.0,83.0,83.0,83.0,83.0,84.0,84.0,84.0,84.0,84.0,84.0,84.0,84.0,84.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,88.0,89.0,89.0,89.0,89.0,89.0,90.0,90.0,90.0,90.0,90.0,90.0,91.0,91.0,92.0,92.0,92.0,93.0,94.0,95.0,95.0,95.0,95.0,96.0,97.0,97.0,97.0,97.0,97.0,97.0,97.0,97.0,97.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,100.0,100.0&chg=2.0,10.0,1.0,2.0&chco=0077cc&chm=B,e6f2fa,0,0,0&chs=1000x300&cht=ls&chxl=1:|0|378|757|1212|1515|1893|2277|2657|3029|0:|Aug+06|Jan+09|May+11&chls=2.0,1.0,0.0) for the user _xalernita_ and the band _Ladytron_. More examples can be found at USAGE file.

# Future Plans
- Propper packaging
- Propper documentation
- Better examples
- Tests
- Use [lxml](http://lxml.de/) instead of BeautifulSoup
- Support for more than one band stats per graph


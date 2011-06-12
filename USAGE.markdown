# Basic Usage

You need to define your lastfm api key and api secret at charts.py:

- LASTFM_API_KEY = 'your_api_key'
- LASTFM_SECRET = 'your_api_secret'

Once you have done this, you have to give a username and a band's name to
query lastfm's api, and search through your scroblings historic timeline,
by using this two methods:

- getDates(user): This method will get your weekly scroblings data. You need
                this information for using the next method.

- getArtistsGraph(artist, user, dates): This method will get the number of
                scroblings per week and will add to the total.
                
- getCharts(artist_graph, dates): This method will get the chart image url

You have to keep in mind that if your lastfm's account has a lot of
scrobling during time (ie: a lot of weeks since you registered the
account), the reading process may be quite slow.

You may also want to query your scroblings in a certain range of time,
for example, the last three months. In this case, you can use 
getDates_weeks(user, 12) for the data information instead of getDates().


## Example

This example will generate a graph for the number of scroblings from
the user _xalernita_ for the band _Eels_ for the last 3 months.

dates = getDates_weeks(u'xalernita', 12)

artist_graph = getArtistsGraph(u'Eels', 'xalernita', dates)

rs = getCharts(artist_graph, dates)


The result of this would be this [image](http://chart.apis.google.com/chart?chxt=x,y&chd=t:0.0,15.0,57.0,85.0,86.0,86.0,86.0,88.0,91.0,91.0,97.0,97.0,100.0&chg=2.0,10.0,1.0,2.0&chco=0077cc&chm=B,e6f2fa,0,0,0&chs=1000x300&cht=ls&chxl=1:|0|12|24|38|48|60|72|84|96|0:|Feb+11|Apr+11|May+11&chls=2.0,1.0,0.0
)


Another example, for the user _xalernita_ and the band _Ladytron_ for the entire
account's timeline, would be [this](http://chart.apis.google.com/chart?chxt=x,y&chd=t:0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11.0,12.0,12.0,12.0,12.0,17.0,18.0,18.0,20.0,20.0,20.0,21.0,21.0,21.0,21.0,22.0,22.0,23.0,23.0,25.0,26.0,27.0,27.0,27.0,28.0,28.0,30.0,30.0,30.0,31.0,31.0,33.0,33.0,33.0,33.0,34.0,34.0,35.0,35.0,36.0,37.0,37.0,38.0,38.0,38.0,39.0,39.0,40.0,41.0,42.0,43.0,43.0,43.0,43.0,44.0,44.0,44.0,44.0,44.0,45.0,47.0,52.0,52.0,52.0,53.0,53.0,54.0,54.0,54.0,55.0,56.0,57.0,58.0,59.0,59.0,59.0,60.0,60.0,61.0,61.0,63.0,68.0,73.0,73.0,74.0,75.0,76.0,77.0,79.0,81.0,81.0,82.0,82.0,83.0,83.0,83.0,83.0,83.0,83.0,84.0,84.0,84.0,84.0,84.0,84.0,84.0,84.0,84.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,85.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,86.0,88.0,89.0,89.0,89.0,89.0,89.0,90.0,90.0,90.0,90.0,90.0,90.0,91.0,91.0,92.0,92.0,92.0,93.0,94.0,95.0,95.0,95.0,95.0,96.0,97.0,97.0,97.0,97.0,97.0,97.0,97.0,97.0,97.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,98.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,99.0,100.0,100.0&chg=2.0,10.0,1.0,2.0&chco=0077cc&chm=B,e6f2fa,0,0,0&chs=1000x300&cht=ls&chxl=1:|0|378|757|1212|1515|1893|2277|2657|3029|0:|Aug+06|Jan+09|May+11&chls=2.0,1.0,0.0)
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

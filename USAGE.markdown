# Basic Usage

You need to define your lastfm api key and api secret at charts.py:

LASTFM_API_KEY = 'your_api_key'
LASTFM_SECRET = 'your_api_secret'

Once you have done this, you have to give a username and a band's name to
query lastfm's api, and search through your scroblings historic timeline,
by using this two methods:

getDates(user): This method will get your weekly scroblings data. You need
                this information for using the next method.

getArtistsGraph(artist, user, dates): This method will get the number of
                scroblings per week and will add to the total.
                
getCharts(artist_graph, dates): This method will get the chart image url

You have to keep in mind that if your lastfm's account has a lot of
scrobling during time (ie: a lot of weeks since you registered the
account), the reading process may be quite slow.

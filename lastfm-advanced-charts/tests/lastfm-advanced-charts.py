# encoding: utf-8

#from urllib import urlopen
import logging
from urllib import urlopen
from lib.BeautifulSoup import BeautifulSoup

LASTFM_API_KEY = 'your_api_key'
LASTFM_SECRET = 'your_api_secret'

def prepare(dates, limite):
    """
    Prepares data for the urlopen
    """
    longitud = len(dates)
    a1 = longitud % limite
    a2 = longitud / limite
    total = a2
    if (a1 !=0):
        a3 = longitud - a2*limite
        total+=1
    return total

def getDates(user):
    """
    Obtains given user's weekly charts data
    """
    url_dates = u'http://ws.audioscrobbler.com/2.0/?method=user.getweeklychartlist&user='+user+'&api_key='+settings.LASTFM_API_KEY
    f = urlopen(url_dates)
    soup = BeautifulSoup(f)
    f.close()
    chart = soup.findAll('chart')
    dates = []

    for c in chart:
        dates.append([c['from'],c['to']])

    return dates

def getDates_weeks(user,weeks=52):
    dates = getDates(user)
    longitud = len(dates)
    if (longitud<=weeks):
        inicio = 0
    else:
        inicio = longitud-weeks

    return dates[inicio:longitud]

def getArtistsGraph(artist,user,dates):
    """
    Obtains scrobblings for the given band
    """
    soup = None

    #g1 = artist.decode('utf-8').lower()
    g1 = artist.lower()
    a1 = {0:0}
    i = 0

    for elem in dates:
        i = i+1
        a1[i] = a1[i-1]

        nfrom = elem[0]
        nto = elem[1]
        url_chart = u'http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user='+user+'&from='+nfrom+'&to='+nto+'&api_key='+settings.LASTFM_API_KEY
        f = urlopen(url_chart)
        soup = BeautifulSoup(f.read())
        f.close()
        aux = soup.findAll({'name':True})
        aux2 = soup.findAll({'playcount':True})

        for elem in range(len(aux)):
            if (aux[elem].renderContents().decode('utf-8').lower() == g1):
                a1[i] = int(a1[i-1]) + int(aux2[elem].renderContents().decode('utf-8'))
                break
    return a1

def getImg(artist,how_many):
    #Fallan los artistas con espacios

    url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getimages&artist='+artist+'&limit='+str(how_many)+'&order=popularity&api_key='+settings.LASTFM_API_KEY
    img = []
    aux = []

    try:
        f = urlopen(url)
        soup = BeautifulSoup(f.read())
        f.close()

        aux = soup.findAll('size')
    except Exception, e:
        print 'getImg Exception: '+str(e)

    for c in aux:
        if (c['name'] == u'largesquare'):
            img.append(c.renderContents())

    return img

def getArtistsGraph2(g1,user,a1,dates,indice):

    soup = None
    a1[0] = 0
    m = indice
    i = 0

    for elem in dates:
        i = i+1
        m = m+1

        nfrom = elem[0]
        nto = elem[1]
        url_chart = u'http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user='+user+'&from='+nfrom+'&to='+nto+'&api_key='+settings.LASTFM_API_KEY

        try:
            f = urlopen(url_chart)
            soup = BeautifulSoup(f.read())
            f.close()
        except Exception, e:
            print 'getArtistGraph Exception 1: '+str(e)

        aux = soup.findAll({'name':True})
        aux2 = soup.findAll({'playcount':True})

        try:
            for elem in range(len(aux)):
                if (aux[elem].renderContents().decode('utf-8') == g1.decode('utf-8')):
                    a1[m] = int(a1[m-1]) + int(aux2[elem].renderContents().decode('utf-8'))
                try:
                    a1[m]
                except:
                    a1[m] = a1[m-1]

        except Exception, e:
            logging.error(u'getArtistGraph Exception 2: %s' % str(e))
    return a1


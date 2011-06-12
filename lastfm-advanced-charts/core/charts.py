# encoding: utf-8

import logging

from urllib import urlopen
from BeautifulSoup import BeautifulSoup

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
    if a1 != 0:
        #a3 = longitud - a2 * limite
        total += 1
    return total


def getDates(user):
    """
    Obtains given user's weekly charts data
    """
    url_dates = u'http://ws.audioscrobbler.com/2.0/?method=user.getweeklychartlist&user=%s&api_key=%s' % (user, LASTFM_API_KEY)
    f = urlopen(url_dates)
    soup = BeautifulSoup(f)
    f.close()
    chart = soup.findAll('chart')
    dates = []

    for c in chart:
        logging.info(u'Adding data form week %s to week %s' % (c.get('from'), c.get('to')))
        dates.append([c.get('from'), c.get('to')])

    return dates


def getDates_weeks(user, weeks=52):
    """
    Same as getDates but with a week range
    This range should be added as a param to getDates.url_dates instead of
    reading ALL the weeks data and then cropping the results
    """
    dates = getDates(user)
    longitud = len(dates)
    if longitud <= weeks:
        inicio = 0
    else:
        inicio = longitud - weeks

    return dates[inicio:longitud]


def getArtistsGraph(artist, user, dates):
    """
    Obtains scrobblings for the given band
    """
    soup = None

    #g1 = artist.decode('utf-8').lower()
    g1 = artist.lower()
    a1 = {0: 0}
    i = 0

    for elem in dates:
        i += 1
        a1[i] = a1[i - 1]

        nfrom = elem[0]
        nto = elem[1]
        url_chart = u'http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user=%s&from=%s&to=%s&api_key=%s' % (user, nfrom, nto, LASTFM_API_KEY)
        f = urlopen(url_chart)
        soup = BeautifulSoup(f.read())
        f.close()
        aux = soup.findAll({'name': True})
        aux2 = soup.findAll({'playcount': True})

        for elem in range(len(aux)):
            if (aux[elem].renderContents().decode('utf-8').lower() == g1):
                a1[i] = int(a1[i - 1]) + int(aux2[elem].renderContents().decode('utf-8'))
                break
    return a1


def getImg(artist, how_many):
    """
    Adds an image of the artist to the result set
    """
    url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getimages&artist=%s&limit=%s&order=popularity&api_key=%s' % (artist, how_many, LASTFM_API_KEY)
    img = []
    aux = []

    try:
        f = urlopen(url)
        soup = BeautifulSoup(f.read())
        f.close()

        aux = soup.findAll('size')
    except Exception, e:
        print 'getImg Exception: %s' % e

    for c in aux:
        if (c['name'] == u'largesquare'):
            img.append(c.renderContents())

    return img

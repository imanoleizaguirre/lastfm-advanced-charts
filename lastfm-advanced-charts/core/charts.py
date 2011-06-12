# encoding: utf-8
from time import gmtime
from GChartWrapper import Sparkline


def axis_dates(dates):
    """
    Generate the data for the axis
    """
    rs = []
    for elem in dates:
        rs.append(gmtime(float(elem[1])))
    return rs


def regla3(dato, maximo):
    """
    Generates proportional data
    """
    return (100 * dato) / maximo


def getCharts(d1,
             dates,
             maxvalue,
            color = u'0077CC',
             width = 1000,
             height = 300,
             line_g = 2,
             bg = u'yes',
             bgcolor = u'E6F2FA',
             grid_strong = 1):
    """
    Generates the graph url
    """

    values = d1.values()

    l1 = []
    calendar = {}

    #Dates
    calendar[1] = 'Jan'
    calendar[2] = 'Feb'
    calendar[3] = 'Mar'
    calendar[4] = 'Apr'
    calendar[5] = 'May'
    calendar[6] = 'Jun'
    calendar[7] = 'Jul'
    calendar[8] = 'Aug'
    calendar[9] = 'Sep'
    calendar[10] = 'Oct'
    calendar[11] = 'Nov'
    calendar[12] = 'Dec'
    calendar[2002] = '02'
    calendar[2003] = '03'
    calendar[2004] = '04'
    calendar[2005] = '05'
    calendar[2006] = '06'
    calendar[2007] = '07'
    calendar[2008] = '08'
    calendar[2009] = '09'
    calendar[2010] = '10'
    calendar[2011] = '11'
    calendar[2012] = '12'
    calendar[2013] = '13'
    calendar[2014] = '14'
    calendar[2015] = '15'
    calendar[2016] = '16'
    calendar[2017] = '17'
    calendar[2018] = '18'

    if maxvalue != '':
        topL = int(maxvalue)
    else:
        topL = int(max(values))

    if topL == 0:
        topL = 1

    for elem in values:
        l1.append(regla3(elem, topL))

    inicio1 = dates[0][0]
    med1 = dates[int(round(len(dates) / 2, 0))][0]
    fin1 = dates[len(dates) - 1][1]

    inicio = gmtime(float(inicio1))
    med = gmtime(float(med1))
    fin = gmtime(float(fin1))

    p1 = '%s %s' % (calendar[int(inicio[1])], calendar[int(inicio[0])])
    p2 = '%s %s' % (calendar[int(med[1])], calendar[int(med[0])])
    p3 = '%s %s' % (calendar[int(fin[1])], calendar[int(fin[0])])

    L = Sparkline(l1, encoding=u'text')
    L.grid(2, 10, 1, 2)
    L.color(color)
    L.size(width, height)

    if bg == u'yes':
        L.marker('B', bgcolor, 0, 0, 0)

    L.line(line_g, grid_strong, 0)
    L.axes.type('xy')
    L.axes.label(1, '0',
                        int(round(topL / 8, 0)),
                        int(round(topL / 4, 0)),
                        int(round(topL / 2.5, 0)),
                        int(round(topL / 2.0)),
                        int(round(topL / 1.6, 0)),
                        int(round(topL / 1.33, 0)),
                        int(round(topL / 1.14, 0)), topL)

    L.axes.label(0, p1, p2, p3)

    return L

v__author__ = 'mas'
import psycopg2
import sys
import csv
import math

con = None
""" sample csv row  ['20070501', '2007', '5', '1', '106', '14.5', '10.5', '8.85', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', '0.82', '0.97', 'NaN', '20', 'NaN']"""
try:
    con = psycopg2.connect(database='ccs', user='michael')
    cur = con.cursor()
    cur.execute("DELETE FROM  monitor_nutrients")

except psycopg2.DatabaseError, e:
    print 'Error %.4f' % e
    sys.exit(1)


def float_for_db(f):   # nedbat from bostonpython
    if math.isnan(f):
        return None
    else:
        return f
with open('/home/michael/Desktop/dataworking.csv', 'rb') as csvfile:
    try:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for row in reader:
            # print row
            sampleDate = "%s-%s-%s" % (row[1], row[2], row[3])
            print sampleDate
            stationId = row[4]
            print stationId
            a = float_for_db(float(row[5]))
            b = float_for_db(float(row[6]))
            c = float_for_db(float(row[7]))
            d = float_for_db(float(row[8]))
            e = float_for_db(float(row[9]))
            f = float_for_db(float(row[10]))
            g = float_for_db(float(row[11]))
            h = float_for_db(float(row[12]))
            i = float_for_db(float(row[13]))
            j = float_for_db(float(row[14]))
            k = float_for_db(float(row[15]))
            l = float_for_db(float(row[16]))
            m = float_for_db(float(row[17]))
            n = float_for_db(float(row[18]))
            o = float_for_db(float(row[19]))

            cur.execute("INSERT INTO monitor_nutrients (sample_date, station_id, a, b, c,d,e,f,g,h,i,j,k,l,m,n,o)"
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (sampleDate, stationId, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o))
            con.commit()

            # print sampleDate, stationId, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o

    finally:
        csvfile.close()
        if con:
            con.close()

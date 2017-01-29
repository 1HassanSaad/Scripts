import pygeoip

gi = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')

def printRecord(src,dst):
	srec = gi.record_by_name(src)
	drec = gi.record_by_name(dst)
	if srec:
		s = srec['country_name']
	else:
		s = src

	if drec:
                d = drec['country_name']
        else:
                d = dst

	print "src : %s \t dst : %s" % (s,d)

src = '192.168.1.254'
dst = '173.255.226.98'
printRecord(src,dst)

import pygeoip
gi = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')
def retKML(ip):
	rec = gi.record_by_name(ip)
	try:
		longitude = rec['longitude']
		latitude = rec['latitude']
		kml = "<Placemark>\n<name>%s</name>\n<Point>\n<coordinates>%6f,%6f</coordinates>\n</Point>\n</Placemark>\n" % (ip,longitude,latitude)
		return kml
	except Exception, e:
		return ''

ip1 = "156.212.3.14"
ip2 = "8.8.4.4"

res1 = retKML(ip1)
res2 = retKML(ip2)
header = "<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns='http://www.opengis.net/kml/2.2'>\n<Document>\n"
footer = '</Document>\n</kml>'

final = header + res1 + res2 + footer

fl = open("result.kml" , "w")
fl.write(final)
fl.close()


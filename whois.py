import requests
from bs4 import BeautifulSoup

url = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get("http://" +"who.is/whois/"+url)

soup = BeautifulSoup(r.content,"lxml")

var1 = soup.find_all("div", {"class": "col-md-4 queryResponseBodyKey"}) #first variables
value1 = soup.find_all("div", {"class": "col-md-8 queryResponseBodyValue"}) #first values for the first variables
ns_ip = soup.find_all("div", {"class": "col-md-4 queryResponseBodyValue"}) #name server ip address
var2 = soup.find_all("div", {"class": "col-md-offset-1 col-md-4"}) #second variables
value2 = soup.find_all("div", {"class": "col-md-7"}) #second values for the second values

print "\nRegister Info && Important Dates : \n"

#print the first variables in front of the first values example: "Name=MarkMonitor" etc...
#len(var1) = number of elements in var1
for num in range(0,len(var1)):
	print var1[num].text + "\t" + value1[num].text

print "\nName Servers : \n"

#print the name servers in front of name server ips example: "nameserver1=192.168.1.1" etc...
#replace('\n', '') means that replace every new line with nothing -> to delete any new line in the string to look awesome
#len(value1) = number of elements in value1 , len(ns_ip) = number of elements in ns_ip
#value1[len(value1)-len(ns_ip)+num] = to determine the beginnig of name servers variables "nameserver1 , nameserver2"
#becouse of the value1 class contain both the values of var1 and name servers variable
for num in range(0,len(ns_ip)):
	print value1[len(value1)-len(ns_ip)+num].text.replace('\n', '') + "\t" + ns_ip[num].text.replace('\n', '')
	
print "\nRegister Data : \n"
print "Registrant Contact Information : \n"
count = 0 #counter defination

#print the second variables in front of the second values example: "Name=Domain Administrator" etc...
for num in range(0,len(var2)):
	#problem1: email variable don't have text to show , but have img url only so when email variable come print the the img url and skip the loop
	if var2[num].text == "Email": 
	    print var2[num].text + "\t" + "https://who.is" + value2[num].img['src']
	    continue
	
	#just a small trick to print the Administrative and Technical sentence in the right place
	#those sentences always come after the Name variable
	if var2[num].text == "Name": count=count+1
	if count == 2 and var2[num].text == "Name": print "\nAdministrative Contact Information : \n"
	if count == 3 and var2[num].text == "Name": print "\nTechnical Contact Information : \n"
	
	print var2[num].text + "\t" + value2[num].text
	

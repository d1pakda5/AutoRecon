import os
import optparse
import requests
import re
import dns.resolver
from dns.resolver import NXDOMAIN
import nmap
import time


start = time.time()

parser = optparse.OptionParser() 
parser.add_option("-t","--Host", dest="host", help="Please provide the target", default="true")
parser.add_option("-f","--file", dest="file", help="Please provide the filename", default="true") 

options, args = parser.parse_args() 
hostname = options.host
filename = options.file


def find_from_sublister(target):
	if not hostname:
		parser.error("Please use -h to see the help section.")
	else:
		print "\n\n                                                 [PHRASE: 1]                                                 \n"
		print "\n[!][!]Getting Subdomains from Sublister\n\n"
		try:
			os.chdir("/tools/Sublist3r-master/") #Note: Here you can change the Directory of Sublister tool
			files = os.getcwd()
			
			formate = "sublist3r.py -d " + str(target) + " -o " + str(filename)

			subdomain = os.system(formate) 
			fopen = open(filename, 'r')
			os.chdir("C:/")
			print "\n......................................................................................" 	
			
			return fopen.readlines()
			
		except Exception as e:
			print "\nSomething went wrong"

responsecode = []
responsecode.append(200)
responsecode.append(400)
responsecode.append(401)
responsecode.append(403)
responsecode.append(404)

urls_returning200 = []
urls_returning400 = []
urls_returning401 = []
urls_returning403 = []
urls_returning404 = []

			
for url in find_from_sublister(hostname):
    url = "http://" + url.strip()
    try:
		response = requests.get(url)
		if response.status_code == responsecode[0]:
			urls_returning200.append(url)
		if response.status_code == responsecode[1]:
			urls_returning400.append(url)
		if response.status_code == responsecode[2]:
			urls_returning401.append(url)			
		if response.status_code == responsecode[3]:
			urls_returning403.append(url)
		if response.status_code == responsecode[4]:
			urls_returning404.append(url)
		
		
    except requests.exceptions.RequestException as e:
        print "Can't make the request to this Subdomain {}".format(url)
print "\n                                                 [PHRASE: 2]                                                 \n"
print "\n......................................................................................\n"	
print "\n[!]Greping the url's whose status code are 200\n"
	
for x in urls_returning200:
	print x
	
print "\n......................................................................................\n"	
print "\n[!]Greping the url's whose status code are 400\n"

for x in urls_returning400:
	print x
	
print "\n......................................................................................\n"	
print "\n[!]Greping the url's whose status code are 401\n"	

for x in urls_returning401:
	print x
	
print "\n......................................................................................\n"	
print "\n[!]Greping the url's whose status code are 403\n"

for x in urls_returning403:
	print x
	
print "\n......................................................................................\n"	
print "\n[!]Greping the url's whose status code are 404\n"

for x in urls_returning404:
	print x	
print "\n\n                                                 [PHRASE: 3]                                                 \n"	
print "\n......................................................................................\n"	
print "\n[!]Finding the CNAME's of 404 URL's\n"

for y in urls_returning404:
	req2 = requests.get(y)	
	if req2.status_code == 404:
		
		new_url = y.strip("http://")
		new_url2 = new_url.strip('/')
		
		try:
			
			answers = dns.resolver.query(new_url2, 'CNAME')					
			print '\n[+]query qname:', answers.qname
			for rdata in answers:
				print ' cname target address:', rdata.target
			
		except dns.resolver.NXDOMAIN:
			print "[-]"+ str(new_url2) + '-' + " Invalid domain"
			 
		except dns.resolver.Timeout:
			print str(new_url2) + '-' + " Timed out while resolving"
		except dns.exception.DNSException:
			print "[-]" + str(new_url2) + '-' + " Unhandled exception"
	else:
		print "\n[-]Can't find the CNAME of qname: " + new_url2

def nmapscan():
	new_url = x.strip("http://")
	new_url2 = new_url.strip('/')	

	nm.scan(new_url2, '20-25')
	try:
		for host in nm.all_hosts():
			print "\nHost: {0} ({1})"  .format(host, nm[host].hostname()) 
			print "Host State:  %s" % nm[host].state()
			
		
			for proto in nm[host].all_protocols():
				port = nm[host][proto].keys()
				port.sort()
				print "\nPort      State     Service"
				for ports in port:
					
					print "{0}     {1}    {2}" .format(ports, nm[host][proto][ports]['state'], nm[host][proto][ports]['name'])
	except KeyError as e:
		print"[!] Cannot scan host!: " + new_url2 + "\n"		
print "\n                                                 [PHRASE: 4]                                                 \n\n"		
print "\n......................................................................................\n"

print "\n[!]Finding the Ports stats of 200's URL's \n"
nm = nmap.PortScanner()

for x in urls_returning200:
	nmapscan()
	
	
print "\n......................................................................................\n"
print "\n[!]Finding the Ports stats of 400's URL's \n"

for x in urls_returning400:
	nmapscan()
	
print "\n......................................................................................\n"
print "\n[!]Finding the Ports stats of 401's URL's \n"	

for x in urls_returning401:
	nmapscan()

print "\n......................................................................................\n"
print "\n[!]Finding the Ports stats of 403's URL's \n"		

for x in urls_returning403:
	nmapscan()
	
print "\n......................................................................................\n"
print "\n[!]Finding the Ports stats of 404's URL's \n"	

for x in urls_returning404:
	nmapscan()
	
print "\nThe Overall time taken by this script is : ", time.time()-start , 'seconds'  

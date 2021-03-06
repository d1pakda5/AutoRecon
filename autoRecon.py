import os
import optparse
import requests
import re
import dns.resolver
from dns.resolver import NXDOMAIN
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import time
import socket
import threading
import ftplib
from ftplib import FTP
import Queue
import subprocess
import json





start = time.time()

parser = optparse.OptionParser() 
parser.add_option("-t","--Host", dest="host", help="Please provide the target", default="true")
parser.add_option("-f","--file", dest="file", help="Please provide the filename", default="true") 

options, args = parser.parse_args() 
hostname = options.host
filename = options.file


def main():

	def find_from_sublister(target):
		
		

		print "\n\n                                                 [PHASE: 1]: Starts below                                                 \n\n"
		print "\n[!][!]Getting Subdomains from Sublister\n\n\n\n"
		try:
			os.chdir("C:/tools/Sublist3r-master/") #Note: Here you can change the Directory of Sublister tool
			files = os.getcwd()
				
			formate = "sublist3r.py -d " + str(target) + " -o " + str(filename)

			subdomain = os.system(formate) 
			fopen = open(filename, 'r')
			os.chdir("C:/")
			print "\n......................................................................................" 
			print "\n\n                                                 [PHASE: 2]: Starts below                                                 \n\n"
			print "[!!] Unavailable Subdomains\n"
			
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
	
	



	def urlrequests(ur):
		try:
			
			req = requests.get(ur)
			
			
			if req.status_code == responsecode[0]:
				urls_returning200.append(ur)
				
			if req.status_code == responsecode[1]:
				urls_returning400.append(ur)
				
			if req.status_code == responsecode[2]:
				urls_returning401.append(ur)	
				
			if req.status_code == responsecode[3]:
				urls_returning403.append(ur)
				
			if req.status_code == responsecode[4]:
				urls_returning404.append(ur)
				
		except requests.exceptions.RequestException as e:
			print  ur
		

	newurllist = []

	for x in set(find_from_sublister(hostname)):
		url = x.strip('\n\r')
		newurl = "http://" + url
		newurllist.append(newurl)
		
	with ThreadPoolExecutor(max_workers=20) as pool:
		list(pool.map(urlrequests,newurllist))

		
	print "\n..........................................................................\n"	
	print "\n[!]Finding the Urls's status Code is 200\n"

	for x in set(urls_returning200):
		print "\t"+ x

	#print "\n..........................................................................\n"	
	print "\n\n[!]Finding the Urls's status Code is 400\n"

	for x in set(urls_returning400):
		print "\t"+ x 

	#print "\n..........................................................................\n"	
	print "\n\n[!]Finding the Urls's status Code is 401\n"

	for x in set(urls_returning401):
		print "\t"+ x

	#print "\n..........................................................................\n"	
	print "\n\n[!]Finding the Urls's status Code is 403\n"

	for x in set(urls_returning403):
		print "\t"+ x


	print "\n\n[!]Finding the Urls's status Code is 404\n"

	for x in set(urls_returning404):
		print "\t"+ x
			
	print "\n...............................................................................................\n"	
	print "\n\n                                                 [PHASE: 3]: Starts below                                                \n\n"	
		
	print "\n\n[!]Finding the CNAME's of 404 URL's\n"

	for y in urls_returning404:
		
		new_url = y.replace("http://", "")
		
		
		try:
			
			answers = dns.resolver.query(new_url, 'CNAME')					
			print '\t ' +'\n[+]query qname:', answers.qname
			for rdata in answers:
				print '\t Cname Target Address:', rdata.target
			
		except dns.resolver.NXDOMAIN:
			print "\t " +"\n[-]"+ str(new_url) + '-' + " Invalid domain"
			 
		except dns.resolver.Timeout:
			print "\t " +"\n[-]"+ str(new_url) + '-' + " Timed out while resolving"
		except dns.exception.DNSException:
			print "\t " +"\n[-]"+ str(new_url) + '-' + " Unhandled exception"

	ftpurls = []
	ports = []
	httpurls = []
			
	def connCheck(ip, port):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.settimeout(3)
		try:
			if port == 21:
				result = server.connect((ip, port))  # argument must be a tuple pair of ip address and port
				ftpurls.append(ip)	
				print "\t [+]" + str(port)
						
			elif port == 80:
				result = server.connect((ip, port))  # argument must be a tuple pair of ip address and port
				httpurls.append(ip)
				print "\t [+]" + str(port)
			else:
				result = server.connect((ip, port)) 
				print  "\t [+]" + str(port)
			
				
					
				
			
			
			server.close()
		except Exception as e:
			pass
		
		return	


	def socketscan(y):
		
		mid = time.time()
		newurl = y.replace('http://', '')
		
		portss = 21, 22, 80, 8080, 443, 8443, 3306, 445	
		
		thread  = threading.Thread(group=None, target=connCheck, args=(newurl, int(21)))
		thread1 = threading.Thread(group=None, target=connCheck, args=(newurl, int(22)))
		thread2 = threading.Thread(group=None, target=connCheck, args=(newurl, int(80)))
		thread3 = threading.Thread(group=None, target=connCheck, args=(newurl, int(8080)))
		thread4 = threading.Thread(group=None, target=connCheck, args=(newurl, int(443)))
		thread5 = threading.Thread(group=None, target=connCheck, args=(newurl, int(8443)))
		thread6 = threading.Thread(group=None, target=connCheck, args=(newurl, int(3306)))
		thread7 = threading.Thread(group=None, target=connCheck, args=(newurl, int(445)))
		
		print "\n    [~]Host address: "+ newurl + "\n"
		print "\t List of Open Ports: "
		thread.start()
		time.sleep(0.2)
		thread1.start()
		time.sleep(0.2)
		thread2.start()
		time.sleep(0.2)
		thread3.start()
		time.sleep(0.2)
		thread4.start()
		time.sleep(0.2)
		thread5.start()
		time.sleep(0.2)
		thread6.start()
		time.sleep(0.2)
		thread7.start()
		thread7.join()
		
			


	print  "\n...............................................................................................\n"	

	print "\n\n                                                 [PHASE: 4]: Starts below                                                \n\n"
	print "[!]Finding the Port status of 200 status \n"

	for x in urls_returning200:	
		socketscan(x)
		
	#print "\n..........................................................................\n"
	print "\n[!]Finding the Port status of 400 status \n"

	for x in urls_returning400:	
		socketscan(x)
		
	#print "\n..........................................................................\n"
	print "\n[!]Finding the Port status of 401 status \n"	

	for x in urls_returning401:	
		socketscan(x)
		
	#print "\n..........................................................................\n"
	print "\n[!]Finding the Port status of 403 status \n"

	for x in urls_returning403:	
		socketscan(x)
		
	#print "\n..........................................................................\n"
	print "\n[!]Finding the Port status of 404 status \n"	

	for x in urls_returning404:
		socketscan(x)
	print "\n.........................................................................."
	
	print "\n\n                                                 [PHASE: 5]: Starts below                                                \n\n"
	print "Finding the CMS's, Frameworks, Server of subdomains which have HTTP port open\n"

	def httpurlstates(y):
		try:
			newurl = 'http://'+y
			print 
			result = subprocess.check_output('wad -u '+newurl + ' -f txt')
			print "\n[!]Host: " + newurl + '\n'
			print "\t" + result + '\n'
			
		except Exception as e:
			pass
					
	for x in httpurls:
		httpurlstates(x)
		
	print "\n...............................................................................................\n"
	
	print "\n\n                                                 [PHASE: 6]: Starts below                                                \n\n"
	print "[!]Executing anonymous login one by one on Subdomains which have FTP port open. If any.\n"

	'''
	// this is a code for bruteforcing Only those FTP subdomain which have FTP anonymous login dissallowed

	userandpasslist = ['admin','anonymous', 'password','Password','root1','toor','ftp','abc123','test','test123','test1','webadmin','user','user123','system','admin123','Admin','admin1234','testing','qwerty','testuser','123456','root123','toor123','sysadm','nobody','test2','admin2','root2']

	q = Queue.Queue()

	for username in userandpasslist:
		q.put(username)

	def bruteforftp(victim):
		while True:
			try:
				username = q.get(timeout=1)
			except Queue.Empty:
				return
				
			for paswd in userandpasslist:
				try:	
					s1 = ftplib.FTP(host=victim, user=username, acct =paswd )
					
					login = s1.login()	
					if login == True:
						print "\n[+]Vulnerable FTP allows anonymous login"
				
				except ftplib.all_errors as e:
					print "[-]Login Incorrect with " + "Username: "+ str(username) +" Password: "+ str(paswd)
	'''	
		 
	threads = []
		

	for x in ftpurls:
		
		
		try:
			 
			s =ftplib.FTP(host=x, user='', acct='', timeout=6)
			ss =  s.login()	
			if ss:
				print "\n[+]Vulnerable FTP allows anonymous login. Host:- " + str(x)
			
		except ftplib.all_errors as e:
			print "Host : "+ str(x)
			print "[-]Login Incorrect. Not allowing anonymous login.\n"
	print "\n...............................................................................................\n"
	print "\n\n                                                 [PHASE: 7]: Starts below                                                \n\n"

	print "[!]Finding URL's in Wayback machine\n\n"

	def archiveweb(domain, year):
		url = "https://web.archive.org/__wb/calendarcaptures?url={0}&selected_year={1}" .format(domain, year)
		try:
			
			req = requests.get(url)

			
			for x in json.loads(req.content):
				for y in x:
					for z in y:
						if 'ts' in str(z):
							for url_date in z['ts']:
								urls = "https://web.archive.org/web/{0}/{1}" .format(url_date, domain)
								print "\t" + urls
								
		except requests.exceptions.ConnectionError:
			print "\tWayback Machine doesn't have that page archived. "+ domain +"\n"
		except Exception as e:
			print "\tWayback Machine doesn't have that page archived. "+ domain +"\n"
			
			
	def thrededreqtowaybackmachine(x):
		for year in yearlist:		
			
			t1 = threading.Thread(target = archiveweb, args = (x, year))
			t1.daemon =True
			t1.start()
			
			time.sleep(0.4)
			t1.join()
	
	

	yearlist = '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'	
	print "\t[~]Findind urls in way back machine on 401 urls\n"		


		
	for x in urls_returning401:
		
		thrededreqtowaybackmachine(x)
		print "\n"
		
		
	print "\n...............................................................................................\n"		

	print "\t[~]Findind in machine of 403 staruscode urls\n"	


	for x in urls_returning403:
		
		thrededreqtowaybackmachine(x)
		print "\n"

			
	print "\nThe Overall time taken by this script is : ", time.time()-start , 'seconds'  

if __name__ =='__main__':
	
	main()


	

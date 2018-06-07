# AutoRecon

AutoRecon is a tool which have 4 Phrases.

<b>Phrase no.1:</b> It will found the subdomains through the use of the sublister.

<b>Phrase no.2:</b> It will found the status code of each Subdomains which was found by the sublister and make seperate list of each subdomain with there own Status code. Like seperate list of 200's, 400's, 401's, 403's, 404's status code subdomains.

<b>Phrase no.3:</b> In this phrase the tool will try to find the CNAME's entries of 404's subdomains. NOTE: For this Phrase, the main aim is to  find the SUBDOMAIN TAKE-OVER Vuln.

<b>Phrase no.4:</b> Now in the last phrase, the tool will find the Port status and Services running on each Subdomains port. Note: This tool will focus only on ports between "20-25" for future Upgradation. But you can change it, at line 138.

And it will show you how much time has taken by this script.


# Requirements

1. The main requirement is "Sublist3r tool should be in this defined directory i.e. "/tools/Sublist3r-master/" at line 29.

                                              OR
                                                  
                                You can change according to your directory. # which is the best
                                
2. There are lot of different modules are used, So be sure you have installed all the defined modules properly.


# Usage: 

`C:\>autorecon.py -t domainname.com -f anyfilename.txt`

**Note:** 

-t is for "Target" address and should be in this **domainname.com** format
<br>-f is for "Filename", which is required by this tool. And should be in **.txt** extension.

# Working Environment

Perfectly tested in python 2.7 in Windows 10.

# Questions I used to asked myself.

<h2> Goal </h2>

The main aim for this tool is to Automate things, So that you can focus on other things as well.

<h2> Why I use Sublister</h2>

I use it because It covers mostly all site which we use to reveal the subdomains. So, it gives a bunch of Subdomains.

<h2> What is the use of Phrase-4 (nmap-scanning)</h2>

Off-course it will find the nmap ports of each subdomains in between ports 20-25. So if someone finds that there is a port open named FTP, from the bunch of namy subdomains then it has the high probability that it allows anonymously login, and may be some weak passwords as company may not aware about it because of many subdomains. So it alerts you.

# Feedback

I am extreamly waiting for your feedback about this tool. 

# Contact


[agrawalsmart7](http://twitter.com/agrawalsmart7)


# AutoRecon

AutoRecon is a tool which have 6 Phases.

**Phase 1**: It will find the subdomains through the use of the sublister.

**Phase 2**: It will find the status code of each Subdomain found by the sublister and make seperate list of each subdomain with their respective status code. 

**Phase 3**: In this phase the tool will try to find the CNAME's entries of 404's subdomains. NOTE: For this Phase, the main objective is to check for the SUBDOMAIN TAKE-OVER Vuln.

**Phase 4**: In this phase, through the use of Multithreading, this tool will find the Port status running on each Subdomains. Note: The defined ports are "21, 22, 80, 8080, 443, 8443, 3306, 445". And it will make the two seperate list of URL's which have 21 port open and 80 port open.

**Phase 5**: In this phase the tool will find the *What CMS, Server, Framworks are using in the Subdomains with the help of 'WAD' tool.* https://pypi.org/project/wad/

**Phase 6**: At the end, if there is any FTP open found in "Phase 4", then it will try to get the Anonymous login.






# Requirements

1. The main requirement is "Sublist3r tool should be in this defined directory i.e. "/tools/Sublist3r-master/" at line 29.

                                              OR
                                                  
                                You can change this according to your directory. # which is the best
                                
2. There are lot of different modules are used, So be sure you have installed all the defined modules properly.


# Usage: 

`C:\>pip install requirements.txt`<br>
`C:\>autoRecon.py -t domainname.com -f anyfilename.txt`

**Note:** 

-t is for "Target" address and should be in this **domainname.com** format
<br>-f is for "Filename", which is required by this tool. And should be in **.txt** extension.

# Working Environment

Perfectly tested in python 2.7 in Windows 10.

# Demo Video

[Demovideo](http://agrawalsmart7.com/demo.mp4)

# Questions I used to asked myself.

<h2> Goal </h2>

The main aim for this tool is to Automate things, So that you can focus on other things as well.

<h2> Why I use Sublister</h2>

I use it because It covers mostly all site which we use to reveal the subdomains. So, it gives a bunch of Subdomains.

<h2> What is the use of Phase-4 (nmap-scanning)</h2>

Off-course it will find the nmap ports of each subdomains. So if someone finds that there is a port open named FTP, from the bunch of namy subdomains then it has the high probability that it allows anonymously login, and may be some weak passwords as company may not aware about it because of many subdomains. So it alerts you.

<h2>Why I use WAD tool? Why not Wappalyzer module in python?</h2>
I use WAD because wappalyzer module don't give the version of CMS, servers, frameworks so that's useless for me. WAD do all these things.


# Time per subdomain..

It's really weired heading but anyways. So this tool really very cares about the good speed too, so it has the usage of multithreading. Now when we run this tools it takes 11 sec approx for each subdomains. Now note that, this includes the timings of the sublister too.

# Feedback

I am extreamly waiting for your feedback about this tool. 

# Contact


[agrawalsmart7](http://twitter.com/agrawalsmart7)


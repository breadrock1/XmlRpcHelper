# XmlRpcHelper

This simple python script automate process of extrating information or getting access by xmlrpc

Usage: ./XmlPrcHelper.py MODE {AllMethods | Ping | Bruting} -u URL
	
	Script modes (Select one of those methods and '--help' to get more information about options):
	1. pingback.ping        - This method allow you to ping back on our server, you can use netcat, 
				nodejs, python server or other ways. All what you need just set source 
				and destination addresses;
	2. wp.getUsersBlogs 	- This method may help you get access to Wordpress by bruting creds;
	3. system.listMethods - This method allow to get all accessible methods from Wordpress CMS.


	pingback.ping optional arguments:
		-h, --help  		Show this help message and exit
		-s --src		Specify source address (it's your server)
  		-d --dst		Specify destination address (it's target server)

	wp.getUsersBlogs optional arguments:
  		-h, --help		Show this help message and exit
  		-l --login		Specify login
  		-p --pass-wordlist	Specify path to wordlist

	system.listMethods optional arguments:
		-h, --help		Show this help message and exit

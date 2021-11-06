# XmlRpcHelper

![GitHub](https://badgen.net/badge/icon/github?icon=github&label)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![version](https://img.shields.io/badge/version-1.0.0-blue)
[![Build Status](https://travis-ci.com/username/projectname.svg?branch=master)](https://travis-ci.com/username/projectname)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)

## What is WordPress?

Wordpress one of the most famous and popular CMS. This management system allow comfortable creating, editing and monitoring any own websites.

## What is xmlrpc.php in WordPress?

It's actually an API which is provided by Wordpress CMS. This functionality helps to developers make ability to control your website from any devices. Abilities while using this remote protocol control:
	1) Publish a post
	2) Edit a post
	3) Delete a post.
	4) Upload a new file (e.g. an image for a post)
	5) Get a list of comments
	6) Edit comments
	
!!! Using this service is unsafe because any person can use this functionality if you have weak passwords or other misconfiguration...

## XmlRpcHelper
This simple python script automate process of extracting information or getting access by xmlrpc

Usage: ./launch.py MODE {AllMethods | Ping | Bruting} -u URL
	
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

## License

Copyright (C) 2021  Bread White

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Author: Bread White
Date:   2021 year
Email: breadrock1@gmail.com

## TODO

1. Realize pytest module to test each module functionality;
2. Realize specified command line arguments validation.


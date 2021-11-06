# XmlRpcHelper

![GitHub](https://badgen.net/badge/icon/github?icon=github&label)
![version](https://img.shields.io/badge/version-1.1.2-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)

## What is WordPress?

Wordpress one of the most famous and popular CMS. This management system allow comfortable creating, editing and monitoring any own websites.

## What is xmlrpc.php in WordPress?

It's actually an API which is provided by Wordpress CMS. This functionality helps to developers make ability to control your website from any devices. Abilities while using this remote protocol control:
1) Publish a post;
2) Edit a post;
3) Delete a post;
4) Upload a new file (e.g. an image for a post);
5) Get a list of comments;
6) Edit comments.

<b>!!! Using this service is unsafe because any person can use this functionality if you have weak passwords or other misconfiguration...</b>

## XmlRpcHelper
This simple python script automate process of extracting information or getting access by xmlrpc

```bash
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
```

## License

Copyright (c) 2021 Bread White

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

#!/usr/bin/python3

"""
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

    Author: Bread White
    Date:   2021 year
    Email: breadrock1@gmail.com
"""

from argparse import ArgumentParser

from src.XmlRpcHelper import XmlRpcHelper


def main() -> None:
    argumentParser = ArgumentParser(
        prog='XmlRpcHelper',
        usage='''./XmlPrcHelper.py MODE {AllMethods | Ping | Bruting} -u URL
                Mods details (Select one of those methods and '--help' to get more information about options):
                1. pingback.ping        - This method allow you to ping back on our server, you can use netcat, 
                                          nodejs, python server or other ways. All what you need just set source 
                                          and destination addresses;
                2. wp.getUsersBlogs     - This method may help you get access to Wordpress by bruting creds;
                3. system.listMethods   - This method allow to get all accessible methods from Wordpress CMS.
            ''',
        description='''
                This simple python script automate process of extracting information or getting access by xmlrpc
            ''',
        add_help=True,
        allow_abbrev=True
    )

    mode = ''

    subArgumentParser = argumentParser.add_subparsers(title='Script Mods', dest=mode)
    ping = subArgumentParser.add_parser('pingback.ping', help='ping back feature')
    brute = subArgumentParser.add_parser('wp.getUsersBlogs', help='brute force credentials')
    methods = subArgumentParser.add_parser('system.listMethods', help='get all accessible methods')

    methods.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')

    ping.add_argument('-s', type=str, required=True, metavar='--src', help='Specify source address (it\'s your server)')
    ping.add_argument('-d', type=str, required=True, metavar='--dst', help='Specify destination address (it\'s target server)')
    ping.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')

    brute.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')
    brute.add_argument('-l', type=str, required=False, metavar='--login', help='Specify login')
    brute.add_argument('-p', type=str, required=False, metavar='--pass-wordlist', help='Specify path to wordlist')

    ping.set_defaults(mode='pingback.ping')
    brute.set_defaults(mode='wp.getUsersBlogs')
    methods.set_defaults(mode='system.listMethods')

    arguments = argumentParser.parse_args()
    xmlRpcHelper = XmlRpcHelper(args=arguments)
    xmlRpcHelper.selectScriptMode()


if __name__ == '__main__':
    main()

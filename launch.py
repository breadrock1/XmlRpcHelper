from argparse import ArgumentParser, Namespace

from src.XmlRpcHelper import XmlRpcHelper


def main() -> None:
    mode = ''

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

    subArgumentParser = argumentParser.add_subparsers(title='Script Mods', dest=mode)
    ping = subArgumentParser.add_parser('pingback.ping', help='ping back feature')
    brute = subArgumentParser.add_parser('wp.getUsersBlogs', help='brute force credentials')
    methods = subArgumentParser.add_parser('system.listMethods', help='get all accessible methods')

    methods.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')

    ping.add_argument('-s', type=str, required=True, metavar='--src', help='Specify source address (it\'s your server)')
    ping.add_argument('-d', type=str, required=True, metavar='--dst',
                      help='Specify destination address (it\'s target server)')
    ping.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')

    brute.add_argument('-l', type=str, required=False, metavar='--login', help='Specify login')
    brute.add_argument('-p', type=str, required=False, metavar='--pass-wordlist', help='Specify path to wordlist')
    brute.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')

    ping.set_defaults(mode='pingback.ping')
    brute.set_defaults(mode='wp.getUsersBlogs')
    methods.set_defaults(mode='system.listMethods')

    arguments = argumentParser.parse_args()
    xmlRpcHelper = XmlRpcHelper(args=arguments)
    xmlRpcHelper.selectScriptMode()


if __name__ == '__main__':
    main()

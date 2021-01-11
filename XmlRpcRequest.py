import requests

class XmlRpcRequest(object):
    def __init__(self, url, method):
        self.url = url
        self.method = method

    def isInvalidCreds(self, recv_data) -> bool:
        return not (recv_data.__contains__('Incorrect') or recv_data.__contains__('Insufficient'))

    def sendRequest(self, first_param='', second_param='') -> str:
        response = requests.post(
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
            headers={
                'User-Agent': 'Mozilla/5.0',
                'Content-Type': 'application/xml'
            },
            allow_redirects=True
        )

        return response.text


# This code block for testing
if __name__ == '__main__':
    xmlRpcRequest = XmlRpcRequest('http://10.129.79.114/xmlrpc.php', 'wp.getUsersBlogs')
    xmlRpcRequest.sendRequest('admin', 'passwd')
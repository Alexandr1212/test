import requests
import uuid
from config import (
    SERVER_UUID,
    CLIENT_UUID,
    MESSAGE,
    SERVER_UUID_HEADER,
    config
)

class Client:
    client_uuid = ''
    server_uuid = ''
    registration_url = '{0}{1}:{2}'.format(
            config['path']['protocol'],
            config['path']['host_name'],
            config['path']['registration_port']
        )
    authentication_url = '{0}{1}:{2}'.format(
            config['path']['protocol'],
            config['path']['host_name'],
            config['path']['authentication_port']
        )

    def registration(self):
        # generate client uuid
        self.__generation_client_uuid()

        # set data with client uuid before send
        data = {CLIENT_UUID: self.client_uuid}

        # send post request with data for registration
        resp = requests.post(url = self.registration_url, data=data)

        # try get from response header server uuid
        try:
            self.server_uuid = resp.headers[SERVER_UUID_HEADER]
        except:
            print('Cannot find {0}'.format(SERVER_UUID_HEADER))


    def authentication(self):
        # set data with client uuid, server uuid and text before send
        data = {CLIENT_UUID: self.client_uuid, SERVER_UUID: self.server_uuid, MESSAGE: 'Some message'}

        # send post request with data for authentication
        resp = requests.post(url = self.authentication_url, data=data)
        print(resp.headers)

        # do something ...
    
    def __generation_client_uuid(self):
        self.client_uuid = str(uuid.uuid4())

    def __call__(self):
        self.registration()
        self.authentication()


if __name__ == "__main__":
    run = Client()
    run()

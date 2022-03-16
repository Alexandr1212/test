from locust import HttpLocust, TaskSet
import uuid
from config import (
    SERVER_UUID,
    CLIENT_UUID,
    MESSAGE,
    SERVER_UUID_HEADER,
    config
)

def load_testing(l):
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

    client_uuid = str(uuid.uuid4())
    resp = l.client.post(registration_url, {CLIENT_UUID: client_uuid})

    server_uuid = resp.headers[SERVER_UUID_HEADER]
    resp = l.client.post(authentication_url, {CLIENT_UUID: client_uuid, SERVER_UUID: server_uuid, MESSAGE: 'Some text'})

class UserBehavior(TaskSet):
    tasks = {load_testing: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
import requests
from requests.auth import HTTPBasicAuth
import getpass
import argparse


def _get_applications(url, hash):
    response = requests.get(url + '/api/server/v1/applications?limit=9999', auth=hash, headers={
        'Accept': 'application/json'
    })
    return response.json()

def _get_application(url, self, hash):
    response = requests.get(url + self, auth=hash, headers={
        'Accept':'application/json'
    })
    return response.json()

def _process(url, username):

    applications_json = []
    password = getpass.getpass(prompt='Password: ')
    auth_hash = HTTPBasicAuth(username,password)

    applications_response = _get_applications(url,auth_hash)

    if applications_response and 'applications' in applications_response:
        applications = applications_response['applications']       
        for app in applications:
            applications_json.append(_get_application(url, app['self'], auth_hash))
    return applications_json

def main():

    parser = argparse.ArgumentParser(description="WSO2 Identity Server: Retrieve application(s)")
    parser.add_argument('url', type=str, help='WSO2 Identity Server URL')
    parser.add_argument('username', type=str, help='Username')

    args = parser.parse_args()

    print(_process(args.url, args.username))

if __name__ == "__main__":
    main()

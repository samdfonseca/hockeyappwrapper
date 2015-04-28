from __future__ import print_function
from os import getenv
from os.path import abspath, join
from urlparse import urljoin
from requests import get, post
from simplejson import loads

from hockeyapp import __HOCKEYAPP_API_ROOT__


def hockey_url(endpoint):
    url = '/'.join([__HOCKEYAPP_API_ROOT__, endpoint])
    return url

def hockey_get(api_method, token=None, **kwargs):
    """Generic requests to the api_method endpoint"""
    headers = kwargs.pop('headers', {})
    api_token = getenv('HOCKEYAPP_API_TOKEN') if token is None else token
    url = hockey_url(api_method)
    if api_token is not None:
        headers['X-HockeyAppToken'] = api_token
    req = get(url, headers=headers, **kwargs)
    return req

def hockey_post(api_method, token=None, **kwargs):
    """Generic requests to the api_method endpoint"""
    headers = kwargs.pop('headers', {})
    api_token = getenv('HOCKEYAPP_API_TOKEN') if token is None else token
    url = hockey_url(api_method)
    if api_token is not None:
        headers['X-HockeyAppToken'] = api_token
    if kwargs:
        form_data = kwargs
    req = post(url, data=form_data, headers=headers)
    return req

def auth_tokens(email, password):
    """Lists all API tokens for the given user.

    http://support.hockeyapp.net/kb/api/api-basics-and-authentication#authentication-api

    :param email: The user's email as a string.
    :param password: The user's password as a string.
    :return: The response from the auth_token endpoint.
    """
    api_method = 'auth_tokens'
    resp = hockey_get(api_method, auth=(email, password))
    return loads(resp.content)

def apps(token=None):
    """List all apps for the logged in user, including owned apps, member apps, and tester apps.

    http://support.hockeyapp.net/kb/api/api-apps#list-apps

    :param token: The user's hockeyapp API token as a string.
    :return: The response from the apps endpoint.
    """
    api_method = 'apps'
    resp = hockey_get(api_method, token=token)
    return loads(resp.content)

def versions(app_id, token=None):
    """List all versions of an app.

    http://support.hockeyapp.net/kb/api/api-versions#list-versions

    :param app_id: The public_identifier attribute of the app.
    :param token: The user's hockeyapp API token as a string.
    :return: The response from the app_versions endpoint.
    """
    api_method = 'apps/{0}/app_versions'.format(app_id)
    resp = hockey_get(api_method, token=token)
    return loads(resp.content)

def download_apk(destination_file, download_url):
    """Downloads an APK file from the given download_url and writes it to the destination_file.

    :param destination_file: The path to download the file to as a string.
    :param download_url: The url to download the APK file from as a string.
    :return: The absolute path to the downloaded file.
    """
    download_url = download_url.replace('apps', 'api/2/apps') if download_url.find('api/2/apps') == -1 else download_url
    path = abspath(destination_file) if not destination_file.startswith('/') else destination_file
    resp = get(download_url)
    with open(path, 'wb') as f:
        f.write(resp.content)
    return path

# def upload_apk(apk, token=None, **kwargs):
#     """Upload an .apk file to create a new app. If an app with the same bundle identifier or package
#     name and the same release type already exists, the uploaded file is assigned to this existing app.
#
#     http://support.hockeyapp.net/kb/api/api-apps#upload-app
#
#     :param apk: The path to the apk file to upload.
#     :param kwargs: See docs.
#     """
#     # notes = kwargs.get('notes')
#     # notes_type = kwargs.get('notes_type')
#     # notify = kwargs.get('notify', '0')
#     # status = kwargs.get('status', '2')
#     # tags = kwargs.get('tags')
#     # teams = kwargs.get('teams')
#     # users = kwargs.get('users')
#     # mandatory = kwargs.get('mandatory')
#     # release_type = kwargs.get('release_type')
#     # private = kwargs.get('private')
#     # commit_sha = kwargs.get('commit_sha')
#     # build_server_url = kwargs.get('build_server_url')
#     # repository_url = kwargs.get('repository_url')
#     
#     api_method = 'apps/upload'
#     apk_path = abspath(apk) if not apk.startswith('/') else apk
#     form_data = kwargs
#     form_data['notify'] = kwargs.get('notify', '0')
#     form_data['status'] = kwargs.get('status', '2')
#     form_data['ipa'] = apk_path
#     resp = hockey_post(api_method, token=token, data=form_data)
#     return loads(resp.content)


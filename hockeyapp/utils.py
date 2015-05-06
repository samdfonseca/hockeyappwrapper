import re
from hockeyapp import api as hockeyapi


def get_apps_by(app_property, value):
    apps = hockeyapi.apps()
    filtered_apps = filter(lambda app: re.match(value, app[app_property]), apps['apps'])
    return filtered_apps

def get_app_by(app_property, value):
    return get_apps_by(app_property, value)[0]

def get_version(app, version):
    """Returns a JSON object of the first version of the app where app_version['shortversion'].startswith(version) is
    true

    :param app: The target app as returned by get_app_by.
    :param version: The version number of the target app as a string.
    :return: A JSON object of the app version.
    """
    app_id = app['public_identifier']
    versions = hockeyapi.versions(app_id)
    return filter(lambda app_version: app_version['shortversion'].startswith(str(version)), versions['app_versions'])[0]


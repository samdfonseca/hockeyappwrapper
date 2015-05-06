import re
from hockeyapp import api as hockeyapi


def get_apps_by(app_property, value):
    apps = hockeyapi.apps()
    filtered_apps = filter(lambda app: re.match(value, app[app_property]), apps['apps'])
    return filtered_apps

def get_app_by(app_property, value):
    return get_apps_by(app_property, value)[0]

def get_version(app_id, version):
    """Returns a JSON object of the first version of the app where app_version['shortversion'].startswith(version) is
    true

    :param app_id: The public_identifier of the target app as a string.
    :param version: The version number of the target app as a string.
    :return: A JSON object of the app version.
    """
    versions = hockeyapi.versions(app_id)
    return filter(lambda app_version: app_version['shortversion'].startswith(version), versions['app_versions'])[0]


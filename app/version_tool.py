from pkg_resources import parse_version


def get_newer_version(version1, version2):
    return version1 if parse_version(version1) >= parse_version(version2) else version2

get_newer_version("1.0.1-beta.1", "1.0.0")
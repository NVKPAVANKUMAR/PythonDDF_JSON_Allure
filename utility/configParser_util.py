from configparser import ConfigParser


def parse_data(section,key):
    config = ConfigParser()
    config.read('C:/Users/npavankumar/PycharmProjects/SeleniumPythonPOM/config/config.ini')
    return config.get(section, key)



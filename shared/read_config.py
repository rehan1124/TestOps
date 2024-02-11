import configparser

CONFIG_FILE = "qaenv.ini"
CONFIG_DIR = "config"


def read_config(category, key):
    config = configparser.ConfigParser()
    filepath = f"{CONFIG_DIR}/{CONFIG_FILE}"
    config.read(filenames=filepath)
    return config.get(category, key)

# print(read_config("DEFAULT", "url"))

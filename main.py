import json_settings
import user_input
from json_gen import generate_json

SETTINGS: dict = json_settings.parse()
SETTINGS_LOADED: bool = SETTINGS["LOADED"]

def main():
    generate_json(user_input, io_settings=SETTINGS["IO_DATA"])

if __name__ == "__main__":
    main()
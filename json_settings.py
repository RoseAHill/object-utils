import json

settings_file: str = "config.json"
default_settings_path: str = "defaults/default_config.json"

placeholder_settings: dict = {"IS_PLACEHOLDER": True, "LOADED": False}

load_success: bool = False

def _load_settings(settings_file_name: str, file_status: str = "main") -> dict:
    settings: dict = placeholder_settings
    try:
        with open(settings_file_name, "r") as file:
            settings = json.load(file)
            file.close
            return settings
    except Exception as e:
        print(f"Error while loading {file_status} settings: {e}")
        return _load_settings(default_settings_path, "default")

def parse() -> dict:
    settings: dict = _load_settings(settings_file)
    if settings["LOADED"]:
        return settings
    else:
        print(f"Error recieving settings load status, using settings PLACEHOLDER!")
        return placeholder_settings

def main():
    settings: dict = parse()
    print(f"Settings has a type of {type(settings)}")
    print(f"Current settings data: {settings}")

if __name__ == "__main__":
    main()
import configparser
from . import user_input

extension = ".ini"
config_file_name: str = user_input.title or "config"
default_config_path: str = "defaults/default_config" + extension

placeholder_config: dict = {"loaded": "yes", "version": "0.0.01"}
config = configparser.ConfigParser()

def generate(file_data = user_input, settings: dict = {"output_path": "gen/output/"}) -> bool:
    data: dict = file_data.data
    file_name: str = config_file_name
    output_dir: str = settings["output_path"]

    for key, value in data.items():
        config[key] = value

    try:
        with open(f"{output_dir}{file_name}{extension}", "w+") as config_file:
            config.write(config_file)
            config_file.close()
    except Exception as e:
        print(f"Error while opening file: {e}")
        return False
    return True

def main():
    print(f"Conversion from Python dictionary to ini config file {"successful!" if generate() else "failed..."}")

if __name__ == "__main__":
    main()
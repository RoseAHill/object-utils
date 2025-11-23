from gen import my_config, my_json
import configparser

config = configparser.ConfigParser()
config_file = "config.ini" 

try:
    config.read(config_file)
except FileExistsError:
    print(f"config.ini not found in working dir, using default config...")
    config.read("defaults/default_config.ini")
except Exception as e:
    print(f"Error while loading config: {e}")

def run_if_yes(callback, settings, prompt) -> str:
    user_answer = input(prompt)
    response = "Skipping..."
    if user_answer.lower() == "y":
        response = "Successful!" if callback(settings = settings) else "Failed!"
    return response

def main():
    print(f"Settings are{" " if len(config.sections()) > 0 else " not "}loaded...")

    print(f"{run_if_yes(my_config, config["IO_DATA"], "Generate config file? (y/N) ")}")
    print(f"{run_if_yes(my_json, config["IO_DATA"], "Generate json file? (y/N) ")}")

if __name__ == "__main__":
    main()
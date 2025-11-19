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

def main():
    print(f"Settings are{" " if len(config.sections()) > 0 else " not "}loaded...")

if __name__ == "__main__":
    main()
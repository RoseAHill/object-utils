import configparser, os, shutil

def load_config(path: str = "config.ini", default_config: str = "defaults/default_config.ini"):
    config = configparser.ConfigParser()
    try:
        config.read(path)
    except FileExistsError:
        print(f"config.ini not found in working dir, using default config...")
        with open(path, "x") as file:
            file.close()
        if not os.path.exists(default_config):
            raise
        shutil.copyfile(default_config, path)
        config.read(path)
        if len(config.sections()) < 1: 
            raise ValueError("Invalid config data!")
    except Exception as e:
        print(f"Error while loading config: {e}")
    return config

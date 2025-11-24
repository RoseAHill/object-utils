import parse
from gen import my_config, my_json
from display import game_map

config = parse.config("config.ini")

map_path_to_display = "input/my_mountain_map.json"

def gen_if_yes(callback, settings, prompt) -> str:
    user_answer = input(prompt)
    response = "Skipping..."
    if user_answer.lower() == "y":
        response = "Successful!" if callback(settings = settings) else "Failed!"
    return response

def main():
    print(f"Settings are{" " if len(config.sections()) > 0 else " not "}loaded...")

    print(f"{gen_if_yes(my_config, config["IO_DATA"], "Generate config file? (y/N) ")}")
    print(f"{gen_if_yes(my_json, config["IO_DATA"], "Generate json file? (y/N) ")}")
    print(f"{gen_if_yes(game_map, config["MAP_FEATURES"], "Generate map data? (y/N) ")}")
    
    map_data: dict = parse.json_data(map_path_to_display)
    
    print(f"Displaying map from '{map_path_to_display}'...\n{game_map(map_data["data"],config["MAP_FEATURES"])}")

if __name__ == "__main__":
    main()
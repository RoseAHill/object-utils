import json
import gen.user_input as user_input

def generate_json(data, io_settings:dict = {"output_path": "output/"}) -> bool:
    data_to_dump: dict = data.data
    json_file_name: str = io_settings["output_file"] if not io_settings["output_file"] else data.title
    output_dir: str = io_settings["output_path"]

    try:
        with open(f"{output_dir}{json_file_name}.json", "+w") as file:
            json.dump(data_to_dump, file, indent=4)
            file.close
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
        return False
    return True

def main():
    print(f"Conversion from Python dictionary to json file {"successful!" if generate_json(user_input) else "failed..."}")

if __name__ == "__main__":
    main()
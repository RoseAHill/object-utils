import json
from . import user_input

def generate(data = user_input, settings:dict = {"output_path": "gen/output/"}) -> bool:
    data_to_dump: dict = data.data
    json_file_name: str = data.title
    output_dir: str = settings["output_path"]

    try:
        with open(f"{output_dir}{json_file_name}.json", "+w") as file:
            json.dump(data_to_dump, file, indent=4)
            file.close
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
        return False
    return True

def main():
    print(f"Conversion from Python dictionary to json file {"successful!" if generate() else "failed..."}")

if __name__ == "__main__":
    main()
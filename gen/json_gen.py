import json, os
import user_input

def generate(data: dict = user_input.data, title: str = user_input.title, settings: dict = {"output_path": "gen/output/"}) -> bool:
    data_to_dump: dict = data
    json_file_name: str = title
    output_dir: str = settings["output_path"]
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    try:
        with open(f"{output_dir}{json_file_name}.json", "w+") as file:
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
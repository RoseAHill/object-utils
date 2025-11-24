import json

def json_data(json_file_path)-> dict:
    data: dict = {}
    try:
        with open(json_file_path) as file:
            data = json.load(file)
            file.close()
    except Exception as e:
        print(f"An error occurred: {e}")
    return data
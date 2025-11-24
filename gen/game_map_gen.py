if __name__ == "__main__":
    from json_gen import generate
else:
    from .json_gen import generate

default_cell_label: str = "Mountain"

def generate_map_data(settings: dict = {}, x: int = 8, y: int = 6, default_cell: str = default_cell_label) -> list:
    width: int = x
    height: int = y
    cell: str = default_cell
    if len(settings.keys()) > 0:
        try:
            width = int(settings["map_width"])
            height = int(settings["map_height"])
            cell = settings["default_cell"]
        except Exception as e:
            print(f"Invalid settings {e}")
    MAP_WIDTH: int = width
    MAP_HEIGHT: int = height
    CELL_CONTENTS: dict = {"label": cell, "save_data": {}}
    map_data: list[list] = [[CELL_CONTENTS for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    return map_data

def _export_map_data(my_map: list, map_title: str = "default_map_data") -> bool:
    try:
        generate({"title": map_title, "data": my_map}, title=map_title)
    except Exception as e:
        print(f"Error generating map json: {e}")
        return False
    return True

def main():
    map_data = generate_map_data()
    print(f"Map data {"successfully" if _export_map_data(map_data) else "NOT"} generated and exported")

if __name__ == "__main__":
    main()
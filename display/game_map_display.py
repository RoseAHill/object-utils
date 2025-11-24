def generate_map_display(map_data: list[list], settings: dict) -> str:
    line_char: str = "-"
    border_char: str = "|"
    cell_padding: int = 2
    max_cell_chars: int = 6
    abrv: str = "."
    if len(settings.keys()) > 0:
        try:
            pass
        except Exception as e:
            print(f"Invalid settings {e}")
    return ""

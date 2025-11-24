import json

def _display_string(top_label, line, row_data) -> str:
    display_string: str = f"{top_label}\n{line}\n"
    for row in row_data:
        display_string = f"{display_string}{row}\n{line}\n"
    return display_string

def generate_map_display(map_data: list[list], settings: dict) -> str:
    line_char: str = "-"
    border_char: str = "|"
    cell_padding_size: int = 2
    max_cell_chars: int = 6
    abbreviation: str = "."
    if len(settings.keys()) > 0:
        try:
            line_char = settings["line_char"]
            border_char = settings["border_char"]
            cell_padding_size = settings["cell_padding"]
            max_cell_chars = settings["max_cell_chars"]
            abbreviation = settings["abbreviation"]
        except Exception as e:
            print(f"Invalid settings {e}")
    num_rows = len(map_data)
    num_cols = len(map_data[0])
    
    cell_padding: str = " " * cell_padding_size
    top_label: str = f"{" " * (int(num_rows > 9) + 1)}{cell_padding}{border_char}"
    line: str = f"{line_char * (int(num_rows > 9) + 1)}{line_char * cell_padding_size}{border_char}"
    rows: list[str] = []
    
    for col_num in range(num_cols):
        # the padding to go around the one or two digit column label
        label_padding: str = (" " * int(max_cell_chars/ 2)) + cell_padding
        # the column label generator that appends to the column labels string inc:
        # - label padding
        # - column number
        # - extra space if the total rows is double digits and column number is greater than 10
        # - label padding again
        # - border character
        # the generator removes the first space if the max cells is even to compensate for the label digit
        top_label = top_label + f"{label_padding}{col_num}{" " * int(num_rows > 9 and col_num > 10)}{label_padding}{border_char}"[int(max_cell_chars % 2 < 1):]
        # the row separation line generator that appends to the line string inc:
        # - the line character repeated by the padding size
        # - the line character repeated by the number of characters in each cell label
        # - the padding again
        # - the border character
        line = line + f"{line_char * cell_padding_size}{line_char * max_cell_chars}{line_char * cell_padding_size}{border_char}"
    # Generation of the list of rows based on the cells of the map data, including index of row for proper labeling
    for row_index, row in enumerate(map_data):
        # starts the row string with the label of which row the loop is on
        current_row: str = f"{row_index}{cell_padding}{border_char}"
        # iterates over each column to generate the cells string
        for col in row:
            column: str = col["label"]
            # generates the text of the column, abbreviating the text if the length is greater than the max length of the cell, otherwise it uses the full text in the column with additional spaces to bring the number of characters up to the max length of the cell
            col_text = (column[:max_cell_chars - len(abbreviation)] + abbreviation) if len(column) > max_cell_chars else (column + (" " * (max_cell_chars - len(column))))
            # appends the cell's text to the current row, inc:
            # - pre-generated cell padding
            # - pre-generated column text
            # - cell padding again
            # - the border character
            current_row = current_row + f"{cell_padding}{col_text}{cell_padding}{border_char}"
        # appends the current row as a list item onto the list of rows
        rows.append(current_row)        
    
    return _display_string(top_label, line, rows)

def main():
    map_data: list[list] = [[]]
    default_data_path: str = "./defaults/default_map_data.json"
    try:
        with open(default_data_path) as file:
            data = json.load(file)
            map_data = data["data"]
            file.close()
    except FileNotFoundError:
        print(f"No default map data present in {default_data_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print(f"{generate_map_display(map_data, settings={})}")

if __name__ == "__main__":
    main()
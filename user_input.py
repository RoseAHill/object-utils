# INPUT CONFIGURATION:
# (all files will be placed in the "Output/" directory)
# Title of the generated json file
title: str = "output"
# DICTIONARY TO CONVERT:
# data to insert into the new json file
to_json: dict = {
    "NAME": "config",
    # The current itteration of the settings file
    "VERSION": "",
    # Default input/ouput data
    "IO_DATA": {
        "input_path": ".",
        "output_path": "output/",
        "output_file": "output"
    },
    "DEFAULTS": {
        # parent directory for default json files
        "defaults_path": "defaults/",
        # use all the default json data rather than user created json (overrides defaults_as_placeholders) 
        "use_all_defaults": True,
        # use default json files in place of missing user created json files
        "defaults_as_placeholders": False,
    },
    # Settings for the map display feature
    "DISPLAY_FEATURES": {
        # Character to represent the row dividers
        "line_char": "-",
        # character to represent a column border
        "border_char": "|",
        # cell padding for map cells
        "cell_padding": 2,
        # maximum number of characters to displau within a cell before abbreviating
        "max_cell_chars": 6,
        # how to abbreviate cell labels that exceed the max cell characters
        "abbreviation": "."
    },
}
# INPUT ARCHIVE:
# (rename the "to_json" dict to archive the previously converted data)
settings: dict = {
    # The current itteration of the settings file
    "VERSION": "",
    # Default input/ouput data
    "IO_DATA": {
        "input_path": ".",
        "output_path": "output/",
        "output_file": "output"
    },
    "DEFAULTS": {
        # parent directory for default json files
        "defaults_path": "defaults/",
        # use all the default json data rather than user created json (overrides defaults_as_placeholders) 
        "use_all_defaults": True,
        # use default json files in place of missing user created json files
        "defaults_as_placeholders": False,
    },
    # Settings for the map display feature
    "DISPLAY_FEATURES": {
        # Character to represent the row dividers
        "line_char": "-",
        # character to represent a column border
        "border_char": "|",
        # cell padding for map cells
        "cell_padding": 2,
        # maximum number of characters to displau within a cell before abbreviating
        "max_cell_chars": 6,
        # how to abbreviate cell labels that exceed the max cell characters
        "abbreviation": "."
    },
}
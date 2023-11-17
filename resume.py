from json import load


def resume(scr):
    with open('game_conf.json', 'r', encoding='utf-8') as f:
        records = load(f)
    if records["resume"] == 0:  # bash
        from menu_for_commands_in_theme import theme_commands_page
        theme_commands_page(scr)
    elif records["resume"] == 1:  # sys
        from menu_sys_files import sys_files_draw
        sys_files_draw(scr)
    elif records["resume"] == 2:  # tools
        from menu_utilities import utilities_draw
        utilities_draw(scr)

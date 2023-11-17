from json import load, dump


def get_menu_list(to_find: str) -> list:
    import os
    cur_dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(cur_dir_path):
        if to_find in root:
            cur_dir_path = root
            break
    # print(f'tmp path: {cur_dir_path}')
    menu = []
    for root, dirs, files in os.walk(cur_dir_path):
        # print(f'root: {root}')
        # print(f'dirs: {dirs}')
        # print(f'files: {files}')
        for file in files:
            # menu.append(os.path.join(os.path.split(root)[0], file))
            menu.append(os.path.join(root, file))
    return menu


def get_main_menu_names() -> dict:
    with open('app_conf.json', 'r', encoding='utf-8') as f:
        records = load(f)
    return records['main_menu_info']


def get_themes_root_files_names() -> list:
    with open('app_conf.json', 'r', encoding='utf-8') as f:
        records = load(f)
    return records['themes_root_files']


def get_themes_menu_names() -> dict:
    with open('app_conf.json', 'r', encoding='utf-8') as f:
        records = load(f)
    return records['themes_menu_info']


def get_settings(key: str) -> int:
    with open('game_conf.json', 'r', encoding='utf-8') as f:
        records = load(f)
        return records[key]


def save_settings(json_file: str, key: str, num: int = 0) -> None:
    with open(json_file, 'r', encoding='utf-8') as f:
        records = load(f)
    records[key] = num
    with open(json_file, "w", encoding="UTF-8") as f:
        dump(records, f, ensure_ascii=False, indent=2)


def clear_settings():
    with open("game_conf.json", 'r', encoding='utf-8') as f:
        records = load(f)
    for k in records:
        records[k] = 0
    with open("game_conf.json", "w", encoding="UTF-8") as f:
        dump(records, f, ensure_ascii=False, indent=2)

    for k in ['Commands', 'SysFiles', 'Utilities']:
        data = get_menu_list(k)
        for file in data:
            with open(file, 'r', encoding='utf-8') as f:
                records = load(f)
            records["question_state"] = 0
            with open(file, "w", encoding="UTF-8") as f:
                dump(records, f, ensure_ascii=False, indent=2)

import os
from json import load
from files import get_menu_list
from flet import ListView, ElevatedButton, ControlEvent, View, AppBar, Text, colors, app, WEB_BROWSER
from check_box_functions import create_check_boxes_plane


def theme_commands_page(page, theme: str) -> ListView([ElevatedButton()]):
    """
    make a new page with a scrollable list of available commands
    :param page: the dir of page, where to put the list
    :param theme: the theme for questions: BASH Commands, Sys Files or Utilities, etc...
    :return: ListView([ElevatedButton])
    """
    print('in bash_commands_draw func')

    def button_clicked(e: ControlEvent):
        #
        def next_button_clicked(_):
            # page.clean()
            # print(f'want to pop route={page.route}')
            # print(f'page.views = {page.views}')
            page.views.pop()
            # print(f'and now page.views={page.views}')
            top_view = page.views[-1]
            # print(f'will use route={top_view.route}')
            page.go(top_view.route)
            nonlocal is_need_the_following_question
            is_need_the_following_question = True

        command_title = e.control.text
        # print(command_title)
        i = menu.index(command_title)
        # print(f'file = {files_lst[i]}')
        with open(files_lst[i], 'r', encoding='utf-8') as st_f:
            records = load(st_f)
        # print(records)
        question_idx = 0
        question_list = records['questions']
        is_need_the_following_question = True

        while question_idx < len(question_list):
            # print(question_list[question_idx])
            if is_need_the_following_question:
                is_need_the_following_question = False
                # page.go(f'{page.route}/question')
                page.views.append(
                    View(
                        f'{page.route}/question',
                        [
                            AppBar(title=Text(f'Вопрос о команде {command_title}'), bgcolor=colors.SURFACE_VARIANT),
                            create_check_boxes_plane(page, question_list[question_idx]),
                            ElevatedButton(text='далее', on_click=next_button_clicked)
                        ],
                    )
                )
                page.update()
            while not is_need_the_following_question:
                ...
            question_idx += 1

    files_lst = sorted(get_menu_list(theme), key=lambda f: os.path.split(f)[-1].removesuffix(".json"))
    menu = [os.path.split(f)[-1].removesuffix(".json") for f in files_lst]

    return ListView(controls=[ElevatedButton(text=m, on_click=button_clicked) for m in menu],
                    expand=1, spacing=10, padding=20, auto_scroll=False)


def main(page):
    lv = theme_commands_page(page, 'Commands')
    page.add(lv)


if __name__ == '__main__':
    app(target=main)  # , view=WEB_BROWSER)

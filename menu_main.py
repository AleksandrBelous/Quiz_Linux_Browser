from flet import ControlEvent, Column, ElevatedButton, app, WEB_BROWSER
from files import get_main_menu_names

main_menu_info = get_main_menu_names()
head_main_menu: str = main_menu_info['title']
menu_main: list = main_menu_info['menu']


def main_menu_page(page) -> Column([ElevatedButton()]):
    """
    create the page with main menu buttons
    :param page: page to create
    :return: Column([ElevatedButton()])
    """

    def button_clicked(e: ControlEvent):
        m = e.control.text
        print(m)
        page.go(f'/{m}')
        # page.update()

    return Column(controls=[ElevatedButton(text=m, on_click=button_clicked) for m in menu_main])


def main(page):
    lv = main_menu_page(page)
    page.add(lv)
    page.update()


if __name__ == '__main__':
    app(target=main, view=WEB_BROWSER)

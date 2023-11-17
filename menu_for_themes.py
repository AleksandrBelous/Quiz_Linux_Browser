from flet import ControlEvent, Column, ElevatedButton, app, WEB_BROWSER
from files import get_themes_menu_names

themes_menu_info = get_themes_menu_names()
head_themes_menu: str = themes_menu_info['title']
menu_themes: list = themes_menu_info['menu']


def themes_menu_page(page) -> Column([ElevatedButton()]):
    """
    create the page with themes menu buttons
    :param page: page to create
    :return: Column([ElevatedButton()])
    """

    def button_clicked(e: ControlEvent):
        m = e.control.text
        print(m)
        page.go(f'{page.route}/{m}')
        # page.update()

    return Column(controls=[ElevatedButton(text=m, on_click=button_clicked) for m in menu_themes])


def main(page):
    page.route = '/Новая игра'
    lv = themes_menu_page(page)
    page.add(lv)
    page.update()


if __name__ == '__main__':
    app(target=main, view=WEB_BROWSER)

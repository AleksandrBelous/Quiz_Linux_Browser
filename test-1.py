import flet as ft


def main(page: ft.Page):
    import os

    from files import get_menu_list
    files_lst = sorted(get_menu_list('Commands'), key=lambda f: os.path.split(f)[-1].removesuffix(".json"))
    menu = [os.path.split(f)[-1].removesuffix(".json") for f in files_lst]

    def check_list(theme):
        ...

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

    for m in menu:
        lv.controls.append(list_of(m))

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Продолжить",
                content=ft.Container(
                    content=lv, alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )

    page.add(t)


ft.app(target=main, view=ft.WEB_BROWSER)

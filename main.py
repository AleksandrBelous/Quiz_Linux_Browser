from flet import AppBar, Page, Text, View, colors, app, WEB_BROWSER
from files import get_themes_root_files_names, get_menu_list
from menu_main import head_main_menu, menu_main, main_menu_page
from menu_for_themes import head_themes_menu, menu_themes, themes_menu_page
from menu_for_commands_in_theme import theme_commands_page


def main(page: Page):
    #
    main_menu_state_key = 'main_menu_state_key'
    if not page.client_storage.contains_key(main_menu_state_key):
        page.client_storage.set(main_menu_state_key, 0)
    main_menu_state_value = page.client_storage.get(main_menu_state_key)
    #
    resume_key = 'resume_key'
    if not page.client_storage.contains_key(resume_key):
        page.client_storage.set(resume_key, 0)
    resume_value = page.client_storage.get(resume_key)

    # # # # # # # # # #
    # # # # # # # # # #
    # # # # # # # # # #

    page.title = "Quiz Linux"

    print("Initial route:", page.route)

    def route_change(_):
        print("Route change:", page.route)
        # page.views.clear()
        theory_path_end = page.route.split('/')[-1]
        print(f'theory_path_end = {theory_path_end}')
        print(f'page.views[-1].route= {page.views[-1].route}')
        stack_path_end = page.views[-1].route.split("/")[-1] if page.views[-1].route else '-1'
        print(f'stack_path_end = {stack_path_end}')
        #
        # next, we will add views to the page stack, according to the theoretical path
        # the theoretical path may coincide with the physical one if a return to the previous page was made
        #
        if theory_path_end == '':
            page.views.clear()
            print(f'before +/ page.views = {page.views}')
            page.views.append(
                View(
                    '/',
                    [
                        AppBar(title=Text(head_main_menu)),
                        main_menu_page(page)
                    ],
                )
            )
            print(f'after +/ page.views = {page.views}')
        #
        # the theoretical path may coincide with the physical one if a return to the previous page was made
        #
        elif theory_path_end == menu_main[0] != stack_path_end:  # continue game
            print('want to continue game')
            page.client_storage.set(main_menu_state_key, main_menu_state_value)
            if resume_value == 0:  # bash commands
                print('want to continue bash commands')
                #
                # lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
                # for command in commands_lst:
                #     lv.controls.append(
                #         ElevatedButton(text=command, on_click=lambda _: page.go(f'{page.route}/{command}')))
                #
                # page.views.append(
                #     View(
                #         f'/{theory_path_end}',  # continue game
                #         [
                #             AppBar(title=Text(f'{menu_main[0]}'), bgcolor=colors.SURFACE_VARIANT),
                #             Container(content=lv)
                #             # page.add(ListView(expand=1, spacing=10, padding=20, auto_scroll=False))
                #             # ElevatedButton(
                #             #     f"Go to menu_main", on_click=lambda _: page.go('/' + menu_main[-1])
                #             # ),
                #         ],
                #     )
                # )
            elif resume_value == 1:  # sys commands
                page.views.append(
                    View(
                        '/' + menu_main[0],  # continue game
                        [
                            AppBar(title=Text(f'{menu_main[0]}'), bgcolor=colors.SURFACE_VARIANT),
                            Text(f"находимся в {menu_main[0]}, подраздел sys commands", style="bodyMedium"),
                            # ElevatedButton(
                            #     f"Go to menu_main", on_click=lambda _: page.go('/' + menu_main[-1])
                            # ),
                        ],
                    )
                )
            elif resume_value == 2:  # utilities commands
                page.views.append(
                    View(
                        '/' + menu_main[0],  # continue game
                        [
                            AppBar(title=Text(f'{menu_main[0]}'), bgcolor=colors.SURFACE_VARIANT),
                            Text(f"находимся в {menu_main[0]} , подраздел utilities commands", style="bodyMedium"),
                            # ElevatedButton(
                            #     f"Go to menu_main", on_click=lambda _: page.go('/' + menu_main[-1])
                            # ),
                        ],
                    )
                )
        elif theory_path_end == menu_main[3] != stack_path_end:  # choose the theme
            print('want to choose the theme')
            page.views.append(
                View(
                    f'/{theory_path_end}',
                    [
                        AppBar(title=Text(head_themes_menu)),
                        themes_menu_page(page)
                    ],
                )
            )
        elif theory_path_end in menu_themes and theory_path_end != stack_path_end:  # choose the theme
            page.views.append(
                View(
                    f'{page.route}/{theory_path_end}',
                    [
                        AppBar(title=Text(theory_path_end), bgcolor=colors.SURFACE_VARIANT),
                        theme_commands_page(page, get_themes_root_files_names()[menu_themes.index(theory_path_end)])
                    ],
                )
            )
        elif theory_path_end == menu_main[-1]:  # close the app
            exit(0)
        page.update()

    def view_pop(_):
        print(f'want to pop route={page.route}')
        print(f'page.views = {page.views}')
        page.views.pop()
        print(f'and now page.views={page.views}')
        top_view = page.views[-1]
        print(f'will use route={top_view.route}')
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main, view=WEB_BROWSER)

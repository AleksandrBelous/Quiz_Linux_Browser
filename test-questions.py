from random import shuffle
from json import load
import os
import flet


def questions_window(page):
    page.add(flet.ElevatedButton())
    # with open('C:\\Users\\Немо\\PycharmProjects\\Quiz Linux Browser\\Commands\\Compression\\gzip.json', 'r',
    #           encoding='utf-8') as f:
    #     records = load(f)
    #
    # def check(opt: str, ans: str):
    #     def button_clicked(_):
    #         t.value = "Yes" if b.data else "No"
    #
    #     b = flet.ElevatedButton(opt, on_click=button_clicked, data=lambda _: opt == ans)
    #     t = flet.Text()
    #
    #     return flet.Column(controls=[b, t])
    #
    # tmp = []
    # for q_dct in records["questions"]:
    #     q = flet.Text(q_dct["question"])
    #     lv = flet.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
    #     for opt in q_dct["options"]:
    #         lv.controls.append(check(opt, q_dct["answer"]))
    #     tmp.append(flet.Column([q, lv]))
    #
    # qns = flet.Column(tmp)
    # page.add(qns)


flet.app(target=questions_window, view=flet.WEB_BROWSER)

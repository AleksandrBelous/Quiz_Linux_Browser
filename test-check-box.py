import flet as ft


def create_check_boxes_plane(page, dct: dict):
    #
    def box_clicked(_):
        if any(c.value for c in boxes.controls):
            c = [c for c in boxes.controls if c.value][0]
            if c.label == ans and not any([tmp.value for tmp in boxes.controls if tmp != c]):
                c.fill_color = ft.colors.GREEN
            else:
                c.fill_color = ft.colors.RED
        else:
            for ch_box in boxes.controls:
                ch_box.fill_color = ft.colors.BLUE_100
        page.update()

    q = ft.Text(dct['question'])

    opts = dct['options']
    boxes = ft.Column([ft.Checkbox(label=opts[i], fill_color=ft.colors.BLUE_100, on_change=box_clicked)
                       for i in range(len(opts))])

    ans = dct['answer']

    return ft.Column([q, boxes])  # page.add(q, boxes, t)


def main(page):
    dct = {
        "question": "Какой ключ используется для сжатия файла?",
        "options": [
            "-d",
            "-c",
            "-k",
            "-r"
        ],
        "answer": "-c"
    }
    clm_q_and_boxes = create_check_boxes_plane(page, dct)
    page.add(clm_q_and_boxes)


if __name__ == '__main__':
    ft.app(target=main)

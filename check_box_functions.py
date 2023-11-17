from flet import colors, Text, Column, Checkbox, app


def create_check_boxes_plane(page, dct: dict) -> Column([Text(), Column([Checkbox()])]):
    """
    make a new page with a question block in a form of Checkboxes
    :param page: the dir of page, where to put the block
    :param dct: question block
    :return: Column([q, boxes]) = Column([Text(), Column([Checkbox()])])
    """

    def box_clicked(_):
        if any(c.value for c in boxes.controls):
            c = [c for c in boxes.controls if c.value][0]
            if c.label == ans and not any([tmp.value for tmp in boxes.controls if tmp != c]):
                c.fill_color = colors.GREEN
            else:
                c.fill_color = colors.RED
        else:
            for ch_box in boxes.controls:
                ch_box.fill_color = colors.BLUE_100
        page.update()

    q = Text(dct['question'])

    opts = dct['options']
    boxes = Column([Checkbox(label=opts[i], fill_color=colors.BLUE_100, on_change=box_clicked)
                    for i in range(len(opts))])

    ans = dct['answer']

    return Column([q, boxes])  # page.add(q, boxes)


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
    app(target=main)

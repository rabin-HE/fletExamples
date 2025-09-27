import flet
from flet import Page, colors, ElevatedButton, icons
from flet_toasts import Toast


def main(page: Page):
    btn = ElevatedButton("Toast")
    page.add(btn)
    Toast(
        page,
        Icons.PERSON_SHARP,
        "Toast title",
        "Toast description",
        btn,
        Colors.WHITE,
    ).struct()


if __name__ == "__main__":
    flet.app(target=main)

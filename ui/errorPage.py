from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, Entry, StringVar

from PIL import Image
from tksheet import Sheet

ASSETS_PATH = Path(r"ui/assets/errorPage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def error_page_start(root):
    error_page = Frame(root)
    error_page.pack(fill="both", expand=True)

    canvas = Canvas(
        error_page,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.pack(fill="both", expand=True)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        641.0,
        361.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        640.0,
        360.0,
        image=image_image_2
    )

    try_again_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    try_again_button = Button(
        error_page,
        image=try_again_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    try_again_button.place(
        x=565.0,
        y=475.0,
        width=150.0,
        height=35.0
    )

    canvas.create_rectangle(
        564.0,
        289.0,
        715.0,
        290.0,
        fill="#C42B21",
        outline="")

    error_message = canvas.create_text(
        490.0,
        333.0,
        anchor="nw",
        text="The input is nonnumerical.\nPlease try again.",
        tags="error_message",
        justify="center",
        fill="#C42B21",
        font=("Poppins Bold", 15 * -1)
    )

    canvas.create_text(
        565.0,
        240.0,
        anchor="nw",
        text="NOTICE!",
        fill="#C42B21",
        font=("Poppins Bold", 28 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        641.0,
        159.0,
        image=image_image_3
    )

    error_page.image_image_1 = image_image_1
    error_page.image_image_2 = image_image_2
    error_page.try_again_button_image = try_again_button_image
    error_page.image_image_3 = image_image_3

    error_page.try_again_button = try_again_button

    error_page.canvas = canvas

    error_page.error_message = error_message

    return error_page

from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame

ASSETS_PATH = Path(r"ui/assets/landingPage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def landing_page_start(root):
    landing_page = Frame(root)
    landing_page.pack(fill="both", expand=True)

    canvas = Canvas(
        landing_page,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.pack(fill="both", expand=True)

    start_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    start_button = Button(
        landing_page,
        image=start_button_image,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    start_button.place(
        x=775.0,
        y=540.0,
        width=375.0,
        height=60.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    canvas.create_image(
        965.0,
        215.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    canvas.create_image(
        320.0,
        368.0,
        image=image_image_2
    )

    canvas.create_text(
        700.0,
        350.0,
        anchor="nw",
        text="Let’s Get Started!",
        fill="#000000",
        font=("Poppins Bold", 60 * -1)
    )

    canvas.create_text(
        750.0,
        439.0,
        anchor="nw",
        text="Square Matrices Multiplication",
        fill="#000000",
        font=("Poppins Regular", 28 * -1)
    )

    # Keep references to PhotoImage objects to prevent them from being garbage collected
    landing_page.image_1 = image_image_1
    landing_page.image_2 = image_image_2
    landing_page.image_3 = start_button_image
    landing_page.start_button = start_button

    return landing_page

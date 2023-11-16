from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage, Frame

ASSETS_PATH = Path(r"ui/assets/setMatrixSize")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def set_matrix_size_start(root):
    set_matrix_size = Frame(root)
    set_matrix_size.pack(fill="both", expand=True)

    canvas = Canvas(
        set_matrix_size,
        bg="#FFFFFF",
        height=720,  # You can adjust this if needed
        width=1280,  # You can adjust this if needed
        relief="ridge"
    )

    canvas.pack(fill="both", expand=True)

    set_matrix_size_entry_image = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    set_matrix_size_bg = canvas.create_image(
        835.0,
        434.0,
        image=set_matrix_size_entry_image
    )
    set_matrix_size_entry = Entry(
        set_matrix_size,
        bg="#7853B3",
        fg="#FFFFFF",
        justify="center",
        borderwidth=0,
        font=("Poppins Bold", 30),
    )
    set_matrix_size_entry.place(
        x=800.0,
        y=400.0,
        width=70,
        height=60
    )

    canvas.create_text(
        390.0,
        435.0,
        anchor="nw",
        text="Note: Enter from 2 up to 5 only.",
        fill="#000000",
        font=("Poppins Regular", 22 * -1)
    )

    canvas.create_text(
        390.0,
        388.0,
        anchor="nw",
        text="Square Matrix Dimension:",
        fill="#000000",
        font=("Poppins Bold", 28 * -1)
    )

    size_submit_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    size_submit_button = Button(
        set_matrix_size,
        image=size_submit_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    size_submit_button.place(
        x=452.0,
        y=540.0,
        width=375.0,
        height=60.0
    )

    canvas.create_text(
        0.0,
        80.0,
        anchor="nw",
        text="Square Matrices Multiplication",
        fill="#000000",
        font=("Poppins Bold", 60 * -1)
    )

    canvas.create_text(
        0.0,
        180.0,
        anchor="nw",
        text="Instructions: Please enter your square matrix dimensions (2x2 up to 5x5) in the box below.",
        fill="#000000",
        font=("Poppins Regular", 22 * -1)
    )

    set_matrix_size.image_1 = set_matrix_size_entry_image
    set_matrix_size.image_2 = size_submit_button_image
    set_matrix_size.size_submit_button = size_submit_button

    return set_matrix_size


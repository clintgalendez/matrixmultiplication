from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame
from tksheet import Sheet

ASSETS_PATH = Path(r"ui/assets/setMatrixData")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def set_matrix_data_start(root):
    set_matrix_data = Frame(root)
    set_matrix_data.pack(fill="both", expand=True)

    canvas = Canvas(
        set_matrix_data,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.pack(fill="both", expand=True)
    canvas.create_text(
        615.0,
        293.0,
        anchor="nw",
        text="x",
        fill="#384FBA",
        font=("Poppins Bold", 28 * -1)
    )

    fill_zero_b_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    fill_zero_b_button = Button(
        set_matrix_data,
        image=fill_zero_b_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    fill_zero_b_button.place(
        x=855.0,
        y=534.0,
        width=345.0,
        height=50.0
    )

    reset_matrix_b_button_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    reset_matrix_b_button = Button(
        set_matrix_data,
        image=reset_matrix_b_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    reset_matrix_b_button.place(
        x=696.0,
        y=534.0,
        width=150.0,
        height=50.0
    )

    canvas.create_text(
        696.0,
        60.0,
        anchor="nw",
        text="Matrix B",
        fill="#000000",
        font=("Poppins Bold", 28 * -1)
    )

    fill_zero_a_button_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    fill_zero_a_button = Button(
        set_matrix_data,
        image=fill_zero_a_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    fill_zero_a_button.place(
        x=239.0,
        y=534.0,
        width=345.0,
        height=50.0
    )

    matrix_a_sheet = Sheet(
        set_matrix_data,
        show_header=False,
        show_row_index=False,
        show_top_left=False,
        empty_vertical=0,
        empty_horizontal=0,
        show_x_scrollbar=False,
        show_y_scrollbar=False,
        table_grid_fg="#000000",
        width=505,
        height=415,
        auto_resize_rows=True,
        auto_resize_columns=True,
        total_rows=5,
        total_columns=5,
        row_index_width=0,
        font=("Poppins", 30, "bold")
    )
    matrix_a_sheet.place(x=79, y=111)
    matrix_a_sheet.enable_bindings("all")
    matrix_a_sheet.align("center")

    matrix_b_sheet = Sheet(
        set_matrix_data,
        show_header=False,
        show_row_index=False,
        show_top_left=False,
        empty_vertical=0,
        empty_horizontal=0,
        show_x_scrollbar=False,
        show_y_scrollbar=False,
        table_grid_fg="#000000",
        width=505,
        height=415,
        auto_resize_rows=True,
        auto_resize_columns=True,
        total_rows=5,
        total_columns=5,
        row_index_width=0,
        font=("Poppins", 30, "bold")
    )
    matrix_b_sheet.place(x=700, y=111)
    matrix_b_sheet.enable_bindings("all")
    matrix_b_sheet.align("center")

    reset_matrix_a_button_image = PhotoImage(
        file=relative_to_assets("button_4.png"))
    reset_matrix_a_button = Button(
        set_matrix_data,
        image=reset_matrix_a_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    reset_matrix_a_button.place(
        x=80.0,
        y=534.0,
        width=150.0,
        height=50.0
    )

    calculate_button_image = PhotoImage(
        file=relative_to_assets("button_5.png"))
    calculate_button = Button(
        set_matrix_data,
        image=calculate_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    calculate_button.place(
        x=540.0,
        y=615.0,
        width=200.0,
        height=50.0
    )

    canvas.create_text(
        80.0,
        60.0,
        anchor="nw",
        text="Matrix A",
        fill="#000000",
        font=("Poppins Bold", 28 * -1)
    )

    set_matrix_data.fill_zero_b_button_image = fill_zero_b_button_image
    set_matrix_data.reset_matrix_b_button_image = reset_matrix_b_button_image
    set_matrix_data.fill_zero_a_button_image = fill_zero_a_button_image
    set_matrix_data.reset_matrix_a_button_image = reset_matrix_a_button_image
    set_matrix_data.calculate_button_image = calculate_button_image

    return set_matrix_data

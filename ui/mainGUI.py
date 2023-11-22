from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, Entry, StringVar, Label

from tksheet import Sheet

ASSETS_PATH = Path(r"ui/assets/main")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def main_start(root):
    main_frame = Frame(root)
    main_frame.pack(fill="both", expand=True)

    canvas = Canvas(
        main_frame,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.pack()
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        640.0,
        366.0,
        image=image_image_1
    )

    logo_image = PhotoImage(
        file=relative_to_assets("image_6.png"))
    logo = Label(
        main_frame,
        image=logo_image,
        borderwidth=0,
        width=250,
        height=225,
    )
    logo.place(x=918.0, y=230.0)

    reset_matrices_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    reset_matrices_button = Button(
        main_frame,
        image=reset_matrices_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    reset_matrices_button.place(
        x=954.0,
        y=600.0,
        width=150.0,
        height=35.0
    )

    calculate_button_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    calculate_button = Button(
        main_frame,
        cursor="hand2",
        state="disabled",
        image=calculate_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    calculate_button.place(
        x=320.0,
        y=600.0,
        width=150.0,
        height=35.0
    )

    solution_description_variable = StringVar(value="")
    solution_description_image = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    solution_description_bg = canvas.create_image(
        1040.0,
        117.5,
        image=solution_description_image
    )
    solution_description = Entry(
        main_frame,
        textvariable=solution_description_variable,
        bd=0,
        bg="#97B8CD",
        fg="#000716",
        highlightthickness=0,
        justify="center"
    )
    solution_description.place(
        x=893.0,
        y=100.0,
        width=294.0,
        height=33.0
    )

    canvas.create_rectangle(
        812.007568359375,
        48.49957275390625,
        813.507568359375,
        635.0004272460938,
        fill="#6D7588",
        outline="")

    next_button_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    next_button = Button(
        main_frame,
        cursor="hand2",
        state="disabled",
        image=next_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    next_button.place(
        x=1101.0,
        y=508.0,
        width=89.10891723632812,
        height=28.625951766967773
    )

    back_button_image = PhotoImage(
        file=relative_to_assets("button_4.png"))
    back_button = Button(
        main_frame,
        cursor="hand2",
        state="disabled",
        image=back_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    back_button.place(
        x=890.0,
        y=508.0,
        width=89.1089096069336,
        height=28.625951766967773
    )

    canvas.create_text(
        1005.0,
        160.0,
        anchor="nw",
        text="Matrix C",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    fill_zero_b_button_image = PhotoImage(
        file=relative_to_assets("button_5.png"))
    fill_zero_b_button = Button(
        main_frame,
        cursor="hand2",
        state="disabled",
        image=fill_zero_b_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    fill_zero_b_button.place(
        x=535.0,
        y=509.0,
        width=205.0,
        height=29.0
    )

    clear_matrix_b_button_image = PhotoImage(
        file=relative_to_assets("button_6.png"))
    clear_matrix_b_button = Button(
        main_frame,
        cursor="hand2",
        state="disabled",
        image=clear_matrix_b_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    clear_matrix_b_button.place(
        x=440.0,
        y=509.0,
        width=89.10891723632812,
        height=28.625951766967773
    )

    canvas.create_text(
        555.0,
        160.0,
        anchor="nw",
        text="Matrix B",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    fill_a_zero_button_image = PhotoImage(
        file=relative_to_assets("button_7.png"))
    fill_a_zero_button = Button(
        main_frame,
        cursor="hand2",
        state="disabled",
        image=fill_a_zero_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    fill_a_zero_button.place(
        x=155.0,
        y=509.0,
        width=205.0,
        height=29.0
    )

    clear_matrix_a_button_image = PhotoImage(
        file=relative_to_assets("button_8.png"))
    clear_matrix_a_button = Button(
        main_frame,
        cursor="hand2",
        state="disabled",
        image=clear_matrix_a_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    clear_matrix_a_button.place(
        x=60.0,
        y=509.0,
        width=89.10888671875,
        height=28.625951766967773
    )

    canvas.create_text(
        175.0,
        160.0,
        anchor="nw",
        text="Matrix A",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        399.0,
        346.0,
        image=image_image_5
    )

    canvas.create_text(
        270.0,
        50.0,
        anchor="nw",
        text="Square Matrices Multiplication",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    canvas.create_text(
        1005.0,
        50.0,
        anchor="nw",
        text="Solution",
        fill="#000000",
        font=("Poppins Bold", 20 * -1)
    )

    by_5_size_button_image = PhotoImage(
        file=relative_to_assets("button_9.png"))
    by_5_size_button = Button(
        main_frame,
        image=by_5_size_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    by_5_size_button.place(
        x=505.0,
        y=100.0,
        width=89.1099853515625,
        height=35.0
    )

    by_4_size_button_image = PhotoImage(
        file=relative_to_assets("button_10.png"))
    by_4_size_button = Button(
        main_frame,
        image=by_4_size_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    by_4_size_button.place(
        x=405.0,
        y=100.0,
        width=89.1099853515625,
        height=35.0
    )

    by_3_size_button_image = PhotoImage(
        file=relative_to_assets("button_11.png"))
    by_3_size_button = Button(
        main_frame,
        image=by_3_size_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    by_3_size_button.place(
        x=305.0,
        y=100.0,
        width=89.1099853515625,
        height=35.0
    )

    by_2_size_button_image = PhotoImage(
        file=relative_to_assets("button_12.png"))
    by_2_size_button = Button(
        main_frame,
        image=by_2_size_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_12 clicked"),
        relief="flat"
    )
    by_2_size_button.place(
        x=205.0,
        y=100.0,
        width=89.1099853515625,
        height=35.0
    )

    matrix_a_sheet = Sheet(
        main_frame,
        edit_cell_validation=False,
        enable_edit_cell_auto_resize=False,
        show_header=False,
        show_row_index=False,
        show_top_left=False,
        empty_vertical=0,
        empty_horizontal=0,
        show_x_scrollbar=False,
        show_y_scrollbar=False,
        table_grid_fg="#000000",
        width=300,
        height=300,
        auto_resize_rows=True,
        auto_resize_columns=True,
        total_rows=0,
        total_columns=0,
        row_index_width=0,
        font=("Poppins", 25, "bold")
    )
    matrix_a_sheet.place(x=58, y=195.3)
    matrix_a_sheet.enable_bindings("all")
    matrix_a_sheet.align("center")

    matrix_b_sheet = Sheet(
        main_frame,
        edit_cell_validation=False,
        enable_edit_cell_auto_resize=False,
        show_header=False,
        show_row_index=False,
        show_top_left=False,
        empty_vertical=0,
        empty_horizontal=0,
        show_x_scrollbar=False,
        show_y_scrollbar=False,
        table_grid_fg="#000000",
        width=300,
        height=300,
        auto_resize_rows=True,
        auto_resize_columns=True,
        total_rows=0,
        total_columns=0,
        row_index_width=0,
        font=("Poppins", 25, "bold")
    )
    matrix_b_sheet.place(x=438.2, y=195.3)
    matrix_b_sheet.enable_bindings("all")
    matrix_b_sheet.align("center")

    matrix_c_sheet = Sheet(
        canvas,
        enable_edit_cell_auto_resize=False,
        show_header=False,
        show_row_index=False,
        show_top_left=False,
        empty_vertical=0,
        empty_horizontal=0,
        show_x_scrollbar=False,
        show_y_scrollbar=False,
        table_grid_fg="#000000",
        width=300,
        height=300,
        auto_resize_rows=True,
        auto_resize_columns=True,
        total_rows=0,
        total_columns=0,
        row_index_width=0,
        font=("Poppins", 25, "bold")
    )
    matrix_c_sheet.place(x=888.3, y=195.3)
    matrix_c_sheet.enable_bindings("copy", "drag_select", "single_select", "column_drag_and_drop", "row_drag_and_drop", "column_select", "row_select")
    matrix_c_sheet.align("center")

    # Reference to all the variables
    main_frame.image_image_1 = image_image_1
    main_frame.reset_matrices_button_image = reset_matrices_button_image
    main_frame.calculate_button_image = calculate_button_image
    main_frame.solution_description_image = solution_description_image
    main_frame.next_button_image = next_button_image
    main_frame.back_button_image = back_button_image
    main_frame.fill_zero_b_button_image = fill_zero_b_button_image
    main_frame.clear_matrix_b_button_image = clear_matrix_b_button_image
    main_frame.fill_a_zero_button_image = fill_a_zero_button_image
    main_frame.clear_matrix_a_button_image = clear_matrix_a_button_image
    main_frame.image_image_5 = image_image_5
    main_frame.by_5_size_button_image = by_5_size_button_image
    main_frame.by_size_4_button_image = by_4_size_button_image
    main_frame.by_3_size_button_image = by_3_size_button_image
    main_frame.by_2_size_button_image = by_2_size_button_image
    main_frame.logo_image = logo_image

    main_frame.logo = logo

    main_frame.by_2_size_button = by_2_size_button
    main_frame.by_3_size_button = by_3_size_button
    main_frame.by_4_size_button = by_4_size_button
    main_frame.by_5_size_button = by_5_size_button

    main_frame.calculate_button = calculate_button

    main_frame.next_button = next_button
    main_frame.back_button = back_button

    main_frame.clear_matrix_a_button = clear_matrix_a_button
    main_frame.clear_matrix_b_button = clear_matrix_b_button

    main_frame.reset_matrices_button = reset_matrices_button

    main_frame.solution_description = solution_description_variable

    main_frame.matrix_a_sheet = matrix_a_sheet
    main_frame.matrix_b_sheet = matrix_b_sheet
    main_frame.matrix_c_sheet = matrix_c_sheet

    main_frame.clear_matrix_a_button = clear_matrix_a_button
    main_frame.clear_matrix_b_button = clear_matrix_b_button

    main_frame.fill_a_zero_button = fill_a_zero_button
    main_frame.fill_zero_b_button = fill_zero_b_button

    main_frame.canvas = canvas

    return main_frame

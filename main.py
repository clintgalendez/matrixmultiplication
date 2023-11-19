import time
from tkinter import Tk

import ui.mainGUI as mainGUI
from pynput.keyboard import Key, Controller
import ui.errorPage as errorPage

root = Tk()
root.geometry("1280x720")
root.configure(bg="red")
root.resizable(False, False)

keyboard = Controller()

current_frame = None
time_quantum = 500
matrix_size = 0
row_a = 0
column_b = 0
common = 0
history_stack = []

main_page = mainGUI.main_start(root)
error_page = errorPage.error_page_start(root)

f1 = main_page
f2 = error_page

by_2_size_button = f1.by_2_size_button
by_3_size_button = f1.by_3_size_button
by_4_size_button = f1.by_4_size_button
by_5_size_button = f1.by_5_size_button

calculate_button = f1.calculate_button

next_button = f1.next_button
back_button = f1.back_button

clear_matrix_a_button = f1.clear_matrix_a_button

solution_description = f1.solution_description

matrix_a = f1.matrix_a_sheet
matrix_b = f1.matrix_b_sheet
matrix_c = f1.matrix_c_sheet

canvas = f1.canvas


def show_frame(frame_to_show):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    current_frame = frame_to_show
    frame_to_show.pack(fill="both", expand=True)


def set_matrix_size_submit(matrix_size_to_set):
    global matrix_size

    matrix_size = matrix_size_to_set

    matrix_a.set_sheet_data_and_display_dimensions(matrix_size, matrix_size)
    matrix_b.set_sheet_data_and_display_dimensions(matrix_size, matrix_size)
    matrix_c.set_sheet_data_and_display_dimensions(matrix_size, matrix_size)

    matrix_a.refresh()
    matrix_b.refresh()
    matrix_c.refresh()

    canvas.itemconfigure("image_6", state="hidden")


def format_cell():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    root.after(time_quantum, calculate)


def calculate():
    print("hello")
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    # Perform matrix multiplication
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                result[i][j] += (int(matrix_a.get_cell_data(i, k)) * int(matrix_b.get_cell_data(k, j)))
                matrix_c.set_cell_data(i, j, result[i][j])

    matrix_c.refresh()
    next_button.configure(state="normal")


def show_solution_process(is_next: bool):
    global row_a, column_b, common

    matrix_a.dehighlight_all()
    matrix_b.dehighlight_all()
    matrix_c.dehighlight_all()

    if is_next:
        history_stack.append((row_a, column_b, common))
    elif history_stack:
        row_a, column_b, common = history_stack.pop()

        # Check if there's another item in the stack
        if history_stack:
            row_a, column_b, common = history_stack[-1]

    for r in range(matrix_size):
        matrix_a.highlight_cells(
            row=row_a, column=r, bg="#7ED957"
        )

        matrix_b.highlight_cells(
            row=r, column=column_b, bg="#7ED957"
        )

    matrix_c.highlight_cells(
        row=row_a, column=column_b, bg="#7ED957"
    )

    current_solution_text = "C" + str(row_a + 1) + str(column_b + 1) + " = "

    current_solution_text += (matrix_a.get_cell_data(row_a, common) + "(" +
                              matrix_b.get_cell_data(common, column_b)) + ")"

    for r in range(1, matrix_size):
        current_solution_text += " + " + (matrix_a.get_cell_data(row_a, r) + "(" +
                                          matrix_b.get_cell_data(r, column_b)) + ")"

    solution_description.set(current_solution_text)

    matrix_a.refresh()
    matrix_b.refresh()
    matrix_c.refresh()

    if column_b < matrix_size - 1:
        column_b += 1
    else:
        column_b = 0
        if row_a < matrix_size - 1:
            row_a += 1
        else:
            row_a = 0
            if common < matrix_size - 1:
                common += 1
            else:
                common = 0


def clear_matrix_a():
    #Clear the matrix
    return


by_2_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(2)))
by_3_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(3)))
by_4_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(4)))
by_5_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(5)))

calculate_button.configure(command=lambda: root.after(time_quantum, format_cell))

next_button.configure(command=lambda: root.after(time_quantum, lambda: show_solution_process(True)))
back_button.configure(command=lambda: root.after(time_quantum, lambda: show_solution_process(False)))

clear_matrix_a_button.configure(command=lambda: root.after(time_quantum, lambda: matrix_a.clear_matrix_a()))

# TODO: For (clint galendez) Add a function that it will disable calculate button if there's no data in the matrix

show_frame(f1)
root.mainloop()

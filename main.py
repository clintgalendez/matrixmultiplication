from tkinter import Tk

import ui.mainGUI as mainGUI

root = Tk()
root.geometry("1280x720")
root.configure(bg="red")
root.resizable(False, False)

current_frame = None
time_quantum = 500
matrix_size = 0
row_a = 0
column_b = 0
common = 0
history_stack = []

main_page = mainGUI.main_start(root)

f1 = main_page

by_2_size_button = f1.by_2_size_button
by_3_size_button = f1.by_3_size_button
by_4_size_button = f1.by_4_size_button
by_5_size_button = f1.by_5_size_button

calculate_button = f1.calculate_button

next_button = f1.next_button
back_button = f1.back_button

clear_matrix_a_button = f1.clear_matrix_a_button
clear_matrix_b_button = f1.clear_matrix_b_button

fill_a_zero_button = f1.fill_a_zero_button
fill_zero_b_button = f1.fill_zero_b_button


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


def calculate():
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    # Perform matrix multiplication
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                result[i][j] += int(matrix_a.get_cell_data(i, k)) * int(matrix_b.get_cell_data(k, j))
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
        print(history_stack)
    elif history_stack:
        row_a, column_b, common = history_stack.pop()
        print(history_stack)

        # Check if there's another item in the stack
        if history_stack:
            row_a, column_b, common = history_stack[-1]
            print(history_stack)

    print(row_a, column_b, common)

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

def clear_cell(matrix):
    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix.set_cell_data(i, j, value=None)
            matrix.refresh()

def fill_cell_values_zero(matrix):
    data = matrix.get_sheet_data()
    
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell is None or cell=="":
                matrix.set_cell_data(r, c, 0)
                matrix.refresh()
    matrix.refresh()

def reset_matrices():
    pass

by_2_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(2)))
by_3_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(3)))
by_4_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(4)))
by_5_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(5)))

calculate_button.configure(command=lambda: root.after(time_quantum, calculate))

next_button.configure(command=lambda: root.after(time_quantum, lambda: show_solution_process(True)))
back_button.configure(command=lambda: root.after(time_quantum, lambda: show_solution_process(False)))

clear_matrix_a_button.configure(command=lambda: root.after(time_quantum, lambda: clear_cell(matrix_a)))
clear_matrix_b_button.configure(command=lambda: root.after(time_quantum, lambda: clear_cell(matrix_b)))

fill_a_zero_button.configure(command=lambda: root.after(time_quantum, lambda:fill_cell_values_zero(matrix_a)))
fill_zero_b_button.configure(command=lambda: root.after(time_quantum, lambda:fill_cell_values_zero(matrix_b)))

show_frame(f1)
root.mainloop()

import inspect
import re
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

try_again_button = f2.try_again_button

reset_matrices_button = f1.reset_matrices_button

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

logo = f1.logo

main_canvas = f1.canvas
error_canvas = f2.canvas

error_message = f2.error_message


def show_frame(frame_to_show):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    current_frame = frame_to_show
    frame_to_show.pack(fill="both", expand=True)


def set_matrix_size_submit(matrix_size_to_set, font_size: int):
    global matrix_size

    matrix_size = matrix_size_to_set

    matrix_a.set_sheet_data_and_display_dimensions(matrix_size, matrix_size)
    matrix_b.set_sheet_data_and_display_dimensions(matrix_size, matrix_size)
    matrix_c.set_sheet_data_and_display_dimensions(matrix_size, matrix_size)

    reset_to_defaults()

    matrix_a.refresh()
    matrix_b.refresh()
    matrix_c.refresh()

    matrix_a.font(newfont=("Poppins", font_size, "bold"), reset_row_positions=True)

    logo.place_forget()
    calculate_button.configure(state="normal")
    clear_matrix_a_button.configure(state="normal")
    clear_matrix_b_button.configure(state="normal")
    fill_a_zero_button.configure(state="normal")
    fill_zero_b_button.configure(state="normal")


def register_cell():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    root.after(time_quantum, format_cell)


def format_cell():
    for i in range(matrix_size):
        for j in range(matrix_size):
            formatted_value_a = begin_cell_format(matrix_a.get_cell_data(i, j))
            formatted_value_b = begin_cell_format(matrix_b.get_cell_data(i, j))

            if isinstance(formatted_value_a, str):
                error_canvas.itemconfig("error_message", text=formatted_value_a)
                show_frame(f2)
                return

            if isinstance(formatted_value_b, str):
                error_canvas.itemconfig("error_message", text=formatted_value_b)
                show_frame(f2)
                return

            matrix_a.set_cell_data(i, j, begin_cell_format(matrix_a.get_cell_data(i, j)))
            matrix_b.set_cell_data(i, j, begin_cell_format(matrix_b.get_cell_data(i, j)))

    matrix_a.refresh()
    matrix_b.refresh()
    calculate()


def begin_cell_format(fraction):
    fraction = str(fraction)
    # Define regex patterns
    simple_fraction_pattern = r'^(-?\d+(\.\d+)?)\/(-?\d+(\.\d+)?)$'
    mixed_fraction_pattern = r'^(-?\d+(\.\d+)?) (-?\d+(\.\d+)?)\/(-?\d+(\.\d+)?)$'
    whole_number_pattern = r'^(-?\d+(\.\d+)?)$'

    # Check if fraction is empty
    if not fraction:
        return "There are cell/s that are empty. \n Please try again."

    # Match whole number pattern
    match_whole = re.match(whole_number_pattern, fraction)
    if match_whole:
        return float(match_whole.group(1))

    # Match simple fraction pattern
    match_simple = re.match(simple_fraction_pattern, fraction)
    if match_simple:
        numerator, _, denominator, _ = match_simple.groups()
        numerator, denominator = int(numerator), int(denominator)
        if denominator == 0:
            print("Error: Division by zero in fraction input: " + fraction)
            return "There are cell/s with division by zero which is not allowed. \n Please try again."
        return round(numerator / denominator, 2)

    # Match mixed fraction pattern
    match_mixed = re.match(mixed_fraction_pattern, fraction)
    if match_mixed:
        whole, _, numerator, _, denominator, _ = match_mixed.groups()
        whole, numerator, denominator = int(whole), int(numerator), int(denominator)
        if denominator == 0:
            print("Error: Division by zero in fraction input: " + fraction)
            return "There are cell/s with division by zero which is not allowed. \n Please try again."
        return round(whole + numerator / denominator, 2)

    # Invalid input
    print("Invalid fraction input: " + fraction)
    return "There are cell/s that are nonnumerical.\nPlease try again."


def calculate():
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    # Perform matrix multiplication
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                result[i][j] += (matrix_a.get_cell_data(i, k) * matrix_b.get_cell_data(k, j))
                matrix_c.set_cell_data(i, j, round(result[i][j], 2))

    matrix_c.refresh()
    next_button.configure(state="normal")
    back_button.configure(state="normal")


def show_solution_process(is_next: bool):
    global row_a, column_b

    matrix_a.dehighlight_all()
    matrix_b.dehighlight_all()
    matrix_c.dehighlight_all()

    if is_next:
        history_stack.append((row_a, column_b))
    elif history_stack:
        row_a, column_b = history_stack.pop()

        # Check if there's another item in the stack
        if history_stack:
            row_a, column_b = history_stack[-1]

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

    current_solution_text += (str(matrix_a.get_cell_data(row_a, 0)) + "(" +
                              str(matrix_b.get_cell_data(0, column_b))) + ")"

    for r in range(1, matrix_size):
        current_solution_text += " + " + (str(matrix_a.get_cell_data(row_a, r)) + "(" +
                                          str(matrix_b.get_cell_data(r, column_b))) + ")"

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


def reset_to_defaults():
    matrix_a.dehighlight_all()
    matrix_b.dehighlight_all()
    matrix_c.dehighlight_all()

    next_button.configure(state="disabled")
    back_button.configure(state="disabled")


def begin_clear_cells(matrix):
    reset_to_defaults()
    clear_cell(matrix)


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
    reset_to_defaults()
    clear_cell(matrix_a)
    clear_cell(matrix_b)
    clear_cell(matrix_c)
    return


by_2_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(2, 25)))
by_3_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(3, 20)))
by_4_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(4, 15)))
by_5_size_button.configure(command=lambda: root.after(time_quantum, lambda: set_matrix_size_submit(5, 12)))

calculate_button.configure(command=lambda: root.after(time_quantum, register_cell))

try_again_button.configure(command=lambda: root.after(time_quantum, lambda: show_frame(f1)))

next_button.configure(command=lambda: root.after(time_quantum, lambda: show_solution_process(True)))
back_button.configure(command=lambda: root.after(time_quantum, lambda: show_solution_process(False)))

clear_matrix_a_button.configure(command=lambda: root.after(time_quantum, lambda: begin_clear_cells(matrix_a)))
clear_matrix_b_button.configure(command=lambda: root.after(time_quantum, lambda: begin_clear_cells(matrix_b)))

reset_matrices_button.configure(command=lambda: root.after(time_quantum, reset_matrices))

fill_a_zero_button.configure(command=lambda: root.after(time_quantum, lambda:fill_cell_values_zero(matrix_a)))
fill_zero_b_button.configure(command=lambda: root.after(time_quantum, lambda:fill_cell_values_zero(matrix_b)))

show_frame(f1)
root.mainloop()

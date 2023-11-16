from tkinter import Tk
import ui.landingPageGUI as landingPageGUI
import ui.setMatrixSizeGUI as setMatrixSizeGUI
import ui.setMatrixDataGUI as setMatrixDataGUI

root = Tk()
root.geometry("1280x720")
root.configure(bg="#FFFFFF")
root.resizable(False, False)

current_frame = None


def show_frame(frame_to_show):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    current_frame = frame_to_show
    frame_to_show.pack(fill="both", expand=True)


landing_page = landingPageGUI.landing_page_start(root)
set_matrix_size = setMatrixSizeGUI.set_matrix_size_start(root)
set_matrix_data = setMatrixDataGUI.set_matrix_data_start(root)

f1 = landing_page
f2 = set_matrix_size
f3 = set_matrix_data

landing_page_button = landing_page.start_button
landing_page_button.bind("<Button-1>", lambda event: root.after(500, lambda: show_frame(f2)))

size_submit_button = set_matrix_size.size_submit_button
size_submit_button.bind("<Button-1>", lambda event: root.after(500, lambda: show_frame(f3)))

show_frame(f1)
root.mainloop()

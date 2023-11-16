from tkinter import Tk
import ui.landingPageGUI as landingPageGUI
import ui.setMatrixSizeGUI as setMatrixSizeGUI

root = Tk()
root.geometry("1280x720")
root.configure(bg="#FFFFFF")

current_frame = None


def show_frame(frame_to_show):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    current_frame = frame_to_show
    frame_to_show.pack(fill="both", expand=True)


landing_page = landingPageGUI.landing_page_start(root)
set_matrix_size = setMatrixSizeGUI.set_matrix_size_start(root)

f1 = landing_page
f2 = set_matrix_size

landing_page_button = landing_page.button_1
landing_page_button.bind("<Button-1>", lambda event: show_frame(f2))

show_frame(f1)
root.mainloop()

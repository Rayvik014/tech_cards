import tkinter
import graphic_services as GServices

def main_window():
    window = tkinter.Tk()
    window.title = 'Cards for kids'
    window.geometry('800x600')

    buttons_box_frame = tkinter.Frame(window, padx=10, pady=10)
    preview_image_frame = tkinter.Frame(window, padx=10, pady=70)
    buttons_box_frame.pack(expand=False)
    preview_image_frame.pack(expand=False)

    change_1_button = tkinter.Button(buttons_box_frame, text="Change 1")
    change_1_button.grid(row=1, column=1)
    change_2_button = tkinter.Button(buttons_box_frame, text="Change 2")
    change_2_button.grid(row=1, column=2)
    change_3_button = tkinter.Button(buttons_box_frame, text="Change 3")
    change_3_button.grid(row=1, column=3)
    change_4_button = tkinter.Button(buttons_box_frame, text="Change 4")
    change_4_button.grid(row=1, column=4)

    save_button = tkinter.Button(buttons_box_frame, text="Save result")
    save_button.grid(row=2, column=1)
    newl_button = tkinter.Button(buttons_box_frame, text="New list")
    newl_button.grid(row=2, column=2)

    preview_image_binary = GServices.make_preview_image_binary()
    canvas = tkinter.Canvas(window, width=640, height=480)
    canvas.pack()
    img = tkinter.PhotoImage(data=preview_image_binary, format='png')
    canvas.create_image(20, 20, anchor=tkinter.NW, image=img)
    

    window.mainloop()



if __name__ == "__main__":
    main_window()
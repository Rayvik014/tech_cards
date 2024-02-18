import PySimpleGUI as sg 
import graphic_services as GServices

def main_window():
    preview_image_binary = GServices.make_preview_image_binary()

    layout = [ [sg.Button('Change 1'), sg.Button('Change 2'), sg.Button('Change 3'), sg.Button('Change 4')],
               [sg.Button('Save Result'), sg.Button('New list')],
               [sg.Image(data=preview_image_binary)] ]

    window = sg.Window('Cards for Kids', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main_window()
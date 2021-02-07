from dramakul import name as package_name, __version__
import PySimpleGUI as sg

layout = [[sg.Text(package_name)], [sg.Text(__version__)]]


def gui():
    window = sg.Window(package_name, layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

    window.close()

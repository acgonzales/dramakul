import PySimpleGUI as sg

from dramakul import name as package_name, __version__


def watch_gui():
    layout = [[sg.Text(package_name)], [sg.Text(__version__)]]

    window = sg.Window(package_name + " Watch", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

    window.close()


def download_gui():
    layout = [[sg.Text(package_name)], [sg.Text(__version__)]]

    window = sg.Window(package_name + " Download", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

    window.close()


def config_gui():
    layout = [[sg.Text(package_name)], [sg.Text(__version__)]]

    window = sg.Window(package_name + " Config", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

    window.close()

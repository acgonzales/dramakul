import PySimpleGUI as sg

from dramakul import name as package_name, __version__
from dramakul.util import play_on_mpv
from dramakul.sites import SITES, get_site

SITE_NAMES = [site.name for site in SITES]

THEME = "DarkAmber"
LABEL_SIZE = (10, 1)
INPUT_SIZE = (30, 1)
BUTTON_SIZE = (10, 1)
LISTBOX_SIZE = (25, 15)

window_title = f"{package_name} {__version__}"
window_heading = package_name

sg.theme(THEME)


def watch_gui():
    browse_layout = [
        [sg.Text("Search query:", size=LABEL_SIZE),
         sg.Input("", key="-QUERY-", size=INPUT_SIZE)],
        [sg.Text("Source", size=LABEL_SIZE), sg.Combo(SITE_NAMES, SITE_NAMES[0], key="-SOURCE-", size=(INPUT_SIZE[0] - 2, 1)), sg.Button(
            "Search", key="-SEARCH-", size=BUTTON_SIZE)],
        [sg.Text("_" * 60)],
        [sg.Text("Drama URL:", size=LABEL_SIZE),
         sg.Input("", key="-URL-", size=INPUT_SIZE), sg.Button("Go", key="-DRAMA_GET-", size=BUTTON_SIZE)]
    ]

    dramas_layout = [
        [sg.Listbox([], size=LISTBOX_SIZE, key="-DRAMAS-",
                    enable_events=True, disabled=True)]
    ]

    episodes_layout = [
        [sg.Listbox([], select_mode="multiple", size=LISTBOX_SIZE,
                    key="-EPISODES-", disabled=True)]
    ]

    layout = [
        [sg.Text(package_name + " Watch", font=("Any", 20))],
        [sg.Frame("Browse / Search", browse_layout)],
        [sg.Frame("Dramas", dramas_layout, key="-RESULTS-"),
         sg.VerticalSeparator(), sg.Frame("Episodes", episodes_layout)],
        [sg.Button("Play", key="-PLAY-")]
    ]

    window = sg.Window(window_title + " - Watch", layout)

    dramas_listbox = window["-DRAMAS-"]
    episodes_listbox = window["-EPISODES-"]

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

        print(event)

        if event == "-SEARCH-":
            episodes_listbox.update(disabled=True)

            query = values["-QUERY-"]
            source = values["-SOURCE-"]

            site = get_site(source)
            results = site.search(query)

            dramas_listbox.update(results, disabled=False)
        elif event == "-DRAMA_GET-":
            episodes_listbox.update(disabled=True)

            drama_url = values["-URL-"]

            try:
                site = get_site(drama_url)

                if not site:
                    raise ValueError(
                        "Can't find any dramas in that URL. Its either we don't currently support that website or the URL is invalid.")

                drama = site.get_info(drama_url)

                dramas_listbox.update([drama])
                episodes_listbox.update(drama.episodes, disabled=False)
            except Exception as e:
                sg.Popup(
                    str(e), title="An error occured!")
        elif event == "-DRAMAS-":
            selected_result = values["-DRAMAS-"][0]

            drama = selected_result.get_info()
            episodes_listbox.update(drama.episodes, disabled=False)
        elif event == "-PLAY-":
            # TODO: Video player process on other thread

            sorted_episodes = sorted(values["-EPISODES-"])
            urls = [
                episode.stream_url for episode in sorted_episodes]

            sg.Popup(f"Playing {len(sorted_episodes)} episodes. Have fun!")

            p = play_on_mpv(urls)
            p.wait()

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

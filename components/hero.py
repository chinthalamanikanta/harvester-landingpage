from nicegui import ui
from translations import translations

selected_language = ui.select(

    ["en","hi","te"],

    value="en",

    label="Language"

).classes("w-40")

def t(key):

    return translations[selected_language.value][key]

def create_hero():

    with ui.row().classes(
        "w-full min-h-screen items-center justify-between px-24 bg-gradient-to-r from-green-50 to-green-100"
    ).props("id=hero"):

        ##################################################
        # LEFT SIDE
        ##################################################

        with ui.column().classes("w-1/2"):

            ui.label((
                "Harvest Smarter")
            ).classes(
                "text-7xl font-extrabold text-green-800"
            )

            ui.label(
                "India's Digital Platform Connecting Farmers with Harvester Owners."
            ).classes(
                "text-xl text-gray-700 mt-6"
            )

            with ui.row().classes("gap-4 mt-10"):

                ui.button(
                    "Book Harvester",
                    icon="agriculture",
                    color="green",
                )

                # ui.button(
                #     "Download APK",
                #     icon="download",
                #     color="orange",
                # )

            with ui.row().classes("gap-10 mt-14"):

                # ui.card().classes("p-6 shadow-xl") \
                #     .style("min-width:150px") \
                #     .tight()

                with ui.card().classes("p-5 w-40 items-center"):

                    ui.label("150+" ).classes("text-4xl text-green-700 font-bold")
                    ui.label("Farmers")

                with ui.card().classes("p-5 w-40 items-center"):

                    ui.label("40+" ).classes("text-4xl text-green-700 font-bold")
                    ui.label("Machines")

                with ui.card().classes("p-5 w-40 items-center"):

                    ui.label("2").classes("text-4xl text-green-700 font-bold")
                    ui.label("Districts")

        ##################################################
        # RIGHT SIDE
        ##################################################

        with ui.column().classes(
            "items-center justify-center"
        ):

            ui.image(
                "static/screenshots/home.png"
            ).classes(
                "w-80 rounded-3xl shadow-2xl"
            )

            ui.label(
                "Android Mobile App"
            ).classes(
                    "text-2xl font-bold mt-4"
            )
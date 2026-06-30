# from nicegui import ui

# def create_navbar():

#     with ui.header().classes(
#         "bg-white shadow-lg items-center justify-between px-10 py-4"
#     ):

#         with ui.row().classes("items-center gap-3"):

#             ui.icon("agriculture", color="green").classes("text-4xl")

#             ui.label(
#                 "Harvester Connect"
#             ).classes(
#                 "text-2xl font-bold text-green-700"
#             )

#         with ui.row().classes("items-center gap-8"):

#             ui.link("Home", "#hero")

#             ui.link("About", "#about")

#             ui.link("Features", "#features")

#             ui.link("Farmers", "#farmers")

#             ui.link("Owners", "#owners")

#             ui.link("Contact", "#contact")

#             ui.select(
#                 ["English", "తెలుగు", "हिन्दी"],
#                 value="English",
#             ).props("dense outlined")

#             ui.switch().props("color=green").tooltip("Dark Mode")

from nicegui import ui
dark = ui.dark_mode()

def create_navbar():

    with ui.header().classes(
        """
        bg-white
        shadow-md
        items-center
        justify-between
        px-10
        py-3
        fixed
        top-0
        z-50
        """
    ):

        #################################################
        # LEFT LOGO
        #################################################

        with ui.row().classes(
            "items-center gap-3"
        ):

            ui.icon(
                "agriculture",
                color="green",
            ).classes(
                "text-5xl"
            )

            with ui.column().classes("gap-0"):

                ui.label(
                    "Harvester Connect"
                ).classes(
                    "text-2xl font-bold text-green-700"
                )

                ui.label(
                    "Smart Agriculture Platform"
                ).classes(
                    "text-xs text-gray-500"
                )

        #################################################
        # CENTER MENU
        #################################################

        with ui.row().classes(
            "items-center gap-8 text-lg"
        ):

            ui.link(
                "🏠 Home",
                "#hero",
            ).classes(
                "text-gray-700 hover:text-green-700 no-underline font-medium"
            )

            ui.link(
                "ℹ About",
                "#about",
            ).classes(
                "text-gray-700 hover:text-green-700 no-underline font-medium"
            )

            ui.link(
                "⭐ Features",
                "#features",
            ).classes(
                "text-gray-700 hover:text-green-700 no-underline font-medium"
            )

            ui.link(
                "🚜 Farmers",
                "#farmers",
            ).classes(
                "text-gray-700 hover:text-green-700 no-underline font-medium"
            )

            ui.link(
                "👨‍🌾 Owners",
                "#owners",
            ).classes(
                "text-gray-700 hover:text-green-700 no-underline font-medium"
            )

            ui.link(
                "📞 Contact",
                "#contact",
            ).classes(
                "text-gray-700 hover:text-green-700 no-underline font-medium"
            )

        #################################################
        # RIGHT
        #################################################

        with ui.row().classes(
            "items-center gap-4"
        ):

            ui.select(

                [
                    "English",
                    "తెలుగు",
                    "हिन्दी",
                ],

                value="English",

            ).props(
                "dense outlined"
            ).classes(
                "w-36"
            )

            

           
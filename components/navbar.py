from nicegui import ui

dark = ui.dark_mode()


def create_navbar():

    ############################################################
    # Mobile Drawer
    ############################################################

    with ui.left_drawer(value=False).classes("bg-white w-72 shadow-xl") as drawer:

        ui.label("Harvester Connect").classes(
            "text-2xl font-bold text-green-700 px-6 pt-6"
        )

        ui.separator().classes("my-4")

        links = [
            ("🏠 Home", "#hero"),
            ("ℹ About", "#about"),
            ("⭐ Features", "#features"),
            ("🚜 Farmers", "#farmers"),
            ("👨‍🌾 Owners", "#owners"),
            ("📞 Contact", "#contact"),
        ]

        for text, target in links:
            ui.link(text, target).classes(
                """
                block
                px-6
                py-3
                text-lg
                no-underline
                text-gray-700
                hover:bg-green-50
                hover:text-green-700
                rounded-lg
                transition-all
                """
            )

        ui.separator().classes("my-4")

        ui.select(
            ["English", "తెలుగు", "हिन्दी"],
            value="English",
        ).props("outlined dense").classes("mx-5")

        ui.switch(
            "Dark Mode",
            value=False,
            on_change=lambda e: dark.set_value(e.value),
        ).classes("mx-5 mt-4")

    ############################################################
    # Header
    ############################################################

    with ui.header().classes("""
        bg-white
        shadow-md
        fixed
        top-0
        left-0
        right-0
        z-50
        px-4
        sm:px-6
        md:px-8
        lg:px-10
        py-3
        items-center
        justify-between
    """):

        ########################################################
        # Left
        ########################################################

        with ui.row().classes("items-center gap-3"):

            ui.button(
                icon="menu",
                on_click=drawer.toggle,
            ).props(
                "flat round"
            ).classes(
                "lg:hidden"
            )

            ui.icon(
                "agriculture",
                color="green",
            ).classes(
                """
                text-3xl
                sm:text-4xl
                md:text-5xl
                """
            )

            with ui.column().classes("gap-0"):

                ui.label(
                    "Harvester Connect"
                ).classes(
                    """
                    text-lg
                    sm:text-xl
                    md:text-2xl
                    font-bold
                    text-green-700
                    """
                )

                ui.label(
                    "Smart Agriculture Platform"
                ).classes(
                    """
                    hidden
                    sm:block
                    text-xs
                    text-gray-500
                    """
                )

        ########################################################
        # Desktop Menu
        ########################################################

        with ui.row().classes("""
            hidden
            lg:flex
            items-center
            gap-6
            xl:gap-8
            text-base
            xl:text-lg
        """):

            menu = [
                ("🏠 Home", "#hero"),
                ("ℹ About", "#about"),
                ("⭐ Features", "#features"),
                ("🚜 Farmers", "#farmers"),
                ("👨‍🌾 Owners", "#owners"),
                ("📞 Contact", "#contact"),
            ]

            for text, link in menu:

                ui.link(text, link).classes("""
                    text-gray-700
                    hover:text-green-700
                    no-underline
                    font-medium
                    transition-colors
                    duration-200
                """)

        ########################################################
        # Right
        ########################################################

        with ui.row().classes("""
            hidden
            md:flex
            items-center
            gap-3
        """):

            ui.select(
                [
                    "English",
                    "తెలుగు",
                    "हिन्दी",
                ],
                value="English",
            ).props(
                "outlined dense"
            ).classes(
                "w-32"
            )

            ui.switch().props(
                "color=green"
            ).tooltip(
                "Dark Mode"
            ).on(
                "update:model-value",
                lambda e: dark.set_value(e.args),
            )

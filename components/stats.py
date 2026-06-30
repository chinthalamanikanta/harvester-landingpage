from nicegui import ui


def stat_card(icon, color, number, title):

    with ui.card().classes(
        "w-60 p-6 items-center shadow-xl rounded-xl hover:scale-105 transition-all duration-300"
    ):

        ui.icon(icon, color=color).classes("text-6xl")

        ui.label(f"{number}+").classes(
            "text-5xl font-bold text-green-700 mt-3"
        )

        ui.label(title).classes(
            "text-lg text-gray-600 mt-2"
        )


def create_stats():

    with ui.column().classes(
        "w-full items-center py-14 bg-white"
    ).props("id=stats"):

        ui.label(
            "Trusted Across Telangana"
        ).classes(
            "text-5xl font-bold text-green-800"
        )

        ui.label(
            "Growing every day with happy farmers and machine owners."
        ).classes(
            "text-lg text-gray-600 mt-4 mb-12"
        )

        with ui.row().classes(
            "justify-center gap-8 flex-wrap"
        ):

            stat_card(
                "agriculture",
                "green",
                40,
                "Machines"
            )

            stat_card(
                "groups",
                "blue",
                50,
                "Farmers"
            )

            stat_card(
                "calendar_month",
                "orange",
                100,
                "Bookings"
            )

            stat_card(
                "star",
                "amber",
                5,
                "Average Rating"
            )
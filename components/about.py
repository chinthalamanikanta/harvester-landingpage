from nicegui import ui


def create_about():

    with ui.column().classes(
        "w-full items-center py-14 bg-white"
    ).props("id=about"):

        ui.label(
            "Why Choose Harvester Connect?"
        ).classes(
            "text-5xl font-bold text-green-800"
        )

        ui.label(
            "Connecting Farmers and Machine Owners through technology."
        ).classes(
            "text-lg text-gray-600 mt-4 mb-12"
        )

        with ui.row().classes(
            "gap-8 justify-center flex-wrap"
        ):

            ##############################

            with ui.card().classes(
                "w-72 p-6 shadow-xl hover:shadow-2xl"
            ):

                ui.icon(
                    "agriculture",
                    color="green"
                ).classes("text-5xl")

                ui.label(
                    "For Farmers"
                ).classes(
                    "text-2xl font-bold mt-4"
                )

                ui.label(
                    "Find nearby harvesters quickly and book them in just a few clicks."
                ).classes(
                    "text-gray-600 mt-2"
                )

            ##############################

            with ui.card().classes(
                "w-72 p-6 shadow-xl hover:shadow-2xl"
            ):

                ui.icon(
                    "engineering",
                    color="orange"
                ).classes("text-5xl")

                ui.label(
                    "Machine Owners"
                ).classes(
                    "text-2xl font-bold mt-4"
                )

                ui.label(
                    "Receive more bookings and increase your earnings with digital visibility."
                ).classes(
                    "text-gray-600 mt-2"
                )

            ##############################

            with ui.card().classes(
                "w-72 p-6 shadow-xl hover:shadow-2xl"
            ):

                ui.icon(
                    "notifications",
                    color="blue"
                ).classes("text-5xl")

                ui.label(
                    "Instant Notifications"
                ).classes(
                    "text-2xl font-bold mt-4"
                )

                ui.label(
                    "Get real-time booking updates, approvals, and alerts instantly."
                ).classes(
                    "text-gray-600 mt-2"
                )

            ##############################

            with ui.card().classes(
                "w-72 p-6 shadow-xl hover:shadow-2xl"
            ):

                ui.icon(
                    "location_on",
                    color="red"
                ).classes("text-5xl")

                ui.label(
                    "Nearby Machines"
                ).classes(
                    "text-2xl font-bold mt-4"
                )

                ui.label(
                    "Locate available harvesters near your village using GPS."
                ).classes(
                    "text-gray-600 mt-2"
                )
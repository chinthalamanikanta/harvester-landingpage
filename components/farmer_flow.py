from nicegui import ui


def step(icon, color, title, description):

    with ui.card().classes(
        "w-60 p-5 shadow-lg rounded-xl items-center hover:shadow-2xl transition-all duration-300"
    ):

        ui.icon(
            icon,
            color=color,
        ).classes(
            "text-5xl"
        )

        ui.label(title).classes(
            "text-xl font-bold mt-3"
        )

        ui.label(description).classes(
            "text-center text-gray-600 mt-2"
        )


def arrow():

    ui.icon(
        "arrow_forward",
        color="green",
    ).classes(
        "text-4xl mt-16"
    )


def create_farmer_flow():

    with ui.column().classes(
        "w-full items-center py-14 bg-white"
    ).props("id=farmers"):

        ui.label(
            "Farmer Journey"
        ).classes(
            "text-5xl font-bold text-green-800"
        )

        ui.label(
            "Book a Harvester in just a few simple steps."
        ).classes(
            "text-lg text-gray-600 mt-4 mb-12"
        )

        #####################################################

        with ui.row().classes(
            "justify-center items-start gap-4 flex-wrap"
        ):

            step(
                "person_add",
                "green",
                "1. Register",
                "Create your free farmer account."
            )

            arrow()

            step(
                "search",
                "blue",
                "2. Search",
                "Find nearby harvesters."
            )

            arrow()

            step(
                "compare",
                "orange",
                "3. Compare",
                "Compare prices and machine details."
            )

        #####################################################

        with ui.row().classes(
            "justify-center items-start gap-4 mt-10 flex-wrap"
        ):

            step(
                "calendar_month",
                "purple",
                "4. Book",
                "Select your preferred harvesting date."
            )

            arrow()

            step(
                "notifications",
                "red",
                "5. Get Updates",
                "Receive booking approval instantly."
            )

            arrow()

            step(
                "star",
                "amber",
                "6. Rate",
                "Rate the machine owner after work."
            )
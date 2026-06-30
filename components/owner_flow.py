from nicegui import ui


def owner_step(icon, color, title, description):

    with ui.card().classes(
        "w-60 p-5 shadow-lg rounded-xl items-center hover:shadow-2xl transition-all duration-300"
    ):

        ui.icon(
            icon,
            color=color,
        ).classes(
            "text-5xl")

        ui.label(title).classes(
            "text-xl font-bold mt-3")

        ui.label(description).classes(
            "text-center text-gray-600 mt-2")


def arrow():
    ui.icon(
        "arrow_forward",
        color="green",
    ).classes(
        "text-4xl mt-16")


def create_owner_flow():

    with ui.column().classes(
        "w-full items-center py-24 bg-green-50"
    ).props("id=owners"):

        ui.label(
            "Machine Owner Journey"
        ).classes(
            "text-5xl font-bold text-green-800"
        )

        ui.label(
            "Earn more by connecting directly with nearby farmers."
        ).classes(
            "text-lg text-gray-600 mt-4 mb-12"
        )

        ########################################################

        with ui.row().classes(
            "justify-center items-start gap-4 flex-wrap"
        ):

            owner_step(
                "person_add",
                "green",
                "1. Register",
                "Create your owner account."
            )

            arrow()

            owner_step(
                "agriculture",
                "orange",
                "2. Add Machine",
                "Upload harvester details and price."
            )

            arrow()

            owner_step(
                "photo_camera",
                "blue",
                "3. Upload Photos",
                "Show your machine to attract farmers."
            )

        ########################################################

        with ui.row().classes(
            "justify-center items-start gap-4 mt-10 flex-wrap"
        ):

            owner_step(
                "notifications_active",
                "red",
                "4. Receive Booking",
                "Get notified instantly."
            )

            arrow()

            owner_step(
                "check_circle",
                "green",
                "5. Accept Booking",
                "Approve or reject requests."
            )

            arrow()

            owner_step(
                "payments",
                "purple",
                "6. Earn Money",
                "Complete harvesting and receive payment."
            )
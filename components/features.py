from nicegui import ui


def feature_card(icon, color, title, description):

    with ui.card().classes(
        "w-72 p-6 shadow-lg hover:shadow-2xl transition-all duration-300 rounded-xl"
    ):

        ui.icon(
            icon,
            color=color,
        ).classes("text-5xl")

        ui.label(title).classes(
            "text-2xl font-bold mt-4"
        )

        ui.label(description).classes(
            "text-gray-600 mt-2"
        )


def create_features():

    with ui.column().classes(
        "w-full items-center py-14 bg-green-50"
    ).props("id=features"):

        ui.label(
            "Powerful Features"
        ).classes(
            "text-5xl font-bold text-green-800"
        )

        ui.label(
            "Everything you need to simplify harvesting."
        ).classes(
            "text-lg text-gray-600 mt-4 mb-12"
        )

        ################################################

        with ui.row().classes(
            "gap-8 justify-center flex-wrap"
        ):

            feature_card(
                "calendar_month",
                "green",
                "Easy Booking",
                "Book harvesters in just a few clicks."
            )

            feature_card(
                "location_on",
                "red",
                "Nearby Machines",
                "Find available machines near your village."
            )

            feature_card(
                "notifications",
                "orange",
                "Live Notifications",
                "Receive instant booking updates."
            )

            feature_card(
                "payments",
                "blue",
                "Secure Payments",
                "Safe and transparent transactions."
            )

        ################################################

        with ui.row().classes(
            "gap-8 justify-center flex-wrap mt-8"
        ):

            feature_card(
                "history",
                "purple",
                "Booking History",
                "View all your previous bookings."
            )

            feature_card(
                "star",
                "amber",
                "Ratings",
                "Rate farmers and machine owners."
            )

            feature_card(
                "dashboard",
                "teal",
                "Dashboard",
                "Track earnings and booking statistics."
            )

            feature_card(
                "language",
                "indigo",
                "Multi-language",
                "English, Telugu & Hindi support."
            )
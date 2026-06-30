from nicegui import ui


def section_heading(title: str, subtitle: str = ""):
    """Reusable centered section heading"""

    # ui.separator().classes("w-full mt-10")

    with ui.column().classes("w-full items-center py-8"):

        ui.label(title).classes(
            "text-4xl font-bold text-green-700 text-center"
        )

        if subtitle:
            ui.label(subtitle).classes(
                "text-lg text-gray-600 text-center max-w-3xl"
            )


def testimonials_section():

    section_heading(
        "❤️ Loved by Farmers & Machine Owners",
        "See what our users are saying about Harvester Connect."
    )

    testimonials = [

        {
            "name": "Bandaru Nageshwar Rao",
            "role": "Farmer",
            "comment": "Very easy booking. I found a harvester in just 2 minutes."
        },

        {
            "name": "Ch Suresh",
            "role": "Machine Owner",
            "comment": "Now my harvester gets bookings every week."
        },

        {
            "name": "Yerra Keshavllu",
            "role": "Farmer",
            "comment": "Excellent app. Saves time and money."
        }

    ]

    with ui.row().classes(
        "w-full justify-center gap-8 flex-wrap"
    ):

        for t in testimonials:

            with ui.card().classes(
                "w-80 shadow-xl rounded-xl p-5"
            ):

                ui.label("⭐⭐⭐⭐⭐").classes(
                    "text-yellow-500 text-xl"
                )

                ui.label(
                    t["comment"]
                ).classes(
                    "text-gray-700 mt-3"
                )

                ui.separator()

                ui.label(
                    t["name"]
                ).classes(
                    "font-bold text-lg"
                )

                ui.label(
                    t["role"]
                ).classes(
                    "text-gray-500"
                )


def stats_section():
    with ui.column().classes(
        "w-full bg-green-50 py-10 mt-10"
    ):

        section_heading(
            "📈 Harvester Connect in Numbers"
        )

        stats = [

            ("250+", "Farmers"),

            ("50+", "Machine Owners"),

            ("800+", "Bookings"),

            ("20+", "Cities"),

        ]

        with ui.row().classes(
            "w-full justify-center gap-12 mt-8 flex-wrap"
        ):

            for number, title in stats:

                with ui.card().classes(
                    "w-48 h-40 shadow-lg items-center justify-center"
                ):

                    ui.label(number).classes(
                        "text-5xl font-bold text-green-600"
                    )

                    ui.label(title).classes(
                        "text-xl font-medium"
                    )


def trust_section():

    section_heading(
        "🌾 Why Farmers Trust Harvester Connect?"
    )

    data = [

        ("🔒", "Secure Booking"),

        ("⚡", "Instant Notifications"),

        ("📍", "Nearby Machines"),

        ("💰", "Affordable Pricing"),

        ("⭐", "Verified Owners"),

        ("🌾", "Made for Indian Farmers"),

    ]

    with ui.row().classes(
        "justify-center gap-8 mt-8 flex-wrap"
    ):

        for icon, title in data:

            with ui.card().classes(
                "w-60 h-40 shadow-lg items-center justify-center rounded-xl"
            ):

                ui.label(icon).classes(
                    "text-5xl"
                )

                ui.label(title).classes(
                    "text-lg font-bold mt-3 text-center"
                )
from nicegui import ui


def contact_section():

    with ui.column().classes(
        "w-full bg-green-50 py-16 px-6 mt-8"
    ).props('id=contact'):
        # ui.separator().classes("w-full")

        # Heading
        with ui.column().classes("w-full items-center mb-10"):

            ui.label("📞 Contact Us").classes(
                "text-4xl font-bold text-green-700 text-center"
            )

            ui.label(
                "We're here to help farmers and machine owners across India."
            ).classes(
                "text-lg text-gray-600 text-center max-w-3xl"
            )

        # Cards
        with ui.row().classes(
            "w-full justify-center gap-10 flex-wrap"
        ):

            # Owners
            with ui.card().classes(
                "w-96 shadow-2xl rounded-2xl p-6"
            ):

                ui.label("👨‍💻 Founders").classes(
                    "text-2xl font-bold text-green-700 text-center w-full"
                )

                ui.separator()

                ui.label(
                    "Bandaru Venkata Krishna"
                ).classes(
                    "text-xl font-bold text-center w-full"
                )

                ui.label(
                    "Chinthala Manikanta"
                ).classes(
                    "text-xl font-bold text-center w-full"
                )

                ui.separator()

                ui.label(
                    "Harvester Connect connects farmers and machine owners through a simple, secure and transparent digital platform."
                ).classes(
                    "text-center text-gray-700 mt-3"
                )

            # Contact
            with ui.card().classes(
                "w-96 shadow-2xl rounded-2xl p-6"
            ):

                ui.label("📞 Contact Information").classes(
                    "text-2xl font-bold text-green-700 text-center w-full"
                )

                ui.separator()

                ui.label("📧 Email").classes("font-bold")
                ui.link(
                    "krishnabandaru@gmail.com",
                    "mailto:krishnabandaru@gmail.com"
                )

                ui.separator()

                ui.label("📱 Phone").classes("font-bold")

                ui.label("+91 78937 78882")

                ui.separator()

                ui.label("📍 Location").classes("font-bold")

                ui.label(
                    "Konijerla Village,\nKonijerla Mandal,\nKhammam District,\nTelangana - 507305,\nIndia"
                )

        ui.separator().classes("w-full mt-12")

        with ui.column().classes(
            "w-full items-center"
        ):

            ui.label(
                "© 2026 Harvester Connect"
            ).classes(
                "text-xl font-bold text-green-700"
            )

            ui.label(
                "Built with ❤️ by Bandaru Venkata Krishna"
            ).classes(
                "text-gray-600"
            )
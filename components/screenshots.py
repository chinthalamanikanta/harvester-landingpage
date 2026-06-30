from nicegui import ui

screens = [
    ("Login", "/static/screenshots/login.png"),
    ("Home", "/static/screenshots/home.png"),
    ("Machines", "/static/screenshots/machines.png"),
    ("Booking", "/static/screenshots/booking.png"),
    ("Notifications", "/static/screenshots/notifications.png"),
    ("Profile", "/static/screenshots/profile.png"),
]


def phone_mockup(title, image):

    with ui.card().classes(
        "w-82 items-center p-5 rounded-3xl shadow-2xl hover:scale-105 transition-all duration-300"
    ):

        ui.label(title).classes(
            "text-xl font-bold text-green-700 mb-4"
        )

        ui.image(image).classes(
            "rounded-2xl border-0 border-black"
        ).style(
            "width:290px;height:460px;object-fit:cover;"
        )


def create_screenshots():

    with ui.column().classes(
        "w-full items-center py-14 bg-green-50"
    ).props("id=screenshots"):

        ui.label(
            "Application Screens"
        ).classes(
            "text-5xl font-bold text-green-800"
        )

        ui.label(
            "Simple • Fast • Secure"
        ).classes(
            "text-lg text-gray-600 mt-3 mb-10"
        )

        with ui.row().classes(
            "justify-center gap-8 flex-wrap"
        ):

            for title, image in screens:
                phone_mockup(title, image)
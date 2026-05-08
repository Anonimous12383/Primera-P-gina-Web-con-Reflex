
"""Welcome to Jhoan's page! This file outlines the steps to create a basic app."""

import reflex as rx


class State(rx.State):
    """The app state."""

    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Jhoan's Page!", size="9"),
            rx.hstack(
                rx.button(
                    "Decrement",
                    color_scheme="ruby",
                    on_click=State.decrement,
                ),
                rx.heading(State.count, font_size="2em"),
                rx.button(
                    "Increment",
                    color_scheme="grass",
                    on_click=State.increment,
                ),
                spacing="4",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)


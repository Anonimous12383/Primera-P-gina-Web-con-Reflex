"""Mi primera página web con Reflex."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """El estado de la aplicación."""

    mensaje: str = "¡Bienvenido a mi primera página web con Reflex!"
    count: int = 0

    @rx.event
    def cambiar_mensaje(self):
        self.mensaje = "¡Hiciste clic! Funciona correctamente."

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            # Título principal
            rx.heading(
                "¡Bienvenido a la Jhoan's Page!",
                size="9",
            ),

            rx.text(
                "Esta página fue creada con Reflex, "
                "un framework para el desarrollo web.",
                size="5",
                color="gray",
            ),

            # Mensaje dinámico
            rx.text(
                State.mensaje,
                size="4",
                weight="bold",
                color="violet",
            ),

            # Botón para cambiar mensaje
            rx.button(
                "¡Haz clic aquí!",
                on_click=State.cambiar_mensaje,
                color_scheme="violet",
                size="3",
                radius="full",
            ),

            # Contador
            rx.hstack(
                rx.button(
                    "Decrementar",
                    on_click=State.decrement,
                    color_scheme="ruby",
                ),

                rx.heading(
                    State.count,
                    size="7",
                ),

                rx.button(
                    "Incrementar",
                    on_click=State.increment,
                    color_scheme="grass",
                ),

                spacing="4",
            ),

            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    )


app = rx.App()
app.add_page(index, title="Página de Jhoan con Reflex")
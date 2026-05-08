import reflex as rx

config = rx.Config(
    app_name="Mi_Primera_Pagina_de_Reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
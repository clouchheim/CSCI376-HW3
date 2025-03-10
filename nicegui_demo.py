from nicegui import ui

with ui.row().classes("mx-auto"): # container for cards, put styling rules in the classes
    with ui.card(): # this uses a card organizer
        input_field = ui.input(on_change=lambda e: result.set_text(e.value.lower()))
        result = ui.label() # stand in

ui.run() # essential to run the code 
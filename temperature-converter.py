from nicegui import ui

ui.colors(
      primary='#e44a29',
      secondary='#99ad62',
      accent='#2972b6',
      positive='#f26676',
      negative='#a2e0b0',
      info='#91c2dd',
      warning='#f8dc2b'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F") # this sets the empty text in result_lable later
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mx-auto")
        # text-positive: Uses the 'positive' color from ui.colors 
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold !text-negative mt-auto")
        # text-negative: Uses the 'negative' color from ui.colors 

def convert_2():
     

with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-white border border-gray-300"):
        # w-100: Set element width to be fixed at 100
        # p-6: Adds padding of 6 units
        # shadow-xl: Adds extra-large shadow effect
        # mx-auto: Centers the element horizontally
        # mt-10: Adds top margin of 10 units
        # rounded-xl: Applies extra-large border radius for rounded corners
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: Sets text size to extra-large
        # font-bold: Makes text bold
        # text-accent: Uses the 'accent' color from ui.colors
        # mb-4: Adds bottom margin of 4 units
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded focus:ring-2 focus:ring-accent")
        # w-full: Makes the input take full width
        # border: Adds a border around the input field
        # rounded: Rounds the corners slightly
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: Ensures button text is white for contrast
        # py-2: Adds vertical padding
        # px-4: Adds horizontal padding
        result_label = ui.label("").classes("text-lg font-bold mt-4")
        
    # STEP 4: NEW INPUT TYPE
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-white border border-gray-300"):
        ui.label("Temperature Converter #2").classes("text-2xl font-bold text-accent mb-4")
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded focus:ring-2 focus:ring-accent")
        
        


ui.run()
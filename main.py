import tkinter as tk
import random

# List of meme-inspired error messages
error_messages = [
    "Error: i-forgor to load the page 💀",
    "404: File Not Found, but we might’ve misplaced it in the void",
    "500: Server's taking a nap. Please try again later",
    "Error: i-forgor to install this app. Oops 💀",
    "404: Wi-Fi not found. Have you tried turning it off and on again?",
    "Critical Error: Your app crashed because it decided it’s too fancy for this.",
    "Oops! Looks like your computer has lost all sense of reality.",
    "Error: Your computer is now in a digital void. Don't panic.",
    "Application Error: Your app has evolved into a sentient being and refuses to run.",
    "404: The file is hiding from you. Maybe it’s on vacation."
]

# Function to generate a random meme-inspired error
def generate_error():
    error = random.choice(error_messages)
    error_label.config(text=error)

# Function to generate a custom error entered by the user
def generate_custom_error():
    error_message = custom_error_input.get()
    if error_message:
        error_label.config(text=error_message)
    else:
        error_label.config(text="Please enter a custom error message.")

# Create the main window
root = tk.Tk()
root.title("i-forgor Error Generator 💀")

# Create the UI components
error_label = tk.Label(root, text="Click 'Generate Error' to get an error", font=('Arial', 12), width=50, height=4)
generate_button = tk.Button(root, text="Generate Meme Error", command=generate_error, font=('Arial', 12))

# Custom Error input field and button
custom_error_input = tk.Entry(root, font=('Arial', 12), width=50)
generate_custom_button = tk.Button(root, text="Generate Custom Error", command=generate_custom_error, font=('Arial', 12))

# Layout the components
error_label.pack(pady=20)
generate_button.pack(pady=10)
custom_error_input.pack(pady=10)
generate_custom_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

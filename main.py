import tkinter as tk
import random

# Global variables
balance = 0

# Function to generate a random fruit
def generate_fruit():
    fruits = [0, 1, 2, 3, 4]  # Updated with numbers
    return random.choice(fruits)

# Function to handle the spin button click event
def spin():
    global balance

    # Generate fruits for each column
    fruit1 = generate_fruit()
    fruit2 = generate_fruit()
    fruit3 = generate_fruit()
    fruit4 = generate_fruit()

    column1.configure(image=fruit_images[fruit1])
    column2.configure(image=fruit_images[fruit2])
    column3.configure(image=fruit_images[fruit3])
    column4.configure(image=fruit_images[fruit4])

    # Check for winning combination
# Check for winning combination
    if fruit1 == fruit2 or fruit1 == fruit3 or fruit1 == fruit4 or fruit2 == fruit3 or fruit2 == fruit4 or fruit3 == fruit4:
        balance *= 2
    else:
        balance = 0


    # Update the balance label
    balance_label.configure(text=f"Balance: ${balance}")

# Function to handle the submit button click event
def submit_answer():
    global balance

    # Check if the answer is correct
    if math_entry.get() == "16":
        balance += 1

    # Clear the entry field
    math_entry.delete(0, tk.END)

    # Update the balance label
    balance_label.configure(text=f"Balance: ${balance}")

# Create the main window
window = tk.Tk()
window.title("Fruit Machine")

# Create the math problem section
math_frame = tk.Frame(window)
math_frame.pack(pady=10)
math_label = tk.Label(math_frame, text="20 - 4 = ")
math_label.pack(side=tk.LEFT)
math_entry = tk.Entry(math_frame, width=5)
math_entry.pack(side=tk.LEFT)
submit_button = tk.Button(math_frame, text="Submit", command=submit_answer)
submit_button.pack(side=tk.LEFT)

# Create the balance label
balance_label = tk.Label(window, text="Balance: $0")
balance_label.pack()

# Create the fruit columns
fruit_images = []
fruits = ['apple.png', 'banana.png', 'orange.png', 'grape.png', 'watermelon.png']
for i, fruit in enumerate(fruits):
    img = tk.PhotoImage(file=fruit)
    img = img.subsample(5)  # Reduce the image size by half
    fruit_images.append(img)

column1 = tk.Label(window, image=fruit_images[0])
column1.pack(side=tk.LEFT, padx=10)
column2 = tk.Label(window, image=fruit_images[1])
column2.pack(side=tk.LEFT, padx=10)
column3 = tk.Label(window, image=fruit_images[2])
column3.pack(side=tk.LEFT, padx=10)
column4 = tk.Label(window, image=fruit_images[3])
column4.pack(side=tk.LEFT, padx=10)

# Create the spin button
spin_button = tk.Button(window, text="Spin", command=spin)
spin_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()

import customtkinter as ctk
import random
import time
import tkinter as tk
ctk.set_appearance_mode('dark')
# Create a list of random numbers
arr = [random.randint(1, 100) for i in range(10)]
sorting = False
# Create a function to update the canvas


def toggle_mode():
    # Complete this function to switch between dark and light mode
    pass


def bubble_sort(arr):
    global sorting
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_canvas(arr)
                root.update()
                # Reduce sleep duration for faster visualization
                time.sleep(0.1)
    sorting = False

# Function to visualize insertion sort


def insertion_sort(arr):
    global sorting
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            update_canvas(arr)
            root.update()
            # Reduce sleep duration for faster visualization
            time.sleep(0.1)
        arr[j + 1] = key
    sorting = False


def reset_data():
    # Complete this funciton to again ask the user to reset the data
    pass


def set_data():
    # Complete this funciton to again ask the user to for the data
    pass

# Create a button here to start the visualization


# Create a reset button here to reset the input array


# Create a drop down box to select the algoritm for visualization


# Create a frame for canvas with its width and height compatible to the screen


# Create a button to toggle modes


# Create a Entry button here to set the input array


root = ctk.CTk()
root.title("Algorithm Visualizer")
root.geometry("600x500")

# lable
algo_lable = ctk.CTkLabel(root, text="Algorithm Visualizer",
                          fg_color=('yellow', 'green'),
                          text_color=('black', 'white'),
                          corner_radius=10)
algo_lable.pack(pady=5)
root.mainloop()

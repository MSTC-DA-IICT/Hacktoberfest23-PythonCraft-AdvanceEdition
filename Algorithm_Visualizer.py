import customtkinter as ctk
import random
import time
import tkinter as tk
ctk.set_appearance_mode('dark')

def toggle_mode():
    # Complete this function to switch between dark and light mode
    pass

def bubble_sort(arr):
    # Complete this function to visualize bubble sort.
    pass

def insertion_sort(arr):
    # Complete this function to visualize insertion sort.
    pass

def reset_data():
    # Complete this funciton to again ask the user to reset the data
    pass
def set_data():
    # Complete this funciton to again ask the user to for the data

# Create a button here to start the visualization






# Create a reset button here to reset the input array






# Create a drop down box to select the algoritm for visualization






# Create a frame for canvas with its width and height compatible to the screen





# Create a button to toggle modes



    

# Create a Entry button here to set the input array





root=ctk.CTk()
root.title("Algorithm Visualizer")
root.geometry("600x500")

#lable
algo_lable= ctk.CTkLabel(root,text="Algorithm Visualizer",
                         fg_color=('yellow','green'),
                        text_color= ('black','white'),
                         corner_radius=10)
algo_lable.pack(pady=5)
root.mainloop()

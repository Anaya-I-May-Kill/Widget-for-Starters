from tkinter import *

# Window Base
root = Tk()
root.title("Geting Started with Widgets")
root.geometry("400x300")
root.configure(bg="#355C7D") # BG Color

# Add Label
lbl = Label(text = "Multiplying 2 numbers" , fg = "#F8B195" , bg = "#C06C84" , height = 1 , width = 300)

# Add Labels for Numbers
# Add Entry to Create Text Box for Input
n1_lbl = Label(text = "Enter 1st Number" , bg = "#6C5B7B" , height = 1 , width = 300)
n1_entry = Entry(bg="#F8B195")

n2_lbl = Label(text = "Enter 2nd Number" , bg = "#6C5B7B" , height = 1 , width = 300)
n2_entry = Entry(bg="#F8B195")

# Multiply the Numbers
def multiply():
    
    # Accessing Numbers
    n1 = int(n1_entry.get())
    n2 = int(n2_entry.get())
    
    # The Product
    product = n1 * n2
    
    # Display Product in Text Box
    text_box.insert(END , f"{n1} x {n2} = {product}")
    
# Add Text Box to Display Info
text_box = Text(fg = "#F67280" , bg = "#6C5B7B" , height = 3)

# Add a Button with the Multiply Command
btn = Button(text = "Multiply" , command = multiply , height = 1 , bg = "#C06C84" , fg = "#F8B195")

# Print all the widgets in order
lbl.pack(pady = 10)
n1_lbl.pack()
n1_entry.pack(pady = 5)
n2_lbl.pack(pady = 5)
n2_entry.pack()
btn.pack(pady = 10)
text_box.pack()

# Run the Code
root.mainloop()
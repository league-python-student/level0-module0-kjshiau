from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Ask the user for their name and save it to a variable
    answer = simpledialog.askstring('This is the title', 'How was your day?')

    # name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    messagebox.showinfo('title #2', 'The response is:' + answer )
    # Show a message box with your message using the .showinfo() method
    
    # Print your message to the console using the print() function
    print( 'title is the console: ' + answer )
    # Show an error message using messagebox.showerror()
    messagebox.showerror('error message box', 'ERROR! SORRY, Please Try Again')
    # Run the window's .mainloop() method

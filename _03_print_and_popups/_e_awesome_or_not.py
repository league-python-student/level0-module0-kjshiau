from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    number = random.randint(0,100)
    # 2. Print your variable to the console
    print(number)
    # 3. Get the user to enter something that they think is awesome
    answer = simpledialog.askstring('Title', 'What do you think is aswome? Please answer down below.')
    # 4. If your variable is  0
    if number is 0:
        messagebox = simpledialog.askstring('Title', 'That is aswome! Write a response down below.')
        # -- tell the user whatever they entered is awesome!
        
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if number is 1:
        messagebox = simpledialog.askstring('Title', 'That is, ummm... Ok. Write a response down below')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if number is 2:
        messagebox = simpledialog.askstring('Title', 'That is so boring! Write a response down below.')
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if number is 3:
        messagebox = simpledialog.askstring('Title', 'That is the worse thing I have ever heard!!!! Get out of here!!!!!!!! Write a response down below.')
    # Run the window's .mainloop() method
    window.mainloop()
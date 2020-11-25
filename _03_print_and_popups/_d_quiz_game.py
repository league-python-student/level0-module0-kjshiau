from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    #      // 2.  Ask the user a question 
    answer = simpledialog.askstring('This is the title', 'What helps you see through walls?')
    #      // 3.  Use an if statement to check if their answer is correct
    if answer == 'window':
        messagebox.showinfo('this is a title', 'correct!!!')
        score += 1
    else:
        messagebox.showinfo('this is a title', 'sorry, incorrect')
    #      // 4.  if the user's answer was correct, add one to their score 

    print('score is: ' + str(score))
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    answer = simpledialog.askstring('This is the title', 'What is at the beging of eternity but at the end of time?')
    if answer == 'e':
        messagebox.showinfo('this is a title', 'correct!!!')
        score += 1

    else:
        messagebox.showinfo('this is a title', 'sorry, incorrect')
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 

    messagebox.showinfo('title #2', 'Your score is:' + str(score))
    # Run the window's .mainloop() method

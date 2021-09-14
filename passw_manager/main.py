# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
from tkinter import messagebox
from tkinter import *
from random import choice, randint, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    char_list = [choice(letters) for _ in range(randint(8, 10))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]
    sym_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = char_list+num_list+sym_list
    shuffle(password_list)

    return "".join(password_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

# window(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file='passw_manager/logo.png')
canvas.create_image(100, 100, image=img)

canvas.grid(column=1, row=0)

label = Label(text="Website")
label.grid(column=0, row=1)
label2 = Label(text="Email")
label2.grid(column=0, row=2)
label3 = Label(text="Password")
label3.grid(column=0, row=3)

entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2)
entry_email = Entry(width=35)
entry_email.grid(column=1, row=2,  columnspan=2)
entry_email.insert(0, "kh@gmail.com")
entry_passw = Entry(width=24)
entry_passw.grid(column=1, row=3)


def fill_password():
    entry_passw.insert(0, generate())


def save_passw():
    website = entry_website.get()
    entry_website.delete(0, 'end')
    email = entry_email.get()
    password = entry_passw.get()
    entry_passw.delete(0, 'end')
    print(website, email, password)
    if website == "" or email == "" or password == "":
        messagebox.showwarning(
            title=website, message="Please enter valid information")

    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"Do you want to save this information:\nEMAIL: {email}\nPASSWORD: {password}")
        if is_ok:
            f = open("passw_manager/data.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()


btn_generate = Button(text="Generate", command=fill_password)

btn_add = Button(text="Add", width=33, command=save_passw)
btn_generate.grid(column=2, row=3)
btn_add.grid(column=1, row=4,  columnspan=2)


window.mainloop()

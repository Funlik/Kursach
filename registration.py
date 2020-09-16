import time
from tkinter import *
from tkinter import messagebox

tkinter_window = Tk()
first_name = StringVar()
patronymic = StringVar()
last_name = StringVar()
birth_date = StringVar()

tkinter_title = "cis.makc.ru"
label_font = ("Helvetica", 14)
entry_font = ("Helvetica", 20)
button_font = ("Helvetica", 12)
padx, pady = 5, 4


def login_or_signup(window):
    window.title("Вход/Регистрация")

    window.mainloop()


def tkinter_main(window):
    window.title(tkinter_title)

    Label(text=" Введите фамилию:", font=label_font).grid(row=0, column=0, sticky="w")
    last_name_entry = Entry(textvariable=last_name, font=entry_font)
    last_name_entry.grid(row=0, column=1, padx=padx, pady=pady)

    Label(text=" Введите имя:", font=label_font).grid(row=1, column=0, sticky="w")
    first_name_entry = Entry(textvariable=first_name, font=entry_font)
    first_name_entry.grid(row=1, column=1, padx=padx, pady=pady)

    Label(text=" Введите отчество:", font=label_font).grid(row=2, column=0, sticky="w")
    patronymic_entry = Entry(textvariable=patronymic, font=entry_font)
    patronymic_entry.grid(row=2, column=1, padx=padx, pady=pady)

    Label(text=" Введите дату рождения:", font=label_font).grid(row=3, column=0, sticky="w")
    birth_date_entry = Entry(textvariable=birth_date, font=entry_font)
    birth_date_entry.grid(row=3, column=1, padx=padx, pady=pady)

    # last_name_entry.insert(0, "Рыжкова")
    # first_name_entry.insert(0, "Татьяна")
    # patronymic_entry.insert(0, "Алексеевна")
    # birth_date_entry.insert(0, "14.02.1987")

    Button(text=f"Начать поиск", font=button_font, command=search_button).grid(row=4, columnspan=2, padx=5, pady=5)

    tkinter_center(window)

    window.mainloop()


def tkinter_center(window):
    window.update_idletasks()
    width, height = window.winfo_width(), window.winfo_height()
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x_delta, y_delta = (screen_width - width) // 2, (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x_delta}+{y_delta}")


def start_search():
    pass


def search_button():
    # first_name.set("Андрей")
    # birth_date.set("18.07.1997")
    birth_date_good = True if re.findall(r"\s*\d\d\.\d\d.\d\d\d\d", birth_date.get()) else False
    first_name.set(first_name.get().strip().capitalize())
    patronymic.set(patronymic.get().strip().capitalize())
    last_name.set(last_name.get().strip().capitalize())
    name_good = True if first_name.get() or patronymic.get() or last_name.get() else False
    if name_good and birth_date_good:
        start_search(first_name.get(), patronymic.get(), last_name.get(), birth_date.get())
    elif name_good is False:
        messagebox.showinfo(tkinter_title, "Enter at least one person's initials")
    elif birth_date_good is False:
        messagebox.showinfo(tkinter_title, "Enter the birth date in the correct format: 01.01.1970")


if __name__ == '__main__':
    print("Starting the program...")

    tkinter_main(tkinter_window)

    time.sleep(5)

    login_or_signup(tkinter_window)

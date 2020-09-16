import tkinter as tk
import threading
import time


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # initialize the main window
        tk.Tk.__init__(self, *args, **kwargs)
        self.birth_date = tk.StringVar()
        self.last_name = tk.StringVar()
        self.first_name = tk.StringVar()


        print("registration")
        # self.clear()

        self.window_width, self.window_height = None, None

        label_font = ("Helvetica", 14)
        entry_font = ("Helvetica", 20)
        button_font = ("Helvetica", 12)

        padx, pady = 5, 4

        tk.Label(text=" Введите фамилию:", font=label_font).grid(row=0, column=0, sticky="w")
        last_name_entry = tk.Entry(textvariable=self.last_name, font=entry_font)
        last_name_entry.grid(row=0, column=1, padx=padx, pady=pady)

        tk.Label(text=" Введите имя:", font=label_font).grid(row=1, column=0, sticky="w")
        first_name_entry = tk.Entry(textvariable=self.first_name, font=entry_font)
        first_name_entry.grid(row=1, column=1, padx=padx, pady=pady)

        tk.Label(text=" Введите дату рождения:", font=label_font).grid(row=3, column=0, sticky="w")
        birth_date_entry = tk.Entry(textvariable=self.birth_date, font=entry_font)
        birth_date_entry.grid(row=3, column=1, padx=padx, pady=pady)

        tk.Label(text=" Введите username:", font=label_font).grid(row=4, column=0, sticky="w")
        birth_date_entry = tk.Entry(textvariable=self.birth_date, font=entry_font)
        birth_date_entry.grid(row=4, column=1, padx=padx, pady=pady)

        tk.Label(text=" Введите пароль:", font=label_font).grid(row=5, column=0, sticky="w")
        birth_date_entry = tk.Entry(textvariable=self.birth_date, font=entry_font)
        birth_date_entry.grid(row=5, column=1, padx=padx, pady=pady)

        tk.Label(text=" Повторите пароль:", font=label_font).grid(row=6, column=0, sticky="w")
        birth_date_entry = tk.Entry(textvariable=self.birth_date, font=entry_font)
        birth_date_entry.grid(row=6, column=1, padx=padx, pady=pady)

        tk.Button(text=f"Начать поиск", font=button_font, command=init_new).grid(row=7, columnspan=2,
                                                                                               padx=5, pady=5)
        # self.geometry("%dx%d" % (self.window_width, self.window_height))

        # add a container which will take all the widgets
        container = tk.Frame(self, bg="green")
        container.grid(row=8, column=0, padx=5, pady=5)

        # Add a titlebar object (defined below)
        self.titleBar = TitleBar(container, controller=self)
        self.titleBar.grid(row=0, column=0, columnspan=2, sticky=tk.N+tk.W+tk.E)

    def login(self):
        print("login")

    def registration(self):
        print("registration")
        self.clear()

class TitleBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # the title bar contains only one label element
        self.titleLabel = tk.Label(self, text="This is the initial text")
        self.titleLabel.pack(side=tk.LEFT)


# Define a thread that runs in the background to perform intensive calculations
class MyTestThread(threading.Thread):
    def run(self):
        for i in range(10):
            time.sleep(1)
            a = i+100        # intensive calculation

            # from time to time: inform use about status
            print(a)      # printing to console works fine
            app.titleBar.titleLabel['text'] = "status: " + str(a)

def init_new():
    global app
    app = SampleApp()
    t = MyTestThread()
    t.start()
    app.mainloop()


if __name__ == "__main__":
    app = SampleApp()

    #app.titleBar.titleLabel['text'] = "test 2"

    t = MyTestThread()
    t.start()

    app.mainloop()
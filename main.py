import tkinter as tk
from tkinter import messagebox
# from tkinter import Ve
import config
import requests
import threading
import time
import re


button_font = ("Helvetica", 12)
# padx, pady = 5, 4
statuses = ["auth", "registration", "login", "chats", "chat", "create_chat", "change_username", "add_person"]
status_id = 0

root = None
real_password, real_password_repeat = "", ""
token = None

chats = []
chat_ids = []
main_chat_id = 0

chat_result = None




class UserGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.widgets = []
        self.auth_widgets = []
        self.login_widgets = []
        self.reg_widgets = []
        self.chats_widgets = []
        self.create_chat_widgets = []
        self.change_username_widgets = []
        self.chat_widgets = []
        self.add_person_widgets = []
        # self.chats_layout()
        self.auth_layout()
        # self.mainloop()

        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.birth_date = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password_repeat = tk.StringVar()
        self.new_chat_name = tk.StringVar()
        self.change_username = tk.StringVar()
        self.add_person = tk.StringVar()

        self.last_name_entry = None
        self.first_name_entry = None
        self.birth_date_entry = None
        self.username_entry = None
        self.password_entry = None
        self.password_repeat_entry = None
        self.new_chat_name_entry = None
        self.change_username_entry = None
        self.add_person_entry = None

        # birth_date_entry.insert(0, "14.02.1987")

    def clear(self):
        # for element in self.grid_slaves():
        #     element.destroy()
        print(self.auth_widgets, self.login_widgets, self.reg_widgets, self.chats_widgets)
        for widget in self.auth_widgets:
            widget.destroy()
        self.auth_widgets = []
        for widget in self.login_widgets:
            widget.destroy()
        self.login_widgets = []
        for widget in self.reg_widgets:
            widget.destroy()
        self.reg_widgets = []
        for widget in self.chats_widgets:
            widget.destroy()
        self.chats_widgets = []
        for widget in self.create_chat_widgets:
            widget.destroy()
        self.create_chat_widgets = []
        for widget in self.change_username_widgets:
            widget.destroy()
        self.change_username_widgets = []
        for widget in self.chat_widgets:
            widget.destroy()
        self.chat_widgets = []
        for widget in self.add_person_widgets:
            widget.destroy()
        self.add_person_widgets = []






    def my_geometry(self, width=None, height=None):
        if width is None:
            width = self.winfo_width()
        if height is None:
            height = self.winfo_height()
        self.update_idletasks()
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x_delta, y_delta = (screen_width - width) // 2, (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x_delta}+{y_delta}")

    def auth_layout(self):
        global status_id
        status_id = 0
        self.clear()

        # self.my_geometry(480, 240)
        username = tk.StringVar()
        self.title("Вход/Регистрация")
        self.widgets = []
        login_button = tk.Button(text=f"Вход", font=button_font, command=self.login_layout)
        # login_button.pack()
        login_button.grid(row=0, columnspan=1, padx=25, pady=10)
        self.auth_widgets += [login_button]
        reg_button = tk.Button(text=f"Регистрация", font=button_font, command=self.registration_layout)
        # reg_button.pack()
        reg_button.grid(row=1, columnspan=1, padx=25, pady=10)
        self.auth_widgets = [login_button, reg_button]

    def login_layout(self):
        global status_id
        status_id = 2
        self.clear()

        label1 = tk.Label(text=" Введите username:", font=config.label_font)
        label1.grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(textvariable=self.username, font=config.entry_font)
        self.username_entry.grid(row=0, column=1, padx=config.padx, pady=config.pady)

        label2 = tk.Label(text=" Введите пароль:", font=config.label_font)
        label2.grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(textvariable=self.password, font=config.entry_font)
        self.password_entry.grid(row=1, column=1, padx=config.padx, pady=config.pady)

        button = tk.Button(text=f"Войти", font=button_font, command=self.send_login)
        button.grid(row=2, columnspan=3, padx=5, pady=5)

        self.login_widgets = [label1, self.username_entry, label2, self.password_entry, button]

    def registration_layout(self):
        global status_id
        status_id = 1
        self.clear()

        label1 = tk.Label(text=" Введите фамилию:", font=config.label_font)
        label1.grid(row=0, column=0, sticky="w")
        self.last_name_entry = tk.Entry(textvariable=self.last_name, font=config.entry_font)
        self.last_name_entry.grid(row=0, column=1, padx=config.padx, pady=config.pady)

        label2 = tk.Label(text=" Введите имя:", font=config.label_font)
        label2.grid(row=1, column=0, sticky="w")
        self.first_name_entry = tk.Entry(textvariable=self.first_name, font=config.entry_font)
        self.first_name_entry.grid(row=1, column=1, padx=config.padx, pady=config.pady)

        label3 = tk.Label(text=" Введите дату рождения:", font=config.label_font)
        label3.grid(row=3, column=0, sticky="w")
        self.birth_date_entry = tk.Entry(textvariable=self.birth_date, font=config.entry_font)
        self.birth_date_entry.grid(row=3, column=1, padx=config.padx, pady=config.pady)

        label4 = tk.Label(text=" Введите username:", font=config.label_font)
        label4.grid(row=4, column=0, sticky="w")
        self.username_entry = tk.Entry(textvariable=self.username, font=config.entry_font)
        self.username_entry.grid(row=4, column=1, padx=config.padx, pady=config.pady)

        label5 = tk.Label(text=" Введите пароль:", font=config.label_font)
        label5.grid(row=5, column=0, sticky="w")
        self.password_entry = tk.Entry(textvariable=self.password, font=config.entry_font)
        self.password_entry.grid(row=5, column=1, padx=config.padx, pady=config.pady)

        label6 = tk.Label(text=" Повторите пароль:", font=config.label_font)
        label6.grid(row=6, column=0, sticky="w")
        self.password_repeat_entry = tk.Entry(textvariable=self.password_repeat, font=config.entry_font)
        self.password_repeat_entry.grid(row=6, column=1, padx=config.padx, pady=config.pady)

        button = tk.Button(text=f"Зарегистрироваться", font=button_font, command=self.send_registration)
        button.grid(row=7, columnspan=2, padx=5, pady=5)
        # self.geometry("%dx%d" % (self.window_width, self.window_height))

        self.reg_widgets = [label1, self.last_name_entry, label2, self.first_name_entry, label3, self.birth_date_entry,
                            label4, self.username_entry, label5, self.password_entry,
                            label6, self.password_repeat_entry, button]

        self.first_name_entry.insert(0, "Пётр")
        self.last_name_entry.insert(0, "Ботин")
        self.birth_date_entry.insert(0, "30.03.2001")
        self.username_entry.insert(0, "my_username000")
        self.password_entry.insert(0, "123")


    def send_login(self):
        global real_password
        print(real_password)

        if len(self.username.get().strip()) == 0 or len(self.password.get().strip()) == 0:
            messagebox.showinfo("Ошибка", "Заполните все поля")
            return
        response = requests.post("http://45.144.65.25/signin/", data={'username': self.username.get(), 'password': real_password})
        result = response.json()
        print(result)
        if "authenticated" in result and result["authenticated"] is False:
            messagebox.showinfo("Ошибка", "Неправильный логин или пароль")
            return
        elif "authenticated" in result and result["authenticated"] is True:
            global token
            token = result["token"]
            self.chats_layout()

        self.chats_layout()

    def send_registration(self):
        global real_password
        global real_password_repeat

        birth_date_good = True if re.findall(r"\s*\d\d\.\d\d.\d\d\d\d", self.birth_date.get()) else False

        if len(self.last_name.get().strip()) == 0 or len(self.first_name.get().strip()) == 0 \
                or len(self.username.get().strip()) == 0 or len(self.birth_date.get().strip()) == 0:
            messagebox.showinfo("Ошибка", "Заполните все поля")
            return


        if not birth_date_good:
            messagebox.showinfo("Ошибка", "Неправильный формат даты")
            return

        if real_password != real_password_repeat:
            messagebox.showinfo("Ошибка", "Пароли не совпадают")
            return
        response2 = requests.post("http://45.144.65.25/registration/",
                                  data={'name': self.first_name.get(), 'surname': self.last_name.get(), 'username': self.username.get(), 'password': real_password,
                                        'birthdate': self.birth_date.get()})

        result = response2.json()
        print(result)
        if "error" in result:
            messagebox.showinfo("Ошибка", result["error"])
            return
        elif "Registration" in result and result["Registration"] is True:
            global token
            token = result["token"]
            self.chats_layout()
        # if result[]:
        #     messagebox.showinfo("Ошибка", "Имя группы не может быть пустым")

        pass

    def chats_layout(self):
        global status_id
        status_id = 3
        self.clear()

        self.title("Мои чаты")

        global token
        response = requests.get("http://45.144.65.25/getAllChatByUser/",
                                headers={'Authorization': token})
        # 'Token c3c5acabc8024152fa643229f5e5b52aae07c1cc'
        global chats
        global chat_ids
        chats = response.json()["chats"]
        lis = [f"{chat['name']}({chat['numberOfPeople']} человек)" for chat in chats]
        chat_ids = [int(chat['id']) for chat in chats]



        button1 = tk.Button(text=f"Создать чат", font=button_font, command=self.create_chat_layout)
        button1.grid(row=0, column=0, padx=5, pady=5)
        button2 = tk.Button(text=f"Сменить username", font=button_font, command=self.change_username_layout)
        button2.grid(row=0, column=1, padx=5, pady=5)

        scframe = VerticalScrolledFrame(self)
        scframe.grid(row=2, columns=2)

        # tk.Button(scframe, text=f"Вход", font=button_font, command=self.login_layout)


        for i, x in enumerate(lis):

            btn = tk.Button(scframe.interior, height=1, width=20, relief=tk.FLAT,
                            bg="gray99", fg="purple3",
                            font="Dosis", text=lis[i],
                            command=lambda i=i, x=x: openlink(i))
            btn.grid(padx=10, pady=5)  # , side=tk.TOP

        self.chats_widgets = [button1, button2, scframe]

        def openlink(i):
            global chat_id
            chat_id = chat_ids[i]
            self.chat_layout(chat_ids[i])



    def chat_layout(self, chat_id=None):
        global status_id
        status_id = 4
        self.clear()

        global main_chat_id
        if chat_id is None:
            chat_id = main_chat_id
        main_chat_id = chat_id

        messages_field = tk.Text(self)
        messages_field.grid(row=0, column=0)

        input_user = tk.StringVar()
        input_field = tk.Entry(text=input_user)
        # input_field.grid(sticky=tk.E+tk.W+tk.N+tk.S)
        input_field.grid(row=1, column=0, sticky=tk.E + tk.W + tk.N + tk.S)
        button1 = tk.Button(text=f"Добавить", font=button_font, command=self.add_person_layout)
        button1.grid(row=0, column=1, padx=5, pady=5)
        button2 = tk.Button(text=f"Отмена", font=button_font, command=self.chats_layout)
        button2.grid(row=1, column=1, padx=5, pady=5)

        global token
        result = requests.get("http://45.144.65.25/getMessagesByChatId/",
                                headers={'Authorization': token},
                                data={'chatId': chat_id}).json()
        global chat_result
        chat_result = result
        print(result)
        messages = result["messages"][-23:]
        messages = [f"{message['user']['username']} {message['data'][:19].replace('T', ' ')}: {message['text']}" for message in messages]
        for message in messages:
            messages_field.insert(tk.INSERT, f"{message}\n")


        # input_field.pack(side=BOTTOM, fill=X)

        def Enter_pressed(event):
            input_get = input_field.get()
            # print(input_get)
            global token
            requests.post("http://45.144.65.25/createMessage/",
                                     headers={'Authorization': token},
                                     data={'chatId': chat_id, 'text': input_get})

            # messages_field.insert(tk.INSERT, '%s\n' % input_get)
            # label = Label(window, text=input_get)
            input_user.set('')
            self.chat_layout(chat_id)
            # label.pack()
            return "break"

        # frame = Frame(window)  # , width=300, height=300)
        input_field.bind("<Return>", Enter_pressed)
        self.chat_widgets = [messages_field, input_field, button1, button2]

        # self.title("Мои чаты")

    def add_person_layout(self):
        global status_id
        status_id = 7
        self.clear()
        self.title("Добавить в чат")

        label = tk.Label(text=" Введите username:", font=config.label_font)
        label.grid(row=0, column=0, sticky="w")
        self.add_person_entry = tk.Entry(textvariable=self.add_person, font=config.entry_font)
        self.add_person_entry.grid(row=0, column=1, padx=config.padx, pady=config.pady)
        self.add_person_entry.delete(0, "end")

        global main_chat_id
        button1 = tk.Button(text=f"Отмена", font=button_font, command=self.chat_layout)
        button1.grid(row=1, column=0, padx=5, pady=5)
        button2 = tk.Button(text=f"Добавить", font=button_font, command=self.test002)
        button2.grid(row=1, column=1, padx=5, pady=5)

        self.add_person_widgets = [label, self.add_person_entry, button1, button2]

    def test002(self):
        print("Trying add person")
        global token
        global main_chat_id
        username = self.add_person_entry.get()
        result = requests.post("http://45.144.65.25/addUserToChatByUsername/",
                                 headers={'Authorization': token},
                                 data={'chatId': main_chat_id, "username": username}).json()
        print(result)
        if "error" in result:
            messagebox.showinfo("Ошибка", "Пользователя с таким username нет")
            return
        else:
            self.chat_layout()

    def create_chat_layout(self):
        global status_id
        status_id = 5
        self.clear()
        self.title("Создание чата")

        label = tk.Label(text=" Введите название чата:", font=config.label_font)
        label.grid(row=0, column=0, sticky="w")
        self.new_chat_name_entry = tk.Entry(textvariable=self.new_chat_name, font=config.entry_font)
        self.new_chat_name_entry.grid(row=0, column=1, padx=config.padx, pady=config.pady)
        self.new_chat_name_entry.delete(0, "end")

        button1 = tk.Button(text=f"Отмена", font=button_font, command=self.chats_layout)
        button1.grid(row=1, column=0, padx=5, pady=5)
        button2 = tk.Button(text=f"Создать", font=button_font, command=self.create_chat)
        button2.grid(row=1, column=1, padx=5, pady=5)

        self.create_chat_widgets = [label, self.new_chat_name_entry, button1, button2]

    def create_chat(self):
        if len(self.new_chat_name_entry.get().strip()) == 0:
            messagebox.showinfo("Ошибка", "Имя группы не может быть пустым")
            return
        result = requests.post("http://45.144.65.25/createChat/",
                                 headers={'Authorization': token},
                                 data={'name': self.new_chat_name_entry.get()}).json()
        print(result)
        # print(response.json())
        self.chats_layout()

    def change_username_layout(self):
        global status_id
        status_id = 6
        self.clear()
        self.title("Изменение username")

        label = tk.Label(text=" Введите новый username:", font=config.label_font)
        label.grid(row=0, column=0, sticky="w")
        self.new_username_entry = tk.Entry(textvariable=self.change_username, font=config.entry_font)
        self.new_username_entry.grid(row=0, column=1, padx=config.padx, pady=config.pady)
        self.new_username_entry.delete(0, "end")

        button1 = tk.Button(text=f"Отмена", font=button_font, command=self.chats_layout)
        button1.grid(row=1, column=0, padx=5, pady=5)
        button2 = tk.Button(text=f"Изменить", font=button_font, command=self.test001)
        button2.grid(row=1, column=1, padx=5, pady=5)

        self.change_username_widgets = [label, self.new_username_entry, button1, button2]

    def test001(self):
        self.chats_layout()


def tkinter_center(window):
    window.update_idletasks()
    width, height = window.winfo_width(), window.winfo_height()
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x_delta, y_delta = (screen_width - width) // 2, (screen_height - height) // 2
    root.geometry(f"+{x_delta}+{y_delta}")

class MyTestThread(threading.Thread):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):
        while True:
            tkinter_center(self.window)
            global real_password
            global real_password_repeat
            if statuses[status_id] == "registration":
                password_len = len(root.password.get())
                real_password = real_password[:root.password.get().count("*")]
                real_password += root.password.get().replace("*", "")
                root.password_entry.delete(0, "end")
                root.password_entry.insert(0, "*" * password_len)

                password_repeat_len = len(root.password_repeat.get())
                real_password_repeat = real_password_repeat[:root.password_repeat.get().count("*")]
                real_password_repeat += root.password_repeat.get().replace("*", "")
                root.password_repeat_entry.delete(0, "end")
                root.password_repeat_entry.insert(0, "*" * password_repeat_len)
                # if len(root.last_name.get()) > 4:
                #     root.last_name_entry.delete(0, "end")

                last_name = root.last_name.get()
                root.last_name_entry.delete(0, "end")
                root.last_name_entry.insert(0, last_name.strip().capitalize())

                first_name = root.first_name.get()
                root.first_name_entry.delete(0, "end")
                root.first_name_entry.insert(0, first_name.strip().capitalize())

                username = root.username.get()
                root.username_entry.delete(0, "end")
                root.username_entry.insert(0, username.strip())

                birth_date = root.birth_date.get()
                root.birth_date_entry.delete(0, "end")
                root.birth_date_entry.insert(0, birth_date.strip())
            elif statuses[status_id] == "login":
                username = root.username.get()
                root.username_entry.delete(0, "end")
                root.username_entry.insert(0, username.strip())

                password_len = len(root.password.get())
                real_password = real_password[:root.password.get().count("*")]
                real_password += root.password.get().replace("*", "")
                root.password_entry.delete(0, "end")
                root.password_entry.insert(0, "*" * password_len)
            elif statuses[status_id] == "chat":
                print("chat")
                global main_chat_id
                global chat_result
                result = requests.get("http://45.144.65.25/getMessagesByChatId/",
                                      headers={'Authorization': token},
                                      data={'chatId':  main_chat_id}).json()
                if(result != chat_result):
                    root.chat_layout(main_chat_id)
                time.sleep(0.5)
            time.sleep(0.1)

        # for i in range(10):
        #     time.sleep(1)
        #     a = i + 100  # intensive calculation
        #
        #     # from time to time: inform use about status
        #     print(a)  # printing to console works fine
        #     app.titleBar.titleLabel['text'] = "status: " + str(a)





class VerticalScrolledFrame(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!

    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        # vscrollbar.grid()
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        # canvas.grid()
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


if __name__ == '__main__':
    # global root
    root = UserGUI()

    t = MyTestThread(root)
    t.start()


    root.mainloop()

# import tkinter as tk
# from random import shuffle
#
# tkinter_window = Tk()
# first_name = StringVar()
# patronymic = StringVar()
# last_name = StringVar()
# birth_date = StringVar()
#
# tkinter_title = "cis.makc.ru"
# label_font = ("Helvetica", 14)
# entry_font = ("Helvetica", 20)
# button_font = ("Helvetica", 12)
# padx, pady = 5, 4
#
# participants = [
#     "Fred Flintstone", "Barney Rubble", "Wilma Flintstone", "Betty Rubble"
# ]
#
# def get_pairings():
#     '''for simulation purposes, this simply randomizes the participants'''
#     global participants
#
#     # see http://stackoverflow.com/a/23286332/7432
#     shuffle(participants)
#     return zip(*[iter(participants)]*2)
#
# def get_pairings():
#     '''for simulation purposes, this simply randomizes the participants'''
#     global participants
#
#     # see http://stackoverflow.com/a/23286332/7432
#     shuffle(participants)
#     return zip(*[iter(participants)]*2)
#
#
# def reset():
#     '''Reset the list of participants'''
#     for child in app.winfo_children():
#         child.destroy()
#
#     for players in get_pairings():
#         label = tk.Label(app, text="%s vs. %s" % players)
#         label.grid()
#
#
# root = Tk()
#
# root.title("Tournament")
#
# app = tk.Frame(root)
# app.grid()
#
# button=tk.Button(root,text="Next Round", command=reset)
# button.grid()
#
# # this sets up the first round
# reset()
#
# root.mainloop()

# tkinter_window = Tk()
# first_name = StringVar()
# patronymic = StringVar()
# last_name = StringVar()
# birth_date = StringVar()
#
# tkinter_title = "cis.makc.ru"
# label_font = ("Helvetica", 14)
# entry_font = ("Helvetica", 20)
# button_font = ("Helvetica", 12)
# padx, pady = 5, 4
#
# class UserGUI(Tk):
#     def __init__(self):
#         super().__init__()
#         self.login_frame()
#         self.mainloop()
#
#
#     def login_frame(self):
#         self.current_frame = Frame(self)
#         self.title("Вход/Регистрация")
#         Label(text=" Введите фамилию:", font=label_font).grid(row=0, column=0, sticky="w")
#         last_name_entry = Entry(textvariable=last_name, font=entry_font)
#         last_name_entry.grid(row=0, column=1, padx=padx, pady=pady)
#
#         Label(text=" Введите имя:", font=label_font).grid(row=1, column=0, sticky="w")
#         first_name_entry = Entry(textvariable=first_name, font=entry_font)
#         first_name_entry.grid(row=1, column=1, padx=padx, pady=pady)
#
#         Label(text=" Введите отчество:", font=label_font).grid(row=2, column=0, sticky="w")
#         patronymic_entry = Entry(textvariable=patronymic, font=entry_font)
#         patronymic_entry.grid(row=2, column=1, padx=padx, pady=pady)
#
#         Label(text=" Введите дату рождения:", font=label_font).grid(row=3, column=0, sticky="w")
#         birth_date_entry = Entry(textvariable=birth_date, font=entry_font)
#         birth_date_entry.grid(row=3, column=1, padx=padx, pady=pady)
#
#
# if __name__ == '__main__':
#     UserGUI()
#
#
# # def get_pairings():
# #     '''for simulation purposes, this simply randomizes the participants'''
# #     global participants
# #
# #     # see http://stackoverflow.com/a/23286332/7432
# #     shuffle(participants)
# #     return zip(*[iter(participants)]*2)
# #
# #
# # def reset():
# #     '''Reset the list of participants'''
# #     for child in app.winfo_children():
# #         child.destroy()
# #
# #     for players in get_pairings():
# #         label = tk.Label(app, text="%s vs. %s" % players)
# #         label.grid()
# #
# # root = tk.Tk()
# #
# # root.title("Tournament")
# #
# # app = tk.Frame(root)
# # app.grid()
# #
# # button=tk.Button(root,text="Next Round", command=reset)
# # button.grid()
# #
# # # this sets up the first round
# # reset()
# #
# # root.mainloop()

from tkinter import *
from typing import List, Any
import Database

class OrganiserGUI():

    def __init__(self, title, geometry):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.main_menu()

    def main_menu(self):
        self.clear_widgets()
        self.root.configure(bg='#00ffd9')
        self.modules = Database.Module.show_modules()
        headingFrame1 = Frame(self.root, bg="#fff200", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="Welcome to \n Personal organiser system", bg='#00ffee',
                             fg='black', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


        btn1 = Button(self.root, text="EDIT MODULES", bg='#fff200', fg='black', command=self.update_modules_menu)
        btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

        btn5 = Button(self.root, text="EXIT", bg='#fff200', fg='black', command=quit)
        btn5.place(relx=0.72, rely=0.93, relwidth=0.25, relheight=0.05)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def update_modules_menu(self):
        self.clear_widgets()
        #self.modules = create_db.Module.show_modules()
        headingFrame1 = Frame(self.root, bg="#fff200", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="MODULES", bg='#00ffee', fg='black', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        btn1 = Button(self.root, text="MAIN MENU", bg='#fff200', fg='black', command=self.main_menu)
        btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

        btn2 = Button(self.root, text="Create Module", bg='#00ffee', fg='black', command=self.create_module)
        btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

        btn3 = Button(self.root, text="Update Module", bg='#fff200', fg='black', command=self.update_module)
        btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

        btn4 = Button(self.root, text="Delete Module", bg='#00ffee', fg='black', command=self.delete_module)
        btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

        btn5 = Button(self.root, text="EXIT", bg='#fff200', fg='black', command=quit)
        btn5.place(relx=0.72, rely=0.93, relwidth=0.25, relheight=0.05)


    def create_module(self):
        self.clear_widgets()

        headingFrame1 = Frame(self.root, bg="#fff200", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="CREATE MODULE", bg='#00ffee', fg='black', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        lab1 = Label(self.root, text="Enter Module Code Number:", bg='#fff200', fg='black')  # 1
        lab1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.05)
        lab_ans1 = self.module_code_widget = Entry(self.root, width=10)
        lab_ans1.place(relx=0.28, rely=0.35)

        lab2 = Label(self.root, text="Enter Module Label:", bg='#fff200', fg='black')  # 2
        lab2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.05)
        lab_ans2 = self.module_label_widget = Entry(self.root, width=20)
        lab_ans2.place(relx=0.28, rely=0.45)

        btn1 = Button(self.root, text="Click to Create Module", bg='#fff200', fg='black', command=self.create_module_button)
        btn1.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

        btn2 = Button(self.root, text="BACK", bg='#fff200', fg='black', command=self.update_modules_menu)
        btn2.place(relx=0.72, rely=0.93, relwidth=0.25, relheight=0.05)





    def create_module_button(self):
        module_label = self.module_label_widget.get()
        module_code = self.module_code_widget.get()
        if module_label and  module_code:
            m = Database.Module(int(module_code), module_label)
        self.update_modules_menu()

    def update_module(self):

        self.clear_widgets()
        headingFrame1 = Frame(self.root, bg="#fff200", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="UPDATE MODULE", bg='#00ffee', fg='black', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        lab1 = Label(self.root, text="Select Module to Update:", bg='#fff200', fg='black')
        lab1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.05)
        self.select_module(command_function=self.update_module_selected)

        btn1 = Button(self.root, text="MAIN MENU", bg='#fff200', fg='black', command=self.main_menu)
        btn1.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

        btn2 = Button(self.root, text="BACK", bg='#fff200', fg='black', command=self.update_modules_menu)
        btn2.place(relx=0.72, rely=0.93, relwidth=0.25, relheight=0.05)

    def update_module_selected(self, *arg):
        self.clear_widgets()
        tuple_in_str_form = self.modules_list_object.get()
        parts = tuple_in_str_form.split(",")
        self.module_code = int(parts[0][1:])

        headingFrame1 = Frame(self.root, bg="#fff200", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="UPDATE MODULE", bg='#00ffee', fg='black', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        lab1=Label(self.root,text="Enter New Module Label for Module "+str(self.module_code)+":" , bg='#fff200', fg='black')
        lab1.place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.05)

        fun = self.module_label_widget = Entry(self.root, width=20)
        fun.place(relx=0.28, rely=0.42, relwidth=0.45, relheight=0.05)

        but1 = Button(self.root, text="Click to Update Module", bg='#fff200', fg='black',
                      command=self.update_module_button)
        but1.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.05)

        btn1 = Button(self.root, text="MAIN MENU", bg='#fff200', fg='black', command=self.main_menu)
        btn1.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

        btn2 = Button(self.root, text="BACK", bg='#fff200', fg='black', command=self.update_module)
        btn2.place(relx=0.72, rely=0.93, relwidth=0.25, relheight=0.05)
    def update_module_button(self):
        module_label = self.module_label_widget.get()
        if module_label:
            sql = "UPDATE modules SET module_name = '" + module_label + "' WHERE module_code = " + str(
                self.module_code)
            with Database.qb_conn:
                result = Database.qb_conn.execute(sql)
        self.update_modules_menu()

    def select_module(self, command_function=None):

        # get from database
        #self.modules = m
        module_options: list[Any] = Database.Module.show_modules()
        if module_options:
            self.modules_list_object = StringVar()
            self.modules_list_object.set(module_options[0])
            self.modules_list_object.trace('w', command_function)
            self.modules_dropdown = OptionMenu(self.root,
                                               self.modules_list_object,
                                               *module_options)
            self.modules_dropdown.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.05)
            self.modules_dropdown.configure(bg='#2b00ff', fg='black')
        else:

            but1 = Button(self.root, text="No Modules - Press Here", bg='#fff200', fg='black',
                          command=self.update_modules_menu)
            but1.place(relx=0.28, rely=0.42, relwidth=0.45, relheight=0.05)

    def delete_module(self):
        self.clear_widgets()
        headingFrame1 = Frame(self.root, bg="#fff200", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="DELETE MODULE", bg='#00ffee', fg='black', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        lab1 = Label(self.root, text="Select Module to Delete:", bg='#fff200', fg='black')
        lab1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.05)
        self.select_module(command_function=self.delete_module_selected)

        btn1 = Button(self.root, text="MAIN MENU", bg='#fff200', fg='black', command=self.main_menu)
        btn1.place(relx=0.28, rely=0.69, relwidth=0.45, relheight=0.1)

        btn2 = Button(self.root, text="BACK", bg='#fff200', fg='black', command=self.update_modules_menu)
        btn2.place(relx=0.72, rely=0.93, relwidth=0.25, relheight=0.05)

    def delete_module_selected(self, *arg):
        tuple_in_str_form = self.modules_list_object.get()
        parts = tuple_in_str_form.split(",")
        module_code = int(parts[0][1:])
        #print(module_code)
        sql = "DELETE FROM modules WHERE module_code = " + str(module_code)
        with Database.qb_conn:
            result = Database.qb_conn.execute(sql)
        self.update_modules_menu()





RESET_TABLES = True
if RESET_TABLES:
    Database.delete_tables()
    Database.create_tables()


# TEST MODULES
m = Database.Module(2987, 'Maths')
m2 = Database.Module(2896, 'Computer')


organiser = OrganiserGUI("organiser","600x500")
organiser.root.mainloop()






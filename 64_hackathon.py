from tkinter import *
from tkinter import ttk
line_b=" "
line=' '


class Person:
    def __init__(self,name, address, phone_number,email_address):
        self.name=name
        self.address=address
        self.phone_number=phone_number
        self.email_address=email_address
    def add_Pfile(self):
        file = open('details.txt', 'a')
        p=[self.name,"$",self.address,"$",self.phone_number,"$",self.email_address]
        file.writelines(p)
        file.write("\n") 
        file.close()

    


def add_contacts():
    add=Tk()
    add.title("Add person")
    add.geometry("1188x840")
    add.configure(bg='lightyellow')
    Label(add, text="ADD PERSON", font=("CASTELLAR", 50), bg="pink").place(x=350, y=200)
    Label(add, text="NAME", font=45, bg="pink").place(x=200, y=300)
    Label(add, text="ADDRESS", font=45, bg="lavender").place(x=200, y=350)
    Label(add, text="PHONE NUMBER", font=45, bg="lavender").place(x=200, y=400)
    Label(add, text="EMAIL ADDRESS", font=45, bg="lavender").place(x=200, y=450)
    name_ = Entry(add)
    address_ = Entry(add)
    phone_number_ = Entry(add)
    email_address_ = Entry(add)
    name_.place(x=600, y=300)
    address_.place(x=600, y=350)
    phone_number_.place(x=600, y=400)
    email_address_.place(x=600, y=450)
    def add_person_1():
        name = name_.get()
        address = address_.get()
        phone_number = phone_number_.get()
        email_address = email_address_.get()
        value = Person(name, address, phone_number,email_address)
        value.add_Pfile()
    def back_add():
        add.destroy()
    Button(add, text="Submit", command=add_person_1, font=40, bg="light pink").place(x=600, y=600)
    Button(add, text="Go back", command=back_add, font=40, bg="light pink").place(x=800, y=600)
    
    
def view_contact():
    view=Tk()
    view.title("view")
    view.geometry("1188x840")
    view.configure(bg='lightyellow')
    Label(view, text="VIEW DETAILS", font=("JUMBLE",50), bg="pink").place(x=300, y=250)
    Label(view, text=" Enter person name", font=40, bg="pink").place(x=200, y=305)
    name=Entry(view)
    name.place(x=600,y=305)
    
    
    def view_contact_1():
        view_=Tk()
        view_.title("view")
        view_.geometry("1188x840")
        view_.configure(bg='lightyellow')
        name1=name.get()
        print("4"+name1)
        file_1=open("temp_view.txt","w")
        file_1.write(name1)
        file_1.close()
        file_1=open("temp_view.txt","r")
        name1=file_1.read()
        file_1.close()
        global line_b
        file = open('details.txt')
        file.seek(0)  
        for line in file:
            words = line.split('$')
            print("1"+words[0])
            print("2"+name1)
            if words[0]==name1:
                line_b=line
                print(line_b)
                print("HI")
        file.close()
        Label(view_, text="NAME", font=40, bg="pink").place(x=200, y=200)
        Label(view_, text="ADDRESS", font=40, bg="lavender").place(x=200, y=280)
        Label(view_, text="PHONE NUMBER", font=40, bg="lavender").place(x=200, y=360)
        Label(view_, text="EMAIL ADDRESS", font=40, bg="lavender").place(x=200, y=440)
        T=Text(view_,height=15,width=30)
        T.place(x=400,y=200)
        Font_tuple=("Comic San MS",20,"bold")
        T.configure(font=Font_tuple)
        list_name=line_b.split('$')
        line_b=" "
        for word_2 in list_name:
            T.insert(END,word_2)
            T.insert(END,"\n")
            T.insert(END,"\n")
        def back_view_c():
            view_.destroy()
        Button(view_, text="Go back", command=back_view_c, font=40, bg="light pink").place(x=800, y=600)
    def back_view():
        view.destroy()
        
    Button(view, text="Submit", command=view_contact_1, font=40, bg="light pink").place(x=600, y=600)
    Button(view, text="Go back", command=back_view, font=40, bg="light pink").place(x=800, y=600)

def delete():
    del_=Tk()
    del_.geometry("1188x840")
    del_.configure(bg='lightyellow')
    Label(del_, text="Enter name", font=40, bg="lavender").place(x=200, y=450)
    del_name=Entry(del_)
    del_name.place(x=400,y=450)
    def delete_1():
        del_name1=del_name.get()
        print(del_name1)
        with open("temp.txt","w") as temp:
            with open(r"details.txt") as file:
                for line in file.readlines():
                    words = line.split('$')
                    if words[0] != del_name1:
                        temp.write(line)
                       
            file.close()
        temp.close()
        with open("temp.txt", "r") as temp:
            with open("details.txt", "w") as file:
                lines = temp.readlines()
                file.writelines(lines)
            file.close()
        temp.close()    
    def back_delete():
        del_.destroy()
    Button(del_, text="Submit", command=delete_1, font=40, bg="light pink").place(x=400, y=600)
    Button(del_, text="Go back", command=back_delete, font=40, bg="light pink").place(x=800, y=600)
def view_name():
    file = open('details.txt')
    file.seek(0)
    disp=Tk()
    disp.geometry("1188x840")
    disp.configure(bg='lightyellow')
    
    T=Text(disp,height=20,width=40)
    T.place(x=200,y=400)
    Font_tuple=("Comic San MS",20,"bold")
    T.configure(font=Font_tuple)
    for line in file:
        words=line.split('$')
        T.insert(END,words[0])
        T.insert(END,"\n")
        T.insert(END,"\n")
    file.close()
    def back_v_name():
        disp.destroy()
        
    Button(disp, text="Go back", command=back_v_name, font=40, bg="light pink").place(x=800, y=600)
        
def edit():
    edit=Tk()
    edit.geometry("1188x840")
    edit.configure(bg='lightyellow')
    Label(edit, text="NAME", font=45, bg="pink").place(x=200, y=300)
    Label(edit, text="PARAMETER", font=45, bg="lavender").place(x=200, y=350)
    Label(edit, text="CHANGED TO", font=45, bg="lavender").place(x=200, y=400)
    name = Entry(edit)
    parameter = Entry(edit)
    changed_to = Entry(edit)
    name.place(x=600, y=300)
    parameter.place(x=600, y=350)
    changed_to.place(x=600, y=400)
    def edit_():
        file = open('details.txt')
        isFound=False
        name_position = 1
        address_position = 2
        ph_no_position = 3
        email_position = 4
        name1=name.get()
        parameter1=parameter.get()
        changed_to1=changed_to.get()
        print("for loop start")
        index=0
        lines=file.readlines()
        for line in lines:
            words = line.split("$")
            print(words)
            if name1 == words[0]:
                print(words[0])
                if parameter1=="address":
                        words[address_position-1] = changed_to1
                elif parameter1=="number":
                        words[ph_no_position-1] = changed_to1
                elif parameter1=="email":
                        words[email_position-1] = changed_to1

                new_line = '$'.join(words)
                lines[index] = new_line
                isFound = True
                break
            index = index + 1
        file.close()
        file1=open("details.txt","w")
        file1.writelines(lines)
        file1.close()
        if isFound == False:
            print("No such value available")
    Button(edit, text="Submit", command=edit_, font=40, bg="light pink").place(x=200, y=500)
    def back_edit():
        edit.destroy()
    Button(edit, text="Go back", command=back_edit, font=40, bg="light pink").place(x=800, y=600)
find=Tk() 
find.title("Person search")
find.geometry("1188x840")
Button(find,text='BACK',command=find.destroy).place(x=700,y=800)
find.configure(bg='lightgreen')
Label(find, text="CONTACT BOOK", font=60, bg="lavender").place(x=650, y=200)
Button(find, text="Add contact", command=add_contacts, font=40, bg="light pink").place(x=400, y=400)
Button(find, text="view contact", command=view_contact, font=40, bg="light pink").place(x=400, y=600)
Button(find, text="Delete", command=delete, font=40, bg="light pink").place(x=400, y=500)
Button(find, text="View Names", command=view_name, font=40, bg="light pink").place(x=400, y=300)
Button(find, text="Edit", command=edit, font=40, bg="light pink").place(x=500, y=300)
find.mainloop()
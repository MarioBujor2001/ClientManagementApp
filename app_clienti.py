from tkinter import *
import sqlite3

# setup main screen
root = Tk()
root.geometry("430x400")
root.title("Aplicatie Clienti")


def update():

    conn = sqlite3.connect("clienti.db")
    c = conn.cursor()
    record_id = id_entry.get()
    c.execute("""UPDATE clienti SET
        nume = :nume,
        prenume = :prenume,
        adress = :adress,
        nrtlf = :nrtlf,
        nrtlf1 = :nrtlf1
        
        WHERE oid = :oid""",
              {
                  'nume': name_editor.get(),
                  'prenume': prenume_editor.get(),
                  'adress': adress_editor.get(),
                  'nrtlf': numar_editor.get(),
                  'nrtlf1': numar1_editor.get(),
                  'oid': record_id
              })

    conn.commit()
    conn.close()


# def editing function
def edit():
    global editor
    editor = Tk()
    editor.geometry("400x200")
    editor.title("Editor")

    conn = sqlite3.connect("clienti.db")
    c = conn.cursor()
    record_id = id_entry.get()
    try:
        c.execute("SELECT * FROM clienti WHERE oid = " + record_id)
        records = c.fetchall()
    except:
        id_entry.insert(0, "Introdu un id valid !")

    global name_editor
    global prenume_editor
    global adress_editor
    global numar_editor
    global numar1_editor
    # entry boxes
    name_editor = Entry(editor, width=35)
    prenume_editor = Entry(editor, width=35)
    adress_editor = Entry(editor, width=35)
    numar_editor = Entry(editor, width=35)
    numar1_editor = Entry(editor, width=35)

    # labels for entry boxes
    name_editor_label = Label(editor, text="Nume")
    prenume_editor_label = Label(editor, text="Prenume")
    adress_editor_label = Label(editor, text="Adresa")
    numar_editor_label = Label(editor, text="Nr. student")
    numar1_editor_label = Label(editor, text="Nr. parinte")
    update_btn = Button(editor, text="Modifica !", width=40, command=update)

    # display labels and entry boxes
    name_editor_label.grid(row=0, column=0)
    name_editor.grid(row=0, column=1)
    prenume_editor_label.grid(row=1, column=0)
    prenume_editor.grid(row=1, column=1)
    adress_editor_label.grid(row=2, column=0)
    adress_editor.grid(row=2, column=1)
    numar_editor_label.grid(row=3, column=0)
    numar_editor.grid(row=3, column=1)
    numar1_editor_label.grid(row=4, column=0)
    numar1_editor.grid(row=4, column=1)
    update_btn.grid(row=5, column=0, columnspan=2)

    for record in records:
        name_editor.insert(0, record[0])
        prenume_editor.insert(0, record[1])
        adress_editor.insert(0, record[2])
        numar_editor.insert(0,  record[3])
        numar1_editor.insert(0, record[4])


# def delete button
def delete():

    conn = sqlite3.connect("clienti.db")
    c = conn.cursor()
    c.execute("DELETE from clienti WHERE oid = " + id_entry.get())
    conn.commit()
    conn.close()
    id_entry.delete(0, END)


# def query function
def query():
    conn = sqlite3.connect("clienti.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM clienti")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[5]) + ". " + str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + "  0" + \
                         str(record[3]) + "  0" + str(record[4]) + '\n'

    global lista_clienti
    lista_clienti = Tk()
    lista_clienti.title("Lista Clienti")
    lista_clienti.geometry("400x250")
    query_title_label = Label(lista_clienti, text="Lista Clienti", fg="#2BB4D6", font=("Helvetica", 20))
    query_label = Label(lista_clienti, text=print_records)
    query_title_label.grid(row=0, column=0)
    query_label.grid(row=1, column=0)


# def submit function
def submit():
    conn = sqlite3.connect('clienti.db')
    c = conn.cursor()
    if name_entry.get() == "" or prenume_entry.get() == "" or adress_entry == "":
        name_entry.insert(0, "Introdu un nume valid !")
    else:
        c.execute(
            "INSERT INTO clienti VALUES (:nume, :prenume, :address, :nrtlf, :nrtlf1)",
            {
                'nume': name_entry.get(),
                'prenume': prenume_entry.get(),
                'address': adress_entry.get(),
                'nrtlf': numar_telefon_entry.get(),
                'nrtlf1': numar_telefon1_entry.get()
            }
        )
        conn.commit()
        conn.close()

        name_entry.delete(0, END)
        prenume_entry.delete(0, END)
        adress_entry.delete(0, END)
        numar_telefon_entry.delete(0, END)
        numar_telefon1_entry.delete(0, END)


# setting up labels
title_label = Label(root, text="Adauga un client nou!", font=("Helvetica", 20))
name_label = Label(root, text="Nume", font="Helvetica")
prenume_label = Label(root, text="Prenume", font="Helvetica")
adress_label = Label(root, text="Adresa", font="Helvetica")
numar_telefon_label = Label(root, text="Nr. student")
numar_telefon1_label = Label(root, text="Nr. parinte")
id_label = Label(root, text="ID modificare", font="Helvetica", fg="#EE8E7A")
modif_label = Label(root, text="Modificare", font=("Helvetica", 20), fg="#EE8E7A")
delim_label = Label(root, text="")

# setting up entry boxes
name_entry = Entry(root, width=30)
prenume_entry = Entry(root, width=30)
adress_entry = Entry(root, width=30)
numar_telefon_entry = Entry(root, width=30)
numar_telefon1_entry = Entry(root, width=30)
id_entry = Entry(root, width=30, fg="#EE8E7A")


# setting up buttons
submit_btn = Button(root, text="Adauga Client !", width=40, command=submit, fg="#76D141")
modify_client_btn = Button(root, text="Modifica Client !", width=40, command=edit, fg="#EE8E7A")
verify_client_btn = Button(root, text="Verifica Clienti !", width=40, command=query, fg="#2BB4D6")
delete_client_btn = Button(root, text="Sterge Client !", width=40, command=delete, fg="#EE8E7A")

# inserting entry, label, button onto screen
title_label.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
prenume_label.grid(row=2, column=0)
prenume_entry.grid(row=2, column=1)
adress_label.grid(row=3, column=0)
adress_entry.grid(row=3, column=1)
numar_telefon_label.grid(row=4, column=0)
numar_telefon_entry.grid(row=4 , column=1)
numar_telefon1_label.grid(row=5, column=0)
numar_telefon1_entry.grid(row=5, column=1)

submit_btn.grid(row=6, column=0, columnspan=2)
verify_client_btn.grid(row=7, column=0, columnspan=2, padx=10)
delim_label.grid(row=8, column=0)
modif_label.grid(row=9, column=1)
id_label.grid(row=10, column=0)
id_entry.grid(row=10, column=1)
id_entry.insert(0, 1)
modify_client_btn.grid(row=11, column=0, columnspan=2)
delete_client_btn.grid(row=12, column=0, columnspan=2)


root.mainloop()
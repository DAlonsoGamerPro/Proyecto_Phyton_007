from tkinter import *

root = Tk()
root.title("Listas Multidimensionales")
root.geometry("400x400")

label = Label(root)
label2 = Label(root)
label3 = Label(root)

array_1d = ["John", "Jameson", "Thompson"]
print(array_1d[0])

array_2d = [["John", "A+"], ["Jameson", "A"], ["Thompson", "B"]]
print(array_2d[1][1])

array_3d = [[["John", "A+", "Graduado con Honores"], ["Jameson", "A", "Excelente"], ["Thompson", "B", "Bien...pero los otros son mejores ;D"]]]
print(array_3d[0][2][2])

def report():
    label["text"] = array_3d[0][0][0] + " obtuvo la calificaión " + array_3d[0][0][1] + ". " + array_3d[0][0][2] + "."
    label2["text"] = array_3d[0][1][0] + " obtuvo la calificaión " + array_3d[0][1][1] + ". " + array_3d[0][1][2] + "."
    label3["text"] = array_3d[0][2][0] + " obtuvo la calificaión " + array_3d[0][2][1] + ". " + array_3d[0][2][2]
    
btn = Button(root,text="Mostrar reporte",command=report)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)
label2.place(relx=0.5, rely=0.7, anchor=CENTER)
label3.place(relx=0.5, rely=0.8, anchor=CENTER)











root.mainloop()
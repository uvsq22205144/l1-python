from tkinter import *

board=[[6, 7, 4, 8], [5, 15, 13, 2], [12, 14, 9, 1], [3, 11, 10, None]]

FONT=('Ubuntu', 27, 'bold')
master=Tk()
cnv=Canvas(master, width=400, height=400)
cnv.pack()

for i in range(4):
    for j in range(4):
        x, y=100*j, 100*i
        A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
        cnv.create_rectangle(A, B, fill="pink")
        cnv.create_text(C, text=board[i][j], fill="purple",
                            font=FONT)
master.mainloop()



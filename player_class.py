import tkinter
from tkinter import *
import Honor_game_class
import pymysql

def start():
    login = session_entry.get()
    password = password_entry.get()
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT COUNT(*) FROM abyss_game WHERE session = %s AND password1 = %s"
    val = (login, password)
    cursor.execute(sql, val)
    result = cursor.fetchone()[0]
    cursor.close()
    db.close()
    if result > 0:
        root.destroy()
        coa = Honor_game_class.Coagame()
        coa.start()
    else:
        tkinter.Label(root, text="用户名或密码错误，请重新输入").grid(row=3, column=2, sticky=E)


# Create the main window
root = Tk()
root.title("王者荣耀赛事管理系统登录")
root.config(background="light blue")

# Set window size and position it in the center of the screen
window_width = 350
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Create and place widgets
Label(root, text="赛事名", fg="black", bg="light blue", font=("FangSong_GB2312", 12)).grid(row=0, column=0, padx=10, pady=5)
session_entry = Entry(root, width=20)
session_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

Label(root, text="密码", fg="black", bg="light blue", font=("FangSong_GB2312", 12)).grid(row=1, column=0, padx=10, pady=5)
password_entry = Entry(root, width=20, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

login_button = Button(root, text="登录", bg="steel blue", fg="white", font=("FangSong_GB2312", 12), width=10, command=start)
login_button.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

# Start the event loop
root.mainloop()
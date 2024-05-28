import tkinter
from tkinter import *
import information

class Team:
    def __init__(self, team_name):
        self.root = Tk()
        self.root.config(background="light blue")
        self.root.wm_title(team_name)
        self.root.geometry("800x300")
        self.team_name = team_name
        self.player_name_label = \
            tkinter.Label(self.root, text="队员信息：", bg="tan", fg="black", font=("Fangsong", 15))
        self.player_id_label = \
            tkinter.Label(self.root, text="队员id：", bg="tan", fg="black", font=("KaiTi", 15))
        self.player_role_label = \
            tkinter.Label(self.root, text="队员常用角色：", bg="tan", fg="black", font=("KaiTi", 15))
        self.insert_player_name_label = \
            tkinter.Label(self.root, text="队员昵称：", bg="tan", fg="black", font=("KaiTi", 15))
        self.insert_player_new_name_label = \
            tkinter.Label(self.root, text="改后昵称：", bg="tan", fg="black", font=("KaiTi", 15))
        self.insert_player_id_label = \
            tkinter.Label(self.root, text="队员id：", bg="tan", fg="black", font=("KaiTi", 15))
        self.player_name_text = Text(self.root, height=10, width=15, bg="cornsilk", fg="black")
        self.player_id_text = Text(self.root, height=10, width=10, bg="cornsilk", fg="black")
        self.player_role_text = Text(self.root, height=10, width=30, bg="cornsilk", fg="red")
        self.insert_player_name = Entry(self.root, width=10, bg="cornsilk")
        self.insert_player_new_name = Entry(self.root, width=10, bg="cornsilk")
        self.insert_player_id = Entry(self.root, width=10, bg="cornsilk")
        self.course_button = Button(self.root, text="签约", bg="steel blue", fg="black", font=("KaiTi", 12),
                                    command=self.contract_player)
        self.course_button2 = Button(self.root, text="解约", bg="steel blue", fg="black", font=("KaiTi", 12),
                                     command=self.breakoff_player)
        self.course_button3 = Button(self.root, text="改名", bg="steel blue", fg="black", font=("KaiTi", 12),
                                     command=self.rechristen_player)
    def inilize(self):
        self.player_name_label.grid(row=0, column=0, sticky=N)
        self.player_name_text.grid(row=2, column=0,sticky=N)
        self.player_id_label.grid(row=0, column=1, sticky=N)
        self.player_id_text.grid(row=2, column=1, sticky=N)
        self.player_role_label.grid(row=0, column=2, sticky=N)
        self.player_role_text.grid(row=2, column=2, sticky=N)
        self.insert_player_name_label.grid(row=0, column=3, sticky=W)
        self.insert_player_name.grid(row=1, column=3, sticky=W)
        self.insert_player_new_name_label.grid(row=2, column=3, sticky=W)
        self.insert_player_new_name.grid(row=3, column=3, sticky=W)
        self.insert_player_id_label.grid(row=0, column=4, sticky=W)
        self.insert_player_id.grid(row=1, column=4, sticky=W)
        self.course_button.grid(row=1, column=5)
        self.course_button2.grid(row=2, column=5)
        self.course_button3.grid(row=3, column=5)

#     签约
    def contract_player(self):
        new_player_name = self.insert_player_name.get()
        new_player_id = self.insert_player_id.get()
        information.insert_team_player(new_player_name, new_player_id, None, None, self.team_name)
        self.update_ui()

#     解约
    def breakoff_player(self):
        new_player_name = self.insert_player_name.get()
        information.delete_player(new_player_name)
        self.update_ui()

#     选手改名
    def rechristen_player(self):
        old_player_name = self.insert_player_name.get()
        new_player_name = self.insert_player_new_name.get()
        information.change_player_name(new_player_name, old_player_name)
        self.update_ui()

#     更新ui
    def update_ui(self):
        self.player_name_text.delete(1.0, END)
        self.player_id_text.delete(1.0, END)
        self.player_role_text.delete(1.0, END)
        information.display_team_player_name(self.player_name_text, self.team_name)
        information.display_team_player_id(self.player_id_text, self.team_name)
        information.display_team_player_role(self.player_role_text, self.team_name)

    def start(self):
        self.inilize()
        self.update_ui()
        self.root.mainloop()


if __name__=='__main__':
    team = Team("王者荣耀队伍信息查询")
    team.start()

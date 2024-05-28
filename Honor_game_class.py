import tkinter
from tkinter import *
import team_class
import information

class Coagame:
    def __init__(self):
        self.root = Tk()
        self.root.config(background="light blue")
        self.root.wm_title("王者荣耀赛事")
        self.root.geometry("900x600")
        self.coa_team_label = tkinter.Label(self.root, text="参赛队伍信息：",  bg="tan", fg="black", font=("KaiTi", 15))
        self.champion_fmvp_label = \
            tkinter.Label(self.root, text="往届王者赛事结果：",  bg="tan", fg="black", font=("KaiTi", 15))
        self.special_player_label = \
            tkinter.Label(self.root, text="既擅长辅助位，又擅长对抗路的选手：",  bg="tan", fg="black", font=("KaiTi", 15))
        self.insert_old_team_name_label = \
            tkinter.Label(self.root, text="队伍名称：", bg="tan", fg="black", font=("KaiTi", 15))
        self.insert_new_team_name_label = \
            tkinter.Label(self.root, text="改后名称：", bg="tan", fg="black", font=("KaiTi", 15))
        self.insert_player_name_label = \
            tkinter.Label(self.root, text="mvp选手：", bg="tan", fg="black", font=("KaiTi", 15))
        self.insert_coa_session_label = \
            tkinter.Label(self.root, text="比赛换届：", bg="tan", fg="black", font=("KaiTi", 15))
        self.change_session_old_password_label = \
            tkinter.Label(self.root, text="老密码：", bg="tan", fg="black", font=("KaiTi", 15))
        self.change_session_new_password_label = \
            tkinter.Label(self.root, text="新密码：", bg="tan", fg="black", font=("KaiTi", 15))
        self.coa_team_text = Text(self.root, height=13, width=27, bg="cornsilk", fg="black")
        self.champion_fmvp_text = Text(self.root, height=10, width=32, bg="cornsilk", fg="black")
        self.special_player_taxt = Text(self.root, height=10, width=40, bg="cornsilk", fg="black")
        self.insert_new_team_name = Entry(self.root, width=10, bg="cornsilk")
        self.insert_old_team_name = Entry(self.root, width=10, bg="cornsilk")
        self.insert_coa_session = Entry(self.root, width=10, bg="cornsilk")
        self.insert_player_name = Entry(self.root, width=10, bg="cornsilk")
        self.change_session_old_password = Entry(self.root, width=10, bg="cornsilk")
        self.change_session_new_password = Entry(self.root, width=10, bg="cornsilk")
        self.course_button = Button(self.root, text="添加", bg="steel blue", fg="black", font=("KaiTi", 12),
                                    command=self.insert_team)
        self.course_button2 = Button(self.root, text="解散", bg="steel blue", fg="black", font=("KaiTi", 12),
                                     command=self.delete_team)
        self.course_button3 = Button(self.root, text="改名", bg="steel blue", fg="black", font=("KaiTi", 12),
                                     command=self.rechristen_team)
        self.course_button4 = Button(self.root, text="跳转", bg="steel blue", fg="black", font=("KaiTi", 12),
                                     command=self.jump_team)
        self.course_button5 = Button(self.root, text="换届", bg="steel blue", fg="black", font=("KaiTi", 12),
                                     command=self.change_session)
        self.course_button6 = Button(self.root, text="改密码", bg="steel blue", fg="black", font=("KaiTi", 12),
                                     command=self.change_password)
        self.course_button7 = Button(self.root, text="显示", bg="steel blue", fg="black", font=("KaiTi", 12),
                                     command=self.update_ui)

    def inilize(self):
        self.coa_team_label.grid(row=0, column=0, sticky=W)
        self.coa_team_text.grid(row=2, column=0, sticky=W)
        self.champion_fmvp_label.grid(row=0, column=1, sticky=W)
        self.champion_fmvp_text.grid(row=2, column=1, sticky=W)
        self.special_player_label.grid(row=4, column=0, sticky=W)
        self.special_player_taxt.grid(row=5, column=0, sticky=W)
        self.insert_old_team_name_label.grid(row=0, column=2, sticky=W)
        self.insert_old_team_name.grid(row=1, column=2, sticky=W)
        self.insert_new_team_name_label.grid(row=2, column=2, sticky=W)
        self.insert_new_team_name.grid(row=3, column=2, sticky=W)
        self.insert_coa_session_label.grid(row=4, column=2, sticky=W)
        self.insert_coa_session.grid(row=5, column=2, sticky=W)
        self.insert_player_name_label.grid(row=0, column=3, sticky=W)
        self.insert_player_name.grid(row=1, column=3, sticky=W)
        self.change_session_old_password_label.grid(row=2, column=3, sticky=W)
        self.change_session_old_password.grid(row=3, column=3, sticky=W)
        self.change_session_new_password_label.grid(row=4, column=3, sticky=W)
        self.change_session_new_password.grid(row=5, column=3, sticky=W)
        self.course_button.grid(row=0, column=4, sticky=W)
        self.course_button2.grid(row=1, column=4, sticky=W)
        self.course_button3.grid(row=2, column=4, sticky=W)
        self.course_button4.grid(row=3, column=4, sticky=W)
        self.course_button5.grid(row=4, column=4, sticky=W)
        self.course_button6.grid(row=5, column=4, sticky=W)
        self.course_button7.grid(row=6, column=4, sticky=W)

#   添加队伍
    def insert_team(self):
        new_team_name = self.insert_old_team_name.get()
        information.insert_team(new_team_name, None, None)
        self.update_ui()

#   解散队伍
    def delete_team(self):
        team_name = self.insert_old_team_name.get()
        information.delete_team(team_name)
        self.update_ui()

#   队伍改名
    def rechristen_team(self):
        old_team_name = self.insert_old_team_name.get()
        new_team_name = self.insert_new_team_name.get()
        information.change_team_name(new_team_name, old_team_name)
        self.update_ui()

#   跳转队伍信息界面
    def jump_team(self):
        team_name = self.insert_old_team_name.get()
        teamjump = team_class.Team(team_name)
        teamjump.start()

#   换届
    def change_session(self):
        session = self.insert_coa_session.get()
        player_mvp = self.insert_player_name.get()
        champion_team = self.insert_old_team_name.get()
        password = self.change_session_old_password.get()
        information.insert_coa_game_session(session, champion_team, player_mvp, password)
        self.update_ui()

#   改密码
    def change_password(self):
        session = self.insert_coa_session.get()
        new_password = self.change_session_new_password.get()
        old_password = self.change_session_old_password.get()
        information.change_game_password(new_password, old_password, session)
        self.update_ui()

    def update_ui(self):
        team_name = self.insert_old_team_name.get()
        self.coa_team_text.delete(1.0, END)
        self.champion_fmvp_text.delete(1.0, END)
        self.special_player_taxt.delete(1.0, END)
        information.display_team_all(self.coa_team_text)
        information.display_coa_champion_fmvp_all(self.champion_fmvp_text)
        information.select_select_rescue_assist_player(self.special_player_taxt, team_name)

    def start(self):
        self.inilize()
        self.update_ui()
        self.root.mainloop()


if __name__=='__main__':
    coa = Coagame()
    coa.start()

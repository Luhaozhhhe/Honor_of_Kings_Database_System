import pymysql
import numpy as np
from tkinter import *

# 添加队员
def insert_team_player(player_name, player_id, common_role1, common_role2, team_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "INSERT INTO player (player_name, player_id, common_role1, common_role2, team_name) " \
          "VALUES (%s, %s, %s, %s, %s)"
    val = (player_name, player_id, common_role1, common_role2, team_name)

    try:
        cursor.execute(sql, val)
        db.commit()
    except :
        db.rollback()  # 回滚到上一次提交的状态
        print("队伍不存在或该昵称已被占用，该队员添加申请不通过。")

    # 关闭游标和数据库连接
    cursor.close()
    db.close()

# 添加队伍
def insert_team(team_name, coach, team_leader):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "insert into team (team_name, coach, team_leader) values (%s, %s, %s)"
    val = (team_name, coach, team_leader)

    try:
        cursor.execute(sql, val)
        db.commit()
    except :
        db.rollback()  # 回滚到上一次提交的状态
        print("队伍添加失败。")

    # 关闭游标和数据库连接
    cursor.close()
    db.close()

# 添加新一届
def insert_coa_game_session(session, champion_team, player_mvp, password1):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "insert into abyss_game (session, champion_team, player_mvp, password1) values (%s, %s, %s, %s)"
    val = (session, champion_team, player_mvp, password1)

    try:
        cursor.execute(sql, val)
        db.commit()
    except :
        db.rollback()  # 回滚到上一次提交的状态
        print("新一轮赛事添加失败！！！")

    # 关闭游标和数据库连接
    cursor.close()
    db.close()

# 删除队员
def delete_player(player_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "delete from player where player_name = %s "
    val = (player_name,)
    try:
        cursor.execute(sql, val)
        db.commit()
    except :
        db.rollback()  # 回滚到上一次提交的状态
        print("该队员曾获得FMVP，无法删除队员！！！")

    # 关闭游标和数据库连接
    cursor.close()
    db.close()

# 删除队伍
def delete_team(team_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "delete from team where team_name = %s "
    val = (team_name,)
    try:
        cursor.execute('START TRANSACTION')
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        db.rollback()  # 若出现错误，则回滚到上一次提交的状态
        print("该队伍曾获得某赛事冠军，无法删除该队伍！！！")

    # 关闭游标和数据库连接
    cursor.close()
    db.close()

# 打印选手信息
def display_player(text, player_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select * from player where player_name = %s "
    val = (player_name,)
    cursor.execute(sql, val)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, '%s %4s %4s %4s %4s' % tuple(col[0:5]))
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, '%s %4s %4s %4s %4s' % tuple(row[0:5]))
        text.insert(END, '\n')

    # 关闭游标和数据库连接
    cursor.close()
    db.close()

# 显示某支队伍信息
def display_team(text, team_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select * from team  where team_name = %s "
    val = (team_name,)
    cursor.execute(sql, val)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, '%s %4s %4s' % tuple(col[0:3]))
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, '%s %4s %4s' % tuple(row[0:3]))
        text.insert(END, '\n')

    cursor.close()
    db.close()

# 显示全部队伍的信息
def display_team_all(text):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select * from team"
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, '%s %4s %4s' % tuple(col[0:3]))
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, '%s %4s %4s' % tuple(row[0:3]))
        text.insert(END, '\n')

    cursor.close()
    db.close()

# 显示获得某届赛事的冠军队伍及其FMVP选手
def display_coa_champion_fmvp(text, session):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select champion_team,player_mvp from abyss_game where session = %s "
    val = (session,)
    cursor.execute(sql, val)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, '%s %4s' % tuple(col[0:2]))
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, '%s %4s' % tuple(row[0:2]))
        text.insert(END, '\n')

    cursor.close()
    db.close()

# 显示所有的赛事中获得冠军的队伍及其FMVP选手
def display_coa_champion_fmvp_all(text):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select session,champion_team,player_mvp from abyss_game"
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, '%s %4s %4s' % tuple(col[0:3]))
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, '%s %4s %4s' % tuple(row[0:3]))
        text.insert(END, '\n')

    cursor.close()
    db.close()

# 显示队伍的队员
def display_team_player_name(text, team_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select player_name from player where team_name = '%s' " % team_name
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, col)
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, row)
        text.insert(END, '\n')

    cursor.close()
    db.close()

# 显示队伍的队员id
def display_team_player_id(text, team_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select player_id from player where team_name = '%s' " % team_name
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, col)
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, row)
        text.insert(END, '\n')

    cursor.close()
    db.close()

# 显示队伍选手的常用角色
def display_team_player_role(text, team_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select common_role1,common_role2 from player  where team_name = '%s' " % team_name
    cursor.execute(sql)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, '%s %4s' % tuple(col[0:2]))
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, '%s %4s' % tuple(row[0:2]))
        text.insert(END, '\n')

    cursor.close()
    db.close()

# 队伍改名
def change_team_name(newteam_name, oldteam_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "call updateteam_name(%s, %s) "
    val = (newteam_name, oldteam_name)
    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        db.rollback()  # 回滚到上一次提交的状态
        print("出现了一些问题，队伍改名失败！！！")

    # 关闭游标和数据库连接
    cursor.close()
    db.close()

# 选手改名
def change_player_name(newplayer_name, oldplayer_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    val = (newplayer_name, oldplayer_name)
    try:
        cursor.callproc("updateplayer_name", val)
        db.commit()
    except Exception as e:
        db.rollback()  # 回滚到上一次提交的状态
        print("出现了一些问题，选手改名失败！！！")
    # 关闭游标和数据库连接
    cursor.close()
    db.close()

# 修改密码
def change_game_password(new_password, old_password, session):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "UPDATE abyss_game SET password1 = %s WHERE password1 = %s AND session = %s"
    # 执行 SQL 语句
    try:
        cursor.execute(sql, (new_password, old_password, session))
        # 提交更改
        db.commit()
        print("修改密码成功~")
    except Exception as e:
        # 回滚到上一次提交的状态
        db.rollback()
        print("修改密码失败~")

    # 关闭数据库连接
    cursor.close()
    db.close()

# 挑选既擅长辅助位又擅长对抗路的选手
def select_select_rescue_assist_player(text, team_name):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='Honor_of_Kings', charset='utf8')
    cursor = db.cursor()
    sql = "select * from team_rescue_assist where team_name = %s"
    val = team_name
    cursor.execute(sql, val)
    col = []
    for i in list(np.array(cursor.description)):
        col.append(i[0])
    text.insert(END, '%s %4s %4s %4s' % tuple(col[0:4]))
    text.insert(END, '\n')
    result = cursor.fetchall()

    for row in result:
        text.insert(END, '%s %4s %4s %4s' % tuple(row[0:4]))
        text.insert(END, '\n')

    cursor.close()
    db.close()

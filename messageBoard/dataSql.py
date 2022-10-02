import pymysql

def canLogin(username,password):
    sql=f'select password from users where username=%s'
    newCursor.execute(sql,username)
    res=newCursor.fetchall()
    if res:
        if res[0][0]==password:
            return True
        else:
            return False
    else:
        return False
    
def register(id,username,password,power):
    sql=f'select username from users where username=%s'
    newCursor.execute(sql,username)
    res=newCursor.fetchall()
    if res:
        return False
    else:
        sql=f'insert into users (id,username,password,power) values (%s,%s,%s,%s)'
        newCursor.execute(sql,(id,username,password,power))
        db.commit()
        return True
    
def changePassword(username,oldPassword,newPassword):
    sql=f'select password from users where username=%s'
    newCursor.execute(sql,username)
    res=newCursor.fetchall()
    if res:
        if oldPassword==res[0][0]:
            sql=f'update users set password=%s where username=%s'
            newCursor.execute(sql,(newPassword,username))
            db.commit()
            return True
        else:
            return "wrong password"
    else:
        return "username doesn't exist."
    
def uploadMessage(username,message,nowtime,private):
    sql=f'insert into message (username,data,time,private) values (%s,%s,%s,%s)'
    newCursor.execute(sql,(username,message,nowtime,private))
    db.commit()
    return True

def showMessage():
    sql='select * from message'
    newCursor.execute(sql)
    res=newCursor.fetchall()
    return res

def usersName():
    sql='select * from users'
    newCursor.execute(sql)
    res=newCursor.fetchall()
    sql='select * from users'
    newCursor.execute(sql)
    res=newCursor.fetchall()
    return len(res)

def getPower(username):
    sql=f'select power from users where username=%s'
    newCursor.execute(sql,username)
    res=newCursor.fetchall()
    return res


def deleteMessage(username,pubTime):
    sql=f'delete from message where username=%s and time=%s'
    newCursor.execute(sql,(username,pubTime))
    res=newCursor.fetchall()
    db.commit()
    return True



db = pymysql.connect(host='localhost',#数据库地址
                       port=3306,#数据库端口
                       user='root',#数据库用户名
                       passwd='xlyyds',#数据库密码
                       database='messageboard',#数据库名
                       charset = 'utf8'
                       )

newCursor = db.cursor()#获取操作游标

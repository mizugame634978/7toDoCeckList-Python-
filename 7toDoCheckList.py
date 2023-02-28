import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import datetime



# SQLiteデータベースに接続
conn = sqlite3.connect('7toDoCheckList.db')
cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()
cur4 = conn.cursor()

global_bln = {}
global_task_name = {}

# GUIアプリケーションの作成#############
root = tk.Tk()
root.title("7toDoCheckList")
root.geometry("400x320")
#root.resizable(True, True)
root.resizable(width=False,height=False)#windowのサイズを固定
#root.attributes('-fullscreen', True)

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

frame2=ttk.Frame(root)#frame2をつかい各flameを作る
frame2.rowconfigure(0,weight=1)
frame2.columnconfigure(0,weight=1)
frame2.grid(row=0,column=0,sticky="nsew")
scan_frame=tk.Frame(frame2,background="beige")#最初に出る画面
scan_frame.grid(row=0,column=0,sticky="nsew")
#####################


def change_check_sql(i):
    global global_bln
    global global_task_name
    if global_bln[i].get():
        # チェックをつけたとき
        #print ("check")
        cur.execute('update ToDo set check_flag =1 where task_name = ?',(global_task_name[i],))
    else:
        # チェックをはずしたとき
        #print ("NoCheck")
        cur.execute('update ToDo set check_flag =0 where task_name = ?',(global_task_name[i],))
    conn.commit()

def create_scan(window):
    window.destroy()
    scan_frame=tk.Frame(frame2,background="red")#最初に出る画面
    scan_frame.grid(row=0,column=0,sticky="nsew")
    #削除ボタンを作成
    delete_button = tk.Button(scan_frame,text='削除',font=18,width=10,height=5, command=delete_item)
    delete_button.place(relx = 0.3,rely = 0.6,anchor=tk.W)

    textBox1 = tk.Entry(scan_frame,font=("",30),width=50)#テキストボックスの横幅を設定,入力できる文字数？
    textBox1.place(relx=0.4, rely=0.1,width=100,height=50)
    textBox1.bind('<Return>', add_task)

    get_button =  tk.Button(scan_frame,text='get_all',font=18,width=10,height=5, command=lambda:get_all())
    get_button.place(relx = 0.3, rely = 0.3, anchor = tk.W)
    #get_all()

def get_all():

    global global_task_name
    #now = datetime.date.today
    cnt = 0
    cur.execute('SELECT task_name FROM ToDo')
    cur2.execute('select add_day from ToDo ')
    cur3.execute('select check_flag from ToDo')
    cur4.execute('SELECT task_name FROM ToDo')
    global global_bln

    #scan_frame.destroy()
    #create_scan()

    #cc0 = tk.Checkbutton(scan_frame,width=10,text="",)
    cc0 = tk.Label(scan_frame,width=14,text='')
    cc0.grid(row= 0,column=10,padx=0,pady=0,ipadx=10,ipady=12)
    #cc1 = tk.Checkbutton(scan_frame,width=10,text="")
    cc1 = tk.Label(scan_frame,width=14,text='')
    cc1.grid(row= 1,column=10,padx=0,pady=0,ipadx=10,ipady=12)
    #cc2 = tk.Checkbutton(scan_frame,width=10,text="")
    cc2 = tk.Label(scan_frame,width=14,text='')
    cc2.grid(row= 2,column=10,padx=0,pady=0,ipadx=10,ipady=12)
    #cc3 = tk.Checkbutton(scan_frame,width=10,text="")
    cc3 = tk.Label(scan_frame,width=14,text='')
    cc3.grid(row= 3,column=10,padx=0,pady=0,ipadx=10,ipady=12)
    #cc4 = tk.Checkbutton(scan_frame,width=10,text="")
    cc4 = tk.Label(scan_frame,width=14,text='')
    cc4.grid(row= 4,column=10,padx=0,pady=0,ipadx=10,ipady=12)
    #cc5 = tk.Checkbutton(scan_frame,width=10,text="")
    cc5 = tk.Label(scan_frame,width=14,text='')
    cc5.grid(row= 5,column=10,padx=0,pady=0,ipadx=10,ipady=12)
    #cc6 = tk.Checkbutton(scan_frame,width=10,text="")
    cc6 = tk.Label(scan_frame,width=14,text='')
    cc6.grid(row= 6,column=10,padx=0,pady=0,ipadx=10,ipady=12)

    for row in cur.fetchall():
        hoge = cur2.fetchone()
        #Check_flag = cur3.fetchmany()
        Check_flag = cur3.fetchone()
        #Check_flag2 = Check_flag[0][0]
        Check_flag2 = Check_flag[0]
        task_name = cur4.fetchone()
        task_name2 = task_name[0]
        now = datetime.date.today()
        #print(Check_flag2)
        ca1 = "gray"
        #print(type(hoge[0]))
        #print(type(now))
        #print(" ")
        if(hoge[0] == str(now)):
            ca1 = "white"
        global_task_name[cnt] = task_name2
        #print(task_name2)

        #bln=tk.BooleanVar(value=True)
        bln= tk.BooleanVar()  # 初期値を設定する場合
        global_bln[cnt] = tk.BooleanVar()

        # if(global_bln[cnt]==check1):
        #     bln.set(True)
        # else:
        #     bln.set(False)           #チェックボックスの初期値
        bln.set(True)




        #g_bln = global_bln[cnt]
        if(cnt == 0):
            c0 = tk.Checkbutton(scan_frame,width=10,text=row,variable = global_bln[cnt],background=ca1,command=lambda:change_check_sql(0))
            c0.grid(row= cnt,column=10,padx=0,pady=0,ipadx=10,ipady=10)  #0列目
        elif(cnt == 1):
            c1 = tk.Checkbutton(scan_frame,width=10,text=row,variable = global_bln[cnt],background=ca1,command=lambda:change_check_sql(1))
            c1.grid(row= cnt,column=10,padx=0,pady=0,ipadx=10,ipady=10)  #列目
        elif(cnt == 2):
            c2 = tk.Checkbutton(scan_frame,width=10,text=row,variable = global_bln[cnt],background=ca1,command=lambda:change_check_sql(2))
            c2.grid(row= cnt,column=10,padx=0,pady=0,ipadx=10,ipady=10)  #列目
        elif(cnt == 3):
            c3 = tk.Checkbutton(scan_frame,width=10,text=row,variable = global_bln[cnt],background=ca1,command=lambda:change_check_sql(3))
            c3.grid(row= cnt,column=10,padx=0,pady=0,ipadx=10,ipady=10)  #列目
        elif(cnt == 4):
            c4 = tk.Checkbutton(scan_frame,width=10,text=row,variable = global_bln[cnt],background=ca1,command=lambda:change_check_sql(4))
            c4.grid(row= cnt,column=10,padx=0,pady=0,ipadx=10,ipady=10)  #列目
        elif(cnt == 5):
            c5 = tk.Checkbutton(scan_frame,width=10,text=row,variable = global_bln[cnt],background=ca1,command=lambda:change_check_sql(5))
            c5.grid(row= cnt,column=10,padx=0,pady=0,ipadx=10,ipady=10)  #列目
        elif(cnt == 6):
            c6 = tk.Checkbutton(scan_frame,width=10,text=row,variable = global_bln[cnt],background=ca1,command=lambda:change_check_sql(6))
            c6.grid(row= cnt,column=10,padx=0,pady=0,ipadx=10,ipady=10)  #列目


        # c = tk.Checkbutton(scan_frame,width=10,text=row,variable = global_bln[cnt],background=ca1)
        # c.grid(row= cnt,column=10,padx=0,pady=0,ipadx=10,ipady=10)  #0列目
        if(Check_flag2 == 1):#とりあえずチェックなしで配置してsqlみてチェックする
            btn_click(True,cnt)
        cnt += 1

        if cnt >= 7:
            break
    #print(global_task_name)
    #print(global_task_name[0])



def btn_click(bln,i):#チェックの切替
    #for i in range(len(global_bln)):
    global_bln[i].set(bln)



def add_task(event):
    cur2.execute('select count(*) from ToDo')
    can_add = cur2.fetchone()
    can_add2 = can_add[0]#count(*)の結果

    char = textBox1.get()
    cur3.execute('select *from ToDo where task_name = ?',(char,))
    judge = cur3.fetchone()
    #print("↓")
    #print( judge)
    if(judge == None):#重複していなかった場合

        if(can_add2 < 7):

            char1 =  textBox1.get()
            now = datetime.date.today()
            #print (now)
            #print(char1)

            #now = "2020-01-03"
            cur.execute('insert into ToDo values (? , ?,"None","None",0) ',(char1,now,))
            conn.commit()
            #cur.execute('INSERT INTO ToDo values( "体操","2020-01-03","None","0")')
            textBox1.delete(0,tk.END)
            get_all()






# 選択された行を削除する関数
def delete_item():
    global_bln
    cur2.execute('select count(*) from ToDo')
    data_count = cur2.fetchone()
    data_couunt2 = data_count[0]#count(*)の結果
    #print("sa")
    i = 0
    while i < data_couunt2:
        if global_bln[i].get():# チェックをつけたとき
            cur.execute('delete from ToDo where task_name = ?',(global_task_name[i],))

            conn.commit()# コミットしないと登録が反映されない
            textBox1.delete(0,tk.END)

        i += 1
    conn.commit()# コミットしないと登録が反映されない

    get_all()
    #create_scan(scan_frame)




#削除ボタンを作成
delete_button = tk.Button(scan_frame,text='チェック済み削除',font=18,width=15,height=3, command=delete_item)
#delete_button.place(relx = 0.3,rely = 0.6,anchor=tk.W)
delete_button.place(x = 150, y =200 )

textBox1 = tk.Entry(scan_frame,font=("",15),width=50)#テキストボックスの横幅を設定,入力できる文字数？
textBox1.place(x=250, y=20,width=140,height=50)
textBox1.bind('<Return>', add_task)

get_button =  tk.Button(scan_frame,text='更新',font=18,width=10,height=3, command=lambda:get_all())
#get_button.place(relx = 0.3, rely = 0.3, anchor = tk.W)
#get_button.place(x = 150, y =100 )

label1 = tk.Label(scan_frame,text='追加：',font = 10,width=5,height=3)
#label1.grid(row= 0,column=11,padx=0,pady=0,ipadx=0,ipady=0)  #0列目
label1.place(x = 150,y = 20)

try:
    get_all()#プログラム起動時にdbとテーブルがないとこれが失敗する

except:
    #print("except")
    cur.execute('CREATE TABLE ToDo(task_name string primay key, add_day string,finish_day string,finish string,check_flag int)')
    conn.commit()
    get_all()#プログラム起動時にdbとテーブルがないとこれが失敗する


root.mainloop()

from sqlalchemy import create_engine
import pandas as pd
import datetime
import subprocess


cnx = create_engine('mysql+pymysql://root:123@localhost:3306/payroll').connect()

def emp_entry():
    ec = eval(input("enter employee code : "))
    fn = input("enter first name of employee : ")
    ln = input("enter last name of employee : " )
    dg = input("enter designation : " )
    ge = input("enter gender : ")
    db = input("enter date of birth : ")
    dj = input("enter date of joining : ")
    mb = input("enter mobile number :")
    pn = input("enter pan number : ")
    ac = input("enter account number : ")
    fc = input("enter IFSC code of bank account : ")
    sl = eval(input("enter pay level : "))
    bs = eval(input("enter basic salary : "))
    ta = eval(input("enter travel allowance : "))
    hr = input("enter employee is eligible for HRA Y/N : ")
    np = input("enter employee is eligible for NPS Y/N : ")
    data = [[ec,fn,ln,dg,ge,db,dj,mb,pn,ac,fc,sl,bs,ta,hr,np]]
    df = pd.DataFrame(data,colums=['ecode','fname','lname','desig','level','gender','dob','doj','mob','pan','acno','ifac','basic','ta','hrayn','npsyn'])
    df.to_sql(name = 'emp',con = cnx, if_exists ='append', index = False)


def per_setter() :
    dap = eval(input("enter DA percentage"))
    hrp = eval(input("enter HRA percentage"))
    data = [[dap,hrp]]
    df = pd.DataFrame(data,colums=['dap','hrap'])
    df.to_sql(name = 'setter', con = cnx, if_exists = 'replace', index = False)

def salary_entry():
    while True:
        try:
            y = eval(input("enter the salary year (press enter for current year otherwise input new year : " + str(datetime.datetime.today().strftime('%Y'))))
        except:
                           y = str(datetime.datetime.today().strftime('%y'))

                           break
    while True:
        try:

            m = eval(input("enter the salary month (press enter for current month otherwise input new month : " + str(datetime.datetime.today().strftime('%m'))))
        except:
            m = str(datetime.datetime.today().strftime('%m'))

            break
    sql="select * from emp "
    df=pd.read_sql(sql,cnx)
    print("enter salary details for the " + str(m) + "/" + str(y))


    lec=[]
    llevel=[]
    lec = df["ecode"]
    ll=[]
    ly = []
    lm = []
    allw = []
    deduc = []
    lfee = []
    it = []
    for x in df["ecode"]:
        print("employee code :" + str(x) + "\n")
        ll.append(eval(input("enter no of days worked ;")))
        allw.append(eval(input("enter other allowence (or 0): ")))
        deduc.append(eval(input("enter other deductions (or 0) : ")))
        it.append(eval(input("enter income tax to be deducted (or o) : ")))
        lfee.append(eval(input("enter other license fee (or o) : ")))
        ly.append(y)
        lm.append(m)
        
     sql=("select * from pay")
     df1=pd.read_sql(sql,cnx)
     df1["year"] = ly
     df1["month"] = lm
     df1["ecode"] = lec
     df1["nodays"] = ll
     df1 = pd.merge(df,df1,on='ecode')
     df1["basic"] = df1["basic"]/30 * df1["nodays"]
     df1["da"] = df1["basic"] * DP/100
     df1["data"] = df1["ta"] *DP/100
     df1["hra"] = df1["ta"] * HP/100
     df1["nps_m"] = (df1["basic"] + df1["da"]) * 10/100
     df1["other_allw"] = allw
     df1["gross"] = df1["basic"] + df1["da"] + df1["data"] + df1["hra"] + df1["nps_m"] + df1["other allw"]
     df1["nps_o"] = df1["nps_m"]
     df1["gpf"] = df1["basic"] * 6/100
     df1["lcfee"] = lfee
     df1["itax"] = it
     
     df1["odeduct"] = deduc

     df1["total_deduc"] = df1["itax"] + df1["nps_m"] + df1["gpf"] + df1["odeduct"] + df1["lcfee"]
     df1["netsal"] = df1["gross"] - df1["total_deduc"]
     df1.to_csv('c:\payroll\salary.csv', mode = 'w')

def Data_operations():
    x = datetime.datetime.today().strftime('%Y-%m-%d')
    print(x)
def sdf_show():
    df = pd.read_csv('c:\payroll\salary.csv')
    print(df)
def show_rates():

    sql = "select * from setter"
    df = pd.read_sql(sql, cnx)
    print(df)

def show_emp():
    sql = "select * from emp"
    df = pd.read_sql(sql, cnx)

    print(df)

def salary_show():
    subprocess.call('c:\program files\microsoft office\office15\excel c:\payroll\salary.csv')



dp = 0
hp = 0
sql = "select * from setter"
df = pd.read_sql (sql, cnx)
dp = df["dap"][0]
hp = df["hrap"][0]
    while (True):
        print("1 : add employee details")
        print("2 : show employee details")
        print("3 : fix da and hra rates")
        print("4 : show current da and hra rates ")
        print("5 : paybill entry")
        print("6 : show paybill")
        print("7 : show paybill (csv file in excel)")
        print("8 : exit")

        choice = int(input("please select an above option:"))
        if(choice == 1):
            emp_entry()
        elif(choice == 2):
            show_emp()
        elif(choice == 3):
            per_setter()
        elif(choice == 4):
            show_rates()
        elif(choice == 5):
            saalry_entry()
        elif(choice == 6):
            sdf_show()
        elif(choice == 7):
            salary_show()
        elif(choice == 8):
            break
        else:
            print("WRONG CHOICE.............")
                      
        
        
        
    
     

     

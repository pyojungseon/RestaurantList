import pymysql
import sys
import configparser
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.logDTO import logDTO
from DTO.restaurantDTO import restaurantDTO

class DBConnection:

    conn = None
    env = None

    def __init__(self, _env):
        print("DB Construcor : %s" % _env)
        self.env = _env

    def __del__(self):
        print("DB Destructor")
        self.conn.close()

    def getDBConfig(self):
        properties = configparser.ConfigParser()
        properties.read('../config/DBconfig.ini')
        if(self.env=='T'):
            props = properties["TEST"]
        else:
            props = properties["PROD"]
        print("DB Mode : %s" % props["env"])
        return props

    def dbConnection(self):
        props = self.getDBConfig()
        _host = props["host"]
        _user = props["user"]
        _password = props["password"]
        _db = props["db"]
        _charset=props["charset"]
        print(props)
        self.conn = pymysql.connect(host=_host, user=_user, password=_password, db=_db, charset=_charset)

    def getMateData(self, telegramID):
        cur = self.conn.cursor()
        sql = 'select * from MateTBL where telegramID ='+str(telegramID)
        cur.execute(sql)
        mateData = []
        while(True):
            row = cur.fetchone()
            if row==None:
                break
            mateData.append(row)
        return mateData

    def insertLogData(self, logData):
        cur = self.conn.cursor()
        print("%s %s %s" %(logData.id, logData.content, logData.tag))
        try:
            sql = "insert into LogTBL values('"+logData.id+"','"+logData.content+"','"+logData.tag+"',current_timestamp)"
            print(sql)
            cur.execute(sql)
        except Exception as ex:
            print("insertLogData error")
            print(ex)
        self.conn.commit()

    def insertSugData(self, sugData):
        cur = self.conn.cursor()
        print("%s %s" %(sugData.id, sugData.content))
        try:
            sql = "insert into SugTBL values('"+sugData.id+"','"+sugData.content+"',current_timestamp)"
            print(sql)
            cur.execute(sql)
        except Exception as ex:
            print("insertSugData error")
            print(ex)
        self.conn.commit()

    def getRestaurant(self, name):
        cur = self.conn.cursor()
        sql = "select * from RestTBL where name='"+name+"';"
        print(sql)
        cur.execute(sql)
        row = cur.fetchone()
        return row

    def getRecRestaurants(self, recData):
        cur = self.conn.cursor()
        sql = "select * from RestTBL " \
                " where tag = '"+recData.tag+"'" \
                " and (lprice="+recData.lprice+" or hprice="+recData.hprice+")" \
                " and ('N'='"+recData.moksung+"' or moksung='"+recData.moksung+"')" \
                " and ('N'='"+recData.payco+"' or payco='"+recData.payco+"')" \
                " and ('N'='"+recData.mn5+"' or mn5='"+recData.mn5+"')" \
                " and ('N'='"+recData.mn4+"' or mn4='"+recData.mn4+"')" \
                " and ('N'='"+recData.mn2+"' or mn2='"+recData.mn2+"');"
        print(sql)
        cur.execute(sql)
        mateData = []
        while (True):
            row = cur.fetchone()
            if row == None:
                break
            mateData.append(row)
        return mateData

    def updateRestEval(self, name, content):
        cur = self.conn.cursor()
        try:
            sql="update RestTBL set eval='"+content+"', modDate=current_timestamp where name = '"+name+"'"
            print(sql)
            cur.execute(sql)
        except Exception as ex:
            print("RestTBL eval update error")
            print(ex)
        self.conn.commit()
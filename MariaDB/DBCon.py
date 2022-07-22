import pymysql
import sys
import configparser
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.LogDTO import LogDTO

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
            print("log insert error")
            print(ex)
        self.conn.commit()
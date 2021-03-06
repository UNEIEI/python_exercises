# coding=utf-8
import sys
import MySQLdb

#TransferMoney类，定义转账方法
class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn        
    
    #检查账号是存在 
    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s" % acctid
            cursor.execute(sql)
            print "check_acct_available:" + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception(u"账号%s不存在" % acctid)
        finally:
            cursor.close()
    
    #检查账号余额是否足够        
    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>%s" % (acctid, money)
            cursor.execute(sql)
            print "has_enough_money:" + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception(u"账户%s余额不足" % acctid)
        finally:
            cursor.close()      
    
    #减款
    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print "reduce_money:" + sql
            if cursor.rowcount != 1:
                raise Exception(u"账号%s减款失败" % acctid)
        finally:
            cursor.close()
    
    #加款
    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print "add_money:" + sql
            if cursor.rowcount != 1:
                raise Exception(u"账号%s加款失败" % acctid)
        finally:
            cursor.close()
    
    #转账        
    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

if __name__ == "__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    
    #建立数据库连接对象
    conn = MySQLdb.Connect(host='127.0.0.1',
                           user='root',
                           passwd='root',
                           port=3306,
                           db='test1')
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print u"出现问题:", unicode(e)
    finally:
        conn.close()
        
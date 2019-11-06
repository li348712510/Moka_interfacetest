# _*_ encoding: utf-8 _*_
import config
import pymysql


class Mysql:
    data = config.sql

    @classmethod
    def connect(cls, db):
        url = cls.data.url
        username = cls.data.usrename
        psw = cls.data.password
        port = cls.data.port
        con = pymysql.connect(host=url, port=port, user=username, passwd=psw, db=db)
        return con

    @classmethod
    def select(cls, databass, sql):
        """查询"""
        con = cls.connect(databass)
        cu = con.cursor()
        cu.execute(sql)
        data = cu.fetchall()
        con.close()
        return data

    @classmethod
    def other(cls, databass, sql):
        """增删改"""
        con = cls.connect(databass)
        cu = con.cursor()
        cu.execute(sql)
        con.commit()

        try:
            cu.execute(sql)
            con.commit()

        except:
            con.rollback()

        con.close()







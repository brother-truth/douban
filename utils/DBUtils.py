# -*- coding: utf-8 -*-


import pymysql  # 导入 pymysql



class DBUtils:

    def __init__(self, host, user, password, db, port):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.conn = None

    # 创建连接和游标
    def getConn(self):
        encoding = "utf8"
        self.conn = pymysql.connect(host=self.host, user=self.user,
                                    password=self.password, db=self.db, port=self.port, charset=encoding)
        self.cursor = self.conn.cursor()

    # 查询, 需要传入SQL
    def query(self, sql):
        try:
            if self.conn is None:
                self.getConn()
            effectLine = self.cursor.execute(sql)  # 执行sql语句
            results = self.cursor.fetchall()  # 获取查询的所有记录
            # print(type(results))
            # 遍历结果results是1个元组
            print("Query Success,effectLine:" + str(effectLine))
            return results
        except Exception as e:
            print("Query Failed, Exception")
            raise e

    # 删除, 需要传入SQL
    def delete(self, sql):
        try:
            if self.conn is None:
                self.getConn()
            effectLine = self.cursor.execute(sql)  # 执行sql语句
            # Commit
            self.conn.commit()
            print("Delete Success,effectLine:" + str(effectLine))
        except Exception as e:
            print("Delete Failed, Rollback")
            self.conn.rollback()
            raise e

    # 修改, 需要传入SQL
    def modify(self, sql):
        try:
            if self.conn is None:
                self.getConn()
            effectLine = self.cursor.execute(sql)  # 执行sql语句
            # Commit
            self.conn.commit()
            print("Update Success" + str(effectLine))
        except Exception as e:
            print("Modify Failed, Rollback")
            self.conn.rollback()
            raise e

    # 插入, 需要传入SQL
    def insert(self, sql):
        try:
            if self.conn is None:
                self.getConn()
            effectLine = self.cursor.execute(sql)  # 执行sql语句
            # Commit
            self.conn.commit()
            print("Insert Success" + str(effectLine))
        except Exception as e:
            print("Insert Failed, Rollback")
            self.conn.rollback()
            raise e

        # 批量插入, 需要传入sql和list

    def insertMany(self, sql, list):

        print(type(list[0][0]))

        try:
            if self.conn is None:
                self.getConn()
            effectLine = self.cursor.executemany(sql, list)  # 执行sql语句
            # Commit
            self.conn.commit()
            print("Insert Success" + str(effectLine))
        except Exception as e:
            print("Insert Failed, Rollback")
            self.conn.rollback()
            raise e

    # 关闭连接
    def close(self):
        if self.conn is not None:
            self.conn.close()


db = DBUtils("localhost", "root", "s89112918", "crawler", 3306)
# queryResult = db.query("select * from test")
# print(queryResult)
# db.close()
# db.insertMany('insert into test(id, name) values (%s, %s)', [[3,'1'],[4,'2']])

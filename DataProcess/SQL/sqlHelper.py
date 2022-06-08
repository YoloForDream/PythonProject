import pymssql


class sqlHelper:
    def __init__(self, host, user, password, dbname, cmd):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.cmd = cmd

    def query(self):
        try:
            con = pymssql.connect(self.host, self.user, self.password, self.dbname)  # 建立连接
            if con:
                print("Data process.....")
            cur = con.cursor()
            sql = self.cmd
            cur.execute(sql)
            result = cur.fetchall()  # 查询全部数据fetchall(),查询一条数据fetchone()
            for result in result:  # 遍历循环打印输出结果
                # print(result)
                ll = list(result)
                # rr = list(str(x) for (x,) in result)
                print(ll[0])
                return ll[0]
            cur.close()
            con.close()
        except Exception as e:
            print(e)

    def delete(self):
        try:
            con = pymssql.connect(self.host, self.user, self.password, self.dbname)  # 建立连接
            if con:
                print("Data process.....")
            cur = con.cursor()
            sql = self.cmd
            cur.execute(sql)
            con.commit()
            cur.close()
            con.close()
            print("数据删除成功！")
        except Exception as er:
            con.rollback()  # 数据回滚
            print("数据修改失败" + (er))

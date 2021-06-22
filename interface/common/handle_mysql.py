import pymysql
from common.handle_config import conf


class HandleMysql:
    """mysql数据库相关操作"""

    def __init__(self):
        """初始化，连接数据库"""
        self.conn = pymysql.connect(host=conf.get("mysql", "host"),
                                    port=conf.getint("mysql", "port"),
                                    user=conf.get("mysql", "user"),
                                    password=conf.get("mysql", "password"),
                                    database=conf.get("mysql", "database"),
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    )
        self.cur = self.conn.cursor()

    def find_one(self, sql):
        """
        查询一条数据
        :param sql:
        :return: 查询到的第一条数据
        """
        try:
            self.conn.commit()
            self.cur.execute(sql)
            return self.cur.fetchone()
        except pymysql.err.ProgrammingError as e:
            raise e

    def find_all(self, sql):
        """
        查询所有数据
        :param sql:
        :return: 查询到的所有数据
        """
        try:
            self.conn.commit()
            self.cur.execute(sql)
            return self.cur.fetchall()
        except pymysql.err.ProgrammingError as e:
            raise e

    def find_count(self, sql):
        """
        查询的数据条数
        :param sql:
        :return: 查询的数据条数
        """
        try:
            self.conn.commit()
            return self.cur.execute(sql)
        except pymysql.err.ProgrammingError as e:
            raise e

    def update(self, sql):
        """
        增删改操作
        :param sql:
        :return: None
        """
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except pymysql.err.ProgrammingError as e:
            raise e

    def close(self):
        """断开游标，关闭连接"""
        self.cur.close()
        self.conn.close()

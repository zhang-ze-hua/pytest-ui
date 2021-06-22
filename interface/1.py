import pymysql
import re


def get_sms(mobile):
    conn = pymysql.connect(host="139.0.233.167",
                           user="root@dvl_ngdb_mid_59#ob_dvl",
                           password="Abcd1234",
                           database="sit_msg_pd",
                           port=3306)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    try:
        sql = "SELECT MRNC_SHRTMSG_CNTNT FROM msg_rcrd_note_capt WHERE MRNC_MBLPN_NO='%s' order by UPD_TME desc"
        cur.execute(sql, mobile)
        res_one = cur.fetchone()
        print(res_one)
        for key, value in res_one.items():
            res = re.search("\d{6}", value)
            return res.group()
    except pymysql.err.ProgrammingError as e:
        print(e)
    cur.close()
    conn.close()


print(get_sms(13750065199))

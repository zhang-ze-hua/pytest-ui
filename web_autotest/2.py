import ibm_db
import time
import re


def db2_sms_code(mobile):
    local_time = time.strftime("%Y%m%d", time.localtime())
    connstr = "DATABASE=isfstdb;HOSTNAME=172.16.249.14;PORT=60000;PROTOCOL=TCPIP;UID=isfstqry;PWD=isfstqry123;"
    conn = ibm_db.connect(connstr, "", "")
    try:
        sql = "select call_content from isfst.t_iss_call_task where mobile='{}' and OTH_RESPOND_DATE='{}' " \
              "order by abs(iss_seq) desc".format(mobile, local_time)
        # print(sql)
        stmt = ibm_db.exec_immediate(conn, sql)
        result = ibm_db.fetch_both(stmt)
        # print(result)
        if result:
            sms_code = result["CALL_CONTENT"]
            sms = re.findall("\d{6}", sms_code)
            return sms[0]
        else:
            return None
    except Exception as e:
        raise e
    ibm_db.close(stmt)
    ibm_db.close(conn)


res = db2_sms_code(13366669999)
print(res)

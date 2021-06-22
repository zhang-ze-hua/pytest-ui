import requests
import time
import random

num = random.randint(00000000, 99999999)
local_time = time.strftime("%Y%m%d%X", time.localtime())
local_time = local_time.replace(":", "")
serial_number = local_time + str(num)

url = "http://107.255.22.220:8089/FD0003.do"
data = {
    # "TCode": "FD0004",
    "sysHead": {"pvdrPltfmDt": "", "glbRqsTmstmp": "", "errorCode": "", "stdIntfcInd": "", "srcConsmTmlType": "",
                "glbSrlNo": "", "retInf": "", "sysRsrvCharStrg": "", "ovtmTmNum": "", "stdIntfcVerNo": "",
                "usrNo": "01ZK015", "retCd": "", "pvdrTxnMchnDt": "", "instNo": "117063", "lglPrsnCd": "01",
                "macVal": "", "chnlNo": "030223", "dcnNo": "", "consmTxnMchnTm": "", "consmMainSrlNo": "",
                "stdSvcInd": "", "consmPltfmDt": "", "txnChrctrstcType": "", "consmSysInd": "DMBANK", "errorMsg": "",
                "pvdrSysInd": "", "pvdrMainSrlNo": "", "srcConsmTmlNo": "", "consmSvcInd": "", "consmTxnCd": "",
                "sysRsrvFlgStrg": "", "txnDstcNo": "", "consmTxnMchnDt": "", "pvdrTxnMchnTm": "",
                "srcConsmSysInd": "DMBANK", "consmSubSrlNo": "", "idcNo": ""},
    "localHead": {"rtFlowno": serial_number,
                  "uuid": "FD35C65E6A207A6ABAD901D4DA303255"
                  },
    "body": {
        "bsnType": "04",
        "qryType": "01",
        "usrId": "USC20210316032406000000000008961",
        "mblpnNo": "13066663605",
        "eqmtNo": "XsuDmmfq+wQDAPjUBrbjRUxd",
        "setComEqmtFlg": "1",
        "bindThirdAppFlg": "1",
        "ipAdr": "10.1.36.233",
        "macAdr": "62:C9:64:DF:89:83",
        "lgnPwd": "FNActZ9w//OehuQefJNcsQ==",
        "custTmlEryptRndmCnt": "weGoQX+VW58AZ8gJi4iZqPWxwAAdVu6vcpVt+JjvNe/j7F9bkE3Tp4Tl0jo1nCO2o7awggBcRdmv1Avsf5EyXhUM9DARgGoJuycSe8iXm776VyMGTNz+fxTuhHCSOpgvKejkv/sdBF+682gdvxks4A==",
        "srvTmlEryptRndmCnt": "A7AA30327F8307822894ED897B138729",
    }
}

res = requests.post(url=url, json=data)
print(res.json())

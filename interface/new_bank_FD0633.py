import requests
import time
import random

num = random.randint(00000000, 99999999)
local_time = time.strftime("%Y%m%d%X", time.localtime())
local_time = local_time.replace(":", "")
serial_number = local_time + str(num)

url = "http://107.255.22.220:8089/FD0633.do"
data = {
    # "TCode": "FD2211",
    "sysHead": {"pvdrPltfmDt": "", "glbRqsTmstmp": "", "errorCode": "", "stdIntfcInd": "", "srcConsmTmlType": "",
                "glbSrlNo": "", "retInf": "", "sysRsrvCharStrg": "", "ovtmTmNum": "", "stdIntfcVerNo": "",
                "usrNo": "01ZK015", "retCd": "", "pvdrTxnMchnDt": "", "instNo": "117063", "lglPrsnCd": "01",
                "macVal": "", "chnlNo": "030223", "dcnNo": "", "consmTxnMchnTm": "", "consmMainSrlNo": "",
                "stdSvcInd": "", "consmPltfmDt": "", "txnChrctrstcType": "", "consmSysInd": "DMBANK", "errorMsg": "",
                "pvdrSysInd": "", "pvdrMainSrlNo": "", "srcConsmTmlNo": "", "consmSvcInd": "", "consmTxnCd": "",
                "sysRsrvFlgStrg": "", "txnDstcNo": "", "consmTxnMchnDt": "", "pvdrTxnMchnTm": "",
                "srcConsmSysInd": "DMBANK", "consmSubSrlNo": "", "idcNo": ""},
    "localHead": {"rtFlowno": serial_number,
                  "usrId": "USC20210316041434000000000009061",
                  "tokenId": 'F3D2AD3540E5560B73AD63E0E00D5B8A'
                  },
    "body": {
        "identType": "01",
    }

}

res = requests.post(url=url, json=data)
print(res.json())

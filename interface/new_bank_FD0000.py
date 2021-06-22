import requests
import time
import random

num = random.randint(00000000, 99999999)
local_time = time.strftime("%Y%m%d%X", time.localtime())
local_time = local_time.replace(":", "")
serial_number = local_time + str(num)

url = "http://107.255.22.220:8089/FD2623.do"
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
                  "usrId": "USC20210324031100000000000009763",
                  "tokenId": 'C6FFDF769F420CF7789B5956BB5D3A0A'
                  },
    # "body": {"srcChannel": "CS",
    #          "crdtCrdNo": "b8acb1796be6e97d0626e92083253ebf",
    #          "qrySrvTmlEryptRndmCnt": "A7AA30327F8307822894ED897B138729",
    #          #"tranCode": "FD0624",
    #          "cfrmPwd": "RAnNZGHJ2XCH32Bhpaw6ZQ==",
    #          "qryCustTmlEryptRndmCnt": "x2yTFNsdIP4Jw/tLWxCMQYPo8W6AmK6ThxBe6GTgzS2qWxFjypn/XuSOD5kL3n/4jAGAEsJDDro4pjeRsyCm86xW1MsCybcxe/FteSc1DkBluy9anaOAlUe1T1H4kojawkcp/IGQdxZpvvXQ0Mn/wA=="
    #          }
    "body": {

    }
}

res = requests.post(url=url, json=data)
print(res.json())

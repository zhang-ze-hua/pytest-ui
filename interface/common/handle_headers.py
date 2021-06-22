import time
import random


class HandleHeader:

    @staticmethod
    def handle_header(data):
        num = random.randint(00000000, 99999999)
        local_time = time.strftime("%Y%m%d%X", time.localtime())
        local_time = local_time.replace(":", "")
        serial_number = local_time + str(num)
        body_data = {
            # "TCode": "FD0001",
            "sysHead": {"Content": "application/json;charset=UTF-8", "stdSvcInd": "", "stdIntfcInd": "",
                        "stdIntfcVerNo": "",
                        "lglPrsnCd": "01", "chnlNo": "030220", "consmSysInd": "DMBANK", "consmSvcInd": "",
                        "consmTxnCd": "",
                        "consmMainSrlNo": "", "srcConsmSysInd": "DMBANK", "glbSrlNo": "", "consmSubSrlNo": "",
                        "txnChrctrstcType": "", "consmPltfmDt": "", "consmTxnMchnDt": "", "consmTxnMchnTm": "",
                        "glbRqsTmstmp": "", "ovtmTmNum": "60", "srcConsmTmlType": "", "srcConsmTmlNo": "",
                        "txnDstcNo": "",
                        "macVal": "", "instNo": "136061", "usrNo": "01ZK011", "idcNo": "", "dcnNo": "",
                        "sysRsrvFlgStrg": "",
                        "sysRsrvCharStrg": ""},
            "localHead": {"rtFlowno": serial_number},
            "body": data
        }
        return body_data

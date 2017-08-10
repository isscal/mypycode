# -*- coding:utf-8 -*-
import requests
import os
import json
import xlrd
import xlwt
postUrl = "http://10.80.73.7/IISP/dailyReportQuota/queryDailyReportQuotaData"


def postData(postUrl):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "91",
        "Content-Type": "application/json",
        "Cookie": "JSESSIONID=24211E8C7F87C626B7069B834735BA77; ZDKJ_TICKET=57157B42FCA3A1472DA3ACBC57745DFB; __session:0.9580642421279824:weeklyReportName=; __session:0.9580642421279824:weeklyFillName=; __session:0.9580642421279824:weeklyFillOrgName=; __session:0.9580642421279824:weeklyFillStatus=; __session:0.9580642421279824:=http:",
        "Host": "10.80.73.7",
        "Origin": "http://10.80.73.7",
        "Referer": "http://10.80.73.7/IISP/views/report/daily/re_daily_quota.jsp?id=HNDailyReportQuo20170601&dateTime=20170601&secondCompanyCode=HN",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"

    }
    playLoad = {"id": "HNDailyReportQuo20170601",
                "dateTime": "20170601", "secondCompanyCode": "HN", "type": 1}
    data = requests.post(postUrl, headers=headers,
                         data=json.dumps(playLoad)).content.decode("utf-8")
    # print(type(data))
    # print(data)
    # print(type(json.loads(data)))
    # print(json.loads(data)["data"])
    respData=json.loads(data)["data"]
    rData=respData[0]
    lenth=len(rData)
    print(lenth)
    for k,v in rData.items():
        print (k,v)
    # print(respData[0])
    return k,v,lenth

if __name__ == '__main__':
    postData(postUrl)


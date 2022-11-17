from heapq import merge
from warnings import catch_warnings
from wsgiref import validate
from numpy import sort
from sqlalchemy import create_engine, false
import urllib
import pandas as pd
from pandas import json_normalize

import datetime as dt
import requests
import json
import pyodbc
import pprint


url = "http://dev2008.scasset.net/scshana/Trans/Account/AcInvoiceMonitorqService.aspx/GetSearchAcInvoiceInterfaceList"

payload = json.dumps({
  "VendorCode": "Con015",
  "BranchID": "",
  "ProjectCode": "",
  "SapVendorCode": "",
  "InvoiceNo": "",
  "DocumentNo": "",
  "InvDoc": "",
  "PayDoc": "",
  "INVDateStr": "",
  "INVDateEnd": "",
  "PAYDateStr": "",
  "PAYateEnd": "",
  "ChkStatus": "WIntPAY",
  "chkIsEntryQue": "",
  "IsOwnerUserID": False
})
headers = {
  'Content-Type': 'application/json',
  'SC-API-SYSTEM': 'SCS_InterfaceSAPQ_Service',
  'SC-CUST-API-KEY': 'U0NJTk9ORUFQSTIwMjA=',
  'UserID': '47431',
  'ProjectID': '32',
  'Program_URL': 'www.google.com',
  'Cookie': 'ASP.NET_SessionId=z23xeo202rmzwmccdniwmhg4'
}


response= requests.request("POST", url, headers=headers, data=payload)
resp_dict=response.json()
#json_res=response.json()
#json_res.get('d')



df = pd.DataFrame(resp_dict.get('d'))
#print(df)
df['index']=range(0,len(df))
Vendor_DF=pd.concat([df.DataFrame(json_normalize(x)) for x in df['Data']] ,sort=false)
Vendor_DF.columns='Data'+ Vendor_DF.columns
Vendor_DF['index']=range(0,len(Vendor_DF))
merge_df=pd.merge(df,Vendor_DF,on='index')
merge_df=merge_df.drop('Data',axis=1)


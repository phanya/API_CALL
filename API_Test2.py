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
import ast

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


response = requests.request("POST", url, headers=headers, data=payload)
#OK ตัวอย่าง
#data = {"A": [1, 2]}
#print (pd.json_normalize(data, "A", record_prefix="Prefix."))

#print (response.text)
apy_data=response.json()
#print (apy_data)
df=pd.json_normalize(apy_data['VendorName'].values())
'''
df=pd.json_normalize(apy_data['Message'].values())
df['keys']=apy_data['Message'].keys()
'''
#print (pd.json_normalize(response, "Data", record_prefix="Prefix."))
#returned = json.loads(response.content)["d","Message"]

#pd.json_nomalize(response,max_level=0)
'''
pd.json_normalize(
  response.text,
  record_path=['Data'],
  meta=['Scalar'],
  meta_prefix='config_params_',
  record_prefix='random_forest_'
  )
'''
#resp_dict=response.json()

#df=pd.DataFrame(resp_dict,columns=["VendorName"]).to_list()

#print (df.to_markdown)
#print (resp_dict)
#json_res=response.json()
#json_res.get('d')

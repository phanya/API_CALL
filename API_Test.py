
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

def validate_string(val):
	if val != None:
		if type(val) is int:
			return str(val).encode('utf-8')
		else:
			return val

response= requests.request("POST", url, headers=headers, data=payload)
resp_dict=response.json()
#json_res=response.json()
#json_res.get('d')



df = pd.DataFrame(resp_dict.get('d'))
#print(df)
df['index']=range(0,len(df))
Vendor_DF=pd.concat([df.DataFrame(json_normalize(x)) for x in df['VendorName']] ,sort=false)
Vendor_DF.columns='VendorName_'+ Vendor_DF.columns
Vendor_DF['index']=range(0,len(Vendor_DF))
merge_df=pd.merge(df,Vendor_DF,on='index')
merge_df=merge_df.drop('VendorName',axis=1)

print(merge_df)
print ("2")

#print(response.json())

#for organizations in r:
 #   print(organizations.get("data"),None)
'''
#validate_string(item.get("VendorName",None))
json_data=json.loads(response.text)
#print ("Vendorame",json_obj["d"])

pd.json_normalize(json_data,
				record_path=['d'],
				meta=['VendorName','InvoiceID'],
				errors='ignore',
				sep='->')

'''
#data = json.loads(response)


##data = json.loads(response.json)
#print(data["VendorName"])
#print(data["d"]) 
#print(employee_dict['name'])



'''
conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=172.20.5.134;'
                            'Database=DATA_Delete;'
                            'Trusted_Connection=yes;')
cursor = conn.cursor()


cursor.execute("Insert Into dbo.Test_API(Data) values(?)",(response))

for record in data:
   
	print (data)
   # cursor.execute("Insert Into dbo.Test_API(__type, VendorName, InvoiceID, XInvoiceID, InvoiceDate, RefDoc) values (?, ?, ?, ?, ?, ?)",
	# ( record['__type'], record['VendorName'], record['InvoiceID'], record['XInvoiceID'], record['InvoiceDate'], record['RefDoc'] ) )
conn.commit()
conn.close()
'''

'''

for i, item in enumerate(json_obj):
    	#VendorName =validate_string(item.get("VendorName",None))
		VendorName =item.get("VendorName",None)
    #cursor.execute("Insert Into Test_API(__type, VendorName, InvoiceID, XInvoiceID, InvoiceDate, RefDoc) values (?, ?, ?, ?, ?, ?)"
	#, ( record['__type'], record['VendorName'], record['InvoiceID'], record['XInvoiceID'], record['InvoiceDate'], record['RefDoc'] ) )
cursor.execute("Insert Into dbo.Test_API(VendorName) values (?)"
	, (VendorName) )



conn.commit()
conn.close()
'''

'''
data = json.loads(response.text)
pd.json_normalize(
	data,
	max_level=1,
	record_path=['d'],
	errors='ignore')

'''

#pd.json_normalize(data,max_level=1)
#pd.json_normalize(parseResponse,record_path=['Data'])
#pd.json_normalize(response,record_path=['Data'])

'''
data_DF = pd.DataFrame(response)
data_DF['index']=range(0,len(data_DF))
dataApi = pd.concat([pd.DataFrame(json_normalize(x)) for x in data_DF['Data']],sort=False)
dataApi.columns = 'Type' + dataApi.columns 
dataApi['index']=range(0,len(dataApi))

merged_df =pd.merge(data_DF,dataApi,on="index")
print (merged_df)
'''



'''
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '172.20.5.134' 
database = 'DATA_Delete' 
username = 'qvreader' 
password = 'Qv11#102' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=172.20.5.134;'
                            'Database=DATA_Delete;'
                            'Trusted_Connection=yes;')
cursor = conn.cursor()



for record in parseResponse:

    #cursor.execute("Insert Into Test_API(__type, VendorName, InvoiceID, XInvoiceID, InvoiceDate, RefDoc) values (?, ?, ?, ?, ?, ?)"
	#, ( record['__type'], record['VendorName'], record['InvoiceID'], record['XInvoiceID'], record['InvoiceDate'], record['RefDoc'] ) )
    cursor.execute("Insert Into dbo.Test_API(VendorName) values (?)"
	, ( record['VendorName']) )



conn.commit()
conn.close()

'''



#print(response.text)
#print(response.json)

#data = json.loads(response)





'''
df=pd.DataFrame (a,columns=['__type' ,
	'VendorName', 
	'InvoiceID' ,
	'XInvoiceID' ,
	'InvoiceNo' ,
	'InvoiceDate', 
	'RefDoc' ,
	'RefDocDate', 
	'SAPInvDoc' ,
	'ProjectCode', 
	'CompanyCode' ,
	'POSTDATE' ,
	'PAYDAT' ,
	'status' ,
	'StartQueDate' ,
	'FinishQueDate' ,
	'SAPInvDocDate' ,
	'IsEntryQue' ,
	'CompanyID' ,
	'VendorID' ,
	'UserControlNameShow' ,
	'SapVendorCode'] )

df.columns=['__type' ,
	'VendorName', 
	'InvoiceID' ,
	'XInvoiceID' ,
	'InvoiceNo' ,
	'InvoiceDate', 
	'RefDoc' ,
	'RefDocDate', 
	'SAPInvDoc' ,
	'ProjectCode', 
	'CompanyCode' ,
	'POSTDATE' ,
	'PAYDAT' ,
	'status' ,
	'StartQueDate' ,
	'FinishQueDate' ,
	'SAPInvDocDate' ,
	'IsEntryQue' ,
	'CompanyID' ,
	'VendorID' ,
	'UserControlNameShow' ,
	'SapVendorCode'] 

print (df)
'''

#pretty = json.dumps(response.json(), indent=2)
#pprint.pprint(pretty)


#print(response.text)
#print(response.json)
#pprint.pprint(json)
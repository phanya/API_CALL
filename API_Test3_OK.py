import pandas as pd
from pandas import json_normalize
import requests
import json
import pyodbc

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
data_api=json.loads(response.text)
df =pd.json_normalize(data_api
                    #,max_level=1
                    ,record_path=['d','Data']
                    #,meta=['Data','VendorName'] 
                    ,errors='ignore'
                    ,sep='->'
                    #,record_prefix='_'
                     )

#OK
#df_column=pd.DataFrame(data_api,columns=['d'])
#print (df_column)              
#df.info()
#print (df)

conn = pyodbc.connect('Driver={SQL Server};Server=172.20.5.134;Database=DATA_Delete;Trusted_Connection=yes;')
#try:                            
cursor = conn.cursor()

for index, row in df.iterrows():
        cursor.execute("""Insert Into dbo.Test_API([__type],[VendorName],[InvoiceID],[XInvoiceID]
        ,[InvoiceNo],[InvoiceDate],[RefDoc],[RefDocDate],[SAPInvDoc],[ProjectCode],[CompanyCode]
        ,[POSTDATE],[PAYDAT],[status],[StartQueDate],[FinishQueDate],[SAPInvDocDate],[IsEntryQue]
        ,[CompanyID],[VendorID],[UserControlNameShow],[SapVendorCode]) 
        values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        , row['__type'],row['VendorName'],row['InvoiceID']
        ,row['XInvoiceID'],row['InvoiceNo'],row['InvoiceDate']
        ,row['RefDoc'],row['RefDocDate'],row['SAPInvDoc']
        ,row['ProjectCode'],row['CompanyCode'],row['POSTDATE']
        ,row['PAYDAT'],row['status'],row['StartQueDate'],row['FinishQueDate']
        ,row['SAPInvDocDate'],row['IsEntryQue'],row['CompanyID'],row['VendorID']
        ,row['UserControlNameShow'],row['SapVendorCode']) 
conn.commit()
conn.close()                                  

#except pyodbc.error as err:
#        print ('Error ! % err')
#except:
#        print('in')
#        conn.commit()
#        conn.close()    
# print ('1')



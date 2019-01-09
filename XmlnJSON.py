import xml.etree.ElementTree as ET
import pandas as pd

df = pd.read_csv('AppData.csv')

#xst = '<ns0:PaynCheckIn xmlns:ns0="http://tempuri.org/"
#xmlns:ns1="http://schemas.datacontract.org/2004/07/ADT.Web.WCF.MaqtaService.Model.MaqtaAppointment"><ns0:invoiceRequest><ns1:AppointmentNumbers><ns1:AppointmentNumber><ns1:AppointmentNbr>4248084</ns1:AppointmentNbr></ns1:AppointmentNumber></ns1:AppointmentNumbers><ns1:BankName></ns1:BankName><ns1:CheckNbr>MQ2003225555718713</ns1:CheckNbr><ns1:ChequeDate></ns1:ChequeDate><ns1:CompanyCode>EC001</ns1:CompanyCode><ns1:PayMode>CREDIT</ns1:PayMode><ns1:ReferenceNbr>MQ2003225555718713</ns1:ReferenceNbr><ns1:RequestedUser>vijayakumar.pargunan</ns1:RequestedUser><ns1:TotalAmount>0</ns1:TotalAmount><ns1:UserName>vijayakumar.pargunan</ns1:UserName></ns0:invoiceRequest></ns0:PaynCheckIn>'
#xst
#='<H1><H2>12</H2><H2>122</H2><H2>1442</H2><H2>32212</H2><H2>1442</H2><H2>22222</H2></H1>'
from io import StringIO

# instead of ET.fromstring(xml)
def removexmlnamespaces(xst):    
    it = ET.iterparse(StringIO(xst))
    for index, el in it:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces
    resp = it.root
    return resp


#parser = ET.XMLParser(encoding='utf-8')
#resp = ET.fromstring(xst)
#root = ET.ElementTree(resp)
#for node in root.iter('ns0:invoiceRequest'):
#    print('HEL')
#txxd = root.findtext('EC001')

#for child in root:
#    print('c1')
#    for child2 in child:
#        print('c2')
#        for child3 in child2:
#            print('c3')
#for child in resp:
#    print(child)
#    for child2 in child:
#        print(child2)
#        for child3 in child2:
#            print(child3)
    
#print(ET.tostring(resp))
#resp2 = resp.find('invoiceRequest')
#print(resp2)
#resp3 = resp.findall('invoiceRequest')
#print(resp3)
#resp4 = resp.findtext('invoiceRequest')
#print(resp4)

#for index,row in df.iterrows():
#    #print(row.ActualMessage)
#    parser = ET.XMLParser(encoding='utf-8')
#    resp = ET.fromstring(row.ActualMessage,parser=parser)
#    resp2 = resp.find('invoiceRequest')
#    #print(resp2)
df['ReqApptNo'] = None 
df['RespApptNo']=None 
df['ErrorMsg']=None 
df['VesselVisitId']=None 

for index,row in df.iterrows():
    xml = removexmlnamespaces(row.ActualMessage)
    xml2 = removexmlnamespaces(row.serviceresponse)
    apptno = xml.find('invoiceRequest/AppointmentNumbers/AppointmentNumber/AppointmentNbr')
    if apptno is None:
        apptno = xml.find('appointmentRequest/Requests/AppointmentRequest/AppointmentNbr')
    if apptno is not None:
        df.at[index,'ReqApptNo'] = apptno.text.strip()

    respapptno = xml2.find('PaynCheckInResult/AppointmentStatuses/AppointmentStatus/AppointmentNumber')
    errormsg = xml2.find('PaynCheckInResult/ErrorMessage')
    if respapptno is None:
        respapptno = xml2.find('BulkTerminalAppointmentsResult/Responses/AppointmentResponse/AppointmentNbr')
    if errormsg is None:
        errormsg = xml2.find('BulkTerminalAppointmentsResult/Responses/AppointmentResponse/ErrorMessage')
    if respapptno is not None:
        df.at[index,'RespApptNo'] = respapptno.text.strip()
    if errormsg is not None:
        df.at[index,'ErrorMsg'] = errormsg.text.strip()
        startIndex = errormsg.text.find('Outbound carrier')
        endIndex = errormsg.text.find('is Canceled')
        if startIndex > -1 and endIndex > -1:
            df.at[index,'VesselVisitId'] = errormsg.text[startIndex+16:endIndex].strip()



print(df[['RespApptNo','VesselVisitId']])


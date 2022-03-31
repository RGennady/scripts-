#!/usr/bin/python
import serial, string , requests , json, time, subprocess
output = ""
headers = {
  'Content-Type': 'application/json'
}
isReadyScaner=False
t=time.time() 
payload = json.dumps({"code": ""})
global ser 
global ip_server

 
def loadIpFromMemory():
 result=""
 bashCommand = "./library ip_server_1"
 return_code = subprocess.call(bashCommand, shell=True)
 result=str(return_code)
 bashCommand = "./library ip_server_2"
 return_code = subprocess.call(bashCommand, shell=True)
 result=result+"."+str(return_code)
 bashCommand = "./library ip_server_3"
 return_code = subprocess.call(bashCommand, shell=True) 
 result=result+"."+str(return_code)
 bashCommand = "./library ip_server_4"
 return_code = subprocess.call(bashCommand, shell=True) 
 result=result+"."+str(return_code)
 return result

ip_server=loadIpFromMemory()

while True:
     if time.time()-t>5:
        ip_server=loadIpFromMemory()
        t=time.time()
     if isReadyScaner!= True: 
      try:
         ser = serial.Serial('/dev/serial/by-id/usb-SuperLead_7100N_PB0S070236-if00', 9600, 8, 'N', 1, timeout=1)
         isReadyScaner=True
      except Exception:
         print('error scaner')
	 isReadyScaner=False
         continue
      time.sleep(2)
     if isReadyScaner!= False:
       try:
         output = ser.readline()
       except Exception:
         print('error scaner read')
         continue
       if output != "":
         payload = json.dumps({"code": output})
         try:
           response =requests.post('http://'+ip_server+':8001/change_status_scan_code',headers=headers, data=payload,timeout=0.5)
	   print(response.json())
         except Exception:
           print('error network')
           continue
        

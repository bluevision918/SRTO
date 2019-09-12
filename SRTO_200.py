#!/usr/bin/python
import httplib,urllib2
import ssl,socket

# This is the input file inlcuding all the hostnames that you want to check
file = open("hostnames_new.txt","r")
#This is the result file inlcuding all the response code
result_file = open("SRTO_Result_200.txt","a")
PATH ="/akamai/sureroute-test-object.html"
for i in file:
    try:
        conn = httplib.HTTPSConnection(i.strip('\n'),timeout=10)
        conn.request("HEAD",PATH)
        response = conn.getresponse() 
        result = i.strip('\n') + ';' +str(response.status)
        result_file.write(result + '\n')
        print result
    except (httplib.HTTPException, socket.error) as error:
        error = i.strip('\n') + ';' + str(error)
        result_file.write(error + '\n')
        print error
    except ssl.CertificateError, error:
        error = i.strip('\n') + ';' + str(error)
        result_file.write(error + '\n')
        print error
    except ssl.SSLError, error:
        error = i.strip('\n') + ';' + str(error)
        result_file.write(error + '\n')
        print error

file.close()
result_file.close()

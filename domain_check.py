# utf-8
import sys
import pandas as pd
import pandas as loc
import csv
import commands
import time

# file name
args = sys.argv

dataset1 = pd.read_csv(args[1])
print dataset1

print "imapsync format -> imapsync --HOST1 --USER1 --PASSWORD1 --HOST2 --USER2 --PASSWORD2"


input_host1_name = BEFORE_IP
input_host2_name = AFTER_IP

input_user1_name = "address"
input_password1 = "PassWord"

imapsync_check = "Detected 0 errors"

test1 = dataset1[input_user1_name]
test2 = dataset1[input_password1]

for item1,item2 in zip( test1 , test2 ):
    print item1 , item2

    #imapsync
    req = "imapsync" + " --host1 "+input_host1_name+" --user1 "+item1+" --password1 "+item2+" --host2 "+input_host2_name+" --user2 "+item1+" --password2 "+item2
    print req
    print "=========================================="
    print item1

    output = commands.getoutput(req)
    print output
    if(output.find(imapsync_check)>0):
        print("true")
    else:
        print("false")

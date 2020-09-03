import sys
from Third_Assignment import ConfigDict

cd=ConfigDict('config_file.txt')

if len(sys.argv)==3:
    key=sys.argv[1]
    value=sys.argv[2]
    print('Weiting data {key} {value}'.format(key=key,value=value))
else:
    print('reading data')
    for key in cd.keys():
        print('{key}={value}'.format(key=key,value=cd[key]))

cd['secret_password']='^$#&^&'
cd['username']='milanoid'
cd['password']='secret'
cd['hostname']='localhost'
cd['port']='port'
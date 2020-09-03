import sys
from Third_Assignment import ConfigDict

cd=ConfigDict('config_file.txt')

if len(sys.argv)==3:
    key=sys.argv[1]
    value=sys.argv[2]
    print('writing data: {0}, {1}'.format(key,value))
    cd[key]=value

elif len(sys.argv)==2:
    print('reading a value')
    key=sys.argv[1]
    print('the value for {0} is {1}'.format(sys.argv[1],cd[key]))
 
else:
     print('keys/values:')
     for key in cd.keys():
         print('{0} ={1}'.format(key,cd[key]))

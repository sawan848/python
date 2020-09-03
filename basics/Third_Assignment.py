import os
from Fourth_Assignment import ConfigKeyError

class ConfigDict(dict):

    def __init__(self, config_file):
        self._config_file=config_file
        if not os.path.isfile(self._config_file):
            try:
                open(self._config_file,mode='w')
            except IOError:
                return IOError('could not write file in file {path}'.
                format(path=self._config_file))


        with open(self._config_file)as file:
            for line in file:
                line=line.rstrip()
                key,value=line.split("=",1)
                dict.__setitem__(self,key,value)


    def __setitem__(self, key, value):
        dict.__setitem__(self,key,value)
        with open(self._config_file,'w')as file:
            for key,value in self.items():
                file.write("{key}={value}\n".format(key=key,value=self[key]))

    def __getitem__(self,key):
        if key not in self:
            raise ConfigKeyError(self,key)
        return dict.__getitem__(self,key)


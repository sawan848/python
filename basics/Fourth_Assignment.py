class ConfigKeyError(Exception):
    def __init__(self, config_dict, key):
        available_keys=[key for key in config_dict()]
        self.message="Key '{key}' not found." \
                     "Available Keys:{available_keys} ".format(key=key,available_keys=available_keys)
            
def __str__(self):
    return self.message
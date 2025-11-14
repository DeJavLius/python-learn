"""
[DEFAULT]
debug=False

[web_server]
host=127.0.0.1
port=80

[db_server]
host=127.0.0.1
port=3306
"""
import configparser

# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug': True
# }
#
# config['WEB_SERVER'] = {
#     'host': '127.0.0.1',
#     'port': 80,
# }
#
# config['DB_SERVER'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }
#
# with open('config.ini', 'w') as config_file:
#     config.write(config_file)

config = configparser.ConfigParser()
config.read('config.ini')
print(config['WEB_SERVER'])
print(config['WEB_SERVER']['host'])
print(config['WEB_SERVER']['port'])

print(config['DEFAULT']['debug'])
print(type(config['DEFAULT']['debug']))
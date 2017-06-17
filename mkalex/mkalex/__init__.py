#add by mk ,to instead of mysqlclient
import pymysql
import uuid
from . import deploy
pymysql.install_as_MySQLdb()


def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return mac

print '\n\n\n'
print 'physicadd:'+get_mac_address()

if get_mac_address()==deploy.developmacadd and deploy.autoconfig:
    print 'using mk dev config'
    print '\n\n\n'
    deploy.isDeveloping=True
else:
    print 'using production config'
    print '\n\n\n'

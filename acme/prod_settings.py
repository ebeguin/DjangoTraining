import dj_database_url
from .settings import *

DEBUG = False
TEMPLATE_DEBUG=False

DATAABASE['default'] = dj_database_url.config()

ALLOWED_HOSTS = ["ace-tdn.herokuapp.com"]

SECRET_KEY = 'PRODz(uak49u=_9m(4gq52+_yj#p-yh-2dv_%=li_c$ojek2)ksbh1'
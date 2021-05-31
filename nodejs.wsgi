#!/usr/bin/python3 
import sys 
sys.path.insert(0,"/var/www/nodejs/") 
sys.path.insert(0,"/var/www/nodejs/nodejs/") 
 
import logging
logging.basicConfig(stream=sys.stderr) 
 
from nodejs import app as application

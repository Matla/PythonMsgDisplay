#--------------------------------------------------------------------
#Administration Details
#--------------------------------------------------------------------
__author__ = "Mats Larsen"
__copyright__ = "Mats Larsen 2014"
__credits__ = ["Mats Larsen"]
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"
__description__ = "Module is for displaying messeges. The Class should contain all the desired display messages. The idea is that it is typically the same messages there will be displayed. It should be understand as a fast phototyping of a appluication to display common messages."
__file__ = "test_msg.py"
__class__ ="DisplayMsg"
__dependencies__ = ["DisplayMsg"]
#--------------------------------------------------------------------
#Version
#--------------------------------------------------------------------
__version_stage__ = "Pre_alpha"
__version_number__ = "0.1"
__version_date__ = "20140917"
__version_risk__ = "This current version is in Pre-alpha version, which meaning that the program can crash or perform other unrespected behavoiurs."
__version_modification__ = "The development project has just been created."
__version_next_update__ = "Implementation of more messeages."
#--------------------------------------------------------------------
#Hardware
#--------------------------------------------------------------------
"""
This project is not releated to any kind of hardware, like GPIOs.
"""
#-----------------------------------------------------
#Import
#-----------------------------------------------------
import traceback
from msg import DisplayMsg as DM
import numpy as np
#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 2 # Information level
LOG_ALWAYS = 3 # Always log data
#--------------------------------------------------------------------
#METHODS
#-------------------------------------------------------------------
def log(msg, log_level=LOG_LEVEL):
    """
    Print a message, and track, where the log is invoked
    Input:
    -msg: message to be printed, ''
    -log_level: informationlevel, i
    """
    global LOG_LEVEL
    if log_level <= LOG_LEVEL:
        print(str(log_level) + ' : ' + FILE + '.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)
log_level = 2
file1 = 'common.txt'
#msg = DM(file1)#,name='Test of Display messages', log_level=log_level)

count = 0
field = []
field_data = []
for line in open(file1):
    if line.startswith('#'):
        pass#print('sdsd')
    else:
        count +=1
        #print('sssssssssssssss')
        #print(line)
        field.append(line.split(':')[0].strip())
        field_data.append(line.split(':')[1].strip())
print(field)
print(field_data)
msg = [[0 for x in range(2)] for x in range(count)] 
print(msg)

for x in range(0,len(field)):
    print(x)
    print(field[x])
    print(field_data[x])
    msg[x][0] = field[x]
    msg[x][1] = field_data[x]
print(msg)
print(msg[0][0])
print(msg[0][1])

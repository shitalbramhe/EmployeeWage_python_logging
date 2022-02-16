'''
@Author: Shital Bajait
@Date: 2022-02-16 15:30:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-16 16:30:00
@Title : Check employee is present or absent
'''
import logging
import random
 
# Create and configure logger
logging.basicConfig(filename="emp.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

EMP_RATE_PER_HOUR = 20
number = random.randint(0,2)
def FullTime():
    return 8
def PartTime():
    return 4
def Absent():
    return 0    

switcher = {
    0: Absent(),
    1: FullTime(),
    2: PartTime(),
}
# Get the option from switcher dictionary
option = switcher.get(number)

empWage=option*EMP_RATE_PER_HOUR

#print employee wage
logger.info("Employee Wage:{}".format(empWage))

    
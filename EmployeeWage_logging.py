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
number = random.randint(0,1)
if number == 1:
    logger.info("Employee is FullTime")
    empHrs = 8
else:
    logger.info("Employee is PartTime")
    empHrs = 4
logger.info("Daliy Wage is : {}".format(empHrs * EMP_RATE_PER_HOUR))

    
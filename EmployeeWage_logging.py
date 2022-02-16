'''
@Author: Shital Bajait
@Date: 2022-02-16 15:20:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-16 15:20:00
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

number = random.randint(0,1)
if number == 1:
    logger.info("Employee is present")
else:
    logger.info("Employee is absent")
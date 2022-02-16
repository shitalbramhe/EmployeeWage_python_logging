'''
@Author: Shital Bajait
@Date: 2022-02-16 15:30:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-16 17:30:00
@Title : Store Daily Wage
'''
"""
Description:
    Function to calculate hours
Parameter:
      None
Return:
      None
"""
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
NUM_OF_WORKING_DAYS = 20
MAX_HRS_IN_MONTH = 100
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
def total():
    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage=0
    empWage = []
    while totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:
            number = random.randint(0,2)
            option = switcher.get(number)
            totalEmpHrs=totalEmpHrs+option
            empWage.append(option*EMP_RATE_PER_HOUR)
            logger.info("Daily wage : {} ".format(empWage[totalWorkingDays]))
            totalWorkingDays+=1
    logger.info("Total Employee Hours : {} ".format(totalEmpHrs))
    logger.info("Total Employee Wage : {} ".format(sum(empWage)))


if __name__ == "__main__":
    total()




    
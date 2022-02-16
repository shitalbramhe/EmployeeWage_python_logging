'''
@Author: Shital Bajait
@Date: 2022-02-16 15:30:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-16 17:54:00
@Title : Store Day and Daily wage using Dictionary
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
    """
        Description:
            Function to calculate hours
        Parameter:
            None
        Return:
            None
    """
    return 8
def PartTime():
    return 4
switcher = {
        0: FullTime(),
        1: PartTime(),
    }
def total():
    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage=0
    empWage = {}
    while totalEmpHrs < MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:
            number = random.randint(0,1)
            option = switcher.get(number)
            if totalEmpHrs == 96 and option ==  8:
                logger.info("you are working for more than 100 hours")
                break
            totalEmpHrs=totalEmpHrs+option
            empWage[totalWorkingDays]=option * EMP_RATE_PER_HOUR
            logger.info("Day : {} Daily wage : {}" .format(totalWorkingDays+1 , empWage[totalWorkingDays]))
            totalWorkingDays+=1
    logger.info("Total Employee Hours : {} ".format(totalEmpHrs))
    sum = 0
    for i in empWage.values():
           sum = sum + i
    logger.info("Total Employee Wage : {} ".format(sum))

if __name__ == "__main__":
    total()




    
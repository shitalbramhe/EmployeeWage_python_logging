'''
@Author: Shital Bajait
@Date: 2022-02-16 15:30:00
@Last Modified by: Shital Bajait
@Last Modified time: 2022-02-16 16:51:00
@Title : Calculate wage for a month hours reached maximum 
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
NUM_OF_WORKING_DAYS = 20
empWage = 0
totalEmpWage=0
totalEmpHrs = 0
totalWorkingDays = 0
day=0
MAX_HRS_IN_MONTH = 100
while totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:
    totalWorkingDays+=1
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
    totalEmpHrs+=option
    empWage=option*EMP_RATE_PER_HOUR
    totalEmpWage += empWage

#print employee wage
logger.info("Total Employee Hours : {} ".format(totalEmpHrs))
logger.info("Total Employee Wage : {} ".format(totalEmpWage))



    
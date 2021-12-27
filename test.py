
from math import *

def std_weight(height, gender):
    height_m = height / 100
    if gender == "남자" :
        return round(height_m * height_m * 22, 2)
    elif gender == "여자" :
        return round(height_m * height_m * 21, 2)
    else:
        return 0.00
    
height = 175
gender = "남자"
print ("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight(height, gender)))

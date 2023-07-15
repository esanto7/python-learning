# 9.4 Challenge

# first int is students
universities = [
['California Institute of Technology', 2175, 37704], 
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732], 
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_status():
    uni_list = []
    students_enrolled = []
    ann_fees = []

    for totals in universities:
        uni_list.append(totals[0])
        students_enrolled.append(totals[1])
        ann_fees.append(totals[2])

    return uni_list, students_enrolled, ann_fees

def mean(item_list):
    item_list = sum(item_list) / len(item_list)

    return item_list

def median(item_list):
    item_list.sort()
    mid_point = round(len(item_list) / 2) 

    return mid_point

###############################################

uni_list, total_students, total_fees = enrollment_status()

print("******************************")
print(f"Total students:\t {sum(total_students):,}")
print(f"Total tuition:\t $ {sum(total_fees):,}")
print()
print(f"Student mean:\t {mean(total_students):.2f}")
print(f"Student median:\t {total_students[median(total_students) - 1]:,}")
print()
print(f"Tuition mean:\t $ {mean(total_fees):,.2f}")
print(f"Tuition median:\t $ {total_fees[median(total_fees) - 1]:,}")
print()
print("******************************")

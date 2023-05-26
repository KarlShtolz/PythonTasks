days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_count = 7
s = input()
lst = [str(b) for b in s.split()]
day_num = int(lst[0])
day_week = lst[1]


def make_calender(day_num, day_week):
    days_arr = [".." for i in range(50)]
    for i in range(1, 1 + day_num):
        if i < 10:
            days_arr[i + (days.index(day_week) - 1)] = "." + str(i)
        else:
            days_arr[i + (days.index(day_week) - 1)] = str(i)
    if day_num == 28 and day_week == days[0]:
        count = 4
    elif day_num == 30 and days.index(day_week) < 6:
        count = 5
    elif day_num == 31 and days.index(day_week) < 5:
        count = 5
    elif day_num == 28 and day_week != 0:
        count = 5
    else:
        count = 6
    k = 0
    arr = [[".." for i in range(days_count)] for j in range(count)]
    for i in range(count):
        for j in range(7):
            arr[i][j] = days_arr[k]
            k += 1
            if j == 6:
                print(arr[i][j], sep="", end="")
            else:
                print(arr[i][j], end=" ")
        print()


make_calender(day_num, day_week)

# ####################################
# ###ПРОГОН ВСЕХ ВОЗМОЖНЫХ ТЕСТОВ#####
# ####################################
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# days_count = 7
# def make_calender(day_num, day_week):
#     days_arr = [".." for i in range(50)]
#     for i in range(1, 1 + day_num):
#         if i < 10:
#             days_arr[i + (days.index(day_week) - 1)] = "." + str(i)
#         else:
#             days_arr[i + (days.index(day_week) - 1)] = str(i)
#     if day_num == 28 and day_week == days[0]:
#         count = 4
#     elif day_num == 30 and days.index(day_week) < 6:
#         count = 5
#     elif day_num == 31 and days.index(day_week) < 5:
#         count = 5
#     elif day_num == 28 and day_week != 0:
#         count = 5
#     elif day_num == 29:
#         count = 5
#     else:
#         count = 6
#     k = 0
#     arr = [[".." for i in range(days_count)] for j in range(count)]
#     for i in range(count):
#         for j in range(7):
#             arr[i][j] = days_arr[k]
#             k += 1
#             if j == 6:
#                 print(arr[i][j], sep="", end="")
#             else:
#                 print(arr[i][j], end=" ")
#         print()
# make_calender( 30, "Monday")
# print("################################")
# make_calender( 30, "Tuesday")
# print("################################")
# make_calender( 30, "Wednesday")
# print("################################")
# make_calender( 30, "Thursday")
# print("################################")
# make_calender( 30, "Friday")
# print("################################")
# make_calender( 30, "Saturday")
# print("################################")
# make_calender( 30, "Sunday")
# print("################################")
# make_calender( 31, "Monday")
# print("################################")
# make_calender( 31, "Tuesday")
# print("################################")
# make_calender( 31, "Wednesday")
# print("################################")
# make_calender( 31, "Thursday")
# print("################################")
# make_calender( 31, "Friday")
# print("################################")
# make_calender( 31, "Saturday")
# print("################################")
# make_calender( 31, "Sunday")
# print("################################")
# make_calender( 28, "Monday")
# print("################################")
# make_calender( 28, "Tuesday")
# print("################################")
# make_calender( 28, "Wednesday")
# print("################################")
# make_calender( 28, "Thursday")
# print("################################")
# make_calender( 28, "Friday")
# print("################################")
# make_calender( 28, "Saturday")
# print("################################")
# make_calender( 28, "Sunday")
# print("#######SHEET HAPENS#############")
# make_calender( 29, "Monday")
# print("################################")
# make_calender( 29, "Tuesday")
# print("################################")
# make_calender( 29, "Wednesday")
# print("################################")
# make_calender( 29, "Thursday")
# print("################################")
# make_calender( 29, "Friday")
# print("################################")
# make_calender( 29, "Saturday")
# print("################################")
# make_calender( 29, "Sunday")

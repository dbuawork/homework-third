# #
# a = int(input("Введіть номер дня тижня (1-7): "))
#
# if a==1:
#     print("Понеділок")
#
# elif a==2:
#     print("Вівторок")
#
# elif a==3:
#     print("Середа")
#
# elif a==4:
#     print("Четвер")
#
# elif a==5:
#     print("Пятниця")
#
# elif a==6:
#     print("Суббота")
#
# elif a==7:
#     print("Неділя")
#
# else:
#     print("введене число не є днем тижня")
#
# #
num1 = int(input("Перше число: "))

num2 = int(input("Друге число: "))

if num1 != num2 and num1 < num2:

   print(str(num1) + " " + str(num2))

elif num1 != num2 and num1 > num2:

   print(str(num2) + " " + str(num1))

else:

   print("num1 = num2")
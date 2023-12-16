#
num = int(input("Введіть номер дня тижня (1-7): "))

if num==1:
    print("Понеділок")

elif num==2:
    print("Вівторок")

elif num==3:
    print("Середа")

elif num==4:
    print("Четвер")

elif num==5:
    print("Пятниця")

elif num==6:
    print("Суббота")

elif num==7:
    print("Неділя")

else:
    print("введене число не є днем тижня")

# # #
# num1 = int(input("Перше число: "))
#
# num2 = int(input("Друге число: "))
#
# if num1 != num2 and num1 < num2:
#
#    print(str(num1) + " " + str(num2))
#
# elif num1 != num2 and num1 > num2:
#
#    print(str(num2) + " " + str(num1))
#
# else:
#
# #    print("num1 = num2")
# print(f"Введіть 1 та 2 число,та оберіть варіант математичної операції")
#
# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
#
# try:
#      print("1. Додавання\n2. Віднімання\n3. Множення\n4. Ділення\n5. Вихід")
#      user_select = int(input("Яку математичну операцію виконуемо?: "))
#
#      if user_select == 1:
#          print(num1 + num2)
#      elif user_select == 2:
#          print(num1 - num2)
#      elif user_select == 3:
#          print(num1 * num2)
#      elif user_select == 4:
#          print(num1 / num2)
#      elif user_select == 5:
#          print("Вихід")
#      else:
#          print("Такого пункту нажаль немае(")
# except Exception as e:
#         print(f"Error: {e}")
# except ZeroDivisionError as error:
#         print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Введіть тільки цілі числа, будь ласка!")
#     print(f"ValueError: {error}")
# except Exception as error:
#     print(f"Exception occurred: {error}")
# finally:
#     print("Вихід...")
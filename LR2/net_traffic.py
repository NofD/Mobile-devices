"""Обработка данных трафика NetFlow v5.

   Значения по умолчанию - из варианта 3.
"""
import data_processing as dp

def mode_0():
    """Задание по варианту 3.
    """
    pass

def mode_1():
    """Перевести данные в читабельный вид.
    """
    mode = input("\nВведите имя файла (для значения по умолчанию (nfcapd.202002251200) нажмите Enter): ")
    if mode:
        if dp.check_file(mode):
            print("\nНе удалось открыть файл")
            mode_1()
        else:
            if not dp.translation(mode):
                print("\nФайл result.txt создан")
            else:
                print("\nОшибка. Попробуйте еще раз")
                mode_1()
    else:
        if dp.check_file("nfcapd.202002251200"):
            print("\nНе удалось открыть файл")
            mode_1()
        else:
            if not dp.translation():
                print("\nФайл result.txt создан")
            else:
                print("\nОшибка. Попробуйте еще раз")
                mode_1()

def mode_2():
    """Выборка по IP.
    """
    mode = input("\nВведите имя файла (для значения по умолчанию (result.txt) нажмите Enter): ")
    if mode:
        if dp.check_file(mode):
            print("\nНе удалось открыть файл")
            mode_2()
        else:
            ip_add = input("\nВведите IP-адрес (xxx.xxx.xxx.xxx): ")
            if dp.ip_check(ip_add):
                print("\nНеверный IP-адрес")
                mode_2()
            else: # правильный ip и файл
                sel = dp.ip_selection(mode, ip_add)
                if not sel:
                    print("\nФайл ip_address.txt создан")
                elif sel == 1:
                    print("\nОшибка. Попробуйте еще раз")
                    mode_2()
    else: # по умолчанию
        if dp.check_file("result.txt"):
            print("\nНе удалось открыть файл")
            mode_2()
        else:
            ip_add = input("\nВведите IP-адрес (xxx.xxx.xxx.xxx): ")
            if dp.ip_check(ip_add):
                print("\nНеверный IP-адрес")
                mode_2()
            else: # правильный ip и файл
                sel_1 = dp.ip_selection("result.txt", ip_add)
                if not sel_1:
                    print("\nФайл ip_address.txt создан")
                elif sel_1 == 1:
                    print("\nОшибка. Попробуйте еще раз")
                    mode_2()

def mode_3():
    mode = input("\nВведите имя файла c выборкой по IP-адресу (для значения по умолчанию (ip_address.txt) нажмите Enter): ")
    if mode:
        if dp.check_file(mode):
            print("\nНе удалось открыть файл")
            mode_3()
        else:
            try:
                dp.diagram(mode)
            except:
                print("\nОшибка. Проверьте файл и попробуйте еще раз.")
                mode_3()
    else:
        if dp.check_file("ip_address.txt"):
            print
            print("\nНе удалось открыть файл")
            mode_3()
        else:
            try:
                dp.diagram("ip_address.txt")
            except:
                print("\nОшибка. Проверьте файл и попробуйте еще раз.")
                mode_3()

def mode_4():
    pass

def mode_choice():
    """Выбор задачи.
    """
    mode = input("\nВыберите задачу: \n\t0 - Задание по варианту 3\n\t1 - Перевести данные в читабельный вид\n\t2 - Выборка по IP\n\t3 - Статистика\n\t4 - Тарификация\n\t5 - Выход\n")
    if mode.isdigit():
        if int(mode) == 1:
            mode_1()
        elif int(mode) == 2:
            mode_2()
        elif int(mode) == 3:
            mode_3()
        elif int(mode) == 4:
            mode_4()
        elif int(mode) == 5:
            quit()
        else:
            print("\nНеправильная команда")
            mode_choice()
    else:
        print("\nНеправильная команда")
        mode_choice()



ip = "192.168.250.27"
price = 1.0 # руб/Мб
bonus = 0.0 # Мб

mode_choice()







# plan = int(input("Введите 0, чтобы использовать тарифный план по умолчанию, или 1, чтобы ввести новый тариф: "))

# if plan:
#     in_min = float(input("Стоимость входящих звонков, руб/мин: "))
#     in_min_bonus = int(input("Количество входящих минут бесплатно, мин: "))
#     out_min = float(input("Стоимость исходящих звонков, руб/мин: "))
#     out_min_bonus = int(input("Количество исходящих минут бесплатно, мин: "))
#     sms = float(input("Стоимость смс, руб/шт: "))    
#     sms_bonus = int(input("Количество смс бесплатно, шт: "))
#     customer_id = input("Введите идентификатор абонента: ")

# in_min_am, out_min_am, sms_am = reader(customer_id)
# cost_tel, cost_sms = counter(in_min_am, out_min_am, sms_am, in_min, out_min, sms, in_min_bonus, out_min_bonus, sms_bonus)
# print("Стоимость звонков:", cost_tel, "руб.")
# print("Стоимость СМС:", cost_sms, "руб.")
# print("Сумма по счету равна", cost_sms + cost_tel, "руб.")


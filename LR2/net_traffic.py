"""Обработка данных трафика NetFlow v5.

   Значения по умолчанию - из варианта 3.
"""
import data_processing as dp

def mode_0():
    """Задание по варианту 3.
    """
    # Мб - мегабайты, Мбит - мегабиты (8*Мб)
    ip = "192.168.250.27"
    price = 1.0 # руб/Мб
    bonus = 0.0 # Мб
    file_nm = "ip_address.txt"

    if dp.check_file("nfcapd.202002251200"):
        print("\nНе удалось открыть файл")
        mode_0()
    else:
        dp.translation() 
        dp.ip_selection("result.txt", ip)
        traf = dp.traf_collection(file_nm)
        cost = dp.tariff_ip(traf, price, bonus) #байты, руб/Мб, Мб
        print("\nИтоговая стоимость: " + str(cost) + " руб.")
        dp.diagram(file_nm)

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
    """Статистика - график по выборке.
    """
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

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def price_req():
    """Запрос стоимости услуг.
    """
    price = input("\nВведите коэффициент k тарификации (руб/Мб): ")
    
    if isfloat(price):
        return float(price)
    else:
        print("\nВведите число.")
        return "bad"

def bonus_req():
    """Запрос количества бонусов.
    """
    bonus = input("\nВведите количество бесплатных Мб: ")
    if isfloat(bonus):
        return float(bonus)
    else:
        print("\nВведите число.")
        return "bad"

def mode_4():
    """Тарификация.
    """
    mode = input("\nВведите имя файла c выборкой по IP-адресу (для значения по умолчанию (ip_address.txt) нажмите Enter): ")
    if mode:
        if dp.check_file(mode):
            print("\nНе удалось открыть файл")
            mode_4()
        else:
            try:
                dp.traf_collection(mode)
            except:
                print("\nОшибка. Проверьте файл и попробуйте еще раз.")
                mode_4()
            else:
                traf = dp.traf_collection(mode)
                price = price_req()
                if price == "bad":
                    print("\nПопробуйте еще раз.")
                    quit()
                bonus = bonus_req()
                if bonus == "bad":
                    print("\nПопробуйте еще раз.")
                    quit()
                cost = dp.tariff_ip(traf, price, bonus) #байты, руб/Мб, Мб
                print("\nИтоговая стоимость: " + str(cost) + " руб.")
    else:
        if dp.check_file("ip_address.txt"):
            print("\nНе удалось открыть файл")
            mode_4()
        else:
            try:
                dp.traf_collection("ip_address.txt")
            except:
                print("\nОшибка. Проверьте файл и попробуйте еще раз.")
                mode_4()
            else:
                traf = dp.traf_collection("ip_address.txt")
                price = price_req()
                if price == "bad":
                    print("\nПопробуйте еще раз.")
                    quit()
                bonus = bonus_req()
                if bonus == "bad":
                    print("\nПопробуйте еще раз.")
                    quit()
                cost = dp.tariff_ip(traf, price, bonus) #байты, руб/Мб, Мб
                print("\nИтоговая стоимость: " + str(cost) + " руб.")

def mode_choice():
    """Выбор задачи.
    """
    mode = input("\nВыберите задачу: \n\t0 - Задание по варианту 3\n\t1 - Перевести данные в читабельный вид\n\t2 - Выборка по IP\n\t3 - Статистика\n\t4 - Тарификация\n\t5 - Выход\n")
    if mode.isdigit():
        if not int(mode):
            print("\nИсходный файл: nfcapd.202002251200")
            mode_0()
        elif int(mode) == 1:
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

mode_choice()
input("\nНажмите Enter для выхода...")

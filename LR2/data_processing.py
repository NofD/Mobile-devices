"""Чтение и обработка данных.
"""
import subprocess
import os
import datetime as date
from matplotlib import dates as dateform
import matplotlib.pyplot as plt

def translation(file_name="nfcapd.202002251200"): 
    """Принимает файл, созданный утилитой nfcapd и
       создает файл 'result.txt'.

       Возвращает 0, если файл создан, 
       1 - в противном случае.
    """
    command = "nfdump -r " + file_name + " > subresult.txt"
    call_res = subprocess.call(command, shell = True)

    if not call_res:
        file_size = os.path.getsize("subresult.txt")
        if file_size:
            with open("subresult.txt", "r") as sub_res:
                with open("result.txt", "w") as res:
                    for row in sub_res:
                        if row[0]== "D" or row[0]== "2":
                            res.write(row)
            os.remove("subresult.txt")
            return call_res
        else:
            print("\nФайл пуст")
            return call_res
    else:
        print("\nНе вышло преобразовать.")
        try:
            open("subresult.txt")
        except:
            return call_res
        else:
            os.remove("subresult.txt")
            return call_res

def ip_selection(txt_name, ip_address): 
    """Выбор строк по ip.

       Принимает имя файла и ip-адрес.
       Создает файл 'ip_addree.txt'.    
    """
    
    file_size = os.path.getsize(txt_name)
    ip_address = ip_address + ":"
    if file_size:
        with open(txt_name, "r") as source:
            with open("ip_address.txt", "w") as dest:
                for row in source:
                    if row.find(ip_address) != -1:
                        dest.write(row)
        if os.path.getsize("ip_address.txt"):
            return 0
        else:
            print("\nСовпадений не найдено.")
            os.remove("ip_address.txt")
            return 2
    else:
        print("\nИсходный файл пуст")
        return 1

def check_file(fl_name):
    """Проверка существования файла.
    0 - существует, 1 - нет.
    """
    try:
        open(fl_name)
    except:
        return 1
    else:
        return 0

def diagram(ip_text): 
    """Принимает выборку по ip, выводит график 
       трафик(время).
    """
    dict_ti_tr = {}
    form = dateform.DateFormatter("%Y-%m-%d %H:%M:%S")
    fig, ax = plt.subplots()
   
    with open (ip_text,"r") as inf:
        for row in inf:
            if row[0] == '2':
                information = row.split()
                date_string = date.datetime.strptime(information[0] + " " + information[1][:-4], "%Y-%m-%d %H:%M:%S")
                dict_ti_tr[date_string] = round((float(information[11]) / 1024), 3) #в Кб
                if information[12] == "M":
                    dict_ti_tr[date_string] = round((float(information[11]) * 1024), 3)
                else:
                    dict_ti_tr[date_string] = round((float(information[11]) / 1024), 3)
    
    time = list(dict_ti_tr.keys())
    time.sort()
    traffic = [dict_ti_tr[i] for i in time]

    ax.grid(which='major',
            color = 'gray')
    ax.minorticks_on()
    ax.grid(which='minor',
            color = 'gray',
            linestyle = ':')

    ax.plot(time, traffic, color="indigo")
    ax.xaxis.set_major_formatter(form)
    ax.set_xlabel('Время')
    ax.set_ylabel('Трафик, Кбайт')
    ax.set_title('Статистика по трафику')
    
    fig.autofmt_xdate()
    plt.show()

def traf_collection(txt_cont):
    """Считает весь трафик абонента за отчетный период.
    """
    byte_traf = 0
    mega_traf = 0
    with open(txt_cont, "r") as container:
        for row in container:
            L = row.split()
            if len(L) < 20:
                if L[12] == "M":
                    mega_traf += float(L[11])
                else:
                    byte_traf += float(L[11])
    traf = round((byte_traf + mega_traf*1024*1024), 2) #в байтах
    return traf
         
def tariff_ip(traf, price, bonus): #байты, руб/Мб, Мб
    """Тарификация абонента по ip.
       Считает в Мб.
    """
    cost_traf = (traf/(1024*1024) - bonus) * price
    round_cost = round(cost_traf, 2)
    return round_cost

def ip_check(ip_addr):
    """Проверка валидности IP-адреса.
       0 - валидный, 1 - невалидный.
    """
    IP = [i for i in ip_addr.split(".")]
    if len(IP) != 4:
        return 1
    for part in IP:
        if part.isdigit():
            if 0 <= int(part) < 256:
                continue
            else:
                return 1
        else:
            return 1
    return 0



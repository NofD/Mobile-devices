"""Чтение и обработка данных.
"""
import csv

def reader(id):
    """Читает и разбирает строки из data.csv с id абонента.

       Возвращает количество использованных входящих и исходящих минут и количество смс.
    """
    
    in_min_am = 0.0
    out_min_am = 0.0
    sms_am = 0

    with open("data.csv") as dt:
        reader = csv.reader(dt)
        for row in reader:
            if id in row:
                if row[1] == id:
                    out_min_am += float(row[3])
                    sms_am += int(row[4])
                elif row[2] == id:
                    in_min_am += float(row[3])
    return in_min_am, out_min_am, sms_am


def counter(in_min_am, out_min_am, sms_am, in_min, out_min, sms, in_min_bonus = 0, out_min_bonus = 0, sms_bonus = 0):
    """Подсчитывает итоговую сумму.
       
       Входящие, исходящие, смс, стоимость входящих, стоимость исходящих, стоимость смс, бесплатные исходящие, бесплатные входящие, бесплатные смс.
    """
    cost = (in_min_am - in_min_bonus) * in_min + (out_min_am - out_min_bonus) * out_min + (sms_am - sms_bonus) * sms
    return round(cost, 2)



"""Назначение тарифного плана.

   Значения по умолчанию - из варианта 3.
"""
from data_processing import reader, counter

in_min = 0.0
out_min = 2.0
sms = 2.0
in_min_bonus = 0
out_min_bonus = 20
sms_bonus = 0

id = "915783624"

plan = int(input("Введите 0, чтобы использовать тарифный план по умолчанию, или 1, чтобы ввести новый тариф: "))

if plan:
    in_min = float(input("Стоимость входящих звонков, руб/мин: "))
    in_min_bonus = int(input("Количество входящих минут бесплатно, мин: "))
    out_min = float(input("Стоимость исходящих звонков, руб/мин: "))
    out_min_bonus = int(input("Количество исходящих минут бесплатно, мин: "))
    sms = float(input("Стоимость смс, руб/шт: "))    
    sms_bonus = int(input("Количество смс бесплатно, шт: "))
    id = input("Введите идентификатор абонента: ")

in_min_am, out_min_am, sms_am = reader(id)
cost_tel, cost_sms = counter(in_min_am, out_min_am, sms_am, in_min, out_min, sms, in_min_bonus, out_min_bonus, sms_bonus)
print("Стоимость звонков:", cost_tel, "руб.")
print("Стоимость СМС:", cost_sms, "руб.")
print("Сумма по счету равна", cost_sms + cost_tel, "руб.")


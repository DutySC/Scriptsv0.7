import random

"""Параметы тестирования"""
region = 'Ростовской области' #регион/отдельный клиент
login = 'BARS_TTEST' #логин
password = '123' #пароль
disease = 'J10.0' #диагноз при дневнике врача
patient = '1600046061' #тестовый пациент
doctor = 'Тестирование П.' #врачь
department = 'Поликлиника отд' #отделение
polyclinic = 'Тестирование графиков' #кабинет
g_disease = 'Z00.0' #диагноз при госпитализации
name_patient = 'Тест Патч Пятнадцать' #имя тестового пациента
schedule_patient = 'Тест П.П.' #сокращенное имя тестового пациента
first_name = 'Патча' #имя создаваемого тестового пользователя
last_name = 'Тестирование' #фамилия создаваемого тестового пользователя
surname = 'Новаяверсия' #отчество создаваемого тестового пользователя
data = '01011999' #дата рождения тестового пользователя
post_snils = '//tr[10]/td[1]//input[1]' #поле ввода для СНИЛС
snils = '37833219000' #статичное значение СНИЛС
position = '1'
rand_1 = random.randint(10000000, 99999999) #рандомное значение полиса
rand_2 = random.randint(100000000, 999999999) #рандомное значение полиса
certificate = 'Временное свидетельство' #вид полиса
area = '1' #регион
home = '13' #номер квартиры
mvd = 'МВД' #кем выдан документ
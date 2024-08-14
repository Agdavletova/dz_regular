from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = re.compile(r"(\+7|8)\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(*(доб.)*\s*(\d{4})*\)*")
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
for contact in contacts_list[1:]:
    human = " ".join(contact[:3])
    human_list = human.split()
    contact[0] = human_list[0]
    if len(human_list) > 1:
        contact[1] = human_list[1]
    if len(human_list) == 3:
        contact[2] = human_list[2]
    phone = contact[5]
    if phone:
        result = pattern.sub(r"+7(\2)\3-\4-\5 \6 \7", phone).rstrip()
        contact[5] = result
dicts = {}

for contact in contacts_list[1:]:
    key = (contact[0], contact[1])
    if key not in dicts:
        dicts[key] = contact
    else:
        for i in range(2, len(contact)):
            if not dicts[key][i]:
                dicts[key][i] = contact[i]
new_contacts_list = list(dicts.values())

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)

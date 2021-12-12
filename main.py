import csv
from pprint import pprint
from merge import merge_row
from correction import correction_of_records


if __name__ == '__main__':

  res_list = []

  with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

  temp_list = correction_of_records(contacts_list)

  for tmp in temp_list:

    for i, res in enumerate(res_list):

      if tmp[0] == res[0] and tmp[1] == res[1] and tmp != res:
        res_list[i] = merge_row(tmp, res)
        break

    else:
        res_list.append(tmp)

  pprint(res_list)

  with open("phonebook.csv", "w", encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(res_list)
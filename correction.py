import re

def correction_of_records(list_name):

  res_list = []

  for item in list_name:

    temp_list = ' '.join(item[:3]).split()

    while len(temp_list) < 3:
      temp_list.append("")

    pattern = r"(\+7|8)\s*\(*(\d{3})\)*\-*\s*(\d{3})\-*(\d{2})\-*(\d{2})\s*\(*(\w{3}\.*)*\s*(\d{4})*\)*"
    item[5] = re.sub(pattern, r"+7(\2)\3-\4-\5 \6\7", item[5])

    temp_list.extend(item[3:])

    res_list.append(temp_list)

  return res_list
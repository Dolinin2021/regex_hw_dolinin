
def merge_row(item_temp_list, item_res_list):

  res_list = []

  res_list.extend(item_temp_list[:2])

  min_len = min(len(item_temp_list), len(item_res_list))


  for i in range(min_len)[2:]:

    if item_temp_list[i] != '':
      res_list.append(item_temp_list[i])

    else:
      res_list.append(item_res_list[i])

  return res_list
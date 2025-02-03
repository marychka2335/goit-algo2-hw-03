import csv
import os.path as path
from timeit import default_timer as timer, timeit
from BTrees.OOBTree import OOBTree

class Item:
  def __init__(self, ID: str, Name: str, Category: str, Price: float):
    self.ID = int(ID)
    self.Name = Name
    self.Category = Category
    self.Price = float(Price)
  # end def
# end class

def load_data(file_path):
  csv_data = dict()
  with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
      if row[0] == 'ID': continue
      csv_data[row[0]] = {'ID': row[0], 'Name': row[1], 'Category': row[2], 'Price': row[3]}
    # end for
  # end with
  return csv_data
# end def

def add_item_to_dict(dict_struct, id, item):
  dict_struct[id] = item
# end def

def add_item_to_tree(tree_struct, id, item):
  tree_struct.update({id: item})
# end def

def range_query_dict(dict_struct, start: float, end: float):
  ret_list = list()
  for item in dict_struct.values():
    if start <= (item.Price if isinstance(item, Item) else float(item['Price'])) <= end:
      ret_list.append(item)
  return ret_list
# end def

def range_query_tree(tree_struct, start: float, end: float):
  ret_list = list(tree_struct.items(min=start, max=end))
  return [item for key, item in ret_list if start <= (item.Price if isinstance(item, Item) else float(item['Price'])) <= end]
# end def

if __name__ == '__main__':
  print(f'═'*50)
  print(f"{'Assignment 2 results':^50}")
  print(f'═'*50)

  test_qty = 100
  min_price = 50
  max_price = 150
  file_path = path.dirname(__file__) + '/generated_items_data.csv'

  dict_with_class = dict()
  tree_with_class = OOBTree()
  dict_with_obj = dict()
  tree_with_obj = OOBTree()

  csv_data = load_data(file_path)

  add_dict_class_start_time = timer()
  for item in csv_data.values():
    item_class = Item(int(item['ID']), item['Name'], item['Category'], float(item['Price']))
    add_item_to_dict(dict_with_class, item_class.ID, item_class)
  # end for
  add_dict_class_duration = timer() - add_dict_class_start_time
  print(f'Adding Class to Dict time: {"{:.4f}".format(add_dict_class_duration * 1000)} ms')

  dict_query_class_duration = timeit(lambda: range_query_dict(dict_with_class, min_price, max_price), number=test_qty)
  dict_query_class_quantity = len(range_query_dict(dict_with_class, min_price, max_price))
  print(f'Class in Dict queries finished:\nGot {dict_query_class_quantity:.0f} results, average time: {"{:.4f}".format(dict_query_class_duration * 1000 / test_qty)} ms')

  print(f'─'*50)

  add_tree_class_start_time = timer()
  for item in csv_data.values():
    item_class = Item(int(item['ID']), item['Name'], item['Category'], float(item['Price']))
    add_item_to_tree(tree_with_class, item_class.ID, item_class)
  # end for
  add_tree_class_duration = timer() - add_tree_class_start_time
  print(f'Adding Class to Tree time: {"{:.4f}".format(add_tree_class_duration * 1000)} ms')

  tree_query_class_duration = timeit(lambda: range_query_tree(tree_with_class, min_price, max_price), number=test_qty)
  tree_query_class_quantity = len(range_query_tree(tree_with_class, min_price, max_price))
  print(f'Class in Tree queries finished:\nGot {tree_query_class_quantity:.0f} results, average time: {"{:.4f}".format(tree_query_class_duration * 1000 / test_qty)} ms')

  print(f'─'*50)

  add_dict_obj_start_time = timer()
  for item in csv_data.values():
    item_obj = {'ID': int(item['ID']), 'Name': item['Name'], 'Category': item['Category'], 'Price': float(item['Price'])}
    add_item_to_dict(dict_with_obj, item_obj['ID'], item_obj)
  # end for
  add_dict_obj_duration = timer() - add_dict_obj_start_time
  print(f'Adding Object to Dict time: {"{:.4f}".format(add_dict_obj_duration * 1000)} ms')

  dict_query_obj_duration = timeit(lambda: range_query_dict(dict_with_obj, min_price, max_price), number=test_qty)
  dict_query_obj_quantity = len(range_query_dict(dict_with_obj, min_price, max_price))
  print(f'Object in Dict queries finished:\nGot {dict_query_obj_quantity:.0f} results, average time: {"{:.4f}".format(dict_query_obj_duration * 1000 / test_qty)} ms')

  print(f'─'*50)

  add_tree_obj_start_time = timer()
  for item in csv_data.values():
    item_obj = {'ID': int(item['ID']), 'Name': item['Name'], 'Category': item['Category'], 'Price': float(item['Price'])}
    add_item_to_tree(tree_with_obj, item_obj['ID'], item_obj)
  # end for
  add_tree_obj_duration = timer() - add_tree_obj_start_time
  print(f'Adding Object to Tree time: {"{:.4f}".format(add_tree_obj_duration * 1000)} ms')

  tree_query_obj_duration = timeit(lambda: range_query_tree(tree_with_obj, min_price, max_price), number=test_qty)
  tree_query_obj_quantity = len(range_query_tree(tree_with_obj, min_price, max_price))
  print(f'Object in Tree queries finished:\nGot {tree_query_obj_quantity:.0f} results, average time: {"{:.4f}".format(tree_query_obj_duration * 1000 / test_qty)} ms')

  print(f'═'*50)
  print(f"{'End of results':^50}")
  print(f'═'*50)
# end if

# JavaScript Object Notation - JSON


# Единый фортмат для хранения и передачи данных между компьютерами, сервисами, приложениями и языками програмирования через сеть(Интернет)
# <filename>.json

# {
#     "id": 1,
#     "author": "John",
#     "posts": [...]
# } --- это JSON наша задача перевести его в Python dict

# ## !!!
# JS object == {}
# Py  dict == {}
# JSON == {}

# Процессы Сериализации данных и Десиарилизации 

# Сериализация - это перевод Python Dict в JSON формат (либо сохранить в файле либо просто как текстовые файлы)
# dump - запись данных в JSON фацл 
# dumps - это запись данных в JSON в текстовом формате 

# Десиарилизация - Перевод из JSON в Python Dict


# load - из файла JSON данные и переводим в Dict
# loads - из JSON в текстовом формате переводим данные в Dict

# ---------------------------------------------------------------------------------------------

# '''Процесс десиарилизации'''
# import json
# from urllib.request import urlopen 
# data = urlopen('https://randomuser.me/api/')
# generate_to_dict = json.load(data)
# # print(generate_to_dict)
# # print(type(generate_to_dict))
# # print(generate_to_dict['result'])
# # print(generate_to_dict.keys())

# with open('downAPI', 'w') as file:
#     file.write(str(generate_to_dict))

# =========================================================


# import json 


# data = {
#     'name': 'John', 
#     'last_name': 'Snow',
#     'status': True
# }
# with open('downAPI.json', 'w')as file:
#     json.dump(data, file)





# data = {
#     'name': 'John', 
#     'last_name': 'Snow',
#     'status': True
# }

# string_ = json.dumps(data)
# print(string_)
# print(type(string_))
# py_dict = json.loads(string_)
# print(py_dict)
# print(type(py_dict))

# from urllib.request import urlopen
# import json 

# data = urlopen('https://randomuser.me/api/')
# py_dict = json.load(data)
# print(type(py_dict))

# with open('downAPI.json', 'a') as file: 
#     json.dump(py_dict, file)



# nums  = [4,1,2,1,2]
# O_ = []
# for i in nums:
#     if i != i : 
#         O_.append(i)
#     else: 
#         None
# print(O_)












































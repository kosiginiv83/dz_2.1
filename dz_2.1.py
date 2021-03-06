def import_data():
	cook_book = dict()
	with open('cook_book.txt') as tf:
		for line in tf:
			dish_name = line.strip()
			ingridients_quantity = int(tf.readline())
			ingridients_list = list()
			for i in range(ingridients_quantity):
				raw_ingr_list = tf.readline().split(' | ')
				ingr_dict = dict()
				ingr_dict['ingridient_name'] = raw_ingr_list[0]
				ingr_dict['quantity'] = int(raw_ingr_list[1])
				ingr_dict['measure'] = raw_ingr_list[2].strip()
				ingridients_list.append(ingr_dict)
			cook_book[dish_name] = ingridients_list
			tf.readline()
	return cook_book


def get_shop_list_by_dishes(dishes, person_count):
	cook_book = import_data()
	shop_list = {}
	for dish in dishes:
		for ingridient in cook_book[dish]:
			new_shop_list_item = dict(ingridient)
			new_shop_list_item['quantity'] *= person_count
			if new_shop_list_item['ingridient_name'] not in shop_list:
				shop_list[new_shop_list_item['ingridient_name']
					] = new_shop_list_item
			else:
				shop_list[new_shop_list_item['ingridient_name']
					]['quantity'] += new_shop_list_item['quantity']
	return shop_list


def print_shop_list(shop_list):
	for shop_list_item in shop_list.values():
		print('{ingridient_name} {quantity} {measure}'.format(
						**shop_list_item))


def create_shop_list():
	dishes = input("Введите блюда на одного человека через "
				"запятую (без пробелов): ").lower().split(',')
	person_count = int(input("Введите количество человек: "))
	shop_list = get_shop_list_by_dishes(dishes, person_count)
	print_shop_list(shop_list)


create_shop_list()
input()  # Нужна для того, чтобы окно консоли не закрылось сразу 
# после выполнения программы в случае запуска файла с проводника  
# или файлового менеджера.

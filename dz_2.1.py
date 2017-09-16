import json


def import_data():
	with open('cook_book.json', encoding='utf8') as f:
		dishes = json.load(f)
	return dishes.get('dishes')


def get_shop_list_by_dishes(dishes, person_count):
	cook_book = import_data()
	shop_list = {}
	for dish in dishes:
		dish_index = list(filter(lambda x: cook_book[x]['dish'] ==
					dish, range(len(cook_book))))
		dish_index = dish_index[0]
		for ingridient in cook_book[dish_index]['ingridients']:
			new_shop_list_item = ingridient
			new_shop_list_item['quantity'] *= person_count
			if new_shop_list_item['ingridient name'] not in shop_list:
				shop_list[new_shop_list_item['ingridient name']
								] = new_shop_list_item
			else:
				shop_list[new_shop_list_item['ingridient name']
					]['quantity'] += new_shop_list_item['quantity']
	return shop_list


def print_shop_list(shop_list):
	for shop_list_item in shop_list.values():
		print('{ingridient name} {quantity} {measure}'.format(
						**shop_list_item))


def create_shop_list():
	dishes = input("Введите блюда на одного человека через "
			"запятую (без пробелов): ").lower().split(',')
	person_count = int(input("Введите количество человек: "))
	shop_list = get_shop_list_by_dishes(dishes, person_count)
	print_shop_list(shop_list)


create_shop_list()
input()

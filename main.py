import math

def cost_calculation(product_positions):
	cost_price_products = 0

	for key, value in product_positions.items():
		if key == "positions":
			for item in value:
				cost_price_position = math.ceil((int(item['cost_package'])/int(item['packaged'])) * int(item['recipe']))
				cost_price_products += cost_price_position

	product_positions.update({'cost_price_products': cost_price_products})

	return product_positions

def main():
	print("Расчет себестоимости продукции")
	array_positions = []

	name_products = input("Введите названиие продукции: ")
	product_positions = {'name_products': name_products}
	quantity_positions = int(input("Введите количество позиций: "))
	print("\n")

	for item in range(quantity_positions):
		name_positions = input("Введите название ингредиента: ")
		packaged = input("В упаковке (гр/мл/шт): ")
		cost_package = input("Стоимость упаковки (руб): ")
		recipe = input("В рецепте (гр/мл/шт): ")
		print("\n")

		positions = {'name_positions': name_positions, 'packaged': packaged,
		'cost_package': cost_package, 'recipe': recipe}
		array_positions.append(positions)
	
	product_positions.update({'positions' : array_positions})

	print(cost_calculation(product_positions))

if __name__ == '__main__':
	main()
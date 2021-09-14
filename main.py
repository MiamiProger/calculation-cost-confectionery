import eel


@eel.expose
def cost_calculation(name_pastry, weight_pastry, arr_pastry):
	cost_price_products = 0
	
	for i in arr_pastry:
		cost_price_position = round((int(i[2])/int(i[1])) * int(i[3]))
		cost_price_products += cost_price_position

	return 'Себестоимость '+ name_pastry+ ' = ' + str(cost_price_products)


if __name__ == '__main__':
	eel.init("web")

	eel.start("main.html", size=(850, 600))
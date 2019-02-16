apples = 25
bread = 50
pinapples = 10
bananas = 10
avocados = 20
water_melon = 20

number_of_apples = input("Enter number of Apples: ")
number_of_bread = input("Enter number of Bread: ")
number_of_pinapples = input("Enter number of Pinapples: ")
number_of_bananas = input("Enter number of Bananas: ")
number_of_avocados = input("Enter number of Avocados: ")
number_of_water_melons = input("Enter number of Water Melons: ")


price_of_apples = float(number_of_apples) * apples
price_of_bread = float(number_of_bread) * bread
price_of_pinapples = float(number_of_pinapples) * pinapples
price_of_bananas = float(number_of_bananas) * bananas
price_of_avocados = float(number_of_avocados) * avocados
price_of_water_melons = float(number_of_water_melons) * water_melon


total_payout = price_of_apples + price_of_bread + price_of_pinapples + price_of_bananas + price_of_avocados + price_of_water_melons

print(total_payout)

##### Nombre del estudiante: Edisson Alejandro Castañeda Bermúdez #####
##### Grupo: 213022B_2201 #####
##### Programa: Ingeniería Multimedia #####
##### Código Fuente: autoría propia #####


## IMPORTS ##
# Importación de las librerías que se usarán #
import os
import time
# Final Importación de las librerías que se usarán #
## FINAL IMPORT##

## FUNCIONES ##
# Función limpiar pantalla #
def clear():
	if os.name =="nt":
		os.system("cls")
	else:
		os.system("clear")
# Final Función limpiar pantalla #

# Función imprimir título de la aplicación #
def print_app_title():
	print("\033[36m=" * 50)

	print(f"|{company_name:^48}|")
	
	print("=" * 50)

	print(f"{developer_name:^50}")
	print(f"{academic_program:^50}\033[0m")
# Final Función imprimir título de la aplicación #

# Función imprimir menús #
def print_menu(menu_options, menu_title, error_message=None):
	clear()

	print_app_title()

	print(f"\n-{menu_title:^48}-\n")

	for key, option in menu_options.items():
		print(f"{key}. {option['option_name']}")

	if error_message:
		print(f"\n\033[31m{error_message}\033[0m")

	selected_option = input(f"\nSeleccione una opción (1-{len(menu_options)}): ")

	return selected_option
# Final Función imprimir menús #

# Función ejecutar la opción ingresada por el usuario #
def handle_menu_selection(menu_options, menu_title):
	error_message = None

	while True:
		selected_option = print_menu(menu_options, menu_title, error_message)

		if selected_option not in menu_options:
			error_message = "Opción inválida. Intente nuevamente"
			continue

		error_message = None

		action = menu_options[selected_option]["action"]

		if action is None:
			break

		if isinstance(action,dict):
			handle_menu_selection(action, menu_options[selected_option]["option_name"])
		else:
			action()
# Final Función ejecutar la opción ingresada por el usuario #

# Función agregar un nuevo ítem #
def create_item(items):

	categories = list(items.keys())
	error_message = None

	while True:

		clear()

		print_app_title()
		print(f"\n-{'Agregar un ítem':^48}-\n")

		print("¿Qué tipo de ítem desea agregar?\n")

		for index, category in enumerate(categories, start=1):
			print(f"{index}. {category}")

		print(f"{len(items) + 1}. Salir\n")

		if error_message:
			print(f"\n\033[31m{error_message}\033[0m")

		try:
			category = int(input(f"\nSeleccione una opción (1-{len(items) + 1}): "))
		except ValueError:
			error_message = "Opción inválida. Intente nuevamente"
			continue
			
		if not 1 <= category <= len(items) + 1:
			error_message = "Opción inválida. Intente nuevamente"
			continue
		elif category == len(items) + 1:
			break
		
		error_message = None

		category = categories[category - 1]

		prefix = category.split("(")[1].replace(")", "")
		code = f"{prefix}{len(items[category]) + 1:03}"
		brand = input("Ingrese la marca: ")
		model = input("Ingrese el modelo: ")
		capacity = input("Ingrese la capacidad: ")

		try:
			current_stock = int(input("Ingrese el stock actual: "))
		except ValueError:
			while True:
				clear()
				print_app_title()
				print(f"\n-{'Agregar un ítem':^48}-\n")
				print(
					f"Código: {code}\n" \
					f"Categoría: {category}\n" \
					f"Marca: {brand}\n" \
					f"Modelo: {model}\n" \
					f"Capacidad: {capacity}"
				)
				print(f"\n\033[31mOpción inválida. Intente nuevamente\033[0m")
				try:
					current_stock = int(input("Ingrese el stock actual: "))
				except ValueError:
					continue
				break

		try:
			minimum_stock = int(input("Ingrese el stock mínimo: " ))
		except ValueError:
			while True:
				clear()
				print_app_title()
				print(f"\n-{'Agregar un ítem':^48}-\n")
				print(
					f"Código: {code}\n" \
					f"Categoría: {category}\n" \
					f"Marca: {brand}\n" \
					f"Modelo: {model}\n" \
					f"Capacidad: {capacity}\n" \
					f"Stock actual: {current_stock}"
				)
				print(f"\n\033[31mOpción inválida. Intente nuevamente\033[0m")
				try:
					minimum_stock = int(input("Ingrese el stock mínimo: " ))
				except ValueError:
					continue
				break

		items[category].append(
			{
				"Código": code,
				"Marca": brand,
				"Modelo": model,
				"Capacidad": capacity,
				"Stock actual": current_stock,
				"Stock mínimo": minimum_stock
			}
		)

		clear()
		print_app_title()
		print(f"\n-{'Agregar un ítem':^48}-\n")
		print(
			f"Código: {code}\n" \
			f"Categoría: {category}\n" \
			f"Marca: {brand}\n" \
			f"Modelo: {model}\n" \
			f"Capacidad: {capacity}\n" \
			f"Stock actual: {current_stock}" \
			f"Stock mínimo: {minimum_stock}"
		)

		input("\n\033[92mResgistro actualizado correctamente\033[0m" \
		"\n\nPresione Enter para continuar...")
# Final Función agregar un nuevo ítem #

# Función ver inventario general #
def get_all_items(items):
	clear()

	print_app_title()
	print(f"\n-{'Inventario general':^48}-")

	for category, category_items in items.items():
		print(f"\n\033[1;33m{category:^50}\033[0m")
		for item  in category_items:
			print(f"{'-':^50}")
			for field, value in item.items():
				print(f"{field}: {value}")
		print(f"{'-----':^50}")

	input(f"\nPresione Enter para continuar...")
# Final Función ver inventario general #

# Función ver ítems por reabastecer #
def show_restock_report(items):
	clear()

	print_app_title()
	print(f"\n-{'ítems por reabastecer':^48}-")

	for category, category_items in items.items():
		print(f"\n\033[1;33m{category:^50}\033[0m")
		for item  in category_items:
			print(f"{'-':^50}")
			print(
				f"Ítem: {category} {item['Marca']} " \
		 		f"{item['Modelo']} {item['Capacidad']}"
				)
			print(f"Stock actual: {item['Stock actual']}")
			print(f"Stock mínimo: {item['Stock mínimo']}")
			
			if item['Stock actual'] < item['Stock mínimo']:
				restock_quantity = item['Stock mínimo'] - item['Stock actual']
				print(f"\033[1;31mCantidad a pedir: {restock_quantity}\033[0m")
			else:
				restock_quantity = 0
				print(f"\033[36mCantidad a pedir: {restock_quantity}\033[0m")
		print(f"{'-----':^50}")

	input(f"\nPresione Enter para continuar...")
# Final Función ver ítems por reabastecer #
## FINAL FUNCIONES ##


## VARIABLES, DICCIONARIOS ##
# Variables generales #
APP_NAME = "INVENTORY AUDIT SYSTEM"

APP_VERSION = "1"

company_name = "QUANTIA"

developer_name = "Edisson Alejandro Castañeda Bermúdez"

academic_program = "Ingeniería Multimedia"
# Final variables generales #

# Diccionarios que corresponden a las opciones y acciones del menú y los submenús #
main_menu_options = {
	"1": {
		"option_name": "Agregar un ítem",
		"action": lambda: create_item(items)
	},

	"2": {
		"option_name": "Ver inventario general",
		"action": lambda: get_all_items(items)
	},

	"3": {
		"option_name": "Ver ítems por reabastecer",
		"action": lambda: show_restock_report(items)
	},

	"4": {
		"option_name": "Salir",
		"action": None
	}
}
# Final Diccionarios que corresponden a las opciones y acciones del menú y los submenús #

# Diccionario para almacenar los items del inventario #
items = {
	"Procesadores (P)": [
		{
			"Código": "P001",
			"Marca": "AMD",
			"Modelo": "Ryzen Threadripper PRO 9995WX",
			"Capacidad": "96 C / 2,5 GHz - 5,4 GHz",
			"Stock actual": 1,
			"Stock mínimo": 3
		},

		{
			"Código": "P002",
			"Marca": "AMD",
			"Modelo": "Ryzen 9 9950X3D",
			"Capacidad": "16 C / 4,3 GHz - 5,7 GHz",
			"Stock actual": 4,
			"Stock mínimo": 10
		},

		{
			"Código": "P003",
			"Marca": "Intel",
			"Modelo": "i9 14900KS",
			"Capacidad": "8 P + 16 E / 3,2 GHz - 6,2 GHz",
			"Stock actual": 2,
			"Stock mínimo": 5
		}
	],

	"Placas base (PB)": [
		{
			"Código": "PB001",
			"Marca": "ASUS",
			"Modelo": "Pro WS WRX90E-SAGE SE",
			"Capacidad": None,
			"Stock actual": 2,
			"Stock mínimo": 3
		},

		{
			"Código": "PB002",
			"Marca": "ASUS",
			"Modelo": "ROG CROSSHAIR X870E HERO",
			"Capacidad": None,
			"Stock actual": 8,
			"Stock mínimo": 10
		},

		{
			"Código": "PB003",
			"Marca": "MSI",
			"Modelo": "MEG Z790 GODLIKE MAX",
			"Capacidad": None,
			"Stock actual": 5,
			"Stock mínimo": 5
		}
	],

	"Discos duros (DD)": [
		{
			"Código": "DD001",
			"Marca": "Samsung",
			"Modelo": "9100 PRO",
			"Capacidad": "8 TB",
			"Stock actual": 3,
			"Stock mínimo": 5
		},

		{
			"Código": "DD002",
			"Marca": "Western Digital",
			"Modelo": "WD_BLACK SN850X",
			"Capacidad": "8 TB",
			"Stock actual": 7,
			"Stock mínimo": 12
		},

		{
			"Código": "DD003",
			"Marca": "Crucial",
			"Modelo": "T705",
			"Capacidad": "4 TB",
			"Stock actual": 11,
			"Stock mínimo": 15
		}
	],

	"Memorias RAM (MR)": [

	],

	"Tarjetas gráficas (TG)": [

	]
}
#
## FINAL VARIABLES, DICCIONARIOS ###


## CÓDIGO PRINCIPAL ##
# Función principal #
def main():
	handle_menu_selection(main_menu_options, "Menú principal")
# Final Función principal #

# Ejecución función principal #
main()

print(f"\nCerrando el aplicativo...")
print(f"\n\n\033[36m{APP_NAME}\033[0m")
print(f"\033[36mVersión:\033[0m {APP_VERSION}")
print(f"\033[36mProgramado por:\033[0m {developer_name}")
print(f"\033[36mPrograma:\033[0m {academic_program}")
time.sleep(5)
# Final Ejecución función principal #
## FINAL CÓDIGO PRINCIPAL ##
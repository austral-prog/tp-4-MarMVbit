def leap_year():
    año = input('Ingrese un año: ')
    if (int(año) % 4 == 0 and int(año) % 100 != 0) or int(año)%400 == 0:
        print(f'El año {año} es bisiesto')
    else:
        print(f'El año {año} no es bisiesto')
leap_year()

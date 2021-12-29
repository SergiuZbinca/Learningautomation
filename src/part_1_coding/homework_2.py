# """
# homework_2
# """

# exercitiul_1_aria si perimetrul unui dreptunghi

# lungime = float(input('Introduceti lungimea dreptunghiului: '))
# latime = float(input('Introduceti latimea dreptunghiului: '))
#
# aria = lungime * latime
# perimetrul = 2 * (lungime + latime)
#
# print(f'Aria dreptunghiului este: {aria}')
# print(f'Perimetrul dreptunghiului este: {perimetrul}')
#
# suma = aria + perimetrul
#
# print(f'Suma este aria + perimetrul: {aria} + {perimetrul} = {suma}')

# ***************************************************************************

# exercitiul_2_aria si perimetrul unui triunghi oarecare

# inaltimea1 = float(input('Introduceti inaltimea triunghiului: '))
# latura1 = float(input('Introduceti latura1: '))
# latura2 = float(input('Introduceti latura2: '))
# latura3 = float(input('Introduceti latura3: '))
#
# aria = (latura1 * inaltimea1)/2
# perimetrul = latura1 + latura2 + latura3
#
# print(f'Aria triunghiului este: {aria}')
# print(f'Perimetrul triunghiului este: {perimetrul}')

# ******************************************************************************

# exercitiul_3_aria si perimetrul rombului

# import math
#
# l = float(input('Introduceti latura: '))
# d1 = float(input('Introduceti diagonala1: '))
# d2 = float(input('Introduceti diagonala2: '))
# h = float(input('Introduceti inaltimea: '))
# x = float(input('Introduceti unghiul: '))
#
# perimetrul = 4 * l
# print('')
# print(f'Perimetrul rombului este: {perimetrul} \n')
#
# print('Aria rombului se poate calcula cu 3 formule diferite: \n')
#
# aria1 = (d1 * d2)/2
# print(f'Aria cu formula 1 este: {aria1}')
#
# aria2 = l * h
# print(f'Aria cu formula 2 este: {aria2}')
#
# x_radian = math.radians(x)
# aria3 = (l ** 2) * math.sin(x_radian)
# print(f'Aria cu formula 3 este: {aria3}')

# *********************************************************************************

# exercitiul_4_aria si perimetrul unui hexagon
#
# import math
# l = float(input('Introduceti latura: '))
#
# aria = (3 * math.sqrt(3) * l ** 2) / 2
# perimetrul = 6 * l
# print('')
# print(f'Aria hexagonului cu latura {l} este: {aria} \n')
# print(f'Perimetrul hexagonului cu latura {l} este: {perimetrul}')
#
# *************************************************************************************

# exercitiul_5 - Using strings slicing extract user name and password from the following text message

# message = 'This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages.'
#
# print(f'The username is: {message[]}')
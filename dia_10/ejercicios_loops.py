# ### LOOPS ####

### EJEMPLO DE SALIDA CON UN BREAK EN UN BUCLE WHILE
###  Break: We use break when we like to stop our loop before it is completed.
# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         break

### EJEMPLO DE UN CONTINUE
### Continue: We use continue when we like to skip some of the steps in the iteration of the loop.
# count = 0
# while count < 5:
#     if count == 3:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# for i in range(0,100,5):
    # print(i)

# For Else
# If we want to execute some message when the loop ends, we use else.

# for number in range(11):
#     print(number)
# else:
#     print('The loop stops at', number)

# # Pass
# # In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.

# for number in range(6):
#     pass

# Iterate 0 to 10 using for loop, do the same using while loop.

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# for i in range(10,-1,-1):
#     print(i)

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# for i in range(8):
#     print("#" * i)

# filas = 15
# columnas = 15
# for i in range(filas):
#     print("#" * columnas)

# for i in range(11):
#     resultado = i * i
#     print (f"{i} x {i} = {resultado}")

# lista = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for lenguaje in lista:
#     print(lenguaje)

# for numero in range(101):
#     if numero %2 != 0:
#         continue
#     print(numero)
    
# for numero in range(101):
#     if numero %2 == 0:
#         continue
#     print(numero)

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

# lista = []
# for numero in range(101):
#    lista.append(numero)
# else:
#     print(sum(lista))
#     # print(f"La suma de todos los numero es {numero}")    

# suma = 0
# for numero in range(101):
#     suma += numero
# print(suma)    

suma_pares = 0
suma_impares = 0
for numero in range(101):
    if numero %2 ==0:
        suma_pares += numero
    else:
        suma_impares += numero
print(suma_pares)
print(suma_impares)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

for pais in countries:
    if "land" in pais:
        print(pais)

    

frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_vacia = []

for i in range(len(frutas)-1,-1,-1):
    frutas_vacia.append(frutas[i])
print(frutas_vacia)

datos_paises = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    }]

len_unicos = set()

for pais in datos_paises:
    for lenguaje in pais["languages"]:
        len_unicos.add(lenguaje)
print(len(len_unicos))
        

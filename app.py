import unicodedata
import random

a = open('assets/nomes.csv', 'r', encoding="utf8")
data_names = a.read()
names = data_names.split('\n')
random_name = random.choice(names)

b = open('assets/sobrenomes.csv', 'r')
data_surnames = b.read()
surnames = data_surnames.split('\n')
random_surname = random.choice(surnames)

c = open('assets/dominios.txt', 'r')
data_dominios = c.read()
dominios = data_dominios.split('\n')
random_dominio = random.choice(dominios)


complete_name = random_name + " " + random_surname
print(complete_name)

email = random_name.lower() + random_surname.lower() + random_dominio
email = (email.translate({ord(' '): None})).encode('ascii', 'replace')

print(email)
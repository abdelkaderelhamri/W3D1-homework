# Exercise 1


places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
filtred_list=list(filter(lambda x: True  if x!=" "and x!=""and x!="  " else False , places))
print(filtred_list)

#Exercise 2
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]


author.sort(key=lambda name: name.lower().split()[-1])
print( author)

#Exercise 3

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
Places_fern = list(map(lambda c:  (c[0], (9/5) * c[1]+ 32), places))
print(Places_fern)
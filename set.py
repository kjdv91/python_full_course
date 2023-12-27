# collecion de datos desordenados no indexados, no valores duiplicados
utensils = {"fork","spoon","knife", "knife"}
dishes = {"bowl","plate","cup"}

dishes.update(utensils)

for x in dishes:
    print(x)
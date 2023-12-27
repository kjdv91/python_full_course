#dictionary es cambiable , desordenado, colion clave unica llave : valor

capitals = {
    'Usa': 'Washintong',
    'India': 'New Dehli',
    'Ecuador': 'Quito',
    'Colombia': 'Bogota',
    'Rusia': 'Moscow'
}



print(capitals['India'])
print(capitals['Rusia'])
print(capitals.get('Ecuador'))
print(capitals.get('Argentina'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)

capitals.update({'Germany':'Berlin'})
print(capitals)
capitals.pop('Colombia')
print(capitals)
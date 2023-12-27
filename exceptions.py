
try:
    numerator  = int(input("Ingresa unn nnumero para dividir: \n"))
    denominator = int(input("Ingresa el numero a dividir: \n"))
    result = numerator / denominator
except ZeroDivisionError as e:
   print(e)

except ValueError as e:
    print(e)
except  Exception as e:
    print(e)

else:
    print(result)

finally:
    print("This will always execute")

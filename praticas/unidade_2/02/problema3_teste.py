from problema3 import fraude, desconto_superior

assert fraude(10, 10) == True
assert fraude(10, 20) == True
assert fraude(10, 5) == False

assert desconto_superior(10, 10) == False
assert desconto_superior(10, 20) == False
assert desconto_superior(10, 9) == False
assert desconto_superior(10, 8.9) == True

print('Testes - ok')

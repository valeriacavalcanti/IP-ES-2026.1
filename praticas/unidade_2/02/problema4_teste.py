from problema4 import *

assert converte(0,0,1) == 1
assert converte(0,1,0) == 60
assert converte(0,1,1) == 61
assert converte(1,0,0) == 3600
assert converte(1,0,1) == 3601
assert converte(1,1,1) == 3661

assert hora(1) == 0
assert hora(60) == 0
assert hora(61) == 0
assert hora(3600) == 1
assert hora(3601) == 1
assert hora(3661) == 1

assert minuto(1) == 0
assert minuto(60) == 1
assert minuto(61) == 1
assert minuto(3600) == 0
assert minuto(3601) == 0
assert minuto(3661) == 1

assert segundo(1) == 1
assert segundo(60) == 0
assert segundo(61) == 1
assert segundo(3600) == 0
assert segundo(3601) == 1
assert segundo(3661) == 1

print('Testes ok')

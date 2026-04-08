from questao_05_funcoes import comparar

''''
Assert é um comando que serve para garantir que uma condição seja verdadeira para programa continuar.

Se a condição for verdadeira, o Python não faz nada e segue para a próxima linha.
Se a condição for falsa, o Python interrompe o programa imediatamente e gera um erro chamado AssertionError.

Podemos usar para testar a nossa função! Se o resultado for igual ao esperado ... segue para o próximo teste!

Se nenhum teste falhar ... a mensagem de sucesso será exibida! Caso contrário, o programa será interrompido onde houve a falha.
'''

assert comparar(10, 20) == -1
assert comparar(20, 10) == 1
assert comparar(10, 10) == 0

print('Testes realizados com sucesso!')
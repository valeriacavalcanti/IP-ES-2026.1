qtd_aprovados = int(input('Quantidade de alunos aprovados: '))
qtd_reprovados = int(input('Quantidade de alunos reprovados: '))

qtd_total = qtd_aprovados + qtd_reprovados

porcentagem = qtd_aprovados / qtd_total * 100

print(f'Porcentagem de alunos aprovados: {porcentagem:.1f}%')
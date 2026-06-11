arq = open('servidores.csv', 'r')
registros = arq.read().splitlines()
arq.close()

cargos = []
cargos_professor = []

# matricula,nome,cargo_emprego,jornada_trabalho,lotacao_siape.sigla,
# lotacao_suap.sigla,setor_exercicio.sigla,funcao_codigo,disciplina_ingresso

for i in range(1, len(registros)):
    servidor = registros[i].split(',')
    
    if servidor[2] not in cargos:
        cargos.append(servidor[2])

    if 'PROFESSOR' in servidor[2].upper():
        if servidor[2] not in cargos_professor:
            cargos_professor.append(servidor[2])

    #print(servidor)
    #break

print(cargos_professor)

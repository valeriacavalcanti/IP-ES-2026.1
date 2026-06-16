arq = open('eleitorado_eleicao.csv', 'r')
dados = arq.read().splitlines()
arq.close()

print(dados[0])

grau_instrucao = dict()

# Estado civil;Faixa etária;Grau de instrução;Município;Quantidade de eleitores

for i in range(1, len(dados)):
    registro = dados[i].split(';')
    
    if registro[2] not in grau_instrucao:
        grau_instrucao[registro[2]] = int(registro[4])
    else:
        grau_instrucao[registro[2]] += int(registro[4])

total_eleitores = sum(grau_instrucao.values())

print(grau_instrucao)
print(total_eleitores)


arq = open('template.html', 'r')
template = arq.read()
arq.close()


#"<tr><td>1</td><td>Mark</td><td>Otto</td></tr>"
    
conteudo_dinamico = ''

for k,v in grau_instrucao.items():
    p = v/total_eleitores * 100
    conteudo_dinamico += f"<tr><td>{k}</td><td>{v}</td><td>{p:.2f}</td></tr>"
    #print(k, v, v/total_eleitores * 100)

html = template.replace('[?]', conteudo_dinamico)

arq = open('index.html', 'w')
arq.write(html)
arq.close()

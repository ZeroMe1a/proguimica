from os import system, name # do OS importamos o SYSTEM (executa comandos em um terminal) e o NAME (mostra o nome do sistema)
from math import log # de math importamos o LOG para fazer um calculo mais pra frente

### START CLASSES ###

class important: # Criando uma classe para armazenar algumas variáveis que serão usadas em diferentes funções.
  file_imp = None # Criando a variável 'file_imp' que vai ser onde armazenaremos as opções do arquivo na ordem (OPÇÃO, VALOR1, VALOR2, VALOR3).
  file = 'teste.txt' # ATENÇÃO: aqui é onde armazenamos o nome do arquivo que iremos abrir, caso seu arquivo esteja no mesmo diretório que o script, coloque apenas o nome do arquivo COM extensão. Caso o arquivo não esteja no mesmo diretório, coloque o caminho completo (ex: 'C:/Users/nuvem/Python/Projetos/Proguímica/teste.txt')
  lock1 = False # Vai ser usado para não mostrar algumas informações duas vezes uma vez que a mesma seja True.
  sep = '######' # usado para separar as linhas no documento teste.txt

### END CLASSES ###

### START MISC FUNCS ###

def clear(): # Função para limpar a tela, apenas pra ficar bonitinho
  if name == 'nt': # caso o nome do sistema seja NT (windows) ele usa o cls
    _ = 'cls'
  else:
    _ = 'clear' # caso seja outro nome ele usa o clear, que é universal pra android, mac, linux, etc
  system(_) # executamos o comando que está armazenado na variável _

def create_menu(menunum): # Função para criar menus
  clear() # Limpando a tela
  print('') # printando uma linha limpa (\n seria 2 linhas com esse print)
  print('-=-'*30) # printando um pontilhado 30 vezes (atenção: o pontilhado tem 3 caracteres, ou seja 30x3 = 90)
  print(f'{menunum}'.center(90)) # Encaixando a frase que foi dada entre 90 caracteres no centro
  print('-=-'*30, end='\n\n') # printando um pontilhado 30 vezes mas com linhas limpas no final

def append_to_file(phrase): # Criando uma função para escrever no arquivo (pra ficar mais simples de lêr)
  with open(important.file, 'a') as f: # abrindo o arquivo no modo 'a' (append) e chamando ele de f
    if important.lock1 == False: # para só escrever uma vez a string
      f.write(f'\n###RESULTADOS###\n\n') # escrevendo a string
    f.write(phrase) # escrevendo a frase, que no caso é dada quando o script chama a função
  if important.lock1 == False: # aqui a lock vai ser necessária para não printar isso várias vezes
    print(f'Resultados escritos no arquivo: {important.file}') # avisando que os resultados estão no arquivo
    important.lock1 = True # setando a lock para true

def set_default(): # Criando uma função SET_DEFAULT | Uso: ela vai setar todos os valores da classe important (MENOS o nome do arquivo) para seus valores originais para evitar problemas.
  important.file_imp = None # retornando ao valor normal
  important.lock1 = False # retornando ao valor normal

def automate(): # Criando a função que irá ler os arquivos e passar os argumentos
  try:
    with open(important.file, 'r') as f: # abrindo o arquivo no modo 'Read' e vamos mencionar ele como f
      file = f.read().splitlines() # lendo as linhas e removendo caracteres do tipo '\n' (Indicam novas linhas) e dando isso como valor da variável 'file_imp' (file_imports)
    important.file_imp = ','.join(file) # criando uma string com a lista
    important.file_imp = [line.split(',') for line in important.file_imp.split(important.sep)] # criando sub listas de a cordo com os separadores

    for i in range(len(important.file_imp)):
      if important.file_imp[i][0] == '':
        val = 1
      else:
        val = 0
      if important.file_imp[i][val] == '1':
        options_auto(important.file_imp[i][0+val], important.file_imp[i][1+val], float(important.file_imp[i][2+val]), '', '', '', '', '', '')
        continue

      elif important.file_imp[i][val] == '2':
        options_auto(important.file_imp[i][0+val], '', float(important.file_imp[i][1+val]), float(important.file_imp[i][2+val]), '', '', '', '', '')
        continue

      elif important.file_imp[i][val] == '3':
        options_auto(important.file_imp[i][0+val], '', '', float(important.file_imp[i][2+val]), float(important.file_imp[i][1+val]), float(important.file_imp[i][3+val]), '', '', '')
        continue

      elif important.file_imp[i][val] == '4':
        options_auto(important.file_imp[i][0+val], '', '', '', '', '', float(important.file_imp[i][1+val]), '', '')
        continue

      elif important.file_imp[i][val] == '5':
        options_auto(important.file_imp[i][0+val], '', '', '', '', float(important.file_imp[i][3+val]), '', float(important.file_imp[i][1+val]), float(important.file_imp[i][2+val]))
        continue
  except:
    pass

### END MISC FUNCS ###

### START MAIN ###

def main_menu(): # Função PRINCIPAL, essa função vai chamar as outras e vai dar o primeiro 'Oi' pro usuário
  create_menu('Proguímica CLI | Menu') # Criando um menu com esta frase
  set_default()

  print('1. Importar Dados Manualmente.\n') # Printando informações simples com uma linha de espaçamento
  print('2. Abrir Documento.\n') # Printando informações simples com uma linha de espaçamento
  print('3. Sair.\n') # Printando informações simples com uma linha de espaçamento

  ch = input('?: ') # Esperando input do usuário

  if ch == '1': # Checando se o input é 1
    options_man() # caso for, executar OPTIONS com argumentos vazios

  elif ch == '2': # Checando se o input é 2
    automate()

  elif ch == '3': # Checando se o input é 3
    exit() # caso for, falamos pro python parar de executar

### END MAIN ###

### START AUTO FUNCS ###

def options_auto(ch, formula, mols, vol, press, temp, cons_vel, deltah, deltas):

  if ch == '1':
    for i in range(len(formula)):
      elemento = ''
      indice = 1

      try:
        if formula[i].isupper() == True:
          elemento = formula[i]

          if formula[i+1].islower() == True:
            elemento = elemento+formula[i+1]
          elif formula[i+1].isdigit() == True:
            indice = int(formula[i+1])
            elemento = elemento+str(indice)
        elif formula[i].isdigit() == True:
          elemento = formula[i+1]
      except:
        pass
      final_mols = mols*indice
      if elemento != '':
        natomos = final_mols*(6.02*10**23)
        append_to_file(f'N° Mols: {final_mols}, Elemento: {elemento}\nN° Átomos: {natomos:.3e}\n\n')
      if elemento == formula[-1]:
        break

  elif ch == '2':
    while True:
      c = mols/vol
      append_to_file(f'Mols: {mols}, Volume: {vol}\nA concentração molar é: {c:.3e}mol/L.\n\n')
      break
    
  elif ch == '3':
    while True:
      r = 0.082
      mols = (press*vol)/(r*temp)
      append_to_file(f'Pressão: {press}, Volume: {vol}, Temperatura: {temp}\nGás Prod. (Mols): {mols:.3e}\n\n')
      break

  elif ch == '4':
    while True:
      tmeia = log(2)/cons_vel
      append_to_file(f'Constante (K): {cons_vel}\nO tempo de meia-vida dessa reação de 1° ordem é: {tmeia:.3e}\n\n')
      break

  elif ch == '5':
    while True:
      g = deltah - (temp*deltas)
      append_to_file(f'Delta H: {deltah}, Delta S: {deltas}, Temperatura: {temp}\nO valor da energia livre de Gibbs é: {g:.3e}\n\n')
      break

### END AUTO FUNCS ###

### START MANUAL FUNCS ###

def options_man(): # Opções
  create_menu('Proguímica CLI | Opções')
  print('1. Determinação do número de átomos de cada elemento de uma fórmula a partir do número de mols\n')
  print('2. Cálculo concentração molar de uma solução\n')
  print('3. Cálculo da quantidade de um gás produzido\n')
  print('4. Cálculo do tempo de meia vida para uma reação com cinética de primeira ordem\n')
  print('5. Cálculo da energia livre de Gibbs\n')
  print('6. Voltar\n')
  print('7. Sair\n')

  ch = input('?: ') # Pedindo input e checando ele abaixo
    
  if ch == '1':
    opt1_man()
  elif ch == '2':
    opt2_man()
  elif ch == '3':
    opt3_man()
  elif ch == '4':
    opt4_man()
  elif ch == '5':
    opt5_man()
  elif ch == '6':
    main_menu()
  elif ch == '7':
    exit()

def opt1_man(): # Opção 1
  create_menu('Proguímica CLI | Calculando Opção 1')

  formula = input('Informe a fórmula do composto: ')
  mols_base = int(input('Informe o número de mols do composto: '))

  print(f'\nCalculando: N° Mols: {mols_base}, Fórmula: {formula}')

  for i in range(len(formula)):
      elemento = ''
      indice = 1

      try:
          if formula[i].isupper() == True:
              elemento = formula[i]

              if formula[i+1].islower() == True:
                  elemento = elemento+formula[i+1]
              elif formula[i+1].isdigit() == True:
                  indice = int(formula[i+1])
                  elemento = elemento+str(indice)
          elif formula[i].isdigit() == True:
              elemento = formula[i+1]
      except:
          pass
      
      mols = mols_base*indice

      if elemento != '':
          natomos = mols*(6.02*10**23)
          print('')
          print(f'N° Mols: {mols}, Elemento: {elemento}')
          print(f'N° Átomos: {natomos:.3e}')

          if elemento == formula[-1]:
              break

  print('')
  ch = input('END | Deseja Voltar? (Y/N): ')
  if ch.lower() == 'y':
      options_man()
  elif ch.lower() == 'n':
      exit()

def opt2_man(): # Opção 2
  create_menu('Proguímica CLI | Calculando Opção 2')

  while True:
      mols = float(input('N° Mols: '))
      vol = float(input('Volume (L): '))
      c = mols/vol
      print(f'Calculando Mols: {mols}, Volume: {vol}\nA concentração molar é: {c:.3e}mol/L.\n')
      break

  ch = input('END | Deseja Voltar? (Y/N): ')
  if ch.lower() == 'y':
      options_man()
  elif ch.lower() == 'n':
      exit()

def opt3_man(): # Opção 3
  create_menu('Proguímica CLI | Calculando Opção 3')

  while True:
      press = float(input('Pressão (ATM): '))
      vol = float(input('Volume (L): '))
      temp = float(input('Temperatura (K): '))
      r = 0.082
      mols = (press*vol)/(r*temp)
      print(f'Gás Prod. (Mols): {mols:.3e}')
      break

  ch = input('END | Deseja Voltar? (Y/N): ')
  if ch.lower() == 'y':
      options_man()

  elif ch.lower() == 'n':
      exit()

def opt4_man(): # Opção 4
  create_menu('Proguímica CLI | Calculando Opção 4')

  while True:
      cons_vel = float(input('Constante da reação (K): '))
      tmeia = float(log(2)/cons_vel)
      print(f'O tempo de meia-vida dessa reação de 1° ordem é: {tmeia:.3e}')
      break

  ch = input('END | Deseja Voltar? (Y/N): ')
  if ch.lower() == 'y':
      options_man()
  elif ch.lower() == 'n':
      exit()

def opt5_man(): # Opção 5
  create_menu('Proguímica CLI | Calculando Opção 5')

  while True:
    deltah = float(input('Valor de Delta H (Kcal/mol): '))
    deltas = float(input('Valor de Delta S (Kcal/mol): '))
    temp = float(input('Temperatura (K): '))
    g = float(deltah - (temp*deltas))
    print(f'O valor da energia livre de Gibbs é: {g:.3e}')
    break

  ch = input('END | Deseja Voltar? (Y/N): ')
  if ch.lower() == 'y':
      options_man()
  if ch.lower() == 'n':
      exit()

### END MANUAL FUNCS ###

main_menu() # Iniciando o Proguímica
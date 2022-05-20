# Soma
def somacalc(): 
  escolha1 = 'nulo'
  print()
  num1 = float (input ('Digite o primeiro número que você deseja somar: '))
  print()
  num2 = float (input ('Digite o número que você deseja somar com {}: ' .format(num1)))
  print()
  rsoma = num1 + num2
  print ('A soma de {} com {} é [{}]' .format(num1, num2, rsoma))
  print()
  while escolha1 != 'Sim' and 'Não':
   escolha1 = str (input ('Deseja continuar somando? (Sim/Não) '))
   print()
   if escolha1 == 'Sim':
     print ('Você escolheu continuar a soma, lembrando que seu último resultado foi [{}]' .format(rsoma))
     somacalc()
   elif escolha1 == 'Não':
       print ('Retornando você ao Menu Principal')
       menuprincipal()

# Subtração
def subcalc():
  escolha1 = 'nulo'
  print()
  num1 = float (input ('Digite o primeiro número que você deseja usar na subtração: '))
  print()
  num2 = float (input ('Digite o número que você deseja subtrair por {}: ' .format(num1)))
  print()
  rsub = num1 - num2
  print ('A subtração de {} por {} é [{}]' .format(num1, num2, rsub))
  print()
  while escolha1 != 'Sim' and 'Não':
   escolha1 = str (input ('Deseja continuar subtraindo? (Sim/Não) '))
   print()
   if escolha1 == 'Sim':
     print ('Você escolheu continuar a subtração, lembrando que seu último resultado foi [{}]' .format(rsub))
     subcalc()
   elif escolha1 == 'Não':
       print ('Retornando você ao Menu Principal')
       menuprincipal()

# Multiplicação
def multcalc():   
  escolha1 = 'nulo'
  print()
  num1 = float (input ('Digite o primeiro número que você deseja multiplicar: '))
  print()
  num2 = float (input ('Digite o número que você deseja multiplicar por {}: ' .format(num1)))
  print()
  rmult = num1 * num2
  print ('O produto de {} multiplicado por {} é [{}]' .format(num1, num2, rmult))
  print()
  while escolha1 != 'Sim' and 'Não':
   escolha1 = str (input ('Deseja continuar multiplicando? (Sim/Não) '))
   print()
   if escolha1 == 'Sim':
     print ('Você escolheu continuar a multiplicação, lembrando que seu último resultado foi [{}]' .format(rmult))
     multcalc()
   elif escolha1 == 'Não':
       print ('Retornando você ao Menu Principal')
       menuprincipal()

# Divisão
def divcalc():   
  escolha1 = 'nulo'
  print()
  num1 = float (input ('Digite o dividendo (Número que será dividido): '))
  print()
  num2 = float (input ('Digite o divisor (Número pelo qual {} será dividido): ' .format(num1)))
  print()
  rdiv = num1 / num2
  resto = num1 % num2
  print ('O quociente de {} dividido por {} é [{}]' .format(num1, num2, rdiv))
  print ('O resto de {} dividido por {} é [{}]' .format(num1, num2, resto))
  print()
  while escolha1 != 'Sim' and 'Não':
   escolha1 = str (input ('Deseja continuar dividindo? (Sim/Não) '))
   print()
   if escolha1 == 'Sim':
     print ('Você escolheu continuar a divisão, lembrando que seu último resultado foi [{}] e o resto foi [{}]' .format(rdiv, resto))
     divcalc()
   elif escolha1 == 'Não':
       print ('Retornando você ao Menu Principal')
       menuprincipal()

# Fatorial
def fatcalc():   
  escolha1 = 'nulo'
  print()
  num = int (input ('Digite o número que será fatorado: '))
  fat = 1
  for i in range (1, num+1):
    fat = fat * i
  print ('O fatorial de {} é [{}]' .format(num, fat))
  print()
  while escolha1 != 'Sim' and 'Não':
   escolha1 = str (input ('Deseja continuar fatorando? (Sim/Não) '))
   print()
   if escolha1 == 'Sim':
      print ('Você escolheu continuar a fatoração, lembrando que seu último resultado foi [{}]' .format(fat))
      fatcalc()
   elif escolha1 == 'Não':
        print ('Retornando você ao Menu Principal')
        menuprincipal()

# Raiz  
def raizcalc():   
  escolha1 = 'nulo'
  print()
  num = int (input ('Digite o número que você quer a raiz quadrada: '))
  raiz = num**(1/2)
  print ('A raiz quadrada de {} é [{}]' .format(num, raiz))
  print()
  while escolha1 != 'Sim' and 'Não':
   escolha1 = str (input ('Deseja continuar calculando raiz quadrada? (Sim/Não) '))
   print()
   if escolha1 == 'Sim':
      print ('Você escolheu continuar calculando raiz, lembrando que seu último resultado foi [{}]' .format(raiz))
      fatcalc()
   elif escolha1 == 'Não':
        print ('Retornando você ao Menu Principal')
        menuprincipal()       

# Menu principal
def menuprincipal():   
  print ('1. Soma')
  print ('2. Subtração')
  print ('3. Multiplicação')
  print ('4. Divisão')
  print ('5. Fatorial')
  print ('6. Raiz quadrada')
  print ('7. Desligar calculadora')
  print()
  escolha = str (input ('Digite o número da opção que você deseja: '))
  if escolha == '1':
    somacalc()
  elif escolha == '2':
    subcalc()
  elif escolha == '3':
    multcalc()
  elif escolha == '4':
    divcalc()
  elif escolha == '5':
    fatcalc()
  elif escolha == '6':
    raizcalc()
  elif escolha == '7':
    print()
    print('[OFF]')
    exit()
  else:
    print()
    print('Por favor digite o número da opção corretamente')
    menuprincipal()

# Codigo principal
print ('ReCal Alpha by ReScience')
print ()
menuprincipal()

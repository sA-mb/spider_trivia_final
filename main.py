import time
import os
import random

#colores
RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[39m'
BLUE = '\033[34m'
BLACK = '\033[30m'
WHITE = '\033[37m'


#variable de lista de intentos y score
lista_intentos = [ ]
lista_score = [ ]

# Iniciamos  variable  True
iniciar_spider_trivia = True  
#numero de intento y puntaje
intentos = 1
score = 0

print(RED+"Bienvenid@ a la Spider-Trivia!!!"+RESET)

#funciones que limpian pantalla
def limpieza ():
  time.sleep(5)
  os.system('clear')
  time.sleep(2)

def limpieza_corta ():
  time.sleep(2.5)
  os.system('clear')
  time.sleep(1)

limpieza_corta ()

#cuenta regresiva del desafio
def cuenta_regresiva ():
  for numero_carga in range(5, 0, -1):
   print(numero_carga)
   time.sleep(1) 
   os.system('clear') 

#se llama a la funcion de la cuenta
cuenta_regresiva ()
    
#introduccion
print( RED+"Celebrando un año más de la primera aparición de "+RESET)
print(BLUE+"nuestro héroe favorito, te retamos fiel creyente."+RESET)
print ("")
print("Escribe tu nombre para empezar!\nMi nombre es: ", end="")

#nombre del participante
name = input()
time.sleep(1.5)
os.system('clear')

while iniciar_spider_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  score = 0
  if intentos != 1:
   print("\nIntento número:", intentos)
  
  input("Presiona Enter para continuar")
  
  #score de la trivia
  score = 0
  
  #mensaje respuesta invalida
  re_incorrecto = RED+f"Santas telarañas {name}! Solo puedes ingresar estas alternativas: a, b, c, d o e! \nIngresa nuevamente tu respuesta: "+RESET
  
  #variable pregunta secreta
  secreto = random.randint(0, 50)
  
  pregunta_secreta_uno = BLUE+"""PREGUNTA SECRETA!!!
  
  ¿Quien ya hizo las paces con Peter Parker?
  
  a) Tony Stark
  b) Thor Odinson
  c) Gral. Ross
  d) Eddie Brock
  e) Norman Osborn
  
  Tu respuesta es: """+RESET
  
  #variables de preguntas
  pregunta_secreta_uno = BLACK+"""Pregunta secreta del dia
  ¿Quien de estos personajes ya hizo las paces con Peter Parker?
  
  a) Tony Stark
  b) Thor Odinson
  c) Gral. Ross
  d) Eddie Brock
  e) Norman Osborn
  
  Tu respuesta es: """+RESET
  
  pregunta_uno = """¿En cuál de los siguientes comics fue la primera aparición de la sensación arácnida?
  
  a) The Incredible Hulk #180
  b) The Incredible Hulk #1
  c) Amazing Fantasy #15
  d) New Mutants vol.1 #98
  e) Marvel Spotlight #5
  
  Tu respuesta es: """
  
  pregunta_dos = """¿En que universo Spider-Man cuenta con cierto grado de inmortalidad?
  
  a) U-537
  b) U-161
  c) U-626
  d) U-616
  e) U-777
  
  Tu respuesta es: """
  
  pregunta_tres = WHITE+"""¿Despues de derrotar a que villano es que la tia May descubre la identidad secreta de Peter?
  
  a) Venom
  b) Thanos
  c) Kulan-Gath
  d) Morlun
  e) Mad-Hatter
  
  Tu respuesta es: """+RESET
  
  pregunta_trampa = RED+"""PREGUNTA TRAMPA
  
  ¿Spider - Man usa capa?
  
  a) Si. Todos lo grandes heroes usan capa!
  b) No. Spider - Man no usa capa!
  c) Si. Spidey siempre anda a la moda!
  d) No. Solo cuando se queda sin trajes limpios.
  e) Es mas el traje negro vania con capa.
  
  Tu respuesta es: """+RESET
  #fin de variable de preguntas

  limpieza_corta ()
  #se llama a la funcion de la cuenta
  cuenta_regresiva ()
  #-------------------------------------------------
  #INICIO DE LA TRIVIA
  
  print(f"Excelente {name} comencemos de una vez!")
  limpieza_corta ()
  
  #----------------------
  #INICIO DE PREGUNTAS
  
  #INICIO DE PREGUNTA SECRETA
  if secreto % 2 == 0:
   print(pregunta_secreta_uno, end="")
   respuesta_pregunta_secreta_uno= input()
   respuesta_pregunta_secreta_uno = respuesta_pregunta_secreta_uno.lower()
   time.sleep(2)
  
   while respuesta_pregunta_secreta_uno not in ("a","b","c","d","e","venom"):
      print(re_incorrecto)
      respuesta_pregunta_secreta_uno = input()
   if respuesta_pregunta_secreta_uno == "d":
     print()
     print(f"Sorprendente {name}. Asombroso!")
     score += 20
     limpieza_corta ()
   elif respuesta_pregunta_secreta_uno == "venom":
     print(f"Todo un conocedor! {name} si que estas al dia de todas las novedades!")
     score +=40
     limpieza_corta ()
   else:
     print(f"Incorrecto! Descuida {name} no era una pregunta sencilla.")
     limpieza_corta ()
  
  #FIN DE PREGUNTA SECRETA
  
  #INICIO DE PREGUNTA UNO
  print(pregunta_uno, end="")
  
  respuesta_uno= input()
  respuesta_uno = respuesta_uno.lower()
  time.sleep(2)
  
  while respuesta_uno not in ("a","b","c","d","e","ditko"):
      print(re_incorrecto)
      respuesta_uno = input()
  if respuesta_uno == "c":
     print()
     print(f"Excelsior, {name}!")
     score += 10
  elif respuesta_uno == "ditko":
     print(f"Todo un conocedor! {name} Steve estaria orgulloso de ti!")
     score +=20 
  else:
     print(f"Incorrecto! Descuida {name} no era una pregunta sencilla.")
  #FIN DE PREGUNTA UNO
  limpieza_corta ()
  
  #INICIO DE PREGUNTA DOS
  print(pregunta_dos, end="")
  
  respuesta_dos= input()
  respuesta_dos = respuesta_dos.lower()
  time.sleep(2)
  
  while respuesta_dos not in ("a","b","c","d","e","ultimate"):
      print(re_incorrecto)
      respuesta_dos = input()
  if respuesta_dos == "b":
     print()
     print(f"Pow! Respuesta correcta {name}!")
     score += 10
  elif respuesta_dos == "ultimate":
     print(f"Todo un conocedor! {name} Stan estaria orgulloso de ti!")
     score +=20 
  else:
     print(f"Incorrecto! Descuida {name} no era una pregunta sencilla.")
  #FIN DE PREGUNTA DOS
  
  limpieza_corta ()
  
  #INICIO DE PREGUNTA TRES
  print(pregunta_tres,end="")
  
  respuesta_tres= input()
  respuesta_tres = respuesta_tres.lower()
  time.sleep(2)
  
  while respuesta_tres not in ("a","b","c","d","e","totem"):
      print(re_incorrecto)
      respuesta_tres = input()
  if respuesta_tres == "d":
     print()
     print(f"Wip! {name} sabes tanto que posiblemente tambien sepas la formula de las telarañas!")
     score += 10
  elif respuesta_tres == "totem":
     print(f"Todo un conocedor! {name} Stan estaria orgulloso de ti!")
     score +=20 
  else:
     print(f"Recorcholis! Descuida {name} no era una pregunta sencilla.")
  #FIN DE PREGUNTA TRES
    
  limpieza_corta ()
  
  #INICIO DE PREGUNTA TRAMPA
  
  print(pregunta_trampa,end="")
  
  respuesta_trampa= input()
  respuesta_trampa = respuesta_trampa.lower()
  time.sleep(2)
  
  while respuesta_trampa not in ("a","b","c","d","e","nunca"):
      print(re_incorrecto)
      respuesta_trampa = input()
  if respuesta_trampa == "b":
     print()
     print(f"Gracias {name}, tu y yo sabemos las capas son una deshonra para el manto de nuestro amistoso vecino! \n")
     score *= 2
  elif respuesta_trampa == "nunca":
     print("Miles!!!!!!!!! Spider-Man no usa capa. NUNCA.")
     score *=4 
  else:
     score /= 2
     print(f"Disculpa {name}, pero deberias dejar de leer el DB!.")


  limpieza_corta ()
  
  #FIN DE PREGUNTA TRAMPA
  #FIN DE PREGUNTAS
  #----------------------
  
  
  #puntos de regalo
  if 30 <= score:
   print ("Me has caido bien fiel creyente, una ayuda para un hermano aracnido\n") 
   punto_extra = random.randint(0, 50)
   score += punto_extra

   limpieza_corta ()
    
   print(f"{punto_extra} puntos extra de parte de tu amistoso vecino Spider - Man\n")
    
  #gracias por participar
  gracias =f"Gracias por participar {name}, tu puntaje final es de {score}\n"
  print(gracias)
  #FIN DE LA TRIVIA
  time.sleep(1)
  input("Presiona Enter para continuar")
  os.system('clear')
  
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_spider_trivia = input("Ingresa 'si' para repetir, o cualquier tecla si ya tuviste suficiente por hoy: ").lower()

#ingreso a las listas
  lista_intentos.append(intentos)
  lista_score.append(score)
  
  #REPETICION DE LA TRIVIA
  if repetir_spider_trivia == "si":
   intentos += 1
  else:
   limpieza_corta ()
   print("Estos so tus resultados de hoy: \n")
   for n, lista_intentos in enumerate(lista_intentos):
     print("Intento #",lista_intentos, lista_score[n],"puntos")
   limpieza()
   print(f"\n{name} espero que sigas leyendo nuevos comics, hasta pronto!")
   iniciar_spider_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.







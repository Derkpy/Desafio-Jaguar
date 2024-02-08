import random
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Label, PhotoImage, Toplevel
from tkinter import messagebox
from PIL import Image, ImageTk
from conexion_base_de_datos import obtener_datos

#Creacion de la ventana principal
login = tk.Tk()
color = "#FFFFFF"
color_letras = "#191970"
color_accesorios = "#8B0000"
color_botones = "red"
color_entradas_texto = "#CCCCCC"
login.title("DESAFIO JAGUAR")
login.geometry("800x500")

seleccion = None

ancho_pantalla = login.winfo_screenwidth()                    #Esto es para
alto_pantalla = login.winfo_screenheight()                    #pocisionar la ventana
h = int((ancho_pantalla - login.winfo_reqwidth()) /4)         #en la pantalla
a = int((alto_pantalla - login.winfo_reqheight()) /7)
login.geometry(f"+{h}+{a}")
login.configure(bg=color)
login.resizable(width=False, height=False)

#Estilos de letras

#Calibri
estilo = ttk.Style()
estilo.configure("Pregunta.TLabel", foreground=color_letras, font=("Gabriola", 14, "bold"))

style = ttk.Style()
style.configure("Entrada.TLabel", foreground=color, font=("Century Gothic", 11, "bold"))


#Lista de contraseñas
contraseñas = ["123","343","234","111","222"]

pregunta1A = [{"p": "¿Cuál es el símbolo utilizado en notación sumatoria para indicar la suma de una serie de términos?","r1": "∏","r2": "∆","r3": "∑","r4": "&","rc": "∑"}]
pregunta2A = [{"p": "¿Selecciona cuáles son los métodos de integración?","r1": "Sustitución, por partes y fracciones parciales","r2": "Sustitución, reducción y diferenciación", "r3": "Diferenciación, fracciones parciales y por partes","r4": "Sustitución y por partes", "rc": "Sustitución, por partes y fracciones parciales"}]
pregunta3A = [{"p": "¿Qué se entiende por 'Suma de Riemann'?","r1": "Aproximación del área bajo la curva","r2": "Notación sumita","r3": "Integral inferida","r4": "Integral definida","rc": "Suma de Riemann"}]


frases = [
        "No tengas miedo de fracasar; ten miedo de no intentarlo.",
        "El único límite para tus logros es tu propia imaginación.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "El camino hacia el éxito está lleno de obstáculos, pero cada obstáculo superado te acerca más a tu meta.",
        "Los desafíos son la forma en que la vida te pone a prueba. Demuéstrale que estás dispuesto a luchar.",
        "Recuerda que cada desafío superado te acerca un paso más a tus metas y sueños.",
        "Los desafíos son oportunidades para descubrir tu verdadero potencial.",
        "No tienes que ser grande para empezar. Pero tienes que empezar para poder ser grande.",
        "El que cree que lo sabe todo es incapaz de aprender."
    ]


acertijo01 = ["Es docente, siempre anda muy alegre, sabe de programación, le encanta el fútbol y le resulta ser carismático siendo tutor.", "jaguarundi13"]
acertijo02 = ["Es muy joven, siempre se encuentra feliz y es capaz de explicar con muchos colores hasta los temas más complejos y difíciles de entender.", "ocelote14"]
acertijo03 = ["Podría pasar por galán de telenovelas, siempre lleva un outfit que lo hace resaltar y es muy apreciado por sus estudiantes porque les suele aconsejar.", "tucanes26"]
acertijo04 = ["Suele volver entretenidas y amenas sus clases, también es el encargado de una de las áreas más importantes para los estudiantes de sistemas.", "guacamayas15"]
acertijo05 = ["Es responsable de cuidar y guiar a los estudiantes, se puede acudir a ella cuando se requiera de apoyo o consejo, pues siempre velará por el bien del estudiante.", "manati32"]
acertijo06 = ["¡ZAZ! Es el mero experto en finanzas, la contabilidad es lo suyo, siempre viene muy pulcro con una sonrisa de oro.", "venado49"]
acertijo07 = ["Si de investigar se trata con ella tienes que indagar, pues experta en toda clase de proyectos y muy sonriente ella es, la mamá del año busca ser.", "tlacuaches4"]
acertijo08 = ["Con mil y un ideas en su cabeza, como los rizos que tiene, experto en grandes temas y ávido de palabras como en bromas, es el más atento del evento, si de tentar al destino quieres, entrega tareas antes de que la unidad cierre.", "puercoespin7"]
acertijo09 = ["De los platillos más simples, hasta los más complejos, desde la e de ecología hasta la p de plato, de sistemas es este semestre.", "armadillo21"]
acertijo10 = ["Desde las canchas de basquet, hasta tu aula, establece horarios y revisa que todo marche en orden, su trabajo cumple con esmero, es el amigo del mero mero.", "colibri56"]
acertijo11 = ["De risa risueña, y de liso peinado, siempre está en clase cuando la hora llega, calcula muy ágil sus temas, ten cuidado o repruebas.", "tortuga29"]
acertijo12 = ["Con los electrones se lleva, de todas es la más experta, rizos y risas divertidas en su aula encuentras, prácticas y uno que otro toques de llevas.", "cocodrilo78"]
acertijo13 = ["Si de rangos se trata, se lleva la delantera, pues de todos, es el mero mero, en todos los eventos se encuentra, buscando siempre que sus alumnos crezcan.", "lechuza63"]
acertijo14 = ["Si de discursos se trata, se lleva la corona, del mejor amigo del Tec hablamos en persona, porque una sonrisa siempre manda, cuando entre los pasillos anda.", "monoaraña11"]
acertijo15 = ["Brilla como el oro, su cabello como tesoro, una sonrisa resplandeciente como su trabajo eficiente, anda en todos lados, buscando lo mejor para sus aliados, es la mera mera de todos los docentes.", "flamenco36"]

adivinanzas = [acertijo01, acertijo02, acertijo03, acertijo04, acertijo05, acertijo06, acertijo07, acertijo08, acertijo09, acertijo10, acertijo11, acertijo12, acertijo13, acertijo14, acertijo15]

#Listas para guardar el texto que ya salio y no vuelva a salir
acertijos_mostrados = []
frases_mostradas = []
preguntas_mostradas = []

preguntasA = obtener_datos()

ciclo = 1
num = [1, 2]

#Carga de imagenes pantalla de login

#Redimensionamos las imagenes
logo_campeche = Image.open("logoCampeche.png")
campeche_ancho = 250
campeche_alto = 60
imagen_campeche = logo_campeche.resize((campeche_ancho, campeche_alto))
imagen_campeche.save("campeche.png")

logoitse = Image.open("itselogo.png")
itse_ancho = 98
itse_alto = 80
imagen_itse = logoitse.resize((itse_ancho, itse_alto))
imagen_itse.save("logo itse.png")

logotecnm = Image.open("Logo-TecNM.png")
tcnmancho = 145
tcnmalto = 78
imagenlogotcnm = logotecnm.resize((tcnmancho, tcnmalto))
imagenlogotcnm.save("TECNM LOGO2.png")

logogob = Image.open("EDUCACION-LOGO.png")
gob_ancho = 250
gob_alto = 60
iamgenlogogob = logogob.resize((gob_ancho, gob_alto))
iamgenlogogob.save("logo gob.png")

jaguar = Image.open("jaguarsinfondo.png")
nuevo_ancho = 210
nuevo_alto = 200
imagen_redimensionada = jaguar.resize((nuevo_ancho, nuevo_alto))
imagen_redimensionada.save("imagen_jaguar_redi.png")

trofeo = Image.open("trophy.png")
imagen_trofeo = trofeo.resize((200, 200))
imagen_trofeo.save("Trofeo.png")

img_isc = Image.open("ISC.png")
isc = img_isc.resize((100,100))
isc.save("isc_redimenzionado.png")

#Insertamos las imagenes
jaguaredimensionado = ImageTk.PhotoImage(file="imagen_jaguar_redi.png")
etiqueta_imagen = tk.Label(login, image=jaguaredimensionado, background=color)
etiqueta_imagen.place(x=100, y=200)

campeche_redimensionado = ImageTk.PhotoImage(file="campeche.png")
etiqueta_campeche = tk.Label(login, image=campeche_redimensionado, background=color)
etiqueta_campeche.place(x=430, y=15)

itse_redimensionado = ImageTk.PhotoImage(file="logo itse.png")
etiqueta_itse = tk.Label(login, image=itse_redimensionado, background=color)
etiqueta_itse.place(x=690, y=5)

gob_redimensionado = ImageTk.PhotoImage(file="logo gob.png")
etiqueta_gob = tk.Label(login, image=gob_redimensionado, background=color)
etiqueta_gob.place(x=160, y=20)

tecnmredimensionado = ImageTk.PhotoImage(file="TECNM LOGO2.png")
etiqueta_tecnm = tk.Label(login, image=tecnmredimensionado, background=color)
etiqueta_tecnm.place(x=5, y=10)

imagen_logos = PhotoImage(file="logos_oficiales.png")

imagen_isc = PhotoImage(file="isc_redimenzionado.png")
etiqueta_isc = tk.Label(login, image=imagen_isc, background=color)
etiqueta_isc.place(x=680, y=400)

img_trofeo = PhotoImage(file="Trofeo.png")

#Creacion de las ventanas para las preguntas
def crear_preguntas():
    preguntas = tk.Tk()
    preguntas.geometry("800x500")
    preguntas.title("PREGUNTAS - DESAFIO JAGUAR")
    preguntas.configure(bg=color)

    linea = Label(preguntas, background=color_accesorios, height=1, width=500)
    linea.place(x=0, y=100)

    etiqueta_logos = Label(preguntas, image=imagen_logos)
    etiqueta_logos.place(x=1, y=3)

def crearVentanas():
    ventana_preguntas = tk.Toplevel() # Utilizar Toplevel en lugar de Tk
    ventana_preguntas.title("Preguntas - Desafio Jaguar")
    ventana_preguntas.geometry("800x500")
    ancho_pan = ventana_preguntas.winfo_screenwidth()
    alto_pan = ventana_preguntas.winfo_screenheight()
    ancho = int((ancho_pan - ventana_preguntas.winfo_reqwidth()) / 15)
    alto = int((alto_pan - ventana_preguntas.winfo_reqheight()) / 1.95)
    ventana_preguntas.geometry(f"+{alto}+{ancho}")
    ventana_preguntas.configure(bg=color)
    ventana_preguntas.resizable(width=False, height=False)

    # Linea divisora
    linea = Label(ventana_preguntas,background=color_accesorios, height=1, width=500)
    linea.place(x=0, y=100)

    #Colocación de las preguntas y respuestas

    style = ttk.Style()
    style.configure("Entrada.TLabel", foreground=color_letras, font=("Century Gothic", 12, "bold"))

    preguntas = obtener_pregunta_aleatoria()
    etiqutetapreg = ttk.Label(ventana_preguntas, text=preguntas["p"], style="Entrada.TLabel", wraplength=700, background=color)
    etiqutetapreg.place(x=50, y=150)

    opciones = [preguntas["r1"], preguntas["r2"], preguntas["r3"], preguntas["r4"]]
    random.shuffle(opciones)
    x = 140
    y = 250
    var = 0
    for opcion in opciones:
        boton = tk.Button(ventana_preguntas, text=opcion,wraplength=700, command=lambda opcion=opcion: verificar_respuesta(opcion, preguntas["rc"]))
        boton.place(x=50,y=y)
        y += 60

    def verificar_respuesta(opcion_seleccionada, respuesta_correcta):
        global ciclo
        if ciclo == 10: #Validacion en el desafio oficial: 10
            ventana_preguntas.destroy()
            ventana_terminado()
        else:
            if opcion_seleccionada == respuesta_correcta:
                ciclo += 1
                messagebox.showinfo("Desafio Jaguar", "¡Respuesta correcta!")
                print("¡Respuesta correcta!")
                ventana_preguntas.destroy()
                ventana_acertijo()
            else:
                messagebox.showinfo("Desafio Jaguar", "¡Respuesta incorrecta!")
                print("¡Respuesta incorrecta!")
                ventana_preguntas.destroy()
                abrir_ventana_preguntas()
    # Insertamos las imágenes
    etiqueta_logos = tk.Label(ventana_preguntas, image=imagen_logos, background=color)
    etiqueta_logos.place(x=0, y=3)

    def terminar_desafio():
        respuesta = messagebox.askyesno("¿Cómo qué vas a salir?",
                                        "Oraaaaaa, que te estas descalificando si le das en confirmar, ¡regresa al desafio y no vayas a desertar Jaguar!")
        if respuesta:
            login.quit()
            ventana_preguntas.destroy()

    ventana_preguntas.protocol("WM_DELETE_WINDOW", terminar_desafio)

def ventana_acertijo():
    ventana_acer = tk.Toplevel()
    ventana_acer.title("Acertijos - Desafio Jaguar")
    ventana_acer.geometry("800x500")
    ancho_pan = ventana_acer.winfo_screenwidth()  # Esto es para
    alto_pan = ventana_acer.winfo_screenheight()  # pocisionar la ventana
    ancho = int((ancho_pan - ventana_acer.winfo_reqwidth()) / 15)  # en la pantalla
    alto = int((alto_pan - ventana_acer.winfo_reqheight()) / 1.95)
    ventana_acer.geometry(f"+{alto}+{ancho}")
    ventana_acer.configure(bg=color)
    ventana_acer.resizable(width=False, height=False)

    # Imagenes de la ventana
    etiqueta_logos = tk.Label(ventana_acer, image=imagen_logos, background=color)
    etiqueta_logos.place(x=0, y=3)

    #Accesorios de la ventana
    style = ttk.Style()
    style.configure("Entrada.TLabel", foreground=color_letras, font=("Century Gothic", 12, "bold"))

    # Linea divisora
    linea = Label(ventana_acer,background=color_accesorios, height=1, width=500)
    linea.place(x=0, y=100)

    ingresarContra = tk.Entry(ventana_acer, bg=color_entradas_texto)
    ingresarContra.place(x=120, y=250)

    acertijo = obtener_acertijo_aleatorio()

    etiqueta_acertijo = ttk.Label(ventana_acer, text=acertijo[0],style="Entrada.TLabel" , background=color, wraplength=700)
    etiqueta_acertijo.place(x=50, y=150)

    etiqueta_frase = ttk.Label(
        ventana_acer,
        text=obtener_frase(),
        style="Entrada.TLabel",
        background=color,
        wraplength=400
    )
    etiqueta_frase.place(x=20, y=405)

    linea2 = tk.Label(ventana_acer, background=color_accesorios, height=1, width=500)
    linea2.place(x=0, y=380)

    print(acertijo[1])
    confirmar = tk.Button(ventana_acer, text="Desbloquear siguiente pregunta", wraplength=200,background=color_accesorios,command=lambda: validar_contraseña_acertijo(acertijo[1]))
    confirmar.configure(fg=color)
    confirmar.place(x=300, y=250)

    def validar_contraseña_acertijo(contraseña_correcta):
        contraxusuario = ingresarContra.get()
        if not contraxusuario:
            messagebox.showerror("Acertijos - Desafio Jaguar","El campo esta vacio, ingresa la contraseña por favor")
        else:
            if contraseña_correcta == contraxusuario:
                messagebox.showinfo("Acertijos - Desafio Jaguar","FELICIDADES, PREGUNTA DESBLOQUEADA, PREPARATE PARA LA SIGUIENTE RONDA")
                ventana_acer.destroy()
                abrir_ventana_preguntas()
            else:
                messagebox.showerror("Acertijos - Desafio Jaguar", "Contraseña incorrecta, intenta de nuevo")

    def terminar_desafio():
        respuesta = messagebox.askyesno("¿Cómo qué vas a salir?",
                                        "Oraaaaaa, que te estas descalificando si le das en confirmar, regresa al desafio y no vayas a desertar Jaguar")
        if respuesta:
            login.quit()
            ventana_acer.destroy()

    ventana_acer.protocol("WM_DELETE_WINDOW", terminar_desafio)

def ventana_terminado():
    ventana_game_over = tk.Toplevel()
    ventana_game_over.title("Game Over - Desafio Jaguar")
    ventana_game_over.geometry("800x500")
    ancho_pan = ventana_game_over.winfo_screenwidth()  # Esto es para
    alto_pan = ventana_game_over.winfo_screenheight()  # pocisionar la ventana
    ancho = int((ancho_pan - ventana_game_over.winfo_reqwidth()) / 15)  # en la pantalla
    alto = int((alto_pan - ventana_game_over.winfo_reqheight()) / 2)
    ventana_game_over.geometry(f"+{alto}+{ancho}")
    ventana_game_over.configure(bg=color)
    ventana_game_over.resizable(width=False, height=False)

    #Tipos de estilos para el texto
    estilo = ttk.Style()
    estilo.configure("Indicacion.TLabel", foreground=color_letras, font=("Calibri", 14, "bold"))

    estilo = ttk.Style()
    estilo.configure("Felicidades.TLabel", foreground=color_letras, font=("Gabriola", 18, "bold"))

    estilo_palabra = ttk.Style()
    estilo_palabra.configure(
        "Palabra.TLabel",
        foreground=color_accesorios,
        font=("Arial",
              20,
              "bold"
              )
    )

    # Lineas divisoras
    linea1 = tk.Label(ventana_game_over, background=color_accesorios, height=1, width=500)
    linea1.place(x=0, y=100)

    linea2 = tk.Label(ventana_game_over, background=color_accesorios, height=1, width=500)
    linea2.place(x=0, y=380)

    #Etiquetas de texto

    etiqueta_indicacion = ttk.Label(
        ventana_game_over,
        text="Palabra secreta para confirmar su participación y conclusión en el Desafio Jaguar: ",
        style="Indicacion.TLabel",
        wraplength=300,
        background=color
    )
    etiqueta_indicacion.place(
        x=20,
        y=405
    )

    etiqueta_palabra = ttk.Label(
        ventana_game_over,
        text="",
        style="Palabra.TLabel",
        background=color_entradas_texto
    )
    etiqueta_palabra.place(
        x=400,
        y=425
    )

    etiqueta_game_over = ttk.Label(
        ventana_game_over,
        wraplength=220,
        text="FELICIDADES HAS TERMINADO EL DESAFIO JAGUAR",
        style="Felicidades.TLabel",
        anchor="center",
        justify="center"
    )
    etiqueta_game_over.place(
        x=300,
        y=170
    )
    etiqueta_game_over.configure(background=color)

    #Boton

    btncerrar = tk.Button(ventana_game_over, text="SALIR DEL DESAFIO", command= lambda : terminar_desafio())
    btncerrar.configure(
        background=color_accesorios,
        fg=color
    )
    btncerrar.place(x=360, y=350)

    #Imagenes
    etiqueta_isc = tk.Label(ventana_game_over, image=imagen_isc, background=color)
    etiqueta_isc.place(x=680, y=400)

    etiqueta_logos = tk.Label(ventana_game_over, image=imagen_logos, background=color)
    etiqueta_logos.place(x=0, y=3)

    etiqueta_trofeo = tk.Label(ventana_game_over, image=img_trofeo, background=color)
    etiqueta_trofeo.place(x=550, y=150)

    etiqueta_jaguar = tk.Label(ventana_game_over, image=jaguaredimensionado, background=color)
    etiqueta_jaguar.place(x=30, y=150)

    def imprimir_palabra():
        global seleccion
        palabras = [
            "Perro",
            "Unicornio",
            "Leon",
            "Jaguar",
            "Oso",
            "Toro",
            "Pez",
            "Gato",
            "Cafe",
            "Ballena",
            "Delfin",
            "Tiburon"
        ]
        if seleccion:
            indice = int(seleccion) - 1
            if 0 <= indice < len(palabras):
                frase = palabras[indice]
                etiqueta_palabra.config(text=frase)

    #Funcion para terminar el programa
    def terminar_desafio():
        # Mostrar cuadro de diálogo de confirmación
        respuesta = messagebox.askyesno("¿Seguro que desea salir?", "Antes de salir asegurate de haber escrito o memorizado la palabra secreta, ¡Recuerda que sin ella no será posible validar tu participación en el desafio!")
        if respuesta:
            login.quit()
            ventana_game_over.destroy()

    imprimir_palabra()
    ventana_game_over.protocol("WM_DELETE_WINDOW", terminar_desafio)

def obtener_seleccion():
    opcion_seleccionada = combo.get()
    print("Opción seleccionada:", opcion_seleccionada)

def obtener_frase():
    frase = random.choice(frases)

    while frase in frases_mostradas:
        frase = random.choice(frases)

    frases_mostradas.append(frases)
    return frase

def obtener_acertijo_aleatorio():
    acertijo_ale = random.choice(adivinanzas)

    while acertijo_ale in acertijos_mostrados:
        acertijo_ale = random.choice(adivinanzas)

    acertijos_mostrados.append(acertijo_ale)
    return acertijo_ale

def obtener_pregunta_aleatoria():
    preguntas = random.sample(preguntasA, 1)[0]

    # Verificar si la pregunta ya ha sido mostrada
    while preguntas in preguntas_mostradas:
        preguntas = random.sample(preguntasA, 1)[0]

    # Agregar la pregunta a la lista de preguntas mostradas
    preguntas_mostradas.append(preguntas)

    return random.choice(preguntas)

#Funciones para la ventana principal

def abrir_ventana_preguntas():
    crearVentanas()

def ingresard():
    global seleccion
    seleccion = combo.get()
    texto = obtener_pass.get()

    if not texto:
        messagebox.showerror("Desafio Jaguar","Ingrese la contraseña por favor")
    elif not seleccion:
        messagebox.showerror("Desafio Jaguar", "Escoja su equipo por favor")
    else:
        for palabra in contraseñas:
            if texto == palabra:
                bool = True
                break
            else:
                bool = False
        if bool:
            messagebox.showinfo("Desafio jaguar", "Acceso concedido, el desafio comenzará ahora.")
            btningresar.configure(state=tk.DISABLED)
            abrir_ventana_preguntas()
        else:
            messagebox.showerror("Desafio jaguar", "Contraseña invalida, Ingrese una correcta")

#Botones de la ventana
btningresar = tk.Button(login, text="Comenzar Desafio",bg=color_accesorios ,command=ingresard)
btningresar.configure(fg=color)
btningresar.place(x=480, y=350)

opciones = list(range(1, 13))  # Números del 1 al 12
combo = ttk.Combobox(login, values=opciones, background=color_accesorios)
combo.configure(foreground=color_accesorios)
combo.place(x=450, y=230)

#Linea divisora
linea = tk.Label(background=color_accesorios, height=1, width=500)
linea.place(x=0, y=100)

#Etiquetas de la ventana
obtener_pass = tk.Entry(login, bg=color_entradas_texto)
obtener_pass.place(x=470, y=300)

bienvenida = ttk.Label(login,text="BIENVENIDO AL DESAFIO JAGUAR", style="Pregunta.TLabel")
bienvenida.place(x=70, y=150)
bienvenida.configure(background=color)

indicacion = ttk.Label(login, text="Por favor selecciona el numero del equipo e ingresa la contraseña", style="Pregunta.TLabel" ,wraplength=300, anchor="center", justify="center")
indicacion.place(x=400, y=150)
indicacion.configure(background=color)

#Iniciar la ventana
login.mainloop()
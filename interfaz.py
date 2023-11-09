import tkinter as tk
from PIL import Image, ImageTk


def interfaz_principal():   
    # Crear una instancia de la clase Tk (ventana principal)
    ventana = tk.Tk()
    ventana.geometry("1200x700")
    ventana.title("practical diet")
    # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
    imagen_fondo = Image.open(r"imagenes\fondo_inicio.png")  
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
    fondo_label = tk.Label(ventana, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def cambiar_ventana():
        ventana.withdraw()  # Oculta la ventana actual
        escritorio = tk.Toplevel()  # Crea una nueva ventana
        escritorio.geometry("900x700")
        escritorio.title("practical diet")
        # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
        imag_fondo_escrit = Image.open(r"imagenes\fondo_escritorio.png")  
        imag_fondo_escrit = ImageTk.PhotoImage(imag_fondo_escrit)
        fondo_escri_label = tk.Label(escritorio, image=imag_fondo_escrit)
        fondo_escri_label.place(x=0, y=0, relwidth=1, relheight=1)

        #mensaje de saludo
        etiqueta_saludo=tk.Label(escritorio,text="",font=("Arial",24), foreground="blue")
        etiqueta_saludo.place(x=100,y=50)
        nombre= entrada_nombre.get()
        etiqueta_saludo.config(text=f"¡BIENVENIDO {nombre.upper()}!")
        
        
        def boton1_fun():
        
            escritorio.withdraw()
            vent_calorias = tk.Toplevel()  # Crea una nueva ventana
            vent_calorias.geometry("900x700")
            vent_calorias.title("calorias")
            
            def regresar():
                vent_calorias.withdraw()  # Oculta la ventana actual
                escritorio.deiconify()  # Restaura la ventana anterior
            # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
            imag_fondo_caloria = Image.open(r"imagenes\fondo_calorias.png")
            imag_fondo_caloria= ImageTk.PhotoImage(imag_fondo_caloria)
            fondo_caloria_label = tk.Label(vent_calorias, image=imag_fondo_caloria)
            fondo_caloria_label.place(x=0, y=0, relwidth=1, relheight=1)
            #peso
            eti_intr_peso=tk.Label(vent_calorias,text="INGRESE PESO",font=("Arial",24),bg="blue")
            eti_intr_peso.place(x=100,y=100)
            #ingreso de peso
            entrada_peso=tk.Entry(vent_calorias,font=("Arial",24))
            entrada_peso.place(x=100,y=200,height=30,width=200)
            #pregunta su sexo
            eti_intr_sexo=tk.Label(vent_calorias, text='INGRESE SEXO', font=("Arial",24), bg="blue")
            eti_intr_sexo.place(x=100,y=300)
            #boton masculino
            boton_masculino=tk.Button(vent_calorias,text="MACULINO",font=("Arial",24),foreground="blue",borderwidth=10)
            boton_masculino.place(x=100,y=400)
            #boton femenino
            boton_femenino=tk.Button(vent_calorias,text="FEMENINO",font=("Arial",24),foreground="red",borderwidth=10)
            boton_femenino.place(x=350,y=400)
            
            #boton regresar
            boton_regresar=tk.Button(vent_calorias,text="REGRESAR",font=("Arial",24),background="red",borderwidth=10,command=regresar)
            boton_regresar.place(x=600,y=600)
            vent_calorias.mainloop()
            
        def boton2_fun():
            escritorio.withdraw()
            vent_IMC = tk.Toplevel()  # Crea una nueva ventana
            vent_IMC.geometry("900x700")
            vent_IMC.title("IMC")
            
            def regresar():
                vent_IMC.withdraw()  # Oculta la ventana actual
                escritorio.deiconify()  # Restaura la ventana anterior
            # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
            imag_fondo_IMC = Image.open(r"imagenes\fondo_IMC.png")
            imag_fondo_IMC= ImageTk.PhotoImage(imag_fondo_IMC)
            fondo_IMC_label = tk.Label(vent_IMC, image=imag_fondo_IMC)
            fondo_IMC_label.place(x=0, y=0, relwidth=1, relheight=1)
            #PESO
            eti_intr_peso=tk.Label(vent_IMC,text="INGRESE PESO",font=("Arial",24),foreground="blue")
            eti_intr_peso.place(x=100,y=100)
            #ingreso de peso
            entrada_peso=tk.Entry(vent_IMC,font=("Arial",24))
            entrada_peso.place(x=100,y=200,height=30,width=200)
            #altura
            eti_intr_altura=tk.Label(vent_IMC,text="INGRESE ALTURA",font=("Arial",24),foreground="Blue")
            eti_intr_altura.place(x=500,y=100)
            #ingreso de altura
            entrada_altura=tk.Entry(vent_IMC,font=("Arial",24))
            entrada_altura.place(x=500,y=200,height=30,width=200)
            boton_aceptar=tk.Button(vent_IMC,text="ACEPTAR",font=("Arial",24),borderwidth=8)
            boton_aceptar.place(x=200,y=400)
            
            #boton regresar
            boton_regresar=tk.Button(vent_IMC,text="REGRESAR",font=("Arial",24),background="red",borderwidth=8,command=regresar)
            boton_regresar.place(x=400,y=400)
            
            
            vent_IMC.mainloop()
        
        def boton3_fun():

            escritorio.withdraw()  # Oculta la ventana actual
            vent_aliment = tk.Toplevel()  # Crea una nueva ventana
            vent_aliment.geometry("900x700")
            vent_aliment.title("alimentos")
            
            def regresar():
                vent_aliment.withdraw()  # Oculta la ventana actual
                escritorio.deiconify()  # Restaura la ventana anterior
        
            # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
            imag_fondo_aliment = Image.open(r"imagenes\fondo_alimentos.png")  
            imag_fondo_aliment = ImageTk.PhotoImage(imag_fondo_aliment)
            fondo_aliment_label = tk.Label(vent_aliment, image=imag_fondo_aliment)
            fondo_aliment_label.place(x=0, y=0, relwidth=1, relheight=1)
            

            #alimento
            etiq_intr_aliment=tk.Label(vent_aliment,text="INGRESE ALIMENTO",font=("Arial",24))
            etiq_intr_aliment.place(x=100,y=100)
            #carga de alimento
            entrada_aliement=tk.Entry(vent_aliment,font=("Arial",24))
            entrada_aliement.place(x=100,y=200,width=500)
            #boton buscar
            boton_buscar=tk.Button(vent_aliment,text="BUSCAR",font=("Arial",22),borderwidth=8)
            boton_buscar.place(x=625,y=190)
            #boton regresar
            boton_regresar=tk.Button(vent_aliment,text="REGRESAR",font=("Arial",24),background="red",borderwidth=10,command=regresar)
            boton_regresar.place(x=600,y=600)
            
            #muestra de propiedades
            #HDC
            etiq_HDC= tk.Label(vent_aliment,text="CARBOHIDRATOS:",font=("Arial",20),bg="yellow")
            etiq_HDC.place(x=100,y=300)
            #PROTEINA
            etiq_protein= tk.Label(vent_aliment,text="PROTEINA:",font=("Arial",20),bg="yellow")
            etiq_protein.place(x=100,y=350)
            #GRASAS
            etiq_grasa= tk.Label(vent_aliment,text="GRASAS:",font=("Arial",20),bg="yellow")
            etiq_grasa.place(x=100,y=400)
            #CALSIO
            etiq_CALSIO= tk.Label(vent_aliment,text="CALSIO:",font=("Arial",20),bg="yellow")
            etiq_CALSIO.place(x=100,y=450)
            #HIERRO
            etiq_HIERRO= tk.Label(vent_aliment,text="HIERRO:",font=("Arial",20),bg="yellow")
            etiq_HIERRO.place(x=100,y=500)
            #VITAMINA A
            etiq_VIT_A= tk.Label(vent_aliment,text="VITAMINA A:",font=("Arial",20),bg="yellow")
            etiq_VIT_A.place(x=100,y=550)
            #VITAMINA C
            etiq_VIT_C= tk.Label(vent_aliment,text="VITAMINA C:",font=("Arial",20),bg="yellow")
            etiq_VIT_C.place(x=100,y=600)
            
            vent_aliment.mainloop()
        
        def salir_boton():
            escritorio.destroy()
        #botones
        button_opcion1= tk.Button(escritorio,text="CALORIAS",font=("Arial",24),bg="cadetblue",command=boton1_fun)
        button_opcion1.place(x=50,y=200)
        
        button_opcion2= tk.Button(escritorio,text="IMC",font=("Arial",24),bg="cadetblue",command=boton2_fun)
        button_opcion2.place(x=50,y=300)
        
        button_opcion3= tk.Button(escritorio,text="ALIMENTOS",font=("Arial",24),bg="cadetblue",command=boton3_fun)
        button_opcion3.place(x=50,y=400)

        button_SALIR= tk.Button(escritorio,text="SALIR",font=("Arial",24),bg="yellow",command=salir_boton)    
        button_SALIR.place(x=600,y=600)
        
        escritorio.mainloop()
    #botton enter
    button_enter = tk.Button(ventana, text="ENTRAR", font=("Arial", 24), background="green",command=cambiar_ventana)
    button_enter.place(x=200,y=600)

    etiqueta_instrucciones = tk.Label(ventana, text="Ingresa tu nombre:", font=("Arial",20),bg="yellow")
    etiqueta_instrucciones.place(x=50,y=100)
    # Entry para ingresar el nombre
    entrada_nombre = tk.Entry(ventana,font=("Arial",20))
    entrada_nombre.place(x=300,y=100, height=40, width=400)


        
    # Iniciar el bucle principal de la aplicación
    ventana.mainloop()

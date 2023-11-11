import tkinter as tk
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
from funciones import clasif_edad_hom, clasif_edad_muj,calcular_imc,clasificar_imc,propiedades

def interfaz_principal():
    # Crear una ventana
    ventana = tk.Tk()
    ventana.geometry("1200x700")
    ventana.resizable(False, False)
    ventana.title("practical diet")
    #creo icono
    ventana.iconbitmap(r"imagenes\icon.ico")

    # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
    imagen_fondo = Image.open(r"imagenes\fondo_inicio.png")  
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
    fondo_label = tk.Label(ventana, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    def abrir():
        def cambiar_ventana():
            ventana.withdraw()  # Oculta la ventana actual
            escritorio = tk.Toplevel()  # Crea una nueva ventana
            escritorio.geometry("900x700")
            escritorio.resizable(False, False)
            escritorio.title("practical diet")
            escritorio.iconbitmap(r"imagenes\icon.ico")
            # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
            imag_fondo_escrit = Image.open(r"imagenes\fondo_escritorio.png")  
            imag_fondo_escrit = ImageTk.PhotoImage(imag_fondo_escrit)
            fondo_escri_label = tk.Label(escritorio, image=imag_fondo_escrit)
            fondo_escri_label.place(x=0, y=0, relwidth=1, relheight=1)

            #mensaje de saludo
            etiqueta_saludo=tk.Label(escritorio,text="",font=("Arial",24))
            etiqueta_saludo.place(x=350,y=300)
            nombre= entrada_nombre.get()
            etiqueta_saludo.config(text=f"¡BIENVENIDO {nombre.upper()}!")
            
            
            def boton1_fun():
            
                escritorio.withdraw()
                vent_calorias = tk.Toplevel()  # Crea una nueva ventana
                vent_calorias.geometry("900x700")
                vent_calorias.resizable(False, False)
                vent_calorias.title("calorias")
                vent_calorias.iconbitmap(r"imagenes\icon.ico")
                def calcular_tmb(edad,peso,boton):
                    if boton=="masculino":
                        edad = int(edad)
                        peso = float(peso)
                        resultado = clasif_edad_hom(edad,peso)
                        etiq_mostr_resul.config(text=f"{resultado:.2f} kcal/día")
        
                    else:
                        edad = int(edad)
                        peso = float(peso)
                        resultado = clasif_edad_muj(edad,peso)
                        etiq_mostr_resul.config(text=f"{resultado:.2f} kcal/día")
                
                        
                def regresar():
                    vent_calorias.withdraw()  # Oculta la ventana actual
                    escritorio.deiconify()  # Restaura la ventana anterior
                # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
                imag_fondo_caloria = Image.open(r"imagenes\fondo_calorias.png")
                imag_fondo_caloria= ImageTk.PhotoImage(imag_fondo_caloria)
                fondo_caloria_label = tk.Label(vent_calorias, image=imag_fondo_caloria)
                fondo_caloria_label.place(x=0, y=0, relwidth=1, relheight=1)
                #peso
                eti_intr_peso=tk.Label(vent_calorias,text="INGRESE PESO(kg):",font=("Arial",24),bg="blue")
                eti_intr_peso.place(x=100,y=100)
                # Crear una variable de control 
                peso = tk.DoubleVar()
                #ingreso de peso
                entrada_peso=tk.Entry(vent_calorias,font=("Arial",24),textvariable=peso)
                entrada_peso.place(x=100,y=150,height=30,width=200)

                #edad
                eti_intr_edad=tk.Label(vent_calorias,text="EDAD:",font=("Arial",24),bg="blue")
                eti_intr_edad.place(x=100,y=250)
                # Crear una variable de control 
                edad = tk.DoubleVar()
                #ingreso edad
                entrada_edad=tk.Entry(vent_calorias,font=("Arial",24),textvariable=edad)
                entrada_edad.place(x=100,y=300)
                
                
            
                #pregunta su sexo
                eti_intr_sexo=tk.Label(vent_calorias, text='INGRESE SEXO:', font=("Arial",24), bg="blue")
                eti_intr_sexo.place(x=100,y=400)
                #boton masculino
                boton_masculino=tk.Button(vent_calorias,text="MACULINO",font=("Arial",24),foreground="blue",borderwidth=10,command=lambda:calcular_tmb(edad.get(),peso.get(),"masculino"))
                boton_masculino.place(x=100,y=450)
                #boton femenino
                boton_femenino=tk.Button(vent_calorias,text="FEMENINO",font=("Arial",24),foreground="red",borderwidth=10,command=lambda:calcular_tmb(edad.get(),peso.get(),"femenino"))
                boton_femenino.place(x=350,y=450)
                #resultado
                etiq_resul_cal=tk.Label(vent_calorias,text="CALORIAS",font=("Arial",24),foreground="blue")
                etiq_resul_cal.place(x=550,y=250)
                #mostrar resultado
                etiq_mostr_resul=tk.Label(vent_calorias,text="",font=("Arial",24))
                etiq_mostr_resul.place(x=550,y=300,width=300)
                #boton regresar
                boton_regresar=tk.Button(vent_calorias,text="REGRESAR",font=("Arial",24),background="red",borderwidth=10,command=regresar)
                boton_regresar.place(x=600,y=600)
                vent_calorias.mainloop()
                
            def boton2_fun():
                escritorio.withdraw()
                vent_IMC = tk.Toplevel()  # Crea una nueva ventana
                vent_IMC.geometry("900x700")
                vent_IMC.resizable(False, False)
                vent_IMC.title("IMC")
                vent_IMC.iconbitmap(r"imagenes\icon.ico")
                def mostrar(peso,altura):
                    peso= float(peso)
                    altura= float(altura)
                    imc= calcular_imc(peso,altura)
                    mostr_resul.config(text=f"IMC:{imc}")
                    cond= clasificar_imc(imc)
                    mostr_cond.config(text=f"condicion: {cond}")
            
                def regresar():
                    vent_IMC.withdraw()  # Oculta la ventana actual
                    escritorio.deiconify()  # Restaura la ventana anterior
                # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
                imag_fondo_IMC = Image.open(r"imagenes\fondo_IMC.png")
                imag_fondo_IMC= ImageTk.PhotoImage(imag_fondo_IMC)
                fondo_IMC_label = tk.Label(vent_IMC, image=imag_fondo_IMC)
                fondo_IMC_label.place(x=0, y=0, relwidth=1, relheight=1)
                #PESO
                eti_intr_peso=tk.Label(vent_IMC,text="INGRESE PESO (kg)",font=("Arial",24),foreground="blue")
                eti_intr_peso.place(x=100,y=100)
                peso=tk.DoubleVar()
                #ingreso de peso
                entrada_peso=tk.Entry(vent_IMC,font=("Arial",24),textvariable=peso)
                entrada_peso.place(x=150,y=200,height=30,width=200)
                #altura
                eti_intr_altura=tk.Label(vent_IMC,text="INGRESE ALTUR (cm)",font=("Arial",24),foreground="Blue")
                eti_intr_altura.place(x=500,y=100)
                #control de variable
                altura= tk.DoubleVar()
                #ingreso de altura
                entrada_altura=tk.Entry(vent_IMC,font=("Arial",24),textvariable=altura)
                entrada_altura.place(x=550,y=200,height=30,width=200)
                #mostrar resultado imc
                mostr_resul=tk.Label(vent_IMC,text="IMC:",font=("Arial",24))
                mostr_resul.place(x=30,y=300,width=400)
                #mostrar condicion
                mostr_cond=tk.Label(vent_IMC,text="condicion:",font=("Arial",24))
                mostr_cond.place(x=470,y=300,width=400)
                #boton aceptar
                boton_aceptar=tk.Button(vent_IMC,text="ACEPTAR",font=("Arial",24),borderwidth=8,command=lambda:mostrar(peso.get(),altura.get()))
                boton_aceptar.place(x=250,y=400)
    
                #boton regresar
                boton_regresar=tk.Button(vent_IMC,text="REGRESAR",font=("Arial",24),background="red",borderwidth=8,command=regresar)
                boton_regresar.place(x=450,y=400)
                
                
                vent_IMC.mainloop()
            
            def boton3_fun():

                escritorio.withdraw()  # Oculta la ventana actual
                vent_aliment = tk.Toplevel()  # Crea una nueva ventana
                vent_aliment.geometry("900x700")
                vent_aliment.resizable(False, False)
                vent_aliment.title("alimentos")
                vent_aliment.iconbitmap(r"imagenes\icon.ico")
                
                def regresar():
                    vent_aliment.withdraw()  # Oculta la ventana actual
                    escritorio.deiconify()  # Restaura la ventana anterior
                def mostrar_aliment(aliment,cant):
                    float(cant)
                    list_alim=propiedades(aliment,cant)
                    for i in range(7):
                        if i==0:
                            etiq_mostr_HDC.config(text=f"{list_alim[i]} g")
                        elif i==1:
                            etiq_mostr_protein.config(text=f"{list_alim[i]} g")
                        elif i==2:
                            etiq_mostr_grasa.config(text=f"{list_alim[i]} g")
                        elif i==3:
                            etiq_mostr_CALCIO.config(text=f"{list_alim[i]} g")
                        elif i==4:
                            etiq_mostr_HIERRO.config(text=f"{list_alim[i]} g")
                        elif i==5:
                            etiq_mostr_VIT_A.config(text=f"{list_alim[i]} g")
                        elif i==6:
                            etiq_mostr_VIT_C.config(text=f"{list_alim[i]} g")
                
                # Cargar una imagen y Crear un widget Label para mostrar la imagen de fondo
                imag_fondo_aliment = Image.open(r"imagenes\fondo_alimentos.png")  
                imag_fondo_aliment = ImageTk.PhotoImage(imag_fondo_aliment)
                fondo_aliment_label = tk.Label(vent_aliment, image=imag_fondo_aliment)
                fondo_aliment_label.place(x=0, y=0, relwidth=1, relheight=1)
                
                # Crear una lista de opciones
                Alimentos= ("Leche","Leche parcialmente descremada","Leche descremada","Yogur","Queso 1","Queso 2","Queso 3","Queso 4","Queso unt. Descremado","Queso blando descremado",
                            "Huevo","Carne vaca","Carne cerdo","Carne pollo","Carne pescado","Jamon","Veg A","Veg B","Veg C","Frutas frescas","Frutas desecadas","Frutas secas",
                            "Cereales","Legumbres","Pan frances","Bollo","Galletas","Azucar","Dulces","Aceite","Manteca","Crema leche liviana","Crema leche espesa")

                #alimento
                etiq_intr_aliment=tk.Label(vent_aliment,text="INGRESE ALIMENTO",font=("Arial",24))
                etiq_intr_aliment.place(x=80,y=50)
                #carga de alimento para mostrar las opciones
            
                combo_aliment = ttk.Combobox(vent_aliment, values=Alimentos, font=("Arial",20))
                combo_aliment.place(x=80,y=100)
            
                #cantidad
                etiq_intr_cant=tk.Label(vent_aliment,text="INGRESE CANTIDAD (g)",font=("Arial",24))
                etiq_intr_cant.place(x=80,y=150)
                #control de variable
                cant=tk.DoubleVar()
                #carga de cantidad
                entrada_cant=tk.Entry(vent_aliment,font=("Arial",20),textvariable=cant)
                entrada_cant.place(x=80,y=200)
                #boton buscar
                boton_buscar=tk.Button(vent_aliment,text="BUSCAR",font=("Arial",22),borderwidth=8,command=lambda:mostrar_aliment(combo_aliment.get(),cant.get()))
                boton_buscar.place(x=600,y=100)
                #boton regresar
                boton_regresar=tk.Button(vent_aliment,text="REGRESAR",font=("Arial",24),background="red",borderwidth=10,command=regresar)
                boton_regresar.place(x=660,y=600)
                
                #muestra de propiedades
                #HDC
                etiq_HDC= tk.Label(vent_aliment,text="CARBOHIDRATOS:",font=("Arial",20),bg="yellow")
                etiq_HDC.place(x=80,y=300)
                etiq_mostr_HDC= tk.Label(vent_aliment,text="",font=("Arial",20))
                etiq_mostr_HDC.place(x=350,y=300,width=250)
                #PROTEINA
                etiq_protein= tk.Label(vent_aliment,text="PROTEINA:",font=("Arial",20),bg="yellow")
                etiq_protein.place(x=80,y=350)
                etiq_mostr_protein= tk.Label(vent_aliment,text="",font=("Arial",20))
                etiq_mostr_protein.place(x=350,y=350,width=250)
                #GRASAS
                etiq_grasa= tk.Label(vent_aliment,text="GRASAS:",font=("Arial",20),bg="yellow")
                etiq_grasa.place(x=80,y=400)
                etiq_mostr_grasa= tk.Label(vent_aliment,text="",font=("Arial",20))
                etiq_mostr_grasa.place(x=350,y=400,width=250)
                #CALSIO
                etiq_CALCIO= tk.Label(vent_aliment,text="CALCIO:",font=("Arial",20),bg="yellow")
                etiq_CALCIO.place(x=80,y=450)
                etiq_mostr_CALCIO= tk.Label(vent_aliment,text="",font=("Arial",20))
                etiq_mostr_CALCIO.place(x=350,y=450,width=250)
                #HIERRO
                etiq_HIERRO= tk.Label(vent_aliment,text="HIERRO:",font=("Arial",20),bg="yellow")
                etiq_HIERRO.place(x=80,y=500)
                etiq_mostr_HIERRO= tk.Label(vent_aliment,text="",font=("Arial",20))
                etiq_mostr_HIERRO.place(x=350,y=500,width=250)
                #VITAMINA A
                etiq_VIT_A= tk.Label(vent_aliment,text="VITAMINA A:",font=("Arial",20),bg="yellow")
                etiq_VIT_A.place(x=80,y=550)
                etiq_mostr_VIT_A= tk.Label(vent_aliment,text="",font=("Arial",20))
                etiq_mostr_VIT_A.place(x=350,y=550,width=250)
                #VITAMINA C
                etiq_VIT_C= tk.Label(vent_aliment,text="VITAMINA C:",font=("Arial",20),bg="yellow")
                etiq_VIT_C.place(x=80,y=600)
                etiq_mostr_VIT_C= tk.Label(vent_aliment,text="",font=("Arial",20))
                etiq_mostr_VIT_C.place(x=350,y=600,width=250)
                
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
        if entrada_nombre.get()!="":
            cambiar_ventana()
        else:
            messagebox.showinfo("Aviso", "ingrese un nombre, por favor")
    #botton enter
    button_enter = tk.Button(ventana, text="ENTRAR", font=("Arial", 24), background="green",command=abrir)
    button_enter.place(x=200,y=600)

    etiqueta_instr_nombre = tk.Label(ventana, text="Ingresa tu nombre:", font=("Arial",20),bg="yellow")
    etiqueta_instr_nombre.place(x=50,y=400)
    # Entry para ingresar el nombre
    entrada_nombre = tk.Entry(ventana,font=("Arial",20))
    entrada_nombre.place(x=300,y=400, height=40, width=400)


        
    # Iniciar el bucle principal de la aplicación
    ventana.mainloop()

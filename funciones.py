
#UN DICCIONARIO con todos los alimentos y sus propiedades
dicc_alim= {'Leche':(5,3,3,120,0.1,295,1),'Leche parcialmente descremada':(4.5,4.1,1.5,157,0,75,0),
'Leche descremada':(4.2,3,0.1,142,0,300,0),'Yogur':(4.5,4,3,136,0.1,160,0
),'Queso 1':(4,14,12,75,0.1,1300,0),'Queso 2':(2.3,20,20,600,0,2000,0),
'Queso 3':(0,25,28,890,0,3600,0),'Queso 4':(0,33,29,1100,0,1060,0),
'Queso unt. descremado':(2.7,13,12,933.3,0,989,0),'Queso blando descremado':(0,32,4,533.3,0,0,0),
'Huevo':(0,12,12,54,2.5,1180,0),'Carne vaca':(0,20,10,4,4,30,0),'Carne cerdo':(0,17,21,8,2,0,0),
'Carne pollo':(0,20,6,10,1.7,60,0),'Carne pescado':(0,18,6,0,0.7,0,0),
'Jamon':(0,20,15,15,7.5,0,0),'Veg a':(5,1,0,60,2.5,2324,30),
'Veg b':(10,1.5,0,40,1.4,850,16),'Veg c':(20,2,0,20,1,146,21),
'Frutas frescas':(15,1,0,18,0.4,990,20),'Frutas desecadas':(64,3,1,78,3.3,164,7.8),
'Frutas secas':(26,12,60,131,3.8,19,1.5),'Cereales':(70,10,3,27,2.3,0,0),
'Legumbres':(55,22,3,117,7,44,1.8),'Pan frances':(60,10,0,22,1.1,0,0),
'Bollo':(50,7,23,99,1.5,0,0),'Galletas':(70,11,12,0,0,0,0),
'Azucar':(100,0,0,0,0,0,0),'Dulces':(70,1.5,0,36,0.3,17,5),
'Aceite':(0,0,100,0,0,0,0),'Manteca':(0,0.5,84,15,0.2,2240,0),
'Crema leche liviana':(4,2.9,0,97,0.2,840,1),'Crema leche espesa':(2.2,	1.7,44,60,0.6,1540,1)  }
#el orden que de lo valores es el siguiente:
#dicc_alim[alimento]=(HDC,PROTEINA,GRASAS,CALSIO,HIERRO,VITAMINA_A,VITAMINA_C)
#FUNCIONES RELACIONADA AL TABLA DE ALIMENTOS
def verificacion(alimento):
    if alimento not in dicc_alim:
        return False
    return True

def propiedades(aliment,cant):
    aux_prop=[]
    for i in dicc_alim[aliment]:
        aux_prop.append(i*cant/100)
        
    return aux_prop

def verif_resp(resp):
    if resp.upper()!="SI" and resp.upper()!="NO":
        return True
    return False


def tablas():
    list_prop=("carbohidratos","proteina","grasas","calsio","hierro","vitamina_A","vitamina_B")
    while True:
        aliment= input("ingrese alimento: ")
        while verificacion(aliment)==False:
            print("alimento no encontrado")
            aliment= input("ingrese alimento: ")
            
        cant= float(input("cantidad en gramos: "))
        prop_alim=propiedades(aliment,cant)
        
        for i in range(7):
            print(f"{list_prop[i]} | {prop_alim[i]}g")

        print("¿desea buscar otro alimento?")
        resp=input("si/no: ")
        while verif_resp(resp):
            resp=input("si/no: ")
        if resp.upper()=="NO":
            break
        
#FUNCIONES RELACIONADAS A CALCULO DE CALORIAS

#funciones que calcula las calorias

#calcular calorias hombres

def clasif_edad_hom(edad,peso):
    if 18<=edad<30:
        TMB=15.057*peso+692.2
    elif 30<=edad<60:
        TMB=11.472*peso+873.1
    else:
        if 60<=edad:
            TMB=11.711*peso+587.7
    return TMB
#calcular calorias mujeres
def clasif_edad_muj(edad,peso):
    if 18<=edad<30:
        TMB=14.818*peso+486.6
    elif 30<=edad<60:
        TMB=8.126*peso+845.
    else:
        if 60<=edad:
            TMB=9.082*peso+658.5
    return TMB



#funciion que calcula el porcentaje de las calorias
def porcent_kcal(calorias):
    print("escriba el porcentaje de cada macronutrientes")
    por_HDC=float(input("carbohidratos: "))*calorias/100
    por_PROTEIN=float(input("proteina: "))*calorias/100
    por_GRASA=float(input("grasas: "))*calorias/100

    return (por_HDC,por_PROTEIN,por_GRASA)

def gramos_kcal(list_por):
    list_gram=(list_por[0]*1/4,list_por[1]*1/4,list_por[2]*1/9)
    return list_gram    

#CALCULAR IMC
def calcular_imc(peso, altura):
    imc = peso / ((altura/100) ** 2)
    return imc

def clasificar_imc(imc):
    # Clasifica el IMC en categorías
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"


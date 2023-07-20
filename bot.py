from email import message
import telebot
import telegram
from TOKEN_BOT_CespedSur import TOKEN
print("BOT RUNNING!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["help", "start"])



def send_welcome(message):
    bot.send_message(message.chat.id, "Calculadora CespedSur")
    bot.send_message(message.chat.id, "Para calcular el costo solo envie la cantidad de m² a instalar")
    bot.send_message(message.chat.id, "Para calcular la cantidad de m² necesarios de pasto para dale un borde a una piscina envienlo en el siguiente formato: ")
    bot.send_message(message.chat.id, "`AxB-C\nDonde:\nA: El Largo\nB: El ancho\nC: Cantidad de metros en cada direccion\nLos valores pueden tener hasta un decimal\nPor Ejemplo: 8x3-2,5`", parse_mode=telegram.constants.ParseMode.MARKDOWN)

@bot.message_handler(func=lambda m: True)


def function_name(message):
    texto = message.text
    id= message.chat.id

    #if (len(texto) > 22) or (("-" not in texto) and  (len(texto) > 4) and len(texto) <16):
    if (("/" not in texto) and (len(texto) > 5)) or (len(texto) > 22):

        bot.send_message(id,"Indique una cantidad valida")


    elif (len(texto) <6) and ("-" not in texto):

        calculoM2(texto,id)

    elif ("-" in texto):

        piscina(texto,id)


    elif ("/whatsapp" or "/WhatsApp" in texto):

        whatsapp(texto, id)



################
##  FUNCIONES ##
################

def calculoM2(texto,id):

    #Precios:

    p_domicilio_temuco = 3700 + 500
    p_instalado_temuco = 4700 + 500
    p_instalado_bajo15_temuco = 5500 + 500

    p_domicilio_labranza = 3800 + 500
    p_instalado_labranza = 4700 + 500
    p_instalado_bajo15_labranza = 5500 + 500
    
    
    #Dar formato con puntos al valor
    fp = lambda precio: '{:,}'.format((int(texto) * precio)).replace(',', '.')
        

    if int(texto) >= 15:

        #Repuestas del bot si son 15 o mas m²
        bot.send_message(id,"TEMUCO:")
        bot.send_message(id,f"`El valor con entrega a domicilio para sus {texto}m² en Temuco es de: ${fp(p_domicilio_temuco)}`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(id,f"`El valor con instalación para sus {texto}m² en Temuco es de: ${fp(p_instalado_temuco)}`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(id,"LABRANZA:")
        bot.send_message(id,f"`El valor con entrega a domicilio para sus {texto}m² en Labranza es de: ${fp(p_domicilio_labranza)}`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(id,f"`El valor con instalación para sus {texto}m² en Labranza es de: ${fp(p_instalado_labranza)}`", parse_mode=telegram.constants.ParseMode.MARKDOWN)

    elif int(texto) <15:

        #Repuestas del bot si menos de 15m²
        bot.send_message(id,"TEMUCO:")
        bot.send_message(id,f"`El valor con entrega a domicilio para sus {texto}m² en Temuco es de: ${fp(p_domicilio_temuco)}`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(id,f"`El valor con instalación para sus {texto}m² en Temuco es de: ${fp(p_instalado_bajo15_temuco)}`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(id,"LABRANZA:")
        bot.send_message(id,f"`El valor con entrega a domicilio para sus {texto}m² en Labranza es de: ${fp(p_domicilio_labranza)}`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(id,f"`El valor con instalación para sus {texto}m² en Labranza es de: ${fp(p_instalado_bajo15_labranza)}`", parse_mode=telegram.constants.ParseMode.MARKDOWN)


def piscina(texto,id):

    command, datos_calculo = texto.split(" ")
    # Dividimos el string por el caracter "x"
    largo, ancho_anchoPasto = datos_calculo.split("x")

    # Asignamos el valor de la primera parte a la variable "a"
    largo = float(largo.replace(",", "."))

    # Dividimos la segunda parte por el caracter "-"
    ancho, anchoPasto = ancho_anchoPasto.split("-")

    # Convertimos "b" a entero y "c" a float
    ancho = float(ancho.replace(",", "."))
    anchoPasto = float(anchoPasto.replace(",", "."))  # Reemplazamos la coma por un punto antes de convertir a float

    #Calculos de m2
    m2Esquinas= (anchoPasto*anchoPasto)*4
    m2PlanosVerticales= (largo*anchoPasto)*2
    m2PlanosHorizontales= (ancho*anchoPasto)*2
    #Calculo total
    m2Totales = m2Esquinas + m2PlanosVerticales + m2PlanosHorizontales

    #Repuestas del bot
    bot.send_message(id, f"Largo: {largo}m\nAncho: {ancho}m\nMetros lineales pasto en cada direccion: {anchoPasto}m\n\nEsquinas: {m2Esquinas}m²\nPlanos Verticales: {m2PlanosVerticales}m²\nPlanos Horizontales: {m2PlanosHorizontales}m²")
    bot.send_message(id, f"Total: {m2Totales}m²")


    #Responde con el link para abrir un chat de whatsapp con el cliente
def whatsapp(texto,id):

    command, numero = texto.split(" ")

    if len(numero) == 8:
        bot.send_message(id, f"https://api.whatsapp.com/send?phone=569{numero}")
    elif len(numero) == 9:
        bot.send_message(id, f"https://api.whatsapp.com/send?phone=56{numero}")
    elif "+" in numero:
        bot.send_message(id, f"https://api.whatsapp.com/send?phone={numero.replace('+', '')}")
    else:
        bot.send_message(id, "numero incorrecto")

bot.infinity_polling()

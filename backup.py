from email import message
import telebot
import telegram

bot = telebot.TeleBot("5674863165:AAEi8yDR9FMe5IVi1i2sqNyQC_7ABaBjClg")
@bot.message_handler(commands=["help", "start"])



def send_welcome(message):
    bot.send_message(message.chat.id, "Calculadora CespedSur")
    bot.send_message(message.chat.id, "Para calcular el costo solo envie la cantidad de m² a instalar")
    bot.send_message(message.chat.id, "Para calcular la cantidad de m² necesarios de pasto para dale un borde a una piscina envienlo en el siguiente formato: ")
    bot.send_message(message.chat.id, "`AxB-C\nDonde:\nA: El Largo\nB: El ancho\nC: Cantidad de metros en cada direccion\nLos valores pueden tener hasta un decimal\nPor Ejemplo: 8x3-2,5`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
chat_id= 1

@bot.message_handler(func=lambda m: True)
def function_name(message):

    if ("-" not in message.text):
        #Declaracion de variables y formateo con puntos
        domicilio_temuco = '{:,}'.format((int(message.text) * 3700)).replace(',','.')
        instalado_temuco = '{:,}'.format((int(message.text) * 4500)).replace(',','.')
        instalado_bajo15_temuco = '{:,}'.format((int(message.text) * 5500)).replace(',','.')

        domicilio_labranza = '{:,}'.format((int(message.text) * 3800)).replace(',','.')
        instalado_labranza = '{:,}'.format((int(message.text) * 4700)).replace(',','.')
        instalado_bajo15_labranza = '{:,}'.format((int(message.text) * 5500)).replace(',','.')


    if (len(message.text) > 11) | (("-" not in message.text) and  (len(message.text) > 4)):
        bot.send_message(message.chat.id,"Indique una cantidad valida")
    elif ("-" in message.text):
        # Dividimos el string por el caracter "x"
        largo, ancho_anchoPasto = message.text.split("x")

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
        bot.send_message(message.chat.id,"Largo: " +str(largo) + "m\n" +"Ancho: " +str(ancho) + "m\n" + "Metros lineales pasto en cada direccion: " +str(anchoPasto) + "m\n\n" + "Esquinas: " +str(m2Esquinas) + "m²\n" + "Planos Verticales: " +str(m2PlanosVerticales) + "m²\n" + "Planos Horizontales: " +str(m2PlanosHorizontales) + "m²")
        bot.send_message(message.chat.id,"Total: " +str(m2Totales) + "m²")

    elif int(message.text) >= 15:

        #Repuestas del bot si son 15 o mas m²
        bot.send_message(message.chat.id,"TEMUCO:")
        bot.send_message(message.chat.id,"`El valor con entrega a domicilio para sus " + message.text + "m² en Temuco es de: $" +str(domicilio_temuco) + "`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(message.chat.id,"`El valor con instalación para sus " + message.text + "m² en Temuco es de: $" +str(instalado_temuco) + "`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(message.chat.id,"LABRANZA:")
        bot.send_message(message.chat.id,"`El valor con entrega a domicilio para sus " + message.text + "m² en Labranza es de: $" +str(domicilio_labranza) + "`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(message.chat.id,"`El valor con instalación para sus " + message.text + "m² en Labranza es de: $" +str(instalado_labranza) + "`", parse_mode=telegram.constants.ParseMode.MARKDOWN)

    elif int(message.text) <15:

        #Repuestas del bot si menos de 15m²
        bot.send_message(message.chat.id,"TEMUCO:")
        bot.send_message(message.chat.id,"`El valor con entrega a domicilio para sus " + message.text + "m² en Temuco es de: $" +str(domicilio_temuco) + "`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(message.chat.id,"`El valor con instalación para sus " + message.text + "m² en Temuco es de: $" +str(instalado_bajo15_temuco) + "`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(message.chat.id,"LABRANZA:")
        bot.send_message(message.chat.id,"`El valor con entrega a domicilio para sus " + message.text + "m² en Labranza es de: $" +str(domicilio_labranza) + "`", parse_mode=telegram.constants.ParseMode.MARKDOWN)
        bot.send_message(message.chat.id,"`El valor con instalación para sus " + message.text + "m² en Labranza es de: $" + str(instalado_bajo15_labranza) + "`", parse_mode=telegram.constants.ParseMode.MARKDOWN)

bot.infinity_polling()
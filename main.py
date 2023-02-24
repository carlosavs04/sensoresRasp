import Adafruit_DHT

# Define el tipo de sensor que estás utilizando
sensor = Adafruit_DHT.DHT11

# Define el número del pin GPIO al que está conectado el sensor
pin = 5

# Intenta leer los datos del sensor
humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

# Verifica si la lectura fue exitosa
if humedad is not None and temperatura is not None:
    print('Temperatura={0:0.1f}°C  Humedad={1:0.1f}%'.format(temperatura, humedad))
else:
    print('Error al leer datos del sensor.')

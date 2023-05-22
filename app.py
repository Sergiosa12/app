from flask import Flask, render_template, request
import serial

#arduino = serial.Serial('/dev/ttyACM1', 9600)
informacion = 0
informacion1 = 0
informacion2 = 0
informacion3 = 0
informacion4 = 0

print("Starting!")

app = Flask(__name__)

while True:

    @app.route('/')
    def procesar_informacion():
        # procesar la información recibida
        return render_template('index.html')

    @app.route('/8',methods=['POST', 'GET'])
    def result():
        global informacion
        informacion = request.form['8']
        print("Información recibida:", informacion)
        comando = '8' #Input
        #arduino.write(comando.encode()) #Mandar un comando hacia Arduino
        print(comando)
        return render_template('index.html',informacion=informacion)

    @app.route('/4',methods=['POST', 'GET'])
    def result1():
        global informacion1
        informacion1 = request.form['4']
        print("Información recibida:", informacion1)
        comando = '4' #Input
        #arduino.write(comando.encode()) #Mandar un comando hacia Arduino
        print(comando)
        return render_template('index.html',informacion1=informacion1)

    @app.route('/5',methods=['POST', 'GET'])
    def result2():
        global informacion2
        informacion2 = request.form['5']
        print("Información recibida:", informacion2)
        comando = '5' #Input
        #arduino.write(comando.encode()) #Mandar un comando hacia Arduino
        print(comando)
        return render_template('index.html',informacion2=informacion2)

    @app.route('/6',methods=['POST', 'GET'])
    def result3():
        global informacion3
        informacion3 = request.form['6']
        print("Información recibida:", informacion3)
        comando = '6' #Input
        #arduino.write(comando.encode()) #Mandar un comando hacia Arduino
        print(comando)
        return render_template('index.html',informacion3=informacion3)

    @app.route('/2',methods=['POST', 'GET'])
    def result4():
        global informacion4
        informacion4 = request.form['2']
        print("Información recibida:", informacion4)
        comando = '2' #Input
        #arduino.write(comando.encode()) #Mandar un comando hacia Arduino
        print(comando)
        return render_template('index.html',informacion4=informacion4)
    
    if __name__ == '__main__':
        app.run(debug=True)
        
arduino.close() #Finalizamos la comunicacion
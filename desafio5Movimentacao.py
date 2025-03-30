from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.paramenters import Port
from pybricks.tools import wait

ev3= EV3Brick()
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)

# separei o programa em funções de modo a evitar a repetição 
# de código

def andar_reto(velocidade, tempo):
    motor_esquerdo.run(velocidade)
    motor_direito.run(velocidade)
    wait(tempo)
    motor_esquerdo.stop()
    motor_direito.stop()

def virarDir(velocidade, tempo):
    motor_esquerdo.run(velocidade)
    wait(tempo)
    motor_esquerdo.stop()

    
def virarEsq(velocidade, tempo):
    motor_direito.run(velocidade)
    wait(tempo)
    motor_direito.stop()

def pararRobo():
    motor_esquerdo.hold()
    motor_direito.hold()

################

while True:
    
    for i in range (2):
        andar_reto(200, 3000)
        #vira para esq
        virarEsq(400,2000)

        andar_reto(200, 3000)
        #vira para dir
        virarDir(400,2000)
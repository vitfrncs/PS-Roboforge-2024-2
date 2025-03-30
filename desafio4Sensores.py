#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#Considerei que o robô tem dois motores pq todos os exemplos do slide são assim

# Create your objects here.
ev3 = EV3Brick()
motorB = Motor(Port.B) #c oloquei a mesma porta dos slides
motorC = Motor(Port.C)
sensorCor = ColorSensor(Port.S1) # mede a cor
sensorUltra=UltrasonicSensor(Port.S3)# medirá distância da parede

# Write your program here.
DIAMENTRO_RODA = 6.0
DIST_ENTRE_RODAS = 13.5

velocidade = 100 # é em mm/s
distancia_q_queremos = 500 # em mm tbm
kp = 2 # ganho proporcional


def curvaEsquerda (graus):
    motorB.reset_angle(0)
    motorC.reset_angle(0)
    media_motor = 0
    graus_motor = graus_reais * (DIST_ENTRE_RODAS/DIAMENTRO_RODA)
    while (media_motor < graus_motor):
        motorB.run(velocidade)
        motorC.run(-velocidade)
        media_motor = (motorB.angle() - motorC.angle())/2
    motorB.hold()
    motor.hold()

def curvaDireita (graus):
    motorB.reset_angle(0)
    motorC.reset_angle(0)
    media_motor = 0
    graus_motor = graus_reais * (DIST_ENTRE_RODAS/DIAMENTRO_RODA)
    while (media_motor < graus_motor):
        motorB.run(-velocidade)
        motorC.run(velocidade)
        media_motor = (motorB.angle() - motorC.angle())/2
    motorB.hold()
    motorC.hold()



while True:
    cor = sensorCor.color()

    if cor == Color.RED:
        # não usei giroscopio pq falaram que ele não é muito eficaz
        # como pensei que a parede está na esquerda
        # o robo sempre vira para a direita para desviar do vermelho
        # entra direita -> esquerda -> esquerda -> direita
        # um problema é que ele pode continar no vermelho depois de 
        # voltar pra direçao correta kkkkk
        curvaDireita(90)
        motorB.run_time(velocidade, 3)
        motorC.run_time(velocidade, 3)
        curvaEsquerda(90)
        motorB.run_time(velocidade, 3)
        motorC.run_time(velocidade, 3)
        curvaEsquerda(90)
        motorB.run_time(velocidade, 3)
        motorC.run_time(velocidade, 3)
        curvaDireita(90)

    elif cor = Color.YELLOW:
        motorB.hold()
        motorC.hold()
        ev3.speaker.beep()
        while not any(ev3.buttons.pressed()):
            wait(10)

    elif cor = Color.GREEN:
        motorB.hold()
        motorC.hold()
        break

    distanca = sensorUltra.distance()
    #erro indica quantos mm o robo está fora do ideal
    erro = distancia_q_queremos - distancia
    direcao = erro * kp

    #se o erro for positivo, o robo está mais perto da parede 
    #do que deveria. então é necessário que o motor esquerdo seja
    #mais rápido que o direito (considerei que a parede está do lado
    #esquerdo do robô)
    #se o erro for negativo, a velocidade do motor direito deve ser maior que o 
    #esquerdo

    velocidade_esq = velocidade + correcao
    velocidade_dir = velocidade - correcao

    motorB.run(velocidade_esq)
    motorC.run(velocidade_dir)

    wait(100)







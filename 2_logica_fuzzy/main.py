from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction, QSpinBox


def formulas():

    cash = qtd_cash.value()

    if cash == 0:
        pouco = 0
        razoavel = 0
        adequado = 0

    elif (0<cash)and(cash<=30):
        pouco = 1
        razoavel = 0
        adequado = 0

    elif (cash > 30)and(cash<50):
        pouco = (50-cash)/(50-30)
        razoavel = (cash-30)/(50-30)
        adequado = 0
        
    elif cash >= 70:
        pouco = 0
        razoavel = 0
        adequado = 1

    elif cash == 50:
        pouco = 0
        adequado = 0
        razoavel = 1
        
    elif (cash > 50)and(cash < 70):
        razoavel = (70-cash)/(70-50)
        adequado = (cash-50)/(70-50)
        pouco = 0

    people = quantidade_pessoa.value()

    if people == 0:
        insuficiente = 0
        satisfatorio = 0
    
    elif people >= 70:
        insuficiente = 0
        satisfatorio = 1

    elif (people > 0)and(people <= 30):
        insuficiente = 1
        satisfatorio = 0

    elif (people > 30)and(people < 70):
        insuficiente = (70-people)/(70-30)
        satisfatorio = (people - 30)/(70-30)

    regras(pouco, razoavel, adequado, insuficiente, satisfatorio)


def regras(pouco, razoavel, adequado, insuficiente, satisfatorio):
    
    if (pouco >= insuficiente) and (pouco >= satisfatorio):
        alto = pouco
  
    else:
        if (insuficiente <= satisfatorio):
            alto = insuficiente

        else:
            alto = satisfatorio
 
    if razoavel <= satisfatorio:
        medio = razoavel
    else:
        medio = satisfatorio

    if adequado <= satisfatorio:
        baixo = adequado
    else: 
        baixo = satisfatorio

    soma = 0
    divisor = 0

    if baixo > 0:
        soma += 60 * baixo
        divisor += 3*baixo
    
    if medio > 0:
        soma += 150 * medio
        divisor += 3*medio
    
    if alto > 0:
        soma += 240 * alto
        divisor += 3*alto

    risco_final = soma/divisor
    show(risco_final)


def show(risco_final):
    if (risco_final <= 35):
        resultado.setText('Baixo : ' + str(risco_final))
        resultado.setVisible(True)
    elif(risco_final > 35)and(risco_final <= 65):
        resultado.setText('Médio : ' + str(risco_final))
        resultado.setVisible(True)
    elif(risco_final > 65):
        resultado.setText('Alto : ' + str(risco_final))
        resultado.setVisible(True)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    window = uic.loadUi(r"C:\Users\Aender\Desktop\CC\Inteligencia artificial\ia-cc-2020-2-AendersonSouza\2_logica_fuzzy\interface.ui")

    dinheiro = window.findChild(QLabel, 'dinheiro')
    qtd_cash = window.findChild(QSpinBox, 'qtd_dinheiro')

    pessoa = window.findChild(QLabel, 'pessoa')
    quantidade_pessoa = window.findChild(QSpinBox, 'qtd_pessoa')

    risco = window.findChild(QLabel, 'risco')
    resultado= window.findChild(QLabel, 'resultado')
    resultado.setVisible(False)

    Calcular = window.findChild(QPushButton, 'calcular')
    Calcular.clicked.connect(formulas)
    

    window.show()

    app.exec_()

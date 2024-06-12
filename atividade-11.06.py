from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime
import mysql.connector


banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="led_colors"
)


def enviarCor():
    if tela.radioRed.isChecked():
        cor_selecionada = "vermelho"
    elif tela.radioGreen.isChecked():
        cor_selecionada = "verde"
    elif tela.radioYellow.isChecked():
        cor_selecionada = "amarelo"
    else:
        cor_selecionada = None

    if cor_selecionada:
        timestamp = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        try:
            cursor = banco.cursor()
            comando_sql = "INSERT INTO colors (color, timestamp) VALUES (%s, %s)"
            dados = (cor_selecionada, timestamp)
            cursor.execute(comando_sql, dados)
            banco.commit()
            cursor.close()
            QMessageBox.information(None, 'Sucesso', 'Cor enviada ao banco de dados!')
        except Exception as e:
            QMessageBox.critical(None, 'Erro', f'Erro ao enviar cor: {e}')
    else:
        QMessageBox.warning(None, 'Seleção', 'Por favor, selecione uma cor')


app = QtWidgets.QApplication([])
tela = uic.loadUi("interface.ui")


print(dir(tela))


if hasattr(tela, 'btnEnviar'):
    tela.btnEnviar.clicked.connect(enviarCor)
else:
    print("Erro: btnEnviar não encontrado na interface!")


tela.show()
app.exec_()

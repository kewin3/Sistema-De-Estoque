from PyQt5 import  uic,QtWidgets

#Parte cadastro 

def funcao_principal():
    linha1 = formulario2.codigo.text()
    linha2 = formulario2.descricao.text()
    linha3 = formulario2.preco.text()

    if formulario2.radioButton.isChecked() :
        print("Categoria Informatica foi selecionada")
    elif formulario2.radioButton_2.isChecked() :
        print("Categoria Alimentos foi selecionada")
    else:
        print("Categoria Eletronicos foi selecionada")

    print("Codigo", linha1)
    print("Descrição", linha2)
    print("Preço", linha3)


#Parte Login

def funcao_login():
    tela_login.label_4.setText("")
    nome_usuario = tela_login.usuario.text()
    senha = tela_login.senhausuario.text()
    if nome_usuario == "Kewin" and senha == "220761" :
        tela_login.close()
        tela_formulario.show()
    else :
        tela_login.label_4.setText("Dados de login incorretos!")


def logout():
    tela_formulario.close()
    tela_login.show()


app=QtWidgets.QApplication([])
tela_login=uic.loadUi("tela_login.ui")
tela_formulario=uic.loadUi("tela_formulario.ui")
formulario2=uic.loadUi("tela_formulario.ui")
tela_login.senhausuario.setEchoMode(QtWidgets.QLineEdit.Password)

tela_login.entrar.clicked.connect(funcao_login)
formulario2.enviar.clicked.connect(funcao_principal)
tela_formulario.logout.clicked.connect(logout)

tela_login.show()
app.exec()
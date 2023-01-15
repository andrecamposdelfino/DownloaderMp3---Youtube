
from pytube import YouTube
from PyQt5 import uic, QtWidgets
dados = []
def Downloader():
   try:
       #limpa o label que exibi o resultado do download
       formulario.lbl_fim.setText("")

       #pego o link do youtube
       link = formulario.txt_Downloader.text()

       #crio o objeto passando como parametro o link
       yt = YouTube(link)

       #crio uma variavel para receber o stream do objeto
       downloader = yt.streams.filter(only_audio=True).get_audio_only()

       # coloco dentro do array o titulo da musica
       dados.append(downloader.title)

       #percorro o aaray e coloco o nome da musica dentro do campo de texto
       for dado in dados:
            formulario.txt_lista.addItem(dado)

        # chamo o metodo download(0
       downloader.download()

       #coloco o a resposta dento de uma label caso seja sucesso!
       formulario.lbl_fim.setText(f"{downloader.title} \n"
                                  f"Download Finalizado com sucesso!!...")

       #limpa o campo no final do downloader
       formulario.txt_Downloader.setText("")

      #limpa o array
       dados.pop()
       print(dado)
   except Exception as erro:
       #exibi o erro na label
       formulario.lbl_fim.setText(f"Erro ao tentar fazer o downloader erro: {erro}")

app=QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.btn_Downloader.clicked.connect(Downloader)
formulario.show()

app.exec()





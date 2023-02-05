#!/usr/bin/python3
"""
MESI-TB 2023 - Aluno # 23256
PT SpeechRecognition - Web App com Flask speechrecognition e Pyaudio
Reconhecimento de ficheiros audio formato WAV em português  e transcreve
para texto no ecran.
"""
# Bibibliotecas
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

# Executa a App web define path da app e os métodos get e post.
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

# Funcao que cria o formulario e importa o ficherio audio wav
def pagina():
    transcript = ""
    if request.method == "POST":
        print("DADOS RECEBIDOS - FICHEIRO WAV ")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        # reconhecimento e conversão dos dados
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, language='pt-PT') # Trabalhos futuros automatizar o recolhecimento auto

    return render_template('app.html', transcript=transcript) # importa o ficheiro template app.html


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

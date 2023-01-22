#!/usr/bin/python3
# MESI-TB 2023 - Aluno # 23256
# Web App com Flask speechrecognition to text converter

#Bibibliotecas
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

# Iniciar App com Flask com os metodos get e post
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
        
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, language='pt-PT') # pode ser alterado manualmente para a lingua pretendia por ex. es-ES

    return render_template('app.html', transcript=transcript) # importa o ficheiro template app.html


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

import tkinter as tk

import speech_recognition as sr

def capture_audio():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Habla algo...")
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio, language="es-ES")
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, text)
        except sr.UnknownValueError:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "No se pudo entender el audio")
        except sr.RequestError as e:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Error en la solicitud: {e}")

# Crear ventana principal
root = tk.Tk()
root.title("Captura de Voz a Texto")

# Etiqueta y botón
label = tk.Label(root, text="Presiona el botón y habla:")
label.pack(pady=10)

capture_button = tk.Button(root, text="Capturar Voz", command=capture_audio)
capture_button.pack()

# Cuadro de texto para mostrar el resultado
result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=10)

# Iniciar la ventana principal
root.mainloop()

#pip install Pyaudio
#pip install setuptools
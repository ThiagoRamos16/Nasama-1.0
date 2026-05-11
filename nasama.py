from gtts import gTTS
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import speech_recognition as sr
import sys
import funcoes_so
import funcoes_email
import threading
import interface
import time



def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang = 'pt-br')
    tts.save(audio)
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play() 
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit() 
    os.remove(audio)
    

def monitora_audio(executar_comando=True):
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source, duration=1)
        while True:
            print("Diga alguma coisa")
            audio = recon.listen(source, timeout=10, phrase_time_limit=10)
            try:
                mensagem = recon.recognize_google(audio, language= 'pt-br')
                mensagem = mensagem.lower()
                print("Você disse: ", mensagem)
                interface.adiciona_historico("Você", mensagem)
            
                if executar_comando:
                    executa_comandos(mensagem)
                break
            except sr.WaitTimeoutError:
                interface.inicia_animacao()
                cria_audio("erro.mp3", "Não ouvi nada. Pode repetir?.")
                interface.para_animacao()
            except sr.UnknownValueError:
                interface.inicia_animacao()
                cria_audio("erro.mp3", "Não consegui entender. Tente novamente.")
                interface.para_animacao()
            except sr.RequestError:
                interface.inicia_animacao()
                cria_audio("erro.mp3", "Erro ao conectar ao serviço de reconhecimento.")
                interface.para_animacao()
        return mensagem 
    

def executa_comandos(acao):
    if 'fechar assistente' in acao:
        interface.janela.after(0, interface.janela.destroy)
        sys.exit()
    elif 'horas' in acao:
        hora = funcoes_so.verifica_hora()
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", hora)
        cria_audio('mensagem.mp3', hora)
        interface.para_animacao() 
        interface.atualiza_status("ouvindo")
        
    elif 'enviar email' in acao or 'enviar e-mail' in acao:
        interface.atualiza_status("ouvindo")
        status_email = funcoes_email.enviar_email(cria_audio,monitora_audio)
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", status_email)
        cria_audio('mensagem.mp3', status_email)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
        

def main():
    thread_nasama = threading.Thread(target=inicia_nasama, daemon=True)
    thread_nasama.start()
    time.sleep(0.5) 
    interface.janela.mainloop()
    

def inicia_nasama():
    print("inicia_nasama rodando!")
    time.sleep(2)
    interface.inicia_animacao()
    cria_audio("wellcome.mp3", "Olá, sou a Nasama. Em que posso lhe ajudar?")
    interface.para_animacao()
    interface.adiciona_historico("Nasama", "Olá, sou a Nasama. Em que posso lhe ajudar?")
    while True:                              
        interface.atualiza_status("ouvindo")
        monitora_audio()

main()
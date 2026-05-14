# Bibliotecas padrão do Python
import os
import sys
import threading
import time

# Configuração pygame (antes do import)
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Bibliotecas externas
from gtts import gTTS
import pygame
import speech_recognition as sr

# Módulos do projeto
import funcoes_so
import funcoes_email
import funcoes_cotacao
import funcoes_noticias
import funcoes_clima
import interface



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
                interface.adiciona_historico("Nasama", "Não ouvi nada. Pode repetir?")
                interface.para_animacao()
            except sr.UnknownValueError:
                interface.inicia_animacao()
                cria_audio("erro.mp3", "Não consegui entender. Tente novamente.")
                interface.adiciona_historico("Nasama", "Não consegui entender. Tente novamente.")
                interface.para_animacao()
            except sr.RequestError:
                interface.inicia_animacao()
                cria_audio("erro.mp3", "Erro ao conectar ao serviço de reconhecimento.")
                interface.adiciona_historico("Nasama", "Erro ao conectar ao serviço de reconhecimento.")
                interface.para_animacao()
        return mensagem 
    

def executa_comandos(acao):
    if 'fechar assistente' in acao:
        interface.janela.after(0, interface.janela.destroy)
        sys.exit()
        
    elif 'desligar computador' in acao and 'uma hora' in acao:
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", "Computador será desligado em uma hora")
        cria_audio('mensagem.mp3', "Computador será desligado em uma hora.")
        funcoes_so.desliga_computador_uma_hora()
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
        
    elif 'desligar computador' in acao and 'meia hora' in acao:
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", "Computador será desligado em meia hora.")
        cria_audio('mensagem.mp3', "Computador será desligado em meia hora.")
        funcoes_so.desliga_computador_meia_hora()
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
        
    elif 'cancelar desligamento' in acao:
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        interface.adiciona_historico("Nasama", "Desligamento cancelado.")
        cria_audio('mensagem.mp3', "Desligamento cancelado.")
        funcoes_so.cancela_desligamento()
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
 
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
        
    elif 'cotação' in acao and 'dólar' in acao:
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cotacao = funcoes_cotacao.cotacao_moeda("Dólar")
        interface.adiciona_historico("Nasama", cotacao)
        cria_audio('mensagem.mp3', cotacao)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
        
    elif 'cotação' in acao and 'euro' in acao:
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cotacao = funcoes_cotacao.cotacao_moeda("Euro")
        interface.adiciona_historico("Nasama", cotacao)
        cria_audio('mensagem.mp3', cotacao)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")

    elif 'cotação' in acao and 'bitcoin' in acao:
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cotacao = funcoes_cotacao.cotacao_moeda("Bitcoin")
        interface.adiciona_historico("Nasama", cotacao)
        cria_audio('mensagem.mp3', cotacao)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
        
    elif 'notícias' in acao or 'noticias' in acao or "noticia" in acao or "notícia" in acao:
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        cria_audio('mensagem.mp3', 'De qual site você quer as notícias? Google, Globo, UOL, BBC ou Folha?')
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
        
        resposta = monitora_audio(executar_comando=False)
        
        if 'globo' in resposta or 'g1' in resposta:
            fonte = "globo"
        elif 'bbc' in resposta:
            fonte = "bbc"
        elif 'uol' in resposta:
            fonte = "uol"
        elif 'folha' in resposta:
            fonte = "folha"
        else:
            fonte = "google" # Caso não entender vai pesquisar na fonte do google
        
        interface.atualiza_status("falando")
        interface.inicia_animacao()
        noticias = funcoes_noticias.ultimas_noticias(fonte)
        interface.adiciona_historico("Nasama", noticias)
        cria_audio('mensagem.mp3', noticias)
        interface.para_animacao()
        interface.atualiza_status("ouvindo")
    
    elif 'clima' in acao or 'temperatura' in acao:
        while True:  
            interface.atualiza_status("falando")
            interface.inicia_animacao()
            cria_audio('mensagem.mp3', 'Qual cidade deseja saber a temperatura?')
            interface.adiciona_historico("Nasama", "Qual cidade deseja saber a temperatura?")
            interface.para_animacao()
            interface.atualiza_status("ouvindo")
            
            cidade = monitora_audio(executar_comando=False)
            
            interface.atualiza_status("falando")
            interface.inicia_animacao()
            resultado = funcoes_clima.temperatura(cidade)
            interface.adiciona_historico("Nasama", resultado)
            cria_audio('mensagem.mp3', resultado)
            interface.para_animacao()
            interface.atualiza_status("ouvindo")
            
            if 'Não encontrei' not in resultado and 'Não consegui' not in resultado:
                break  
    

def main():
    thread_nasama = threading.Thread(target=inicia_nasama, daemon=True)
    thread_nasama.start()
    time.sleep(0.5) 
    interface.janela.mainloop()
    

def inicia_nasama():
    print("inicia_nasama rodando!")
    time.sleep(2)
    interface.atualiza_status("falando")
    interface.inicia_animacao()
    cria_audio("wellcome.mp3", "Olá, sou a Nasama. Em que posso lhe ajudar?")
    interface.para_animacao()
    interface.adiciona_historico("Nasama", "Olá, sou a Nasama. Em que posso lhe ajudar?")
    while True:                              
        interface.atualiza_status("ouvindo")
        monitora_audio()

main()
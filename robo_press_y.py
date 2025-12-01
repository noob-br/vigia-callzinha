import pyautogui
import time

#---------------- Assinatura do Pai ----------------
# 1. DEFININDO (Ensinando o Python o que fazer)
def minha_assinatura():
    print(r"""
  _   _  ____   ____  ____  
 | \ | |/ __ \ / __ \|  _ \ 
 |  \| | |  | | |  | | |_) |
 | . ` | |  | | |  | |  _ < 
 | |\  | |__| | |__| | |_) |
 |_| \_|\____/ \____/|____/ 
    """)
    print("created by: NOOB-BR")
   # print("se copiar sem pedir, eu te encho a moringa na tapa, filho da puta")
    print("-" * 80)
# ----------------------- fim da assinatura -------------------

# começo do código

# pedindo a duracao
duracao_min = float(input("Olá Magnata, de quantos minutos será essa chamada?\n Digite aqui: "))
duracao_seg = float(input("E quantos segundos? "))
print("-" * 80)

# Assinando e Vai rodar até parar (Ctrl+C):
minha_assinatura()
print(f"Vigia call está pronto, trabalhará por {int(duracao_min)}min{int(duracao_seg)}... Press Ctrl+C to cancel")

input("Press Y to start: ")
print("-" * 50)

# tempo inicial
tempo_inicio = time.time()
print(f"Começando em: {time.ctime(tempo_inicio)}")
print("-" * 50)

# calcula total em segundos
duracao_total = (duracao_min * 60) + duracao_seg

# Tempo final
tempo_desligar = tempo_inicio + duracao_total

# Inicio da busca 15s antes do fim
inicio_da_busca = tempo_desligar - 15

print(f"Modo Sniper ativado! Vou começar a buscar a imagem às: {time.ctime(inicio_da_busca)}")

# Pa-pa-pa-paredão do While
while time.time() < tempo_desligar:

    # 1. Ja pode? Antes dos 15s
    if time.time() < inicio_da_busca:
        print(f"Aguardando o momento... Falta {int(tempo_desligar - time.time())}s")
        time.sleep(1)
        continue # Se ainda n é tempo de procurar, repete até ser

    # agora o time-time é maior q o tempo de iniciar busca
    # hora de ligar a visao computacional
    try:
        # tentar achar
        posicao_nox = pyautogui.locateOnScreen('app.png', confidence=0.8)
        
        # se achar
        print("\n --> ALVO LOCALIZADO! Preparado para o disparo... <--")

        # 3. Esperando para desligar (tempo de desligar)
        # Enquanto ainda n for a hora exata... espere
        while time.time() < tempo_desligar:
            time.sleep(0.1) #dorme pokin

        # 4. O Disparo (agora mostra a posicao)
        print("Tempo esgotado! Clicando!")
        centro_nox = pyautogui.center(posicao_nox)
         # Clica nas coordenadas (X, Y) desse centro
        pyautogui.click(centro_nox)
        time.sleep(3)

        posicao_back = pyautogui.locateOnScreen('reconhecimento.png', confidence=0.8)
        centro_back = pyautogui.center(posicao_back)
        pyautogui.click(centro_back)
        time.sleep(3)

        posicao_desligar = pyautogui.locateOnScreen('desligar.png', confidence=0.8)
        centro_desligar = pyautogui.center(posicao_desligar)
        pyautogui.click(centro_desligar)

        break

    except pyautogui.ImageNotFoundException:
        #se n achar
     print("Procurando alvo desesperadamente...", end='\r')
     time.sleep(0.1)

# tempo final
print("-" * 50)
print("\nOIIII")
print("O tempo acabou, chefe!")

print(f"\nFinalizado em: {time.ctime(tempo_desligar)}\n")
print("-" * 80)

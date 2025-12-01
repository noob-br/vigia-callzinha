# vigia-callzinha
This project automatically ends calls (focus in WhatsApp) based on scheduled time using computer vision

# Vigia Callzinha 🎯

Seu porteiro virtual que gerencia calls automaticamente usando visão computacional.

## ⚠️ AVISO IMPORTANTE
**Este código é para fins educacionais.** Use por sua conta e risco.

## 🛠️ Como Funciona
1. Agenda o tempo da call
2. 15s antes do fim, ativa modo "sniper" 
3. Usa computer vision para encontrar botões
4. Clica automaticamente para encerrar

## 📋 Pré-requisitos
- Python 3.8+
- PyAutoGUI, OpenCV
- **3 imagens personalizadas** (veja abaixo)

## 🖼️ Preparando as Imagens
Você PRECISA criar 3 screenshots do SEU app:

### 1. `app.png`
- Print da tela com call ativa
- Mostrando onde está a chamada

### 2. `reconhecimento.png` (opcional)
- Botão que faz aparecer o menu de desligar
- Muitos apps precisam disso primeiro

### 3. `desligar.png`  
- Botão de desligar call
- Deve ser exatamente como aparece no SEU app

## 🚀 Como Usar
```bash
pip install pyautogui opencv-python
python vigia_callzinha.py
🔧 Customização

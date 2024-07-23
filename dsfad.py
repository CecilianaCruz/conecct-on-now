import pyautogui
import time

def prevent_screen_off():
    try:
        while True:
            # Movimenta o cursor do mouse para cima e para baixo
            pyautogui.moveRel(0, 1)
            pyautogui.moveRel(0, -1)
            
            # Espera por 5 minutos antes de repetir (ajuste conforme necessário)
            time.sleep(300)  # 300 segundos = 5 minutos
            
    except KeyboardInterrupt:
        print("\nPrograma interrompido. A tela não será mais mantida ativa.")

if __name__ == "__main__":
    prevent_screen_off()
    

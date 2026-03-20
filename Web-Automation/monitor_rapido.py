import requests
import hashlib
import time
import difflib


# URL de la página que deseas monitorear
url = "https://URL.com/"

# Tiempo de espera entre verificaciones (en segundos)
interval = 10
discord_webhook = "https://discord.com/api/webhooks/XXXXXXXXXXXXXXXXXXX"

# Función para obtener el contenido de la página
def get_page_content(url):
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error al conectar con la página: {e}")
        return None
    
# Función para enviar el webhook a Discord
def send_discord_notification(message):
    data = {"content": message}  # Mensaje a enviar
    try:
        response = requests.post(discord_webhook, json=data)
        response.raise_for_status()
        print("Notificación enviada a Discord.")
    except requests.RequestException as e:
        print(f"Error al enviar el webhook a Discord: {e}")

def main():
    print(f"Monitoreando cambios en {url}")
    # Obtén el contenido inicial
    previous_content = get_page_content(url)
    if not previous_content:
        print("No se pudo obtener el contenido inicial. Verifica la URL.")
        return

    while True:
        time.sleep(interval)  # Espera antes de la siguiente verificación
        current_content = get_page_content(url)
        if not current_content:
            print("Error al obtener el contenido. Intentando nuevamente...")
            continue

        if current_content != previous_content:
            print("¡Cambio detectado en la página!")
            
            # Generar diferencias
            diff = difflib.unified_diff(
                previous_content.splitlines(),
                current_content.splitlines(),
                lineterm=""
            )
            diff_text = "\n".join(diff)
            
            # Imprimir las diferencias
            print("Diferencias detectadas:")
            print(diff_text)
            
            # Opcional: Enviar notificación a Discord con un resumen
            send_discord_notification(f"Se detectaron cambios en la página: {url}")
            
            break
        else:
            pass

if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup
import time
from playwright.sync_api import sync_playwright

# URL de la página que quieres monitorear
url = 'https://URL.COM'

# Función para verificar los resultados
def check_results():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Busca el contenedor de resultados
    results = soup.select('.ProductItem__Image')  # Ajusta el selector según la estructura de tu página
    return len(results) > 0

# Función para entrar al primer resultado y realizar la compra usando Playwright
def purchase_first_result():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=False)
        page = browser.new_page()
        page.goto(url)

        # Haz clic en el primer resultado
        page.click('.ProductItem__Image')  # Ajusta el selector según la estructura de tu página

        # Espera a que la página del artículo cargue
        page.wait_for_timeout(500)  # Ajusta el tiempo según sea necesario

        size_label = page.query_selector('label[for="option-product-template-0-3"]')
        if size_label:
            size_label.click()
            print("Talla 'L' seleccionada.")
        else:
            print("No se pudo encontrar la talla 'L'.")

        # Espera a que el botón "Añadir a la cesta" esté disponible y haz clic en él
        page.wait_for_selector('button.ProductForm__AddToCart')
        page.click('button.ProductForm__AddToCart')
        print("Artículo añadido a la cesta.")

        # Espera a que la cesta se actualice y el botón "Checkout" esté disponible
        page.wait_for_selector('button.Cart__Checkout')
        page.click('button.Cart__Checkout')
        print("Proceso de checkout iniciado.")

        # Rellenar la información de pago
        page.fill('#email','eliest@rexithegod.com')
        page.wait_for_timeout(500)
        page.fill('#TextField0','Bautista')
        page.fill('#TextField1','Galmarini')
        page.fill('#shipping-address1','Valle de la ballestera 64')
        page.fill('#TextField2','304')
        page.fill('#TextField3','46015')
        page.fill('#TextField4','Valencia')
        page.fill('#TextField5','652508394')

        page.wait_for_timeout(500)

        page.evaluate("window.scrollTo(10, document.body.scrollHeight)")
        page.wait_for_timeout(500)  # Ajusta el tiempo según sea necesario
        print("Desplazado hasta el final de la página.")

        # Seleccionar PayPal como método de pago utilizando el id del input
        paypal_label = page.query_selector('label[for="basic-PAYPAL_EXPRESS"]')
        if paypal_label:
            paypal_label.click()
            print("PayPal seleccionado.")
        else:
            print("No se pudo encontrar la opción de PayPal.")

        page.wait_for_timeout(1000)

        # Hacer clic en el botón "Pagar con PayPal"
        paypal_button = page.query_selector('div[role="link"][data-funding-source="paypal"]')
        if paypal_button:
            paypal_button.click()
            print("Botón 'Pagar con PayPal' clickeado.")
        else:
            print("No se pudo encontrar el botón 'Pagar con PayPal'.")

        # Esperar un momento para que PayPal procese la solicitud
        page.wait_for_timeout(500)  # Ajusta el tiempo según sea necesario

        # Mantener la pestaña abierta
        print("Script completado. La pestaña se mantendrá abierta.")
        page.wait_for_timeout(300000)  # Espera 5 minutos para inspeccionar la página (ajusta según sea necesario)

# Intervalo de tiempo en segundos entre cada recarga
interval = 3

while True:
    if check_results():
        print("¡Hay resultados disponibles!")
        purchase_first_result()
        break
    else:
        print("No hay resultados. Recargando...")
        time.sleep(interval)

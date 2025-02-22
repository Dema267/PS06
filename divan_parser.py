import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Настройки для Firefox
options = Options()
options.headless = True  # Запуск в фоновом режиме (без открытия браузера)
service = Service('path/to/geckodriver')  # Укажите путь к geckodriver

# Инициализация драйвера
driver = webdriver.Firefox(service=service, options=options)

# URL страницы с товарами
url = "https://www.divan.ru/category/svet"

# Открытие страницы
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)  # Даем странице время для загрузки

# Поиск всех продуктов на странице
products = driver.find_elements(By.CSS_SELECTOR, 'div.lsooF')  # Пример класса для продукта

# Список для хранения данных
parsed_data = []

# Парсинг данных
for product in products:
    try:
        # Название продукта
        title = product.find_element(By.CSS_SELECTOR, 'span.ui-Caption._2Umyc').text  # Пример селектора для названия

        # Цена продукта
        price = product.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.JIybk').text  # Пример селектора для цены

        # Ссылка на продукт
        link = product.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe').get_attribute('href')  # Пример селектора для ссылки

        # Добавление данных в список
        parsed_data.append([title, price, link])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

# Закрытие браузера
driver.quit()

# Сохранение данных в CSV файл
with open("light_products.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['название продукции', 'цена', 'ссылка на продукцию'])
    writer.writerows(parsed_data)

print("Парсинг завершен. Данные сохранены в light_products.csv")
# Автоматизированный E2E тест для сайта Saucedemo.com

## Требования

- Python 3.7+
- Браузер Firefox или Chrome
- Установленный Selenium WebDriver

## Установка

1. Клонируйте репозиторий (если есть) или создайте файлы вручную:

```bash
git clone git@github.com:femstuff/testirovanie-university.git
cd testirovanie-university
```

2. Создайте и активируйте виртуальное окружение (рекомендуется):

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости:

```bash
pip3 install -r requirements.txt
```

## Запуск теста

Выполните команду:

```bash
python3 e2e_test.py
```

## Что делает тест

1. Открывает сайт saucedemo.com в браузере Firefox
2. Авторизуется с тестовыми учетными данными:
   - Логин: `standard_user`
   - Пароль: `secret_sauce`
3. Добавляет товар "Sauce Labs Backpack" в корзину
4. Переходит в корзину и проверяет наличие товара
5. Начинает оформление заказа
6. Заполняет информацию о покупателе:
   - Имя: Мальбо
   - Фамилия: Мальбов
   - Почтовый индекс: 62500
7. Завершает оформление заказа
8. Проверяет сообщение об успешном завершении заказа
9. Закрывает браузер

## Файл теста (e2e_test.py)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("https://www.saucedemo.com/")
time.sleep(1)

browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()
time.sleep(1)

browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

assert "Sauce Labs Backpack" in browser.page_source

browser.find_element(By.ID, "checkout").click()
time.sleep(1)

browser.find_element(By.ID, "first-name").send_keys("Мальбо")
browser.find_element(By.ID, "last-name").send_keys("Мальбов")
browser.find_element(By.ID, "postal-code").send_keys("62500")
browser.find_element(By.ID, "continue").click()
time.sleep(1)

browser.find_element(By.ID, "finish").click()
time.sleep(1)

assert "Thank you for your order!" in browser.page_source
print("Success")

time.sleep(5)
browser.quit()
```

## Файл зависимостей (requirements.txt)

```
selenium==4.9.0
```

## Дополнительные настройки

### Для использования Chrome вместо Firefox

1. Установите ChromeDriver:
   - Скачайте версию, совместимую с вашим Chrome: https://chromedriver.chromium.org/downloads
   - Поместите файл в PATH или укажите путь явно в коде

2. Измените код в e2e_test.py:

```python
# Замените
browser = webdriver.Firefox()
# На
browser = webdriver.Chrome()
# Или с указанием пути
# browser = webdriver.Chrome(executable_path='/путь/к/chromedriver')
```

## Возможные улучшения

1. Добавить конфигурационный файл для учетных данных
2. Реализовать логирование шагов теста
3. Добавить обработку различных ошибок
4. Реализовать параметризацию тестов (разные товары, пользователи)
5. Добавить скриншоты при падении теста

## Проблемы и решения

Если тест не работает:
- Убедитесь, что у вас установлен актуальный драйвер браузера
- Проверьте, что сайт saucedemo.com доступен
- Убедитесь, что учетные данные верны (они могут измениться)
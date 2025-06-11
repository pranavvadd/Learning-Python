from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard

# Get the path to your chromedriver
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the page to load and the language selection to be available
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'langSelect-EN'))
)

# Select English language
language_id = driver.find_element(By.ID, 'langSelect-EN')
language_id.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'bigCookie'))
)

# Finds the big cookie element
big_cookie_id = driver.find_element(By.ID, 'bigCookie')

# Finds the cookies number element
cookies_num = driver.find_element(By.ID, 'cookies')

# Finds the product price elements
product_price_prefix = 'productPrice'

# Finds the product elements
product_prefix = 'product'

print("Press 'q' to stop the program.")

while not keyboard.is_pressed('q'):  # Run until 'q' is pressed
    big_cookie_id.click()
    cookies_num = driver.find_element(By.ID, 'cookies').text.split(" ")[0]
    # Remove commas from the cookies number
    cookies_num = int(cookies_num.replace(',', ''))

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(',', '')
        
        # Check if the product price is a digit
        if product_price.isdigit():
            continue
        
        product_price = int(product_price)

        # Check if we have enough cookies to buy the product
        if cookies_num >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

print("Program stopped.")
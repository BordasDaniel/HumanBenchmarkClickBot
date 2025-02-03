from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver beállítása
chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Weboldal megnyitása
    driver.get("https://humanbenchmark.com/tests/aim")

    wait = WebDriverWait(driver, 1, poll_frequency=0.5)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Consent') or contains(text(), 'Accept')]")))
    accept_button.click()

    # Várakozás a stabil oldalbetöltéshez
    time.sleep(3)

    # Végtelen ciklus, amely folyamatosan figyeli az elemet
    while True:
            # Megvárjuk, hogy az elem megjelenjen és kattintható legyen
            # Próbálkozás 1: Egérrel mozgatás és kattintás
            try:
                print("Egér mozgatása és kattintás...")
                ActionChains(driver).move_to_element(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-z6vxiy")))).click().perform()
                continue
            except:
                print("Egér kattintás sikertelen.")

except KeyboardInterrupt:
    print("Program leállítása...")

finally:
    # Böngésző bezárása
    driver.quit()

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
link = "http://selenium1py.pythonanywhere.com/"
driver.get(link)
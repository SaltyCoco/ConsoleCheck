
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def ConsoleCheck(url, merchant_name):

    options = Options()
    options.add_argument('--headless')
    options.add_argument('ignore-certificate-errors')

    # Load UI
    try:
        driver = webdriver.Chrome(executable_path='C:\Program Files\ChromeDriver\chromedriver.exe', options=options)
        driver.get(url)
    except Exception as e:
        print(f"url {url} not available for {merchant_name}")
        print(f"error: {str(e)}")
    try:
        driver.find_element_by_name('buy-now-button')
        print(f"Available to buy from {merchant_name} at {url} ")
    except Exception:
        print(f"Not available from {merchant_name}")
    driver.close()
    driver.quit()



if __name__ == '__main__':
    amazon_url = "https://www.amazon.com/Xbox-X/dp/B08H75RTZ8/ref=sr_1_16?crid=1JXVRXKXUG4Y9&dchild=1&keywords=xbox+series+x&qid=1611521867&sprefix=xbox%2Caps%2C221&sr=8-16"
    ConsoleCheck(url=amazon_url, merchant_name="amazon")

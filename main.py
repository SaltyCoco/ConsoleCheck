
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def ConsoleCheck(url, merchant_name):

    options = Options()
    options.add_argument('--headless')
    options.add_argument('ignore-certificate-errors')
    options.add_argument('--no-sandbox')

    # try:
    #     driver = webdriver.Chrome(executable_path='C:\Program Files\ChromeDriver\chromedriver.exe', options=options)
    # except Exception as e:
    #     print("driver not available")
    #     print(f"Error: {str(e)}")
    try:
        driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
    except Exception as e:
        print("driver not available")
        print(f"Error: {str(e)}")
        return
    try:
        driver.get(url)
    except Exception as e:
        print(f"url for {merchant_name} not available at {url}")
        print(f"Error: {str(e)}")
        return
    try:
        driver.find_element_by_name('buy-now-button')
        print(f"Available to buy from {merchant_name} at {url} ")
        driver.close()
        driver.quit()
    except Exception:
        print(f"Not available from {merchant_name}")
        driver.close()
        driver.quit()
        return
    return

if __name__ == '__main__':
    amazon_url = "https://www.amazon.com/Xbox-X/dp/B08H75RTZ8/ref=sr_1_16?crid=1JXVRXKXUG4Y9&dchild=1&keywords=xbox+series+x&qid=1611521867&sprefix=xbox%2Caps%2C221&sr=8-16"
    ConsoleCheck(url=amazon_url, merchant_name="amazon")

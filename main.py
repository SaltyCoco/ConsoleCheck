
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def AmazonConsoleCheck(url, merchant_name, executable_path):

    options = Options()
    options.add_argument('--headless')
    options.add_argument('ignore-certificate-errors')
    options.add_argument('--no-sandbox')

    try:
        driver = webdriver.Chrome(executable_path=executable_path, options=options)
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

def WalmartConsoleCheck(url, merchant_name, executable_path):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('ignore-certificate-errors')
    options.add_argument('--no-sandbox')


    try:
        driver = webdriver.Chrome(executable_path=executable_path, options=options)
        driver.find_elements_by_link_text()
        driver.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'some link text')))
    except Exception as e:
        print("driver not available")
        print(f"Error: {str(e)}")
        return


if __name__ == '__main__':
    chrome_executable_path = '/usr/local/bin/chromedriver'

    amazon_url = "https://www.amazon.com/Xbox-X/dp/B08H75RTZ8/ref=sr_1_16?crid=1JXVRXKXUG4Y9&dchild=1&keywords=xbox+series+x&qid=1611521867&sprefix=xbox%2Caps%2C221&sr=8-16"
    AmazonConsoleCheck(url=amazon_url, merchant_name="amazon", executable_path=chrome_executable_path)

    walmart_url = "https://www.walmart.com/ip/Xbox-Series-X/443574645"


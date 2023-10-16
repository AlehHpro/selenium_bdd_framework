from selenium import webdriver


def get_driver(browser: str):
    if browser.upper() == "CH":
        driver = webdriver.Chrome()
    elif browser.upper() == "CH_HL":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options)
    else:
        raise KeyError(
            f"Unexpected browser '{browser.upper()}'." f"Check your behave.ini file for available variables.")
    driver.set_window_size(width=1200, height=800)
    return driver

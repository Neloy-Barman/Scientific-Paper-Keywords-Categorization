import time
import tqdm
import pandas as pd
from selenium import webdriver

def main():
    df = pd.read_csv("csv_files/paper_urls.csv")
    urls = df['urls'].to_list()

    driver = webdriver.Chrome()

    for url in urls:
        driver.get(url=url)
        

    pass

if __name__ == "__main__":
    main()


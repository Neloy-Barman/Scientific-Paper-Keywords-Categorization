import math
import time
from tqdm import tqdm
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

columns = ['urls']

paper_urls = []

failed_pages = []

def main():
    
    df = pd.read_csv("csv_files/failed_page_numbers.csv")
    
    # avail_urls = df['url'].to_list()
    # print(avail_urls)

    driver = webdriver.Chrome()

    for ind in tqdm(range(len(df))):

        url = f"{df.iloc[ind]['url']}pageNumber={str(df.iloc[ind]['page_number'])}"

        driver.get(url=url)

        time.sleep(15)

        try:
            titles_with_urls = driver.find_elements(by=By.XPATH, value="//div[@class='List-results-items']/xpl-results-item/div/div/h3/a")
        except:
            print("Error Occured.")


        print("\n\n--------------------------------------------------")

        print(f"\nFor Page: {url}>>>>>>>>>>>>>>>>>>>>>>>>>")

        # print(titles_with_urls)

        urls = [{'urls': item.get_attribute('href')} for item in titles_with_urls]

        paper_urls.extend(url for url in urls)
    
        df = pd.DataFrame(data=paper_urls, columns=columns)
        df.to_csv("csv_files/failed_page_title_urls.csv", index=False)

    driver.close()
    

if __name__ == "__main__":
    main()
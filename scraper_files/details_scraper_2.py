import time
from tqdm import tqdm
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

paper_details = []

columns = ['abstracts', 'ieee_keywords', 'author_keywords']


def main():
    df = pd.read_csv("csv_files/paper_urls_ieee_access.csv")
    
    urls = df['urls'].to_list()

    driver = webdriver.Chrome()

    for index in tqdm(range(len(urls))):
        
        url = urls[index]

        driver.get(url=url)
        # time.sleep(5)

        print(f"\n{url}                >>>>>>>>>>>>>>>>>>>")

        try:
            # show_more_button = driver.find_element(by=By.CLASS_NAME, value="abstract-text-view-all document-abstract-toggle-btn")
            show_more_button = driver.find_element(by=By.XPATH, value="//div/a[@class='abstract-text-view-all document-abstract-toggle-btn']")
            show_more_button.click()
        except:
            print("No Show More Button.")

        try:
            abstract = driver.find_element(by=By.XPATH, value="//div[@class='u-mb-1']/div").text.replace("\n","")
            print(f"Abstract: {abstract}")
        except:
            abstract = ""
            print("Abstract Not Found!!")

        buttons = driver.find_elements(by=By.XPATH, value="//button[@class='accordion-link text-base-md-lh']")

        try:
            print("Button Clicked.")
            buttons[4].click()
            
            keywords = driver.find_elements(by=By.XPATH, value="//ul[@class='u-mt-1 u-p-0 List--no-style List--inline']")

            # print(keywords)
            if len(keywords) == 4:
                ieee_keywords = keywords[2].find_elements(by=By.XPATH, value="./li")
                ieee_keywords = [item.text.replace(",","").replace("\n","") for item in ieee_keywords]

                author_keywords = keywords[3].find_elements(by=By.XPATH, value="./li")
                author_keywords = [item.text.replace(",","").replace("\n","") for item in author_keywords]
            else:
                ieee_keywords = keywords[3].find_elements(by=By.XPATH, value="./li")
                ieee_keywords = [item.text.replace(",","").replace("\n","") for item in ieee_keywords]

                author_keywords = keywords[4].find_elements(by=By.XPATH, value="./li")
                author_keywords = [item.text.replace(",","").replace("\n","") for item in author_keywords]

            print(f"IEEE keywords: {ieee_keywords}")

            print(f"Author keywords: {author_keywords}")
            
        except:
            print("An error occured.")
            ieee_keywords = []
            author_keywords = []
        
        paper_details.append({
            'abstracts': abstract,
            'ieee_keywords': ieee_keywords,
            'author_keywords': author_keywords
        })

        df = pd.DataFrame(columns=columns, data=paper_details)
        df.to_csv("csv_files/paper_details_ieee_access.csv", index=False)

if __name__ == "__main__":
    main()


import pandas as pd
import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions


paper_details = []

columns = ['abstracts', 'ieee_keywords', 'author_keywords']


def main():
    df = pd.read_csv("csv_files/paper_urls_more.csv")

    
    urls = df['urls'].to_list()

    driver = webdriver.Chrome()

    for index in tqdm(range(0,len(urls))):
        
        url = urls[index]

        try:
            driver.get(url=url)
        except exceptions.TimeoutException as e:
            continue

        print(f"{url}                >>>>>>>>>>>>>>>>>>>")

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

        # buttons = driver.find_elements(by=By.XPATH, value="//button[@class='accordion-link text-base-md-lh']")
        

        # time.sleep(3)

        try:
            # buttons = driver.find_elements(by=By.XPATH, value="//button[@class='accordion-link text-base-md-lh']")
            button = driver.find_element(by=By.XPATH, value="//button[@id='keywords']")
            button.click()
            print("Button Clicked.")
        except:
            print("Button not clicked")
            continue
            
        keywords = driver.find_elements(by=By.XPATH, value="//ul[@class='u-mt-1 u-p-0 List--no-style List--inline']")
            

        try:
            if len(keywords) == 4:
                ieee_keywords = keywords[2].find_elements(by=By.XPATH, value="./li")
                ieee_keywords = [item.text.replace(",","").replace("\n","") for item in ieee_keywords]
                # print(f"IEEE keywords: {ieee_keywords}")

                author_keywords = keywords[3].find_elements(by=By.XPATH, value="./li")
                author_keywords = [item.text.replace(",","").replace("\n","") for item in author_keywords]

            elif len(keywords) == 2:
                ieee_keywords = keywords[1].find_elements(by=By.XPATH, value="./li")
                ieee_keywords = [item.text.replace(",","").replace("\n","") for item in ieee_keywords]
                author_keywords = []
            else:
                ieee_keywords = keywords[3].find_elements(by=By.XPATH, value="./li")
                ieee_keywords = [item.text.replace(",","").replace("\n","") for item in ieee_keywords]
                author_keywords = keywords[4].find_elements(by=By.XPATH, value="./li")
                author_keywords = [item.text.replace(",","").replace("\n","") for item in author_keywords]

            print(f"IEEE keywords: {ieee_keywords}")
            print(f"Author keywords: {author_keywords}")
        except Exception as e:
            print(f"An error occured. {e}")
            ieee_keywords = []
            author_keywords = []

            # print(f"IEEE keywords: {ieee_keywords}")
            
        # try:
        #     if len(keywords) == 4:
        #         # print("Len 4 case")
        #         author_keywords = keywords[3].find_elements(by=By.XPATH, value="./li")
        #         author_keywords = [item.text.replace(",","").replace("\n","") for item in author_keywords]
        #         print(f"Author keywords: {author_keywords}")
        #     else:
        #         author_keywords = keywords[4].find_elements(by=By.XPATH, value="./li")
        #         author_keywords = [item.text.replace(",","").replace("\n","") for item in author_keywords]
        #         print(f"Author keywords: {author_keywords}")
        # except Exception as e:
        #     print(f"An error occured. {e}")
        #     author_keywords = []
        #     print(f"Author keywords: {author_keywords}")

        paper_details.append({
            'abstracts': abstract,
            'ieee_keywords': ieee_keywords,
            'author_keywords': author_keywords
        })

        df = pd.DataFrame(columns=columns, data=paper_details)
        df.to_csv("csv_files/paper_details_more.csv", index=False)


if __name__ == "__main__":
    main()


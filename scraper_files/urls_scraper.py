import time
import tqdm
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

columns = ['urls']

paper_urls = []

failed_pages = []

def main():
    
    user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"

    chrome_options = Options()

    chrome_options.add_argument("--headless")

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument(f"--user-agent={user_agent}")

    driver = webdriver.Chrome()


    prefix_part = "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&pageNumber="
    suffix_part = "&returnFacets=ALL"

    # base_url = "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&pageNumber=&returnFacets=ALL"

    for index in tqdm(range(5473)):
        page_number = index+1
        url = prefix_part+str(page_number)+suffix_part

        # print(url)

        driver.get(url=url)

        time.sleep(5)

        try:
            titles_with_urls = driver.find_elements(by=By.XPATH, value="//div[@class='List-results-items']/xpl-results-item/div/div/h3/a")
        except:
            print("Error Occured.")

        # titles_with_urls = driver.find_elements(by=By.CLASS_NAME, value="List-results-items")

        if not len(titles_with_urls):
            print("Failed")
            failed_pages.append(page_number)
            failed = pd.DataFrame(data=failed_pages, columns=['page_number'])
            failed.to_csv("csv_files/failed_page_numbers.csv", index=False)
            continue

        # print(titles_with_urls)

        # buttons = driver.find_elements(by=By.XPATH, value="//a[@class='inst-sign-in']")


        print("\n\n--------------------------------------------------")
        print(f"For Page: {page_number}>>>>>>>>>>>>>>>>>>>>>>>>>")
        # print(titles_with_urls)

        urls = [{'urls': item.get_attribute('href')} for item in titles_with_urls]
        paper_urls.extend(url for url in urls)
        # print(paper_urls)
        #print(urls)
        # paper_urls.append(item for item in urls)

        # print(urls)


        # for item in titles_with_urls:
        #     title = item
        #     url = item.get_attribute('href')
        #     title_and_url = {
        #         'titles': title,
        #         'urls': url
        #     }

        #     paper_urls.append(title_and_url)
        # for title in titles_with_urls:

        # title_url = {'titles': title.text for title in titles_with_urls}

        


        df = pd.DataFrame(data=paper_urls, columns=columns)
        df.to_csv("csv_files/paper_urls.csv", index=False)

        # time.sleep()

        # title =  titles_with_urls[0].get_attribute("href")

        # urls = [item.get_atti]
        
        # print(title)

        # urls = 

    driver.close()

if __name__ == "__main__":
    main()
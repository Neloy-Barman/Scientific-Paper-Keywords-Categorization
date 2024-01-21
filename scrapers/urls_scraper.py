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
    

    driver = webdriver.Chrome()

    filter_with_urls = [
         {
            "type": "IEEE Access",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Access&returnFacets=ALL&",
            "total": 10000 
        },
        {
            "type": "IEEE Photonics Journal",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Photonics%20Journal&returnFacets=ALL&",
            "total": 5911 
        },
          {
            "type": "Transactions of the South African Institute of Electrical Engineers",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:Transactions%20of%20the%20South%20African%20Institute%20of%20Electrical%20Engineers&returnFacets=ALL&",
            "total": 4677 
        },
          {
            "type": "Journal of Systems Engineering and Electronics",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:Journal%20of%20Systems%20Engineering%20and%20Electronics&returnFacets=ALL&",
            "total": 4077 
        },
          {
            "type": "IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Journal%20of%20Selected%20Topics%20in%20Applied%20Earth%20Observations%20and%20Remote%20Sensing&returnFacets=ALL&",
            "total": 3354 
        },
          {
            "type": "Tsinghua Science and Technology",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:Tsinghua%20Science%20and%20Technology&returnFacets=ALL&",
            "total": 3164 
        },
          {
            "type": "CSEE Journal of Power and Energy Systems",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:CSEE%20Journal%20of%20Power%20and%20Energy%20Systems&returnFacets=ALL&",
            "total": 1343 
        },
          {
            "type": "IEEE Journal of the Electron Devices Society",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Journal%20of%20the%20Electron%20Devices%20Society&returnFacets=ALL&",
            "total": 1318 
        },
          {
            "type": "Journal of Modern Power Systems and Clean Energy",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:Journal%20of%20Modern%20Power%20Systems%20and%20Clean%20Energy&returnFacets=ALL&",
            "total": 1296
        },
          {
            "type": "IEEE Transactions on Neural Systems and Rehabilitation Engineering",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&returnFacets=ALL&refinements=PublicationTitle:IEEE%20Transactions%20on%20Neural%20Systems%20and%20Rehabilitation%20Engineering&returnFacets=ALL&",
            "total": 1241 
        },
          {
            "type": "Chinese Journal of Electronics",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&returnFacets=ALL&refinements=PublicationTitle:Chinese%20Journal%20of%20Electronics&returnFacets=ALL&",
            "total": 970 
        },
          {
            "type": "Journal of Lightwave Technology",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&returnFacets=ALL&refinements=PublicationTitle:Journal%20of%20Lightwave%20Technology&returnFacets=ALL&",
            "total": 714 
        },
          {
            "type": "SAIEE Africa Research Journal",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&returnFacets=ALL&refinements=PublicationTitle:SAIEE%20Africa%20Research%20Journal&returnFacets=ALL&",
            "total": 713 
        },
    ]

    for index in tqdm(range(0,1)):
        print(f"Starting with: {filter_with_urls[index]['type']}------------------------")
        page_range = math.ceil( filter_with_urls[index]['total'] / 100 )

        for page in range(page_range):

            page_number = page+1

            url = f"{filter_with_urls[index]['url']}pageNumber={str(page_number)}"

            driver.get(url=url)

            time.sleep(12)

            try:
                titles_with_urls = driver.find_elements(by=By.XPATH, value="//div[@class='List-results-items']/xpl-results-item/div/div/h3/a")
            except:
                print("Error Occured.")

            if len(titles_with_urls) == 0:
                print("\nFailed")
                failed_pages.append({
                    "title": filter_with_urls[index]['type'],
                    "url": filter_with_urls[index]['url'],
                    "page_number": page_number
                })
                failed = pd.DataFrame(data=failed_pages, columns=['title', 'url', 'page_number'])
                failed.to_csv("csv_files/failed_page_numbers.csv", index=False)
                continue

            print(f"\nFor Page: {page_number}>>>>>>>>>>>>>>>>>>>>>>>>>")

            # print(titles_with_urls)

            urls = [{'urls': item.get_attribute('href')} for item in titles_with_urls]

            paper_urls.extend(url for url in urls)
        
            df = pd.DataFrame(data=paper_urls, columns=columns)
            df.to_csv("csv_files/paper_urls_more.csv", index=False)


    driver.close()

if __name__ == "__main__":
    main()
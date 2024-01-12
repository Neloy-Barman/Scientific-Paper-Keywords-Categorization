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
            "type": "IEEE Open Journal of the Communications Society",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Open%20Journal%20of%20the%20Communications%20Society&returnFacets=ALL&",
            "total": 654  
        },
         {
            "type": "IEEE Transactions on Geoscience and Remote Sensing",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Transactions%20on%20Geoscience%20and%20Remote%20Sensing&returnFacets=ALL&",
            "total": 654  
        },
         {
            "type": "IEEE Sensors Journal",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Sensors%20Journal&returnFacets=ALL&",
            "total": 627  
        },
         {
            "type": "URSI Radio Science Bulletin",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:URSI%20Radio%20Science%20Bulletin&returnFacets=ALL&",
            "total": 585  
        },
         {
            "type": "IEEE Journal of Translational Engineering in Health and Medicine",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Journal%20of%20Translational%20Engineering%20in%20Health%20and%20Medicine&returnFacets=ALL&",
            "total": 510  
        },
         {
            "type": "IEEE Robotics and Automation Letters",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Robotics%20and%20Automation%20Letters&returnFacets=ALL&",
            "total": 464  
        },
         {
            "type": "IEEE Open Journal of Antennas and Propagation",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Open%20Journal%20of%20Antennas%20and%20Propagation&returnFacets=ALL&",
            "total": 443  
        },
         {
            "type": "Monthly Notices of the Royal Astronomical Society",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:Monthly%20Notices%20of%20the%20Royal%20Astronomical%20Society&returnFacets=ALL&",
            "total": 443 
        },
         {
            "type": "Journal of Communications and Networks",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:Journal%20of%20Communications%20and%20Networks&returnFacets=ALL&",
            "total": 443  
        },
         {
            "type": "Journal of Radiation Research",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:Journal%20of%20Radiation%20Research&returnFacets=ALL&",
            "total": 426 
        },
         {
            "type": "IEEE Transactions on Biomedical Engineering",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:IEEE%20Transactions%20on%20Biomedical%20Engineering&returnFacets=ALL&",
            "total": 405  
        },
         {
            "type": "CES Transactions on Electrical Machines and Systems",
            "url": "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&rowsPerPage=100&refinements=PublicationTitle:CES%20Transactions%20on%20Electrical%20Machines%20and%20Systems&returnFacets=ALL&",
            "total": 390  
        },
    ]



    # prefix_part = "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&pageNumber="
    # suffix_part = "&returnFacets=ALL"

    # base_url = "https://ieeexplore.ieee.org/search/searchresult.jsp?sortType=paper-citations&highlight=true&matchPubs=true&returnType=SEARCH&openAccess=true&pageNumber=&returnFacets=ALL"


    for index in tqdm(range(len(filter_with_urls))):
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
                failed.to_csv("csv_files/failed_page_numbers_2.csv", index=False)
                continue

                print("\n\n--------------------------------------------------")

            print(f"\nFor Page: {page_number}>>>>>>>>>>>>>>>>>>>>>>>>>")

            # print(titles_with_urls)

            urls = [{'urls': item.get_attribute('href')} for item in titles_with_urls]

            paper_urls.extend(url for url in urls)
        
            df = pd.DataFrame(data=paper_urls, columns=columns)
            df.to_csv("csv_files/paper_urls_2.csv", index=False)

    driver.close()
    


    # for ind in tqdm(range(5473)):
    #     page_number = ind+1
    #     url = prefix_part+str(page_number)+suffix_part

        # print(url)

        # driver.get(url=url)

        # time.sleep(5)

        # try:
        #     titles_with_urls = driver.find_elements(by=By.XPATH, value="//div[@class='List-results-items']/xpl-results-item/div/div/h3/a")
        # except:
        #     print("Error Occured.")

        # titles_with_urls = driver.find_elements(by=By.CLASS_NAME, value="List-results-items")

        # if not len(titles_with_urls):
        #     print("Failed")
        #     failed_pages.append({"page_number": page_number})
        #     failed = pd.DataFrame(data=failed_pages, columns=['page_number'])
        #     failed.to_csv("csv_files/failed_page_numbers.csv", index=False)
        #     continue

        # print(titles_with_urls)

        # buttons = driver.find_elements(by=By.XPATH, value="//a[@class='inst-sign-in']")


        # print("\n\n--------------------------------------------------")

        # print(f"For Page: {page_number}>>>>>>>>>>>>>>>>>>>>>>>>>")

        # # print(titles_with_urls)

        # urls = [{'urls': item.get_attribute('href')} for item in titles_with_urls]

        # paper_urls.extend(url for url in urls)

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

        


        # df = pd.DataFrame(data=paper_urls, columns=columns)
        # df.to_csv("csv_files/paper_urls.csv", index=False)

    # driver.close()

if __name__ == "__main__":
    main()
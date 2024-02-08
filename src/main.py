from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy.orm import sessionmaker

# as we import anything from models db is autom
from models import CancerResearch, engine


class NCCNDataScraper:
    """NCCN Datascraper
    Scraping cancer data and version information and processing.
    """

    def __init__(self):
        # here could be more driver settings
        # but for this project not necessary
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.nccn.org/guidelines/category_1")
        self._extracted_data = []

    def extract_data(self):
        # Extract with class names (Incase not proper class names can be used xpath)
        # but here not necessary
        all_item_names = self.driver.find_elements(By.CLASS_NAME, "item-name")
        all_version_info = self.driver.find_elements(By.CLASS_NAME, "item-version")
        for count, name in enumerate(all_item_names):
            splitted_version_info = all_version_info[count].text.lower().replace("version:", "").strip().split(".")

            self._extracted_data.append(
                CancerResearch(
                    name=name.text,
                    year_last_updated=splitted_version_info[1],
                    version_number=splitted_version_info[0],
                )
            )

    def import_data(self):
        # import data extracted
        Session = sessionmaker(bind=engine)
        session = Session()
        for elem in self._extracted_data:
            session.add(elem)

        session.commit()

        session.close()
        self._extracted_data = []


if __name__ == "__main__":
    scrape_nccn_data = NCCNDataScraper()
    scrape_nccn_data.extract_data()
    scrape_nccn_data.import_data()

# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Title", "Link", "Date"])

    for article in articles:
        article_tag = article.find("a")
        title = article_tag.get_text()
        url = article_tag["href"]
        date = article.find("time")["datetime"]
        print(title, url, date)
        csv_writer.writerow([title, url, date])
    

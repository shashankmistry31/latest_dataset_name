import requests,bs4
res = requests.get('https://catalog.data.gov/dataset?q=&sort=metadata_created+desc')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
data =soup.select('#content > div.row.wrapper > div > section:nth-child(1) > div.module-content > ul > li:nth-child(1) > div > h3 > a')
print("The latest dataset name is '" + data[0].text +"'")

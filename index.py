import json
import requests
from datetime import date
from datetime import date, timedelta


# solution found in https://stackoverflow.com/questions/68895582/how-to-avoid-a-bot-detection-and-scrape-a-website-using-python
headers = {
  'Accept': 'application/json',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json; charset=utf-8',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'channel': 'INTERNET',
}


url = "https://www.smartplay.lcsd.gov.hk/rest/param/api/v1/publ/venues/{}/info".format(209)
response = requests.get(url, headers=headers).json()
print(response)


for i in range(0, 8): #123
  dt = date.today() + timedelta(days=i)
  response = requests.get(
      'https://www.smartplay.lcsd.gov.hk/rest/facility-catalog/api/v1/publ/facilities?faCode=BASC&playDate={}'.format(dt), 
      headers=headers).json()
  # you should parse items here.
  print(response["data"]["morning"]["distList"][0]["venueList"][0]["fatList"][0]["sessionList"][0]["ssnStartDate"])
  print("\n")


# if not response["items"]:
#     break
# data_dict = json.loads(data)
# data_dict["pagination"]["page"] = data_dict["pagination"]["page"]+1 # get the next page.
# data = json.dumps(data_dict)

from bs4 import BeautifulSoup
import requests
import json
 
 
response = requests.get("https://www.udemy.com/course/codegym-python/")
soup = BeautifulSoup(response.text, "html.parser")

# Find the script tag with the JSON data
script_tag = soup.find('script', {'data-purpose': 'safely-set-inner-html:course-landing-page/seo-info'})

# Extract and parse the JSON content
if script_tag:
    json_data = json.loads(script_tag.string)

    # Check if "offers" key is present
    if "offers" in json_data[0]:
        # Get the first offer (assuming there is only one offer)
        offer = json_data[0]["offers"][0]

        # Check if "price" key is present in the offer
        if "price" in offer:
            price = offer["price"]
            print(price)
        else:
            print("Price key not found in the offer.")
    else:
        print("Offers key not found.")
else:
    print("Script tag not found.")
 
if int(price) < 500:  #將爬取的價格字串轉型為整數
    headers = {
        "Authorization": "Bearer " + "token",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
    params = {"message": "Python基礎課程和網路爬蟲入門實戰 已降價至" +  str(price) + "元"}
 
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)  #200
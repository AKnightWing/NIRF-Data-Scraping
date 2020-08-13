from msedge.selenium_tools import Edge, EdgeOptions
import random
import time

# Launch Microsoft Edge (Chromium)
options = EdgeOptions()
options.use_chromium = True
driver = Edge(r"C:\Users\Sid\Downloads\msedgedriver",options = options)
driver.maximize_window()

year = "2017"
#2017, 2018, 2019 or 2020

url = f"https://www.nirfindia.org/{year}/OverallRanking.html"

driver.get(url)

all_elems = driver.find_elements_by_tag_name("a")

stringlist=[]
for elem in all_elems:
    txt = elem.get_attribute("href")
    if type(txt)==str:
        if txt.endswith(".pdf"):
            stringlist.append(txt)

print(stringlist)

##CHANGE
all_elems = driver.find_elements_by_tag_name("td")

univ_dict={}
for i in range(len(all_elems)):
    print(f"i = {i}/{len(all_elems)}", end="\r")
    idstart = "IR17-"   #"IR-"
    #idstart is "IR17-" for 2017 and "IR-" for rest
    if idstart in all_elems[i].text:
        univ_dict[all_elems[i].text]=all_elems[i+1].text.split("\n")[0]

print(univ_dict)
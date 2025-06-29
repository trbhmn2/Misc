import requests
import random
from bs4 import BeautifulSoup
import googletrans
from googletrans import Translator
import os
translator = Translator()
links = []
query = []
error = "there was an error"
invalid = ["Oops nothing came up, can you rephrase that?", "Oh no, could you rephrase that?", "Argh nothing shows up, maybe ask something else", "I am trying my hardest, but nothing comes up", "Could you ask me again?"]


question = input("what would you like to ask? ")


url = 'https://www.google.com/search?q=' + question

r = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"})
soup = BeautifulSoup(r.text,"html.parser")
# print(soup.prettify)


try:
    # finding links
    for item in soup.find_all(attrs={'class': 'yuRUbf'}):
        for link in item.find_all('a'):
            x = link.get('href')
            # print(link.get('href'))
            links.append(x)
            for i in links:
                if i == '#':
                    links.remove("#")

    #Large text
    try:
        response2 = soup.find(class_="Z0LcW XcVN5d").getText() #large text
        answer2 = translator.translate(response2, dest="en", src="pl").text
        print(answer2)


    except:
        response2 = ""



    #Normal text
    try:
        response1 = soup.find(class_="hgKElc").getText()#Normal text
        answer1 = translator.translate(response1, dest="en", src="pl").text
        print(answer1)
        try:
            r = requests.get(links[1],headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"})
            getintopage = BeautifulSoup(r.content,"html.parser") 
            for p in getintopage.find_all('p'):
                pageanswer = p.getText()
                pageanswer = (pageanswer[:300] + '..') if len(pageanswer) > 300 else pageanswer
            pageanswer = translator.translate(pageanswer, dest="en", src="pl").text
            print(pageanswer)

        except:
            pageanswer = ""
        
        
    except:
        response1 = ""
        #getting into the page
        


    #finding the weather
    try:
        weatherc = soup.find(class_="wob_t TVtOme").getText() #finding the weather
        weatherf = soup.find(class_="wob_t").getText()
        Q = int(input("would you like the weather in celsius (1) or farenheit (2), input 1 or 2"))
        if Q == 1:
            print(weatherc, "Celsius")
        if Q == 2:
            print(weatherf, "Farenheit")
        weather = soup.find(class_="wob_dcp").getText()
        weather = translator.translate(weather, dest="en", src="pl").text
        print(weather)

    except:
        weather = ""

    #finding locations
    try:
        locationn = soup.find(class_="dbg0pd").getText()
        locationn = translator.translate(locationn, dest="en", src="pl").text
        locationd = soup.find(class_="rllt__details lqhpac").getText()
        print(locationn)
        print(locationd)


    except:
        locationn = ""
        locationd = ""

    #finding dates
    try:
        date = soup.find(class_="zCubwf").getText()
        date = translator.translate(date, dest="en", src="pl").text
        print(date)


    except:
        locationn = ""
        locationd = ""

    print("")
    print("")
    print("")
    print("If you want to read more on this topic, here are some links to visit!")

    hm = int(input("How many links would you like to see?"))
    for stuff in range (0,hm):
        for j in range(0,hm): #replace smth in url
            if '/search?safe=strict&q=related:' in links[j]:
                pre = links[j]
                post = pre.replace("/search?safe=strict&q=related:", "")
                links[j] = post
            if 'webcache' in links[j]:
                pre = links[j]
                post = pre[67:]
                links[j] = post
            if 'translate' in links[j]:
                pre = links[j]
                post = pre.replace(j, "")
                links[j] = post
        print(links[stuff])
        print()

except:
    os.system("clear")
    print(random.choice(invalid))
    print()
    another = input("would you like to get into the first page from the links?")
    if another == "yes":
        try:
            r = requests.get(links[1],headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"})
            getintopage = BeautifulSoup(r.content,"html.parser") 
            for p in getintopage.find_all('p'):
                pageanswer = p.getText()
                pageanswer = (pageanswer[:1000] + '..') if len(pageanswer) > 1000 else pageanswer
            pageanswer = translator.translate(pageanswer, dest="en", src="pl").text
            print(pageanswer)

        except:
            pageanswer = ""
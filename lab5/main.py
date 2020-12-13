import requests
from bs4 import BeautifulSoup 
from PIL import Image 
import csv 
import html_text
import webbrowser


#region zmienne globalne:

page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
)
soup = BeautifulSoup(page.content, "html.parser")
#endregion



#region 4-web-scraping-example4.py
def example4():
    # Create all_h1_tags as empty list
    all_h1_tags = [] 
    # Set all_h1_tags to all h1 tags of the soup
    for element in soup.select("h1"):
        all_h1_tags.append(element.text) 
    # Create seventh_p_text and set it to 7th p element text of the page
    seventh_p_text = soup.select("p")[6].text
    all_p = []
    for element in soup.select("p"): 
        all_p.append(element.text) 
    
    print("Menu example 4:")
    print("1.Przykład z zajęć\n2.Pokaż wszystkie\n3.Wyszukaj")
    wybor = input("Twój wybór:")
    if wybor == "1":
        print("Przykład z zajęć: ",all_h1_tags, seventh_p_text)
    elif wybor == "2":
        print("A teraz w pętli sprawdźmy:", len(all_p))
        licznik = 0
        while licznik<len(all_p):
            print(licznik+1, all_p[licznik])
            licznik +=1 
    elif wybor == "3":
        tekst = "który 'p' (max " +  str(len(all_p)-1) + " element wyświetlić?:"
        ktoryP = input(tekst)
        print(ktoryP ," element: ",all_h1_tags, soup.select("p")[int(ktoryP)].text)
    
#endregion

#region 4-web-scraping-example5.py
def example5(): 
    # Create top_items as empty list
    top_items = [] 
    # Extract and store in top_items according to instructions on the left
    products = soup.select("div.thumbnail")
    print("Liczba top items = ", len(products))
    for elem in products:
        title = elem.select("h4 > a.title")[0].text
        review_label = elem.select("div.ratings")[0].text
        info = {"title": title.strip(), "review": review_label.strip()}
        top_items.append(info)
    print("menu:\n1.przykła z zajęć\n2.Wyświetl tytuły produktów\n3.Znajdź produkt po tytule")
    wybor = input("twój wybór:")
    if wybor == "1":
        print(top_items)
    elif wybor == "2":
        print("sprawdźmy jakie produkty są: ")
        licznik = 0
        while licznik<len(top_items):
            print(top_items[licznik]["title"])
            licznik+=1
    elif wybor =="3":
        fragmentTekstu = input("podaj tekst jakiego szukasz:")
        licznik = 0
        jest = False
        while licznik<len(top_items):
            napis = top_items[licznik]["title"]
            if napis.count(fragmentTekstu) != 0:
                print(top_items[licznik]["title"])
                jest = True
            licznik+=1
        if jest == False:
            print("Nie znaleniono produktu")
        print("-----------------------------------------")
#endregion

#region 4-web-scraping-example6.py
def example6(): 
    # Create top_items as empty list
    image_data = []
    domena = "https://codedamn-classrooms.github.io"
    # Extract and store in top_items according to instructions on the left
    images = soup.select("img")
    print("Liczba obrazków =", len(images))
    for image in images:
        # print(type(image))
        src = image.get("src")
        alt = image.get("alt")
        image_data.append({"src": src, "alt": alt})


    print("menu:\n1.Przykład z zajęć\n2.Wyświetl obraz")
    wybor = input("twój wybór:")
    if wybor == "1":
        print(image_data)  
    elif wybor == "2":
        print("Który obraz wyświetlić:")
        licznik = 0
        while licznik<len(images):
            print(licznik,".",image_data[licznik]["alt"])
            licznik += 1
        wybor = input("podaj id:") 
        adres_obrazu = domena + image_data[int(wybor)]["src"]
        print("obraz powinnien się wyświetlić")
    # dobrze jest wiedzieć co pobieramy, wyświetlmy wieć obraz na ekranie:
        print(adres_obrazu)
        im = Image.open(requests.get(adres_obrazu, stream=True).raw)
        im.show() 
#endregion

#region 4-web-scraping-example6_lab.py
def example6_lab():
    # Create top_items as empty list
    all_links = []

    # Extract and store in top_items according to instructions on the left
    links = soup.select("a")
    print("Liczba linków = ", len(links))
    for ahref in links:
        text = ahref.text
        text = text.strip() if text is not None else ""

        href = ahref.get("href")
        href = href.strip() if href is not None else ""
        all_links.append({"href": href, "text": text})

    print("menu:\n1.Przykład z zajęć\n2.Otwórz wybrany link")
    wybor = input("twój wybór:")
    if wybor == "1":
        print(all_links)
    elif wybor == "2":
        licznik = 0
        domena = "https://codedamn-classrooms.github.io"
        
        while licznik<len(links):
            if all_links[licznik]["href"].count("https") > 0:
                adres = all_links[licznik]["href"]
            elif all_links[licznik]["href"].count("#") > 0: 
                adres = domena + "/" + all_links[licznik]["href"]
            else:
                adres = domena + all_links[licznik]["href"]
            print(licznik,".",adres)
            licznik += 1
        wybor = input("podaj id:")
        if all_links[int(wybor)]["href"].count("https") > 0: 
            adres = all_links[int(wybor)]["href"]
        elif all_links[int(wybor)]["href"].count("#") > 0: 
            adres = domena + "/" + all_links[int(wybor)]["href"]
        else: 
            adres = domena + all_links[int(wybor)]["href"]
        
        webbrowser.open(adres, new=2)
#endregion

#region 4-web-scraping-example7.py 
def example7(): 
    
    # Create top_items as empty list
    all_products = []

    # Extract and store in top_items according to instructions on the left
    products = soup.select('div.thumbnail')
    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()
        reviews = product.select('div.ratings')[0].text.strip()
        image = product.select('img')[0].get('src')

        all_products.append({
            "name": name,
            "description": description,
            "price": price,
            "reviews": reviews,
            "image": image
    })


    keys = all_products[0].keys() 
    print("keys = ", keys)

    with open('products.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_products)
    
#endregion

#region 
def example8():
    odpowiedz = requests.get("https://pl.wikipedia.org/wiki/Zygmunt_III_Waza")
    print("odpowiedź = \n", odpowiedz)
    print(odpowiedz.status_code)
    html_text: str = odpowiedz.text
    # print("Strona o Wazie = \n", html_text)

    user1 = requests.get("https://jsonplaceholder.typicode.com/users/1")
    json_text: dict = user1.json()
    print("url = ", user1.url)
    print("json_text = ", json_text)
    print("history = ", user1.history)

    # print("odpowiedź tekstowa = \n", html_text)

    html_doc = """<html>
    <head>
        <title>Moja pierwsza strona!</title>
    </head>
    <body>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec posuere elit at malesuada tempor. Donec eget ligula in ante auctor luctus. Phasellus iaculis porttitor gravida. Donec eget sem lorem. Morbi a libero imperdiet, viverra tellus ac, consequat tortor. Suspendisse nibh massa, accumsan non neque a, vestibulum commodo dui.</p>
    <p>Phasellus vestibulum ut <br>erat sit amet ullamcorper. Nam at elit feugiat, dapibus ante vitae, ullamcorper dui. Nunc rutrum at nibh tincidunt mattis. In finibus sed ante vel mollis. Donec at semper metus. Aenean quis consectetur risus. Sed suscipit felis sed ex pretium euismod. In fermentum mi a odio porttitor, dapibus aliquet leo accumsan. Suspendisse pretium augue et faucibus euismod. Quisque risus metus, ultricies nec tortor at, efficitur convallis nunc.</p>
    <ul>
        <li>Pierwszy punkt</li>
        <li>Drugi punkt</li>
        <li>Trzeci punkt</li>
    </ul>
    <ol>
        <li>Pierwszy punkt</li>
        <li>Drugi punkt</li>
        <li>Trzeci punkt</li>
    </ol>
    <table border="3" bgcolor="#ff00ff" class="tabela blog">
        <tr><th>Naglowek 1</th><th>Naglowek 2</th></tr>
        <tr><td>komorka 11</td><td>komorka 12</td></tr>
        <tr><td>komorka 21</td><td>komorka 22</td></tr>
    </table>
    <a href="http://google.pl">Arcyciekawa strona</a>
    </body>
    </html>"""

    url_amw = "https://www.amw.gdynia.pl/"
    # page = requests.get(url_amw)
    # soup = BeautifulSoup(page.content, "html.parser")
    soup = BeautifulSoup(html_doc, "lxml")

    # Extract head of page
    page_head = soup.head
    print("Typ = ", type(page_head))

    first_p = soup.select("p")[0].text
    print("First p =\n", first_p)

    another_p = soup.select("p")[1].text
    print("Another p =\n", another_p)

    print("Liczba zanaczników 'p' = ", len(soup.select("p")))


    # title
    print("TITLE")
    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)
    print(soup.title.text)
    print(soup.title.contents)
    print("\n")

    # ul
    print("UL")
    print(soup.ul.text)
    print("\n")


    # atrybuty
    print("ATRYBUTY")
    print(soup.table["border"])
    print(soup.table.has_attr("border"))
    print(soup.table.has_attr("href"))
    print(soup.table.attrs)
    print("\n")


    # find
    print("FIND")
    print(soup.find_all("p"))
    print(soup.find(border="3"))
    print("Find klasy = ", soup.find(class_="tabela"))
    print("Select klasy = ", len(soup.select("table.tabela")))
    print(soup.find(href=True))
    # print("Find src = \n", soup.find(src=False)) # be careful!

    print("\n")

    # next
    print("NEXT")
    print(soup.th.next_element)
    print(soup.tr.next_sibling)
    print(soup.tr.next_sibling.next_sibling)
#endregion

#region przykłady 
def przyklady(wybor_menu):
    if wybor_menu == "1": 
        print("------------------------------------------")
        example4()
    elif wybor_menu == "2":
        print("------------------------------------------")
        example5()
    elif wybor_menu == "3":
        print("------------------------------------------")
        example6()
    elif wybor_menu == "4":
        print("------------------------------------------")
        example6_lab()
    elif wybor_menu == "5":
        print("------------------------------------------")
        example7()

    else:
        print("brak pozycji")
#endregion
#region menu
def menu():
    wyjscie_z_programu = False
    wybor_menu = -1
    while wyjscie_z_programu==False:
        print("Menu:")
        print("1. 4-web-scraping-example4.py")
        print("2. 4-web-scraping-example5.py")
        print("3. 4-web-scraping-example6.py")
        print("4. 4-web-scraping-example6_lab.py")
        print("5. 4-web-scraping-example7.py")
        print("0. Wyjście")

        wybor_menu = input("Wprowadź pozycję z menu i zatwierdź enterem:")
        print("Twoj wybor to:" + wybor_menu)
        if wybor_menu == "0":
            print("Wyjście z programu")
            wyjscie_z_programu = True
        else: 
            przyklady(wybor_menu)
    quit()
#endregion 
menu()
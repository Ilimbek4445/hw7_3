import requests, sqlite3
from datetime import datetime, timezone



connect = sqlite3.connect('Laptops.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS laptops(
               id INTEGER PRIMARY KEY,
               title TEXT,
               price INTEGER,
               created TEXT
               
)''')

connect.commit()

def parsing_sulpak():
    n = 0
    for i in range(1, 21):
        url = f'https://www.sulpak.kg/f/noutbuki?page={i}'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')
        # print(response)
        laptops = soup.find_all('div', class_="product__item-name")
        prices = soup.find_all('div', class_="product__item-price")
        # print(laptops)
        for name, price in zip(laptops, prices):
            n += 1
            current_price = "".join(price.text.split())
            print(n, name.text, current_price)
            
            data = datetime.now()
            l = name.text, current_price, data

            cursor.execute('INSERT INTO laptops(title, price, created) VALUES (?, ?, ?)', l)
        connect.commit()
        cursor.execute("SELECT * FROM laptops")



        
parsing_sulpak()
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

base_url = "http://quotes.toscrape.com"

def scrape_quotes():
    url = "/page/1"
    all_quotes = []
    while url:
        res = requests.get(base_url + url)
        soup = BeautifulSoup(res.text, "html.parser")
        print(f"Now scraping {base_url}{url}....")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
                }
                )
        
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(3)
    return all_quotes

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print(quote["author"])
    print("Here's a quote: ")
    print(quote["text"])
    
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Guesses reaming: {remaining_guesses} \n" +
                "Who said this quote?: ")
        if guess.lower() == quote["author"].lower():
            print("Yay, you're not an idiot")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{base_url}{quote['bio-link']}") 
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint:\nThe author was born on {birth_date} " +
                    f"{birth_place}")
        elif remaining_guesses == 2:
            first_initial = quote["author"][0]
            print(f"Here's a hint:\nThe author's first initial is {first_initial}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[-1][0]
            print(f"Here's a hint:\nThe author's last initial is {last_initial}")
        else:
            print(f"Sorry you ran out of guesses.\nThe answer was " +
                    f"{quote['author']}")
    
    again = ""
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)? ")
    
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("Wuss!")

quotes = scrape_quotes()
start_game(quotes)

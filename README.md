# PokeCard

This script is an app to manage your pokemon cards you want to sell.  
There is the simple steps to use it :  

---
## Installation :
Make sur you have python working and execut this commande line 
```sh
pip install sqlite3 flask bs4 webbrowser
```

This wil install you all the dependencies

---
## Preparation :
First, make sure you have an internet connection.

Then, execute the script `init_bd.py`


If you want to fill your data before use the app, fill `cards.txt` file where you will put :
```txt
<Pokemon card name> : <Card status (mint, good, ect)>
<link of the card in cardmarket>
```

Finaly, execute `fill_bd.py`  
It will take a moment

---
## How to use
To lauch the app, execute `app.py`  

You can add, remove and edit all the cards in the app.

### Add a card
Just click on `Add Card` in the menu and fill the form. You must put a name and the link to the card, but the card state isn't mandatory

### Edit Card
Click on your card and press the `Edit` button. You have just to change the values in the form.

### Delete Card
Go in the edit mode, click delete then comfirm
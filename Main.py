import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime


# data + time asking
ticker = input("Read the stock ticker :")
print("Date format = YYYY-MM-DD")
start_period = input("Choose the start date :")
end_period = input("Choose the end data : ")

# data function
def get_ticker_data(ticker, start_period, end_period):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_period, end=end_period)
    return data
    
# get the data
data = get_ticker_data(ticker, start_period, end_period)

print(data.head()) #apercu de la data


# print data graph from close
plt.figure(figsize=(12, 6)) # definition de la taille (l x h)
plt.plot(data.index, data['Close'], label='Prix de clôture')


# nom des axe x et y
plt.xlabel('Date') 
plt.ylabel('Prix de cloture') 

# add last price 
last_date = data.index[-1] # selection of the last date 
last_close = data['Close'].iloc[-1] # selection of the last close
plt.text(last_date, last_close, f'{last_close:.2f}',
         fontsize=8, color='black', ha='left', va='bottom')
plt.axhline(y=last_close, color='black', linestyle='--', linewidth=1) #ajout d'une ligne prix de cloture

# mise en forme du graphique
plt.title(f'Cours de {ticker.upper()} de {start_period.upper()} à {end_period.upper()}') #titre du graph
plt.grid(True)  # ajout de grillet
plt.legend()    # affichage d'une legende

# impression du graph
plt.show()
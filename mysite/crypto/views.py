from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
	#Grab Data
	# Source: https://min-api.cryptocompare.com/documentation?key=Price&cat=multipleSymbolsFullPriceEndpoint
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?" \
		"fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX,DOGE,XMR" \
		"&tsyms=USD,EUR")#
	price = json.loads(price_request.content)

	# Grab crypto nes
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	news = json.loads(news_request.content)
	return render(request, 'home.html', {"news": news, 'price': price})


def prices(request):
	if request.method == "POST":
		quote = request.POST['quote'] # quote is the name of the search button in the base.html (which is included in prices.htlm)
		quote = quote.upper()
		serch_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?" \
		"fsyms=" + quote + \
		"&tsyms=USD,EUR")#
		serch_request = json.loads(serch_request.content)
		return render(request, 'prices.html', {'quote':quote, 'serch_request': serch_request})
	else:
		notFound = "Enter a crypto currency symbol into the form above..."
		return render(request, "prices.html", {'notFound': notFound})
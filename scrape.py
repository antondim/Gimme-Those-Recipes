import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import pandas as pd


# Don't display browser that selenium opens
display = Display(visible=0, size=(800, 600))
display.start()

# select webdriver
driver = webdriver.Firefox(executable_path=r'/usr/bin/geckodriver')

base_url = 'https://akispetretzikis.com'
urls=[]
urls.append('https://akispetretzikis.com/el/tags/grhgora-piata')

# create data arrays
name_of_recipes=[]
avg_recipe_ratings=[]
food_categories=[]


while len(urls) > 0:
	print(urls)
	url = urls.pop(0)
	print(url)
	time.sleep(2)
	# 1. open the desired URL
	# 2. get the html source code of page
	# 3. parse the code using bs
	driver.get(url)
	source_of_page = driver.page_source
	soup = BeautifulSoup(source_of_page,'html.parser')

	next_url = soup.findAll('div',{'id':'next_page_link'})
	if next_url:
		urls.append(base_url + str(next_url[0].find('a')['href']))
		print('Next URl is :', urls[0])

		# Search for all the desired info in html source code
		recs = soup.findAll('div',attrs={'class':'col-md-4 col-sm-4 col-xs-12'})

		for recipe in recs:
			name_of_recipes.append(recipe.div.div.a.text)
			var1 = recipe.findAll('div', attrs={'class':'v_cat'})
			food_categories.append(var1[0].a.text)
			var2 = recipe.findAll('div', attrs={'class':'score-cont'})
			avg_recipe_ratings.append(var2[0].div["data-average-score"])

		# put data in dataframe
		data_frame = pd.DataFrame({'Recipe title':name_of_recipes,'Food categories':food_categories,'Ratings':avg_recipe_ratings},\
																	 columns = ['Recipe title','Food categories','Ratings']) 
		data_frame.to_csv('~/Desktop/scrape/syntages.csv', index=False, encoding='utf-8')

# close "shadow display" & internet page
driver.quit()
display.stop()
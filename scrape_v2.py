#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import pandas as pd
import re
import time

# Don't display browser that selenium opens (choice)
display = Display(visible=0, size=(800, 600))
display.start()

# select webdriver
driver = webdriver.Firefox(executable_path=r'/usr/bin/geckodriver')

# 1. open the desired URL
# 2. get the html source code of page
# 3. parse the code using bs
base_url = 'https://akispetretzikis.com/el/tags/grhgora-piata'
driver.get(base_url)
source_of_page = driver.page_source

# create data arrays
name_of_recipes=[]
avg_recipe_ratings=[]
food_categories=[]

counter = 1

#Scrape only 20 of n pages
while counter <= 20:	
	print(counter)

	# Locate elements based on their class name
	recs = driver.find_elements_by_class_name('texts')
	score_recs = driver.find_elements_by_class_name('score-cont')
	food_categs = driver.find_elements_by_class_name('v_cat')

	for recipe in recs:
		name_of_recipes.append(recipe.get_attribute("textContent"))
	for scores in score_recs:
		avg_recipe_ratings.append(re.sub('[^\d\.]', '', scores.get_attribute("innerHTML")[722:725]).encode('utf-8'))
	for food_c in food_categs:
		food_categories.append(food_c.get_attribute("textContent"))

	# put data in dataframe
	data_frame = pd.DataFrame({'Recipe title':name_of_recipes,'Food categories':food_categories,'Ratings':avg_recipe_ratings},\
																 columns = ['Recipe title','Food categories','Ratings'])
	data_frame.to_csv('~/Projects/scrape/syntages.csv', index=False, encoding='utf-8')

	time.sleep(2) # sleep time (choice)

	# click "Show more" button if it exists
	if (driver.find_element_by_link_text("Περισσότερες συνταγές")):
		print(driver.find_element_by_link_text("Περισσότερες συνταγές").get_attribute("outerHTML"))
		driver.find_element_by_link_text("Περισσότερες συνταγές").click()
		counter = counter + 1;
	else:
		break

#remove duplicates from csv file
df = pd.read_csv('~/Projects/scrape/syntages.csv')
df.drop_duplicates(subset=None, inplace=True)
#replace NaN values with zeros
df=df.fillna(0)
#write to new csv file
df.to_csv('~/Projects/scrape/syntages_non_duplicates.csv', index=False, encoding='utf-8')

# close "shadow display" & internet page
driver.quit()
display.stop()

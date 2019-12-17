# Web-Scraping
This Python project, is an attempt to scrape free access (as stated in [robots.txt](https://en.wikipedia.org/wiki/Robots_exclusion_standard)) text data from an online cooking website, in order to produce statistics based on the extracted data, which we inititally parse into a [csv file](https://en.wikipedia.org/wiki/Comma-separated_values).

## Getting Started
Scraping, is a way of collecting text data from websites, taking advantage of their html source code.

### Prerequisites
In this project, we make use of the following libraries:

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Library for extracting data from HTML and XML files

- [Selenium](https://selenium-python.readthedocs.io/installation.html#introduction): Library, that provides API to access websites' data through a WebDriver (Firefox, Chrome etc)

- [Pandas](https://pandas.pydata.org/): Library, providing high-performance, convenient data structures and data analysis tools

### Installing

**1) BeautifulSoup** :
```
sudo apt-get install python-bs4
```
or
```
sudo pip install beautifulsoup4
```


**2) Selenium** :

```
sudo pip install selenium
```
  Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to        be [installed](https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu) beforehands.
  
**3) pandas** :

```
sudo pip install pandas
```
## Challenges faced in the coding procedure



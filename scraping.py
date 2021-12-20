from bs4 import BeautifulSoup
import requests


"""BEAUTIFUL SOUP HTML PARSING"""
# Use SELECT() method  to find multiple elements and select_one() to find a single element.
from bs4 import BeautifulSoup
data = """
        <ul>
            <li class="item">item1</li>
            <li class="item">item2</li>
            <li class="item">item3</li>
        </ul>
        """
soup = BeautifulSoup(data, "html.parser")
for item in soup.select("li.item"):
    print(item.get_text())




# scrapping a web page table content
res = requests.get('https://www.codechef.com/problems/easy')
page = BeautifulSoup(res.text , 'lxml') # the text field contains the source of the page
# Now use a CSS selector in order to get the table containing the list of problems
datatable_tags = page.select('table.dataTable') # The problems are in the <table> tag, with classnames of datatables
# with class "dataTable"
# We extract the first tag from the list, since that's what we desire
datatable = datatable_tags[0]
# Now since we want problem names, they are contained in <b> tags, which are
# directly nested under <a> tags
prob_tags = datatable.select('a > b')
prob_names = [tag.getText().strip() for tag in prob_tags]
print(prob_names)



# DOWNLOADING WEB PAGE CONTENT of any website
from urllib.request import urlopen
response = urlopen('https://gmail.com')
data = response.read()
# The received bytes should usually be decoded according the response's character set
encoding = response.info().get_content_charset()
html = data.decode(encoding)
print(html)
<img align="right" src="./logo.png">

Lab 16. Web Scraping - Extracting Useful Data from Websites
------------------------------------------------------------------------



In this lab, you will learn about web scraping. You will also learn
about the `beautifulsoup` library in Python, which is used for
extracting information from websites.

In this lab, we will cover the following topics:


-   What is web scraping?
-   Data extraction
-   Extracting information from Wikipedia




Data extraction
----------------------------------



In this section, we are going to see the actual data extraction process. Python has the `beautifulsoup`
library to perform the data extraction task. We are also going to use
the requests library of Python.


#### The beautifulsoup library


Now, to use the `requests` and `beautifulsoup`
functionality in your scripts you must import these two libraries using
the `import` statement. Now, we are going to see an example of
parsing a web page. Here, we are going to parse a web page, which is a
top news page from the IMDb website. For that purpose, create
a `parse_web_page.py` script and write the following content
in it:


```
import requests
from bs4 import BeautifulSoup

page_result = requests.get('https://www.imdb.com/news/top?ref_=nv_nw_tp')
parse_obj = BeautifulSoup(page_result.content, 'html.parser')

print(parse_obj)
```

Run the script and you will get the output as follows:


```
student@ubuntu:~/work$ python3 parse_web_page.py
Output:
<!DOCTYPE html>

<html xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://ogp.me/ns#">
<head>
<meta charset="utf-8"/>
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<meta content="app-id=342792525, app-argument=imdb:///?src=mdot" name="apple-itunes-app"/>
<script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:'java'};</script>
<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadTitle", {wb: 1});
    }
</script>
<script>(function(t){ (t.events = t.events || {})["csm_head_pre_title"] = new Date().getTime(); })(IMDbTimer);</script>
<title>Top News - IMDb</title>
<script>(function(t){ (t.events = t.events || {})["csm_head_post_title"] = new Date().getTime(); })(IMDbTimer);</script>
<script>
    if (typeof uet == 'function') {
      uet("be", "LoadTitle", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "LoadTitle", {wb: 1});
    }
</script>
<link href="https://www.imdb.com/news/top" rel="canonical"/>
<meta content="http://www.imdb.com/news/top" property="og:url">
<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadIcons", {wb: 1});
    }
```

In the preceding example, we collected a page and parsed it using
`beautifulsoup`. First, we imported the `requests`
and `beautifulsoup` modules. Then, we collected the URL using
the `GET` request and assigned that URL to the
`page_result` variable. Next, we created a
`beautifulsoup` object `parse_obj`. This object will
take `page_result`.content as its argument from requests and
then the page parsed using `html.parser`.

Now, we are going to extract the content from a class and a tag. To
perform this operation, go to your web browser and right-click on the
content, that you want to extract and scroll down so you can see the
**Inspect** option. Click on that and you will get the class
name. Mention it in your program and run your script. For that, create
a `extract_from_class.py`script and write the following
content in it:


```
import requests
from bs4 import BeautifulSoup

page_result = requests.get('https://www.imdb.com/news/top?ref_=nv_nw_tp')
parse_obj = BeautifulSoup(page_result.content, 'html.parser')

top_news = parse_obj.find(class_='news-article__content')
print(top_news)
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 extract_from_class.py
Output :
<div class="news-article__content">
<a href="/name/nm4793987/">Issa Rae</a> and <a href="/name/nm0000368/">Laura Dern</a> are teaming up to star in a limited series called “The Dolls” currently in development at <a href="/company/co0700043/">HBO</a>.<br/><br/>Inspired by true events, the series recounts the aftermath of Christmas Eve riots in two small Arkansas towns in 1983, riots which erupted over Cabbage Patch Dolls. The series explores class, race, privilege and what it takes to be a “good mother.”<br/><br/>Rae will serve as a writer and executive producer on the series in addition to starring, with Dern also executive producing. <a href="/name/nm3308450/">Laura Kittrell</a> and <a href="/name/nm4276354/">Amy Aniobi</a> will also serve as writers and co-executive producers. <a href="/name/nm0501536/">Jayme Lemons</a> of Dern’s <a href="/company/co0641481/">Jaywalker Pictures</a> and <a href="/name/nm3973260/">Deniese Davis</a> of <a href="/company/co0363033/">Issa Rae Productions</a> will also executive produce.<br/><br/>Both Rae and Dern currently star in HBO shows, with Dern appearing in the acclaimed drama “<a href="/title/tt3920596/">Big Little Lies</a>” and Rae starring in and having created the hit comedy “<a href="/title/tt5024912/">Insecure</a>.” Dern also recently starred in the film “<a href="/title/tt4015500/">The Tale</a>,
            </div>
```



Now, we are going to see an example of extracting content from a
particular tag. In this example, we are going to extract the content
from the `<a>` tag. Create
an `extract_from_tag.py`script and write the following content
in it:


```
import requests
from bs4 import BeautifulSoup

page_result = requests.get('https://www.imdb.com/news/top?ref_=nv_nw_tp')
parse_obj = BeautifulSoup(page_result.content, 'html.parser')

top_news = parse_obj.find(class_='news-article__content')
top_news_a_content = top_news.find_all('a')
print(top_news_a_content)
```

Run the script and you will get the output as
follows:


```
student@ubuntu:~/work$ python3 extract_from_tag.py
Output:
[<a href="/name/nm4793987/">Issa Rae</a>, <a href="/name/nm0000368/">Laura Dern</a>, <a href="/company/co0700043/">HBO</a>, <a href="/name/nm3308450/">Laura Kittrell</a>, <a href="/name/nm4276354/">Amy Aniobi</a>, <a href="/name/nm0501536/">Jayme Lemons</a>, <a href="/company/co0641481/">Jaywalker Pictures</a>, <a href="/name/nm3973260/">Deniese Davis</a>, <a href="/company/co0363033/">Issa Rae Productions</a>, <a href="/title/tt3920596/">Big Little Lies</a>, <a href="/title/tt5024912/">Insecure</a>, <a href="/title/tt4015500/">The Tale</a>]
```

 



In the preceding example, we are extracting contents from the
`<a>` tag. We used the `find_all()` method to
extract all `<a>` tag contents from the
`'news-article__content'` class.



Extracting information from Wikipedia
--------------------------------------------------------



In this section, we are going to see an example of a list of dance forms from Wikipedia. We are going to
list all classical Indian dances. For that, create
a `extract_from_wikipedia.py`script and write the following
content in it:


```
import requests
from bs4 import BeautifulSoup

page_result = requests.get('https://en.wikipedia.org/wiki/Portal:History')
parse_obj = BeautifulSoup(page_result.content, 'html.parser')

h_obj = parse_obj.find(class_='hlist noprint')
h_obj_a_content = h_obj.find_all('a')

print(h_obj)
print(h_obj_a_content)
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 extract_from_wikipedia.py
Output:
<div class="hlist noprint" id="portals-browsebar" style="text-align: center;">
<dl><dt><a href="/wiki/Portal:Contents/Portals" title="Portal:Contents/Portals">Portal topics</a></dt>
<dd><a href="/wiki/Portal:Contents/Portals#Human_activities" title="Portal:Contents/Portals">Activities</a></dd>
<dd><a href="/wiki/Portal:Contents/Portals#Culture_and_the_arts" title="Portal:Contents/Portals">Culture</a></dd>
<dd><a href="/wiki/Portal:Contents/Portals#Geography_and_places" title="Portal:Contents/Portals">Geography</a></dd>
<dd><a href="/wiki/Portal:Contents/Portals#Health_and_fitness" title="Portal:Contents/Portals">Health</a></dd>
<dd><a href="/wiki/Portal:Contents/Portals#History_and_events" title="Portal:Contents/Portals">History</a></dd>
<dd><a href="/wiki/Portal:Contents/Portals#Mathematics_and_logic" title="Portal:Contents/Portals">Mathematics</a></dd>
<dd><a href="/wiki/Portal:Contents/Portals#Natural_and_physical_sciences" title="Portal:Contents/Portals">Nature</a></dd>
<dd><a href="/wiki/Portal:Contents/Portals#People_and_self" title="Portal:Contents/Portals">People</a></dd>
In the preceding example, we extracted the content from Wikipedia. In this example also, we extracted the content from class as well as tag.
....
```



Summary
--------------------------



In this lab, you learned about what web scraping is. We learned
about two libraries that are used in extracting the data from a web
page. We also extracted information from Wikipedia.

In the next lab, you will learn about statistics gathering and
reporting. You will learn about the NumPy module, data visualization,
and displaying data using plots, graphs, and charts.



Questions
----------------------------



1.  What is web scrapping?
2.  What are the web crawlers?
3.  Can you scrape data behind a login page?
4.  Can you crawl Twitter?
5.  Is it possible to scrap the Java script pages? If yes, how?


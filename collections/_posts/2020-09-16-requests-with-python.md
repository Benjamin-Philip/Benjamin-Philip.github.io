---
layout: post
title: Website Authentication with Python
subtitle: POSTs with the Request Library
tags: [Webscraping, Python]
comments: true
---

When you Web scrape something, you are essentially taking data stored on
the web, and extracting all the information from it (Atleast whatever you
need). Quite often, that content needs an Authentication.  Whether it is
your sibling's Assignment page, to your work's local progress site (If
such a thing exists). Here is a tutorial on how to webscrape *that* Site.

To understand this tutorial, and to write scripts that would log on to
various websites, you would need some basic understanding of HTML. Maybe
not enough to make some amazing looking websites but, to have a general
idea of what is going on.

In this tutorial I am working with python 3.8 and will be using the `request`
and `BeautifulSoup` libraries. 

# Installation

Webscraping is generally done with the BeautifulSoup library. BeautifulSoup
is generally used for websites with HTML content (It is a HTML parser). 

{: .box-warning}
**Warning:** This tutorial is meant for BeautifulSoup. If your website
login page uses a lot of Javascript, You will need
to use Selenium as BeautifulSoup can't parse Javascript, The process
for Authenticating with Selenium may be completely different.(This is
because Selenium may already have functions for authentication.)

We will also be using the requests library to handle cookies, basic Authentication,
HTTP(S) Proxy support etc.

You can install BeautifulSoup and requests with the following:

```
pip install BeautifulSoup4
pip install requests
```

If you use pip3 in Linux, replace pip with pip3.

# What happens in between?

Logging into a website with a script requires a brief knowledge of HTML
and how the web works.  Let's briefly look at how a site works.

Websites have two important computers in-between: The Client and the Server-side.
The Client is the user(you) and the Server is the computer hosting the Website
and where all the business logic is executed.

When you click a link, you make a request to the Server-side to fetch
you the HTML Files, and static files like CSS and JavaScript Files.
This request is called as the GET request.

However, when you fill in a form, upload a document - in general submit
some information. You are passing some information to the server. This
request is called a POST request.

When you try to login, You send a GET request for the login page to the
Server. You then enter in al your data and you sent a POST request to
the server. You then will send a GET request for your home page. If the
Authentication was successful, you would be given the homepage, or else,
be denied.

# Inspecting a website

In order to POST your username and password, you will need to know the
basic structure of your target website because you will need to know
the parameter names of your data. For this you can use the `Inspect
element` feature of your browser. This usually can be accessed with a
right click. If you can't find it, you can always search how to inspect
element on your browser.

![Inspecting on Brave]({{ page.assets-var | append: '2020-09-15.png'}})

# Writing the script

For purpose of this article, we shall be using the [Quotes to
Scrape](http://quotes.toscrape.com/login) website. Since this website is
just used as proof of concept, any username and password goes. I shall
be using ben as the username and 123 as the password.

Now for input, HTMl makes use of the input tag. This is where we can find
the parameter names of our username and password. We will have to inspect
the HTML page and find the tags. 

Since I am lazy, I am going to stick with printing the HTML files on my terminal.
For those more comfortable with the GUI, you can view "Inspecting a website".
The script, for the initial part of our program is a follows:

```python
from bs4 import BeautifulSoup
from requests import Session

with Session() as s:
    # initial GET request
    site = s.get("http://quotes.toscrape.com/login")
    # parsing content
    html_content = BeautifulSoup(site.content, "html.parser")
    print(html_content)
```

Let's see what is the output of that:

```HTML
<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Quotes to Scrape</title>
<link href="/static/bootstrap.min.css" rel="stylesheet"/>
<link href="/static/main.css" rel="stylesheet"/>
</head>
<body>
<div class="container">
<div class="row header-box">
<div class="col-md-8">
<h1>
<a href="/" style="text-decoration: none">Quotes to Scrape</a>
</h1>
</div>
<div class="col-md-4">
<p>
<a href="/login">Login</a>
</p>
</div>
</div>
<body>
<form accept-charset="utf-8" action="/login" method="post">
<input name="csrf_token" type="hidden" value="HctNZCgdWSvXRbhlTGoaJLPQnwrOufVBYKykMAeImpxDizqFUjsE"/>
<div class="row">
<div class="form-group col-xs-3">
<label for="username">Username</label>
<input class="form-control" id="username" name="username" type="text"/>
</div>
</div>
<div class="row">
<div class="form-group col-xs-3">
<label for="username">Password</label>
<input class="form-control" id="password" name="password" type="password"/>
</div>
</div>
<input class="btn btn-primary" type="submit" value="Login"/>
</form>
</body>
</div>
<footer class="footer">
<div class="container">
<p class="text-muted">
                Quotes by: <a href="https://www.goodreads.com/quotes">GoodReads.com</a>
</p>
<p class="copyright">
                Made with <span class="sh-red">❤</span> by <a href="https://scrapinghub.com">Scrapinghub</a>
</p>
</div>
</footer>
</body>
</html>
```

Whoa! That's a lot!

### Using grep
 
Now we only care about the input tags, the rest of it doesn't matter to
us. So here is a "trick" that will only work for the Unix users: we will
pass the output from the python script, and using grep, we will look for
all instances for "input". If you are more comfortable with using the
GUI, you don't need to do any of this. You can just search for it all in
the Document. To me that just seems like a waste of time (something that
I don't have much of).

On my Linux machine the following were the commands:

```
python3 scrape.py | grep  "input"
```

{: .box-note}
**Note:** You will have to change `python3` to `python` if you use an
older interpreter. You will also have to replace `scrape.py` with the
filename of your script

When we search with grep, we are searching for all the input tags.
The input tags will have all the important parameters for login
(This includes all the parameters other than username and passwd)

Quite often, grep will pickup the input tag for the submit button
(something which we can ignore), and things like csrf-tokens.
(something we really want to know about). Unfortunately you
will have to understand what's what. However over time, you 
will get better at deciding which tokens to ignore and which to 
keep an eye out for.

Using grep, we get an output of:
```HTML
<input name="csrf_token" type="hidden" value="MCILzixWZdvTmPaHJsgYGnSroNROecktQuVFjEfADhbKXUBywqpl"/>
<input class="form-control" id="username" name="username" type="text"/>
<input class="form-control" id="password" name="password" type="password"/>
<input class="btn btn-primary" type="submit" value="Login"/>
```

In order, to protect a website from Cross Forgery attacks, some
websites generate internal tokens with dynamic values. One of 
these is a csrf_token.

We can ignore the submit button. We now know the name for username
parameter is username and for password, password.

So let's write our script:

```python
from bs4 import BeautifulSoup
from requests import Session

with Session() as s:
    # initial GET request
    site = s.get("http://quotes.toscrape.com/login")
    # parsing content
    html_content = BeautifulSoup(site.content, "html.parser")
    # fetch token value
    token_value = html_content.find("input", {"name": "csrf_token"})["value"]
    # write login details
    login_data = {"username": "ben", "password": "123", "csrf_token": token_value}
    # POST request
    s.post("http://quotes.toscrape.com/login", login_data)
    # GET request
    site = s.get("http://quotes.toscrape.com")
    # Parse home page
    home_page = BeautifulSoup(site.content, "html.parser")
    print(home_page)
```

[Here](https://raw.githubusercontent.com/Benjamin-Philip/benjamin-philip.github.io/master/assets/post-assets/2020-09-16-requests-with-python/scrape.py) is my script in case you have some use for it.

# Going through each line

```python
from bs4 import BeautifulSoup
from requests import Session
```

We import BeautifulSoup from bs4 and Session form requests

```python
with Session() as s:
```

We declare that we shall use Session as as temporarily as s. The
requests Session is used, to keep all the context, so that cookies and
all the other information can be stored.

```python
    site = s.get("http://quotes.toscrape.com/login")
```

We send a GET request for the login page of Quotes to Scrape.

```python
    # parsing content
    html_content = BeautifulSoup(site.content, "html.parser")
    # fetch token value
    token_value = html_content.find("input", {"name": "csrf_token"})["value"]
    # write login details
    login_data = {"username": "ben", "password": "123", "csrf_token": token_value}
```

We first parse the HTML content for python using BeautifulSoup. We then
fetch the value of the csrf_token. To be precise, We ask BeautifulSoup
to find an input tag where the name is csrf_token and extract the values
in the attribute value. Later we make a dictionary of all the login details.

```python
    # POST request
    s.post("http://quotes.toscrape.com/login", login_data)
    # GET request
    site = s.get("http://quotes.toscrape.com")
    # Parse home page
    home_page = BeautifulSoup(site.content, "html.parser")
    print(home_page)
```

Now we POST the login details to our login page,
GET the homepage, and then parse the homepage and print it out.

# Conclusion

The process of logging in to websites 
with python is quite easy, however, the
setup of some websites is not the same
and some will prove to be much more difficult to
login on to than others. 

The key is to have a good knowledge of HTML, Beautiful Soup requests and
the ability to understand what you got from grep/ information received 
from the Network tab of your web browser’s Developer tools.

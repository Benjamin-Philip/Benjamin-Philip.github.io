---
title: Pdfs with pandoc
subtitle: An efficient replacement to Word
tags: [Pandoc, LaTeX]
comments: True
---

With an increase of students and people using Word for school/college,
I found that there was a tool missing for Linux users to 
quickly write documents (unless you used Libreoffice or paid for Microsoft 360)
Here is a tutorial to write pdfs and docx documents using markdown!

# Installing pandoc

## With a package manager

You can install pandoc with in Debian based systems with:

```
sudo apt install pandoc
```

In Fedora this should be:

```
sudo dnf install pandoc
```

Pandoc is available in Debian, Ubuntu, Slackware, Arch, Fedora, 
NiXOS, openSUSE, Gentoo and Void repositories.

You could search for it using your distro's package manager if it 
uses the repositories of one of the following

## Installing from source

I suggest using a package manager for installation.  If at all it is
not there, you can compile it from source: Please note that you should
avoid this. Just in case you make a mistake.

{: .box-note}
**Note:** This is the installation for version 1.17.0.3 (latest in time of writing)


```
wget https://hackage.haskell.org/package/pandoc-1.17.0.3/pandoc-1.17.0.3.tar.gz
tar xvzf pandoc-1.17.0.3.tar.gz
cd pandoc-1.17.0.3
```

{: .box-note}
**Note:** There may be times when the development code is broken or
depends on other libraries which must be installed separately. Unless
you really know what you’re doing, install the last released version

Let's check if we have pandoc installed:

```
pandoc --version
```

You should see a message telling you which version of pandoc is installed 
and giving you some additional information.

# Installing $ L^{A}T_{E}X $

We need LaTeX to convert our markdown documents to pdf.
You can install it on Debian based systems as follows:

```
sudo apt-get install texlive
```

On Fedora it should be:

```
sudo dnf install texlive-scheme-full
```

# Writing a documents with pandoc and markdown

{: .box-warning}
**Warning:** Markdown is not standardised. Pandoc follows its own markdown 
syntax. Changing the markdown variant used will be explained later in the article.

[Here is the pandoc Markdown Documentation.](https://pandoc.org/MANUAL.html#pandocs-markdown)

There isn't much difference between say kramdown and pandoc markdown
that a knowledgeable user should be aware of.

## Writing our first document

Let's write some random text on our test.md:

```kramdown
# Lorem ipsum dolor amet 

The quick brown fox jumps over the lazy dog

*Damn!* I need to get that dog **working!**

## Betty's dog waking recipe

> Guarnteed to wake your dog!

***No batter making required***

Dog energizing list:

- Dog food
- Water 
- Lazy cats
  * Tabby
  * Tomcat
- Squeaky Toy
- Frisbee

Instructions:

1. Pour some water on your sleepy dog
3. Feed it some food.
67. Play with it with the Squeaky Toy
7. Play with it with your Frisbee
2. Throw those lazy cats near by.

~~~
Some random code
~~~

Some `Code` between text
```
Now Let's convert this to pdf:

```
pandoc -f markdown -o test.pdf test.md
```

Now what we are essentially passing to markdown is:

> Using markdown format, make test.pdf out of test.md

This is how my test.md looks:

[First Test.pdf](/assets/post-imgs/pandoc-pdfs/test.pdf)

As you can see, markdown automatically numbers our numbered list and
rectifies our mistakes.


# Passing LaTeX Parameters

Now our pdf looks like a very plain document without a title, 
date or even a specified margin.

Pandoc supports using YAML in the beginning for passing parameters

Let's beautify this a bit more:

```kramdown
---
title: A Random story in a Farm
author: Benjamin Philip
Date: $\today$
--- 
```
Add this to the top of your document.

This is how our new pdf looks:

[New test.pdf](/assets/post-imgs/pandoc-pdfs/)

# Specifying a different markdown variant

We can change the markdown variant by changing the format after -f:

For example for Github Flavoured Markdown:

```
pandoc -f gfm -o test.pdf test.md
```

Or for MultiMarkdown:

```
pandoc -f markdown_mmd -o test.pdf test.md
```

You can check all the input and output formats available 
with the [pandoc User manual](https://pandoc.org/MANUAL.html)

# Inserting $L^{A}T_{E}X$ snippets

You can insert LaTeX snippets by using the "$" sign.

For example to write $a^{2} + b^{2} = c^{2}$:

```
$a^{2} + b^{2} = c^{2}$
```

Or to write $Fe_{3}O_{4} + H_{2} \rightarrow Fe + H_{2}O$:

```
$Fe_{3}O_{4} + H_{2} \rightarrow Fe + H_{2}O$
```

In order to declare LaTeX script, the value immediately after the "$"
sign *should not be a numeral* .

You can also write the following using pandoc markdown's inline formatting:

```
a^2^ + b^2^ = c^2^
```

```
Fe~2~O~4 + H~2~ -> Fe + H~2~O
```

By using "^" for superscript and "~" for subscript.

However knowing how to directly use LaTeX is handy as you can't write things like this in Markdown!

$$\lim_{h \rightarrow 0 } \frac{f(x+h)-f(x)}{h}$$

What do you use to convert doc types? Tell us in the comments below !

---
layout: post 
title: How to Install Plugins for Vim
subtitle: A quick how-to for the Vim newbie
tags: [Vim]
comments: true
---

# Why use plugins

When I first started using vim, I found the efficiency to be much better
that any of the GUI editors I have used before.  Sure it was a steep
learning curve, but it grew on me. Until I reached a dead-end. How do
I enable code completion? What about a syntax check? And how am I going
to Install and Manage all this?. I could have written all the vimscript
myself but that would have taken too much time.  That's when I searched
around to find a concept of "plugins".

# Choosing a Plugin Manager

If you search around for a plugin manager, you will soon find there
are many names that appear: vim-plug, Vundle, Pathogen, apt-vim and more.
So how do you choose one? What I did was I read a bit about each and 
checked if it fulfilled the following:

- Is it easy to Use?

- Is is it maintained well?

- Is it feature rich?

I found Pathogen and apt-vim just a pain to handle. I actually didn't
notice Vundle, So I just went for vim-plug. To my knowledge, there isn't
much difference between Vundle and vim-plug (that is a difference that
the User should be aware of)

# Installing vim-plug

Installing vim-plug just requires cloning the directory from Github. I will be using `curl`.
You can install it by inserting the following:

```
$ curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```
That's it!

# Enabling plugins

Open your ~/.vimrc file and insert the following:

```
call plug#begin()
Plug 'preservim/NERDTree'
call plug#end()
```

We are installing NERDTree as an example. NERDTree is a beautiful plugin
to that allows you to open and access other files in your Computer from
the comfort of Vim. So back to the installation.  What we are saying
here is, call vim-plug for the text between the `call plug#`s. `Plug`
tells vim-plug to load "x" plugin in this case it is `preservim/NERDTree`.

Now write the file, quit, and again execute Vim again. Call the "terminal of vim"
By typing ":". Then type:

`PlugInstall`

This will open a Window and install NERDTree like this:

[PlugInstall in Action](/assets/post-imgs/Vim-plugin-Install/PlugInstall.png)

{: .box-note}
**Note:** I have already got few other plugins, and hence the extra.

# Using vim-plug

To view the Documentation for vim-plug, use:
```
:help vim-plug
```

You can use `:PlugUpdate` to update all your plugins.

`:PlugUpgrade` Updates vim-plug itself.

What's your favourite plugin/plugin manager? And why?
Tell us in the comments below! 

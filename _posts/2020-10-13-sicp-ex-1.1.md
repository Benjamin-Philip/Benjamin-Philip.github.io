So I had just started reading SICP. It’s this amazing book that was used
to teach Comp Sc. to students who had never programmed before at MIT.
When I thought that I should write a blog post with a solution for every
exercise I attempt. So I am gonna write solutions for all the exercise
in SICP. My plan is to finish this book in one year.

# My setup

My plan is to use emacs(sorry for the adultery vim\!) with slime, and
guile. I haven’t setup it up yet, though I will attach a link to the
post when I do. I strongly encourage you to setup emacs though because
soon the exercises will get really complicated, and the support emacs
has for Lisp (Being written in lisp itself) will be really helpful while
editing.

So without further delay, Let’s get to the exercise

# The Question

**Exercise 1.1:** Below is a sequence of expressions. What is the result
printed by the interpreter in response to each expression? Assume that
the sequence is to be evaluated in the order in which presented.

``` scheme
10
(+ 5 3 4)
(- 9 1)
(/ 6 2)
(+ (* 2 4) (- 4 6))
(define a 3)
(define b (+ a 1))
(+ a b (* a b))
(= a b)
(if (and (> b a) (< b (* a b)))
    b
    a)
(cond ((= a 4) 6)
      ((= b 4) (+ 6 7 a))
      (else 25))
(+ 2 (if (> b a) b a))
(* (cond) ((> a b) a)
          ((< a b) b)
          (else -1))
   (+ a 1)
```

# My Thoughts

So far, the authors have been explaining about the basic syntax of
scheme. If you are reading this, you most likely also read SICP till
this exercise. So I am not gonna speak much about it, but make a table
of the syntax:

<table style="width:72%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">Scheme syntax</th>
<th style="text-align: center;">English equivalent</th>
<th style="text-align: center;">Python equivalent</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">(define &lt;vari</td>
<td style="text-align: center;">able&gt; <value>) | va</td>
<td style="text-align: center;">riable is value | variable = value</td>
</tr>
<tr class="even">
<td style="text-align: right;">define (&lt;name</td>
<td style="text-align: center;"><blockquote>
<p>&lt;formal parameter |</p>
</blockquote></td>
<td style="text-align: center;">s&gt;)
<body>
)| to do name, do body with the help of formal parameters | def <name>(<formal parameters>): |
<body></td>
</tr>
<tr class="odd">
<td style="text-align: right;">(<name> &lt;para</td>
<td style="text-align: center;">meters&gt;)</td>
<td style="text-align: center;"><pre><code>      | using a function                                       | &lt;name&gt;(&lt;parameters&gt;)</code></pre></td>
</tr>
</tbody>
</table>

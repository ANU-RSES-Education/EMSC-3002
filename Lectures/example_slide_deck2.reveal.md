---
title: Example 2
revealOptions:
#    transition: 'fade'
    slideNumber: true
---

# Slides

- Louis Moresi
- Australian National University

---

## Slide 2

Typically, we have one or two images on a slide 

<img class="r-stretch" data-src="images/LithosphereThickness.png">

and text that explains what is going on. 
The markdown image tags are limiting but `reveal.js` has image
classes that can be used directly without too much bother:

```html
<img class="r-stretch" data-src="images/LithosphereThickness.png">
```

---

## Slide 3

Animations / styling work using `reveal.js` classes 

<p class="fragment">Fade in</p>
<p class="fragment fade-out">Fade out</p>
<p class="fragment highlight-red">Highlight red</p>
<p class="fragment fade-in-then-out">Fade in, then out</p>
<p class="fragment fade-up">Slide up while fading in</p>

---

## Slide 4 Math

Mathematics via *mathjax*

$$ e^{i\pi} + 1 = 0$$

With inline available ($e^{i\pi} = -1$) as well

---

## Slide 5 Vertical slides

Reveal has vertical sub-stacks that you can divert through

 - Vertical stack 1

----

## Slide 5.1 Vertical slides


Reveal has vertical sub-stacks that you can divert through

 - Vertical stack 2

----

## Slide 5.2 Vertical slides

Reveal has vertical sub-stacks that you can divert through

![Earth](images/LithosphereThickness.png) <!-- .element height="50%" width="50%" -->

---

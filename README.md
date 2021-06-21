# Mathematical Explorations With Computer Algebra Technology

<img src="graphics/mew_cats/mews_parabola_mouse.png"
     alt="a cat working at a computer, for some mysterious reason"
     title="a cat working at a computer, for some mysterious reason"
     width="400"
     >

## Description

This is the source code for a textbook on using Sage to explore mathematics.
It focuses more on introductory programming and using Sage on a topic-by-topic basis.
This repository contains all the relevant data, including old drafts, going back to `draft1`!

The source code for our Sage textbook has been available
[since its first public release](http://www.math.usm.edu/dont_panic),
but after 5 years, it seems appropriate to make the code available in a manner
more consistent with the times; i.e., GitHub.
We hope that making it available on GitHub will make it easier and more appealing
for others to download, use, and modify to taste.

## Reading

To the right on the GitHub page you should see a panel called "Releases".
That will be a PDF of the most recent version.
Among the files in the main folder you will find several historical releases,
which you can read if you're in the mood to see what our older errors were
and what it was like to use Sage in Python2.

## Editing

You probably want to start from `draft(x).lyx`, where `(x)` is the largest number you find.
At the time of this writing, that would be `draft19.lyx`,
but check that there isn't a later draft, because I might forget to update `README.md`.

We wrote this using [Lyx](https://www.lyx.org/), but I have exported it to LaTeX
for at least the most recent version. A PDF is included for most drafts.

Graphics appear in the `graphics` folder, hope that doesn't shock anyone.

You can also start from the LaTeX version, but if you wish to contribute changes,
please edit the Lyx file or, if that is too burdensome,
open an issue that:

- describes the desired change, or
- includes an altered LaTeX file, or
- includes a marked-up PDF file, or
- whatever communicates the change(s) you want!

## Organization

- Necessary things:
  - The current draft should be in the main folder.
  - The `graphics` folder contains graphics required for the current draft.
    If you move it, you will have to rewrite all the links from scratch.
  - Citations appear in `citations.bib`.
    If you move it, you will have to adjust the file reference in the current draft.
- Not-strictly-necessary things:
  - `nimber.py` and `nimber.sage` are what we used when writing Chapter 11.
    They remain for the sake of experimentation, and because it's a convenient place.
  - `legacy` contains older drafts. Feel free to move one out, compile it, look at older texts.
    (Unfortunately, `diff` doesn't always work well with Lyx and Lyx-generated LaTeX.)

## License

![CC-BY-SA](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)

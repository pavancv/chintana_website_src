# chintana_website_src

## Motivation
I found that गीताविवृत्ति by Sri Raghavendra Theertha Swamy is not available online (natively).
Most complete website for Bhagavadgeeta:- https://www.gitasupersite.iitk.ac.in/.  does not have commentary by SriRaghavendra Theerta.
Hence this attempt.


Most of us rely on scanned pages or Old style hard copy books. They have obvious disadvantages to having native online version (not scanned).

- Hardcopy 
    - Paper/book can deteriorate over time
    - Error cannot be corrected
    - Cannot cross-reference

- Scanned copy
    - Often from older books: Readability is compromised
    - Searching is impossible.
    - Unless whole book is scanned, disorganized
    - All the negatives of Hardcopy book continue to exist

## Vision 
    Website for easy reading of BhagavadGeeta and a few philosophy books
    Website is organized into books
    Each book has two different views:-
        - List view: which can be used for Parayana
        - Detailed view:- Each shloka's commentaries are provided



### This is a static website
### Hugo to used to generate the site. Bootstrap is used for CSS/JS.

### To contribute:-

Install Hugo --> https://gohugo.io/
Install VSCode [For easy dev process]

### The source code is divided into two parts 
    - Hugo contents -  Website Source code and the **content** [ This repo ] 

The  generated website :- https://pavancv.github.io/chintana/

The generated website is a sub-module of this repo.

### To clone full repo along with sub-module 
git clone --recurse-submodules <this repo>

### Command to run
#### Local server
- hugo server -D
#### Generate website
- hugo -d ../chintana (from site_src)

#### To create a new page
- hugo new <path>
  ex hugo new contents/books/geeta/chapter18/shloka9.md


#### Commit
- First commit and push chintana dir
- Add git module also while commiting to parent git repo(chintana_website_src)


LICENSE:  MIT

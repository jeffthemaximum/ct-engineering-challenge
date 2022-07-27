# CT Eng Challenge

### some info
- I solved the challenge using a modified trie, and this is in the `/trie` directory
- I also imagined solving the challenge with postgres or, alternately, with a suffix tree. I wrote a little about these below, but I did not write any code.
- I have a working implementation, but it has some limitations. See `major current limitations` below.
- It was important to me to finish my code and submit my result under 3 hrs, so some parts may currently feel unfinished.

### first time setup
- uses python 3.8.2
    - likely works on other python versions, but this is all I tried for now.

### to run
```
=> python main.py
Time to build trie:
Elapsed time: 7.6284 seconds
What searm term would you like to search for?
hamm
Time to search trie:
Elapsed time: 0.0003 seconds
hamm
{
    "inbox": [
        "1270."
    ]
}
```

### major current limitations
- I didn't run against the production data, only the demo data.
   - this is because I only looked at the staging data for most of the challenge, and I saw it was a flat directory structure
   - I wrote my `trie.main.build` function to depend on that flat structure, and it will need to be refactored to accomodate the nested directory structure of the prod data.
   - this wouldn't take long, I just ran out of time.
- I load all the data to memory
    - A requirement of the challenge is "You can't just load everything into RAM. You need to be as efficient as possible about organizing the data on disk, keeping as little data as possible in memory."
    - I did not meet this requirement, I current load everything to memory.
    - To fix my implementation I would update my `trie.main.build` function to build a persistent trie - one that's saved to disc. And I'd update my `trie.main.find_exact` function to read from that file.
- I have some `nice-to-have TODOs` [https://github.com/jeffthemaximum/ct-engineering-challenge/pull/2](https://github.com/jeffthemaximum/ct-engineering-challenge/pull/2) that I didn't complete.


### notes

#### method 1 : postgres full text search

- So my plan here is to implement this two ways.
- I'm not sure if I can get it all done in 3 hrs, so I'll write out some notes here to explain my plan each way.
- The first way is Postgres Full text search, such as (https://amitosh.medium.com/full-text-search-fts-with-postgresql-and-sqlalchemy-edc436330a0c)
- I'm not sure if this first way counts as a library or not. The email says, "Please implement a solution yourself. Don't use a library (e.g. install Lucene)." I have an email out to Zach with this question.
- That first way uses some powerful tools in Postgres, such as tsvectors and lexemes, tqueryes, a GIN index. In short, it preprocesses the data a bit into a cached datastructure, then it optimizes searching that datastructure for us.
- In this first way, I do not plan to implement any sort of ranking in this search. As a MVP during a 3hr challenge, I plan to just load the plain text into the datastructure without any search ranking.


#### method 2 : trie
- As a second method, I plan to build out a data structure "from scratch". In this case, I'm planning to build a trie.
- This trie will have a letter from each word as a node.
- At a leaf, it will have a list of all the email id's that contain that word.
- I've drawn an image [here](https://github.com/jeffthemaximum/ct-engineering-challenge/blob/main/trie/IMG_8753.png) to hopefully demostrate.
- This v1, MVP datastructure is something I think I can implement in the time I have left.
- There's a few limitations to this strategy. A key one is that it only matches on single words, such as "Enron" and not on phrases, such as "I love fraud".

#### method 3 : suffix tree
- If I had more time, I would implement a suffix tree as my datastructure for searching: https://en.wikipedia.org/wiki/Suffix_tree

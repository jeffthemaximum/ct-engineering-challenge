# CT Eng Challenge

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
- I've drawn an image below to hopefully demostrate.
- This v1, MVP datastructure is something I think I can implement in the time I have left.

#### method 3 : suffix tree
- If I had more time, I would implement a suffix tree as my datastructure for searching: https://en.wikipedia.org/wiki/Suffix_tree

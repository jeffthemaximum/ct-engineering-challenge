import json

from timer.timer import Timer
from trie.main import build, find_prefix

t1 = Timer()

t1.start()
root = build()
print("Time to build trie:")
t1.stop()

while True:
    term = input("What searm term would you like to search for?\n")

    t2 = Timer()
    t2.start()
    results = find_prefix(root, term.lower())
    print("Time to search trie:")
    t2.stop()

    print(results[0])
    print(json.dumps(results[1].email_ids, sort_keys=True, indent=4))

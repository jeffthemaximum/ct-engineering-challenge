import json

from timer.timer import Timer
from trie.main import build, find_prefix, find_exact

t1 = Timer()

t1.start()
print("initializing data structure...")
root = build()
print("Time to build trie:")
t1.stop()

while True:
    term = input("What searm term would you like to search for?\n")

    t3 = Timer()
    t3.start()
    results = find_prefix(root, term.lower())
    print("Time to search trie:")
    t3.stop()

    for result in results:
        prefix, result_data = result
        print(prefix)
        print(json.dumps(result_data[1].email_ids, sort_keys=True, indent=4))

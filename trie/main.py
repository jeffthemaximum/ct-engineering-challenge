import json

from os import listdir
from os.path import isfile, join
from pathlib import Path

"""
TrieNode, add, find_prefix, and build are heavily influenced by
https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

the major update I made is around the self.email_ids attribute of TrieNode
"""

class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """
    
    def __init__(self, char):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # the ID's of the emails containing the word
        self.email_ids = {}
    

def add(root, word, email_id, email_directory):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True

    # add data around email containing word to node
    if node.email_ids.get(email_directory) is None:
        node.email_ids[email_directory] = []

    if email_id not in node.email_ids[email_directory]:
        node.email_ids[email_directory].append(email_id)


def find_exact(root, prefix):
    """
    Check and return 
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # which emails contain the string
    return True, node

def find_prefix(root, prefix):
    # get to the starting point
    found, current = find_exact(root, prefix)

    if not found:
        return False

    found = []
    stack = [(current, prefix)]
    while stack:
        current, prefix = stack.pop()

        if current.word_finished:
            # this is a complete word, named by prefix
            found.append(prefix)

        # add the children to the stack, each with their letter added to the
        # prefix value.
        for child in current.children:
            if child is None:
                continue
            stack.append((child, prefix + child.char))

    results = []

    for leaf_string in found:
        result = find_exact(root, leaf_string)
        if result[0]:
            results.append((leaf_string, result))

    return results

def build():
    directories = [
        '_sent_mail',
        'all_documents',
        'calendar',
        'contacts',
        'deleted_items',
        'discussion_threads',
        'inbox',
        'mark',
        'notes_inbox',
        'sent',
        'sent_items'
    ]
    # init trie
    root = TrieNode('*')

    for directory in directories:
        path = f"/Users/jmaxim/code/columntax/engineering-challenge/data/skilling-j/{directory}"
        files = [f for f in listdir(path) if isfile(join(path, f))]

        # read each file
        for file in files:
            # get email_id
            email_id = file
            pointer = open(f"{path}/{file}", "rb")
            # read each line
            for line in pointer:
                # read each word
                words = str(line).split(" ")
                for word in words:
                    # add word to trie
                    add(root, word.lower(), email_id, directory)

    return root

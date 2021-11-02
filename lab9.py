# Author: Nicole Giron nqg5259@psu.edu
# Collaborator: Nireeha Veeraballi nzv5126@psu.edu
# Collaborator: Bakhtiar Reza bmr5782@psu.edu
# Collaborator: Cody Gearhart cag5608@psu.edu
# Section: 4
# Breakout: 9
from sys import argv
def get_words(filename):
  """
  Given a filename (as a str), open the file and retrieve words from
  each line to create a list with whitespaces stripped.
  """
  ans = []
  with open(filename) as fin:
    for line in fin:
      ans.append(line.strip())
  return ans

def invert_dict(d):
  """
  Given a dictionary d, create the invert of the dictionary where
  the key is a value v in d, and v is mapped to a set of keys in original
  d whose values are equal to v.
  Return the inverted dictionary mapping value to set of keys
  """
  inverse = {}
  for key in d:
    if d[key] not in inverse:
      inverse[d[key]] = set([key])
    else:
      inverse[d[key]].add(key)
  return inverse

def histogram(words):
  """
  Given a list of words, create a histogram dictionary where the key
  is the length of a word and the value is the count of how many
  words in the list are of that length.
  Return the histogram dictionary mapping length to word counts
  """
  d = dict()
  for x in words:
    if len(x) not in d: 
      d[len(x)] = 1
    else: 
      d[len(x)] += 1
  return d

def max_kv(d):
  """
  Given a dictionary, return a tuple of key value pair where the key
  is the largest in d.
  """
  m = max(d)
  return (m, d[m])

def run():
  """
  Get words list from the file listed in argv[1];
  create histogram of count of each word length;
  create invert dictionary that maps count to list of word length;
  use invert dictionary to find the list of word length with the
  most popular word count (use max_kv)
  """
  words = get_words(argv[1])
  # fill in code here
  d = histogram(words)
  invert = invert_dict(d)
  # modify the line below so that count, length_set has the right values
  count, length_set = max_kv(invert)
  print(f"These word length {length_set} each has {count} words.") 

if __name__ == "__main__":
  run()

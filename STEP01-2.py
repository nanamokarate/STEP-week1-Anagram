def solution(word,dictionary):
  new_dictionary=[]
  answer=[]
  for i in range(len(dictionary)):
    new_dictionary.append((sorted(dictionary[i]), dictionary[i]))
  new_dictionary=sorted(new_dictionary)
  for i in range(len(new_dictionary)):
    sorted_word=sorted(word)
    count=0
    for j in new_dictionary[i][0]:
      if j in sorted_word:
        count+=1
        sorted_word.remove(j)
      if count == len(new_dictionary[i][0]):
        answer.append(new_dictionary[i][1])
  return answer

def count(anagram):
  x=[]
  for i in range(len(anagram)):
    x.append(len(anagram[i]))
    for j in anagram[i]:
      if j == ('j' or 'k' or 'q' or 'x' or 'z'):
        x[i] +=4
      elif j == ('b' or 'f' or 'g' or 'p' or 'v' or 'w' or 'y'):
        x[i] +=3
      elif j == ('c' or 'd' or 'l' or 'm' or 'u'):
        x[i] +=2
      else:
        x[i] +=1
  return anagram[x.index(max(x))]
  
result=[]
print("Input small.txt or medium.txt or large.txt")
txt=input()
if txt == 'small.txt':
  with open("small.txt") as fp:
    word=fp.read()
if txt == 'medium.txt':
  with open("medium.txt") as fp:
    word=fp.read()
if txt == 'large.txt':
  with open("large.txt") as fp:
    word=fp.read()
word=word.split('\n')
with open ("words.txt") as f:
  dictionary=f.read()
dictionary=dictionary.split('\n')
print(len(word)-1)
for i in range(len(word)-1):
  anagram=solution(word[i],dictionary)
  result.append(count(anagram))

with open("answer_file.txt",mode='w') as f:
  f.write('\n'.join(result))
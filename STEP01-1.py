def binary_search(sorted_random_word,new_dictionary):
  left=0
  right=len(new_dictionary)-1
  while left<right:
    middle=(left+right)//2
    middle_word=new_dictionary[middle][0]
    if sorted_random_word < middle_word:
      right=middle-1
    elif sorted_random_word == middle_word:
      return middle
    else:
      left=middle+1
  return -1


def better_solution(random_word,dictionary):
  new_dictionary=[]
  answer=[]
  sorted_random_word="".join(sorted(random_word))
  for i in range(len(dictionary)):
    new_dictionary.append(("".join(sorted(dictionary[i])), dictionary[i]))
  new_dictionary=sorted(new_dictionary)
  anagram=binary_search(sorted_random_word,new_dictionary)
  if anagram == -1:
    return "nun"
  else:
    for i in range(anagram,len(new_dictionary)):
      if new_dictionary[i][0] == sorted_random_word:
        answer.append(new_dictionary[i][1])
      else:
        break
    for i in range(1,anagram):
      if new_dictionary[anagram-i][0] == sorted_random_word:
        answer.append(new_dictionary[anagram-i][1])
      else:
        break
  return answer

print("Input random words")
random_word=input()
with open ("words.txt") as f:
  dictionary=f.read()
dictionary=dictionary.split('\n')
anagram=better_solution(random_word,dictionary)
print(anagram)
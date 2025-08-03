from collections import Counter

def intersection_with_dupes(a, b):
  count_a = Counter(a)
  count_b = Counter(b)
  result = []
  
  print(a)
 
  print(count_a)

  for ele in count_a:
      
      #setup a loop 
    for i in range(0, min(count_a[ele], count_b[ele])):
      result.append(ele)

  return result

if __name__ == "__main__":
    list1 = [1, 2, 2, 3, 4, 4, 4]
    list2 = [2, 2, 4, 4, 5, 6]

    result = intersection_with_dupes(list1, list2)
    print("Intersection with duplicates:", result)
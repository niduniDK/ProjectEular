# -----Number Pattern Designer---
# -----26th of November 2022----

# Creating anti-clockwise number spiral
def anti_clock(a):
  num_l = [[1]]
  n = 2
  for i in range(len(num_l)+2, a+1, 2):
      num_l.append([])
      num_l.insert(0, [])
      # inserting numbers top to bottom
      for j1 in range(1, i):
          num_l[j1].append(n)
          n += 1
      # inserting numbers right to left
      for j2 in range(i-2, 0, -1):
          num_l[i-1].append(n)
          n += 1
      num_l[i-1].reverse()
      # inserting numbers bottom to top
      for j3 in range(i-1, -1, -1):
          num_l[j3].insert(0, n)
          n += 1
      # inserting numbers left to right
      for j4 in range(1, i):
          num_l[0].append(n)
          n += 1
  return num_l


# Creating clockwise number spiral
def clock_wise(a):
  num_l = [[1]]
  n = 2
  for i in range(len(num_l) + 2, a + 1, 2):
      num_l.append([])
      num_l.insert(0, [])
      # inserting numbers bottom to top
      for j1 in range(i-2, -1, -1):
          num_l[j1].append(n)
          n += 1
      # inserting numbers right to left
      for j2 in range(i - 1, 0, -1):
          num_l[0].append(n)
          n += 1
      # inserting numbers top to bottom
      num_l[0].reverse()
      for j3 in range(1, i):
          num_l[j3].insert(0, n)
          n += 1
      # inserting numbers left to right
      for j4 in range(1, i):
          num_l[i-1].append(n)
          n += 1
  return num_l


# Creating right angle triangular number pattern.
def triangular(a):
  nt = 0
  for i in range(1, a+1):
      nt += i
  tri = []
  x = 1
  y = 1
  for it in range(1, a+1):
      tri.append([])
      for jt in range(y, nt+1):
          tri[it-1].append(jt)
          if len(tri[it-1]) == x:
              x += 1
              y += it
              break
  return tri


name = input("Please enter your name: ")
while True:
  print("Hey", name, "!!!\nPlease enter the number pattern you want:\n\
  1.anti-clockwise spiral\n\
  2.clockwise spiral\n\
  3.right-angle triangle\n\
  4.Quit\n\
  >> Please enter 1 or 2 or 3 or 4 here: ")
  ans = int(input())
  if ans == 4:
      break
  else:
      b = int(input('Please enter up to how many times you want to create the pattern: '))
      if ans == 1:
          res = anti_clock(b)
          for ir in res:
              for ic in ir:
                  print(ic, end='\t')
              print()
          print()
      elif ans == 2:
          res_1 = clock_wise(b)
          for jr in res_1:
              for jc in jr:
                  print(jc, end='\t')
              print()
          print()
      elif ans == 3:
          res_2 = triangular(b)
          for i3 in res_2:
              for jt3 in i3:
                  print(jt3, end='\t')
              print()
          print()
      else:
          print("Oops!!! Something went wrong.\nPlease enter 1 or 2 or 3.")

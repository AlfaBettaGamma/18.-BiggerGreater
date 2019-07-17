def is_number(st):
    try:
        int(st[0])
        return True
    except ValueError:
        return False

def englishLetters(st):
  res = []
  num = is_number(st)
  s = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
       'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,
       'x':24,'y':25,'z':26}
  if num == True:
    for i in range(len(st)):
      for key in s:
        if s[key] == st[i]: 
          res.append(key)
    return res
  else:
    for i in range(len(st)):
      res.append(s.get(st[i]))
    return res

def russianLetters(st):
  res = []
  num = is_number(st)
  s = {'а':1,'б':2,'в':3,'г':4,'д':5,'е':6,'ё':7,'ж':8,'з':9,'и':10,'к':11,'л':12,
      'м':13,'н':14,'о':15,'п':16,'р':17,'с':18,'т':19,'у':20,'ф':21,'х':22,'ц':23,
      'ч':24,'ш':25,'щ':26,'ъ':27,'ы':28,'ь':29,'э':30,'ю':31,'я':32}
  if num == True:
    for i in range(len(st)):
      for key in s:
        if s[key] == st[i]: 
          res.append(key)
    return res
  else:
    for i in range(len(st)):
      res.append(s.get(st[i]))
    return res

def magicRussian(result):
  stres = []
  res = []
  res1 = []
  for i in range(len(result)):
    stres.append(result[i])
    res1.append(result[i])
  for i in range(0,len(stres) - 1):
    for j in range(0,len(stres) - i - 1):
      if stres[j] < stres[j + 1]:
        stres[j],stres[j + 1] = stres[j + 1], stres[j]
  if len(result) == 2:
    if result[0] < result[1]:
      res.append(result[1])
      res.append(result[0])
    res = russianLetters(res)
    return res
  elif result[0] == stres[1] or result[1] == stres[0]:
    res.append(stres[1])
    stres.reverse()
    for i in range(len(stres)):
      if res[0] != stres[i]:
        res.append(stres[i])
    stres.reverse()
    res = russianLetters(res)
    return res
  else:
    res1.reverse()
    for i in range(len(res1)):
      if res1[i] > res1[i + 1] and i + 2 != len(res1):
        res1[i],res1[i + 1] = res1[i + 1],res1[i]
        break
      else:
        break
    res1.reverse()
    res1 = russianLetters(res1)
    return res1

def magicEnglish(result):
  stres = []
  res = []
  res1 = []
  for i in range(len(result)):
    stres.append(result[i])
    res1.append(result[i])
  for i in range(0,len(stres) - 1):
    for j in range(0,len(stres) - i - 1):
      if stres[j] < stres[j + 1]:
        stres[j],stres[j + 1] = stres[j + 1], stres[j]
  if len(result) == 2:
    if result[0] < result[1]:
      res.append(result[1])
      res.append(result[0])
    res = englishLetters(res)
    return res
  elif result[0] == stres[1] or result[1] == stres[0]:
    res.append(stres[1])
    stres.reverse()
    for i in range(len(stres)):
      if res[0] != stres[i]:
        res.append(stres[i])
    stres.reverse()
    res = englishLetters(res)
    return res
  else:
    res1.reverse()
    for i in range(len(res1)):
      if res1[i] > res1[i + 1] and i + 2 != len(res1):
        res1[i],res1[i + 1] = res1[i + 1],res1[i]
        break
      else:
        break
    res1.reverse()
    res1 = englishLetters(res1)
    return res1

def BiggerGreater(input):
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
              'm','n','o','p','q','r','s','t','u','v','w',
              'x','y','z']
  index = 0
  st = list(input)
  for i in range(len(st)):
    if is_number(st[i]) == True:
      return 'Неверные данные!'
  p = st[0]
  n = 0
  for i in range(len(alphabet)):
    if p == alphabet[i]:
      index +=1 
  for i in range(len(st)):
    if st[i] == p:
      n += 1
  if len(st) == n:
    return ''
  if index > 0:
    result = englishLetters(st)
    result = magicEnglish(result)
    return result
  else:  
    result = russianLetters(st)
    result = magicRussian(result)
    return result
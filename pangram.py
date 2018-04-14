print("pangram")
y=0
while y==0:
  
  def checkPangram(s):
  	List = []
  	for i in range(26):
  		List.append(False)
  	for c in s.lower(): 
  		if not c == " ":
  			List[ord(c) -ord('a')]=True
  	for ch in List:
  		if ch == False:
  			return False
  	return True
  sentence = str(input("enter something:"))
  
  if (checkPangram(sentence)):
  	print (sentence)
  	print ("is a pangram")
  else:
  	print (sentence)
  	print ("is not a pangram")
  y=int(input("enter 0 to continue"))

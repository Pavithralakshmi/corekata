wordstring= &#39;it wasthe best of times it was the worst of times &#39;

wordstring += &#39;it was the age of wisdom it was the age of foolishness&#39;

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
  wordfreq.append(wordlist.count(w))

  print(&quot;String\n&quot; + wordstring +&quot;\n&quot;)
  print(&quot;List\n&quot; + str(wordlist) + &quot;\n&quot;)
  print(&quot;Frequencies\n&quot; + str(wordfreq) + &quot;\n&quot;)
  print(&quot;Pairs\n&quot; + str(zip(wordlist, wordfreq)))

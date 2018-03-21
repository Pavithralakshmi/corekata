word_count = 0

file_name = &quot;D//in.txt&quot;
with open(file_name,&#39;r&#39;) as file:
for line in file:
word_count += len(line.split())
print (&quot;number of words : &quot;,word_count)

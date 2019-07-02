import re

Pattern=r'Hello\s\w\w\w\w\w'
Result=re.search(Pattern,'Hello World')
print(Result.group())

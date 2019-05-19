import requests
word = requests.get('https://random-word.ryanrk.com/api/en/word/random').json()[0]
tries = 10
s = set()

hangman = ['----|\n|  lll\n| (O.O)\n| -|.|-\n|  / \\\n-',
'----|\n|  lll\n| (O.O)\n| -|.|-\n|    \\\n-',
'----|\n|  lll\n| (O.O)\n| -|.|-\n|     \n-',
'----|\n|  lll\n| (O.O)\n| -|.| \n|     \n-',
'----|\n|  lll\n| (O.O)\n|  |.| \n|     \n-',
'----|\n|  lll\n| ( .O)\n|  |.| \n|     \n-',
'----|\n|  lll\n| ( .O)\n|      \n|     \n-',
'----|\n|  lll\n| ( . )\n|      \n|     \n-',
'----|\n|  lll\n| (   )\n|      \n|     \n-',
'----|\n|     \n| (   )\n|      \n|     \n-',
'----|\n|     \n|      \n|      \n|     \n-']

while tries > 0 and s != set(word):
    print 'tries left: %s' % tries
    print hangman[tries]
    print ' '.join(word[i] if word[i] in s else '_' for i in range(len(word)))
    c = raw_input("guess a letter: ")
    if c in word and c not in s:
        s.add(c)
    else:
        tries -= 1
    if tries == 0:
        print(hangman[tries])
        print('you lost! the word was: %s' % word)
    if set(word) == s:
        print('you won! congratulations!')

import util_twitter
following = []
fi=open('following.txt','r')
for line in fi:
    following.append(line.strip())
fi.close()
for user in following:
    try:
        tweets = util_twitter.get_twits(user)
        print ("OK with "+user)
    except:
        print ("BLOCKED : "+user)

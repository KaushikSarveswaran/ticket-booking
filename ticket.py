import urllib2
import time
from datetime import datetime
from bs4 import BeautifulSoup
import subprocess
from datetime import datetime
FileName = #your alarm

oldurl = #url of the movie you wanna watch
while True:
	res = urllib2.urlopen(oldurl)
	finalurl = res.geturl()
	if str(finalurl) != oldurl:
		print "redirected" + str(datetime.now())
		time.sleep(60)
	else:
		print "done"
		subprocess.call(['open', FileName])
		break

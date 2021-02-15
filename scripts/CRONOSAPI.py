import urllib2, sys
sys.path.append('C:/gispy/sample_scripts/ch20')
import BeautifulSoup

dataPath = "http://climate.ncsu.edu/dynamic_scripts/cronos/getCRONOSdata.php?station=LAKE&start=2017-06-01&end=2017-11-02&obtype=H¶meter=temp,rh,sr,ws,precip&hash=8a8f8fd5e81269b0fa63ed540be91ad745ec72ae3d49a7a715815dfda1ed7"
response = urllib2.urlopen(dataPath)
contents = response.read()
response.close()

soup = BeautifulSoup.BeautifulSoup(contents)
print soup

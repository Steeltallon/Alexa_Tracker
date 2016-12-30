from urllib2 import Request, urlopen
import json
uname = raw_input("What is the Username?")
pform = raw_input("Which platform? PC,PS,or Xbox?")
if pform = "Xbox"
 pform = "1"
else:
if pform ="PSN"
 pform = "2"
else:
pform = "3"

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {
  'TRN-Api-Key': 'edd7761e-4317-4e82-ae1f-ea45315bc49d',
  'User-Agent': user_agent,
}
rurl = Request('https://battlefieldtracker.com/bf1/api/Stats/BasicStats?platform=2&displayName=' + uname, headers=headers)


r = urlopen(rurl).read()

data = json.loads(r)
print "Rank:", data["result"]["rank"]["number"]
print "Kills:", data["result"]["kills"]
print "Deaths:", data["result"]["deaths"]
print "Wins:", data["result"]["wins"]
print "Losses:", data["result"]["losses"]
print "KPM:", data["result"]["kpm"]
print "SPM:", data["result"]["spm"]
print "Skill:", data["result"]["skill"]

print "Display Name:", data["profile"]["displayName"]
print "ID Number:", data["profile"]["personaId"]
#print r


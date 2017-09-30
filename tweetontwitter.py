from TwitterAPI import TwitterAPI

CONSUMER_KEY = 'N6DRUjHnHe2B0zXwaKsAb28fz'
CONSUMER_SECRET = 'K50hwZ4iGUloKqMIlUdgxv5w9vmXaAi3BqsY0VJXWMPlINK15L'
ACCESS_TOKEN_KEY = '912239966889025538-sELyQrELrG50uDffX1GyR1NKBK0V0t1'
ACCESS_TOKEN_SECRET = 'mLut3S3Q14b3vmoAXfLVNa4T56tlfOoSBuut3pKtXNUt4'

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
file = open('/home/pi/cam/imgs/1.jpg', 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'Your tweet'}, {'media[]':data})
print(r.status_code)

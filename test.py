from gpapi.googleplay import GooglePlayAPI

import sys

EMAIL = "maracaiboez"
PASSWD = "fjgozwjmkwyvvutt"

testApps = ['com.cpuid.cpu_z']
server = GooglePlayAPI(True)

try:
    print('\nLogging in with email and password\n')
    server.login(EMAIL, PASSWD, None, None)
    ac2dmToken = server.ac2dmToken
    gsfId = server.gsfId

    print('\nNow trying secondary login with ac2dm token and gsfId saved\n')
    server.login(EMAIL, PASSWD, ac2dmToken, gsfId)

    apps = server.search('telegram', 1, None)
    print('\nFound those apps:\n')
    for a in apps:
        print(a['docId'])
    docid = apps[0]['docId']
    version = apps[0]['versionCode']
    print('\nTelegram docid is: %s\n' % docid)
    print('\nAttempting to download %s\n' % docid)
    fl = server.download(docid, version)
    with open(docid + '.apk', 'wb') as f:
        f.write(fl)
        print('\nDownload successful\n')
        f.close()
    print('\nGetting details for %s\n' % testApps[0])
    bulk = server.bulkDetails(testApps)
    print(bulk)
except Exception as e:
    print(str(e))
    sys.exit(1)

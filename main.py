import requests
import os, sys, time, json


# 每個檔案間隔時間
st = 1.0

# json 檔案位置
json_path = sys.argv[1]

with open(json_path, 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)

    for c in data['cards']:
        print (c['name'])
        path = "%s-%s" % (c['name'], c['id'])
        os.mkdir(path)

        for a in c['attachments']:
            print ('\t' + a['name'])
            print ('\t' + a['url'])

            r = requests.get(a['url'])
            file_path = os.sep.join([path, a['name']])

            with open(file_path, 'wb') as f:
                f.write(r.content)
                time.sleep(1)
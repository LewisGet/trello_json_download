import requests
import os, sys, time, json, shutil


# 每個檔案間隔時間
st = 1.0

# json 檔案位置
json_path = sys.argv[1]

# 只下載一張卡片的 id
card_id = None

try:
    card_id = sys.argv[2]
except:
    pass


def clear_path_string(value):
    remove = "\\/:*?\"<>|\'\(\)\&\=\!\@\#\$\%\^&"
    return_value = []

    for c in value:
        if c not in remove:
            return_value.append(c)

    return "".join(return_value)


with open(json_path, 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)

    for c in data['cards']:
        if card_id == None or card_id == c['shortLink']:
            print (c['name'])
            path = "%s-%s" % (clear_path_string(c['name']), c['id'])

            if not os.path.exists(path):
                os.mkdir(path)

            for a in c['attachments']:
                print ('\t' + a['name'])
                print ('\t' + a['url'])

                file_name, file_ext = os.path.splitext(a['name'])

                r = requests.get(a['url'])
                file_path = os.sep.join([path, "%s-%s%s" % (clear_path_string(file_name), a['id'], file_ext)])

                with open(file_path, 'wb') as f:
                    f.write(r.content)
                    time.sleep(1)

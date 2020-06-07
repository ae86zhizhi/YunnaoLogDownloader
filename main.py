import requests, json

taskPod = "54b6dc600a76f011ea0be7402db12957e6c8-rb2-0-0-0"

url_json = 'http://192.168.204.24/es/_search?_source=message'
data_json = json.dumps({
    "query":{
        "match":{
            "kubernetes.pod.name":"placeholder"
        }
    },
    "size":10000,
    "from":0,
    "sort":"log.offset"
})
data_json = data_json.replace("placeholder", taskPod)
headers = {"Content-Type": "application/json; charset=utf-8"}
r_json = requests.post(url_json, data_json, headers=headers)
d = json.loads(r_json.text)
print(len(d["hits"]))
for record in d["hits"]["hits"]:
    print(record['_source']['message'])

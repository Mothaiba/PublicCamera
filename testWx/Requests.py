import requests

def sampleRequest():

    r = requests.get("http://128.199.77.122/publiccamera/api/index.php/v1/node-datas");
    print r.status_code
    print r.text
    result = r.json()
    print result


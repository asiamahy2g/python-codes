import requests
def url_check(url):
    isUP=True
    try:
        resp = requests.get(url)

    except:
        print("please double check your url")
    else:
        #print(dir(resp))
        status = resp.status_code

        if status == 200:
            isUP=True
        else:
            isUP=False
    return isUP

a=url_check('http://google.com')
print(a)
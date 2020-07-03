from shorten import app
from flask import request,redirect
import redis,uuid,re,shortuuid,json

rconn = redis.Redis(host='localhost', port=6379, db=0)
url_regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

@app.route('/shorten', methods = ['POST'])
def url_shorten():
    long_url = request.form['url']

    if long_url[:4] != 'http':
        long_url = 'http://' + long_url

    idd = shortuuid.uuid(name=long_url)
    if rconn.get(idd):
        dat = {"shorten_url": request.host + "/" + idd, "url_info": request.host + "/info/" + idd}
        return json.dumps(dat)

    if re.match(url_regex,long_url):
        rconn.set(idd,json.dumps({'url':long_url,"hit":0}))
        dat = {"shorten_url":request.host+"/"+idd, "url_info": request.host+"/info/"+idd}
        return json.dumps(dat)
    else:
        return "Please Enter a Valid URL"


@app.route('/<url_id>')
def page_redirect(url_id):
    meta = rconn.get(url_id)
    if meta:
        dat = json.loads(meta)
        dat['hit'] +=1
        rconn.set(url_id,json.dumps(dat))
        return redirect(dat['url'])
    else:
        return "Not Found"

@app.route('/info/<url_id>', methods=['POST', 'GET'])
def info(url_id):
    meta = rconn.get(url_id)
    return json.loads(meta)

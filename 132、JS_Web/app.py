from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
import sys

# 重新设置控制台编码为 UTF-8
sys.stdout.reconfigure(encoding='utf-8') 

app = Flask(__name__, template_folder='templates')
@app.route('/')
def index_url():
    location ="113.88,22.55"
    data = get_weather(location)
    # temp = 26
    # desc = '小雨'
    # return render_template('index.html', location=location, temp=temp, desc=desc)
    return render_template('index.html',location=data['name'], temp=data['temp'], desc=data['desc'])

@app.route('/get_data')
def get_data():
    loc = request.args.get('loc')
    ua = request.headers.get('User-Agent')
    token = request.cookies.get('token')
    data = ''
    if 'python' in ua:
        msg = '检测到自动化程序'
    elif not token or token != 'abc':
        msg = 'Token参数错误'
    elif not loc:
        msg = '查询参数错误'
    else:
        locations = get_city_lng_lat(loc)
        location = f"{locations[0]},{locations[1]}"
        # print(locations)
        data = get_weather(location)
        msg = '请求正常'
    sender_data = {
        'msg':msg,
        'data':data
    }
    sender_str = json.dumps(sender_data)
    return sender_str

@app.route('/post_data', methods=['POST'])
def post_data():
    # loc = request.form.get('loc')
    loc = request.json.get('loc')
    locations = get_city_lng_lat(loc)
    location = f"{locations[0]},{locations[1]}"
    # print(locations)
    data = get_weather(location)
    msg = '请求正常'
    sender_data = {
        'msg':msg,
        'data':data
    }
    sender_str = json.dumps(sender_data)
    return sender_str


def get_weather(location):
    weather_url = f"https://devapi.qweather.com/v7/weather/now?location={location}&lang=zh&key=7f0adfab52f64e3d9f9539be2b58e101"
    r = requests.get(weather_url)
    # print(r.status_code)

    data = json.loads(r.text) 
    temp = data["now"]["temp"]
    desc = data["now"]["text"]
    fx_link = data["fxLink"]
    name = fx_link.split("/")[-1].split("-")[0]
    weather = {
        "temp": temp,
        "desc": desc,
        "name": name,
    }
    return weather

def get_city_lng_lat(city):
    url = f'https://restapi.amap.com/v3/geocode/geo?address={city}&output=JSON&key=1dff3c8ea640aec5c4627f645729174c'
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text)
        lng = data['geocodes'][0]['location'].split(',')[0]
        lat = data['geocodes'][0]['location'].split(',')[1]
        locations = [lng, lat]
        # print(locations)
        return locations
    else:
        return None

@app.route('/axios')
def axios():
    return '这是一个Axios请求'



if __name__ == '__main__':
    app.run(host='127.1.1.0',port=9999,debug=True)
    # get_weather()
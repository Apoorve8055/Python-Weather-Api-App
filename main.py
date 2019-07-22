import requests as req
ip_url = req.get('https://api6.ipify.org/?format=json').json()
city_api_addrs = req.get("http://extreme-ip-lookup.com/json/"+ip_url['ip']).json()
json_data = req.get("https://api.apixu.com/v1/current.json?key=603dd028615e4f45b5284518192107&q="+city_api_addrs['city']).json()
#print('http:'+json_data['current']['condition']['icon'])
print('City Name: ' + json_data['location']['name'])
print('region Name: ' +json_data['location']['region'])
print('country Name: ' +json_data['location']['country'])
print('last Updated: ' +json_data['current']['last_updated'])
print('Status: ' +json_data['current']['condition']['text'])
print('Wind Speed: ' + str(json_data['current']['wind_kph']) + " k/p")


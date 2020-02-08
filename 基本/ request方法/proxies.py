import requests

proxies = {"http" : "http://user:password@host:port",
"https" : "http://user:password@host:port",
}
#proxies = {"http" : "socks5://user:password@host:port"}
requests.get('https://www.taobao.com', proxies = proxies)

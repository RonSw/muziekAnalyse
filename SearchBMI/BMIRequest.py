# General
# Request URL: http://repertoire.bmi.com/DetailView.aspx?blnWriter=True&blnPublisher=True&blnArtist=False&blnAltTitles=False
# Request Method: POST
# Status Code: 302 Found
# Remote Address: 68.71.107.235:80
# Referrer Policy: no-referrer
# 
# Response Headers
# Cache-Control: private
# Content-Length: 36742
# Content-Type: text/html; charset=utf-8
# Date: Sun, 07 Jun 2020 14:52:31 GMT
# Location: /DetailView.aspx?blnWriter=True&blnPublisher=True&blnArtist=False&blnAltTitles=False
# Referrer-Policy: no-referrer
# Server: Microsoft-IIS/8.5
# X-AspNet-Version: 4.0.30319
# X-Content-Type-Options: nosniff
# X-Frame-Options: SAMEORIGIN
# X-Powered-By: ASP.NET
# X-XSS-Protection: 1;mode=block
# 
# Request headers
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate
# Accept-Language: nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7
# Cache-Control: max-age=0
# Connection: keep-alive
# Content-Length: 1453
# Content-Type: application/x-www-form-urlencoded
# Cookie: _ga=GA1.2.1283436025.1580411406; _gid=GA1.2.1473456406.1591559101; ASP.NET_SessionId=qaeozr0uvarmsk1i430ishwm; TiPMix=57.2779644081732; x-ms-routing-name=self; ARRAffinity=10576f13315c7f895b39b3667462633b4324d833d0d593e15abdaef9f894ec2e; __utma=112510103.1283436025.1580411406.1591559910.1591559910.1; __utmc=112510103; __utmz=112510103.1591559910.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=112510103.1.10.1591559910; _gat_UA-136722-12=1; __unam=73f8473-16ff7dc4ab6-e2ac25a-16
# Host: repertoire.bmi.com
# Origin: null
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36
# 
# Query string
# blnWriter: True
# blnPublisher: True
# blnArtist: False
# blnAltTitles: False
# 
# Form data
# __VIEWSTATE: /wEPDwUKLTk1NzQ1Mzc0Mw8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFhICBQ9kFgICAQ9kFgICBw8WAh4Fc3R5bGUFDGRpc3BsYXk6bm9uZRYCAgEPFgIeBWNsYXNzBRRjb250ZW50LWRpc3BsYXktZGFya2QCBw8WAh4HVmlzaWJsZWhkAgkPFgIfA2hkAgsPFgIfA2hkAg0PFgIeBFRleHQFAzFYMWQCDw8WAh4JaW5uZXJodG1sBQVUaXRsZWQCEw8PFgIfA2hkZAIVD2QWAgIBD2QWAgIDD2QWAmYPZBYCZg8PFgIfBAUwPHN0cm9uZz5Ub3RhbCBDb250cm9sbGVkIGJ5IEJNSTo8L3N0cm9uZz4gNTUuMDAlZGQCGQ9kFgoCAQ8PFgIfBAUHOTAwLDAwMGRkAgMPDxYCHwQFEW5lYXJseSAxNCBtaWxsaW9uZGQCBQ8PFgIfBAUHOTAwLDAwMGRkAgcPDxYCHwQFEW5lYXJseSAxNCBtaWxsaW9uZGQCCQ8PFgIfBAUTQ29weXJpZ2h0IDE5OTQtMjAyMGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYEBRhzZWFyY2hDb250cm9sJGluY1dyaXRlcnMFG3NlYXJjaENvbnRyb2wkaW5jUHVibGlzaGVycwUYc2VhcmNoQ29udHJvbCRpbmNBcnRpc3RzBRpzZWFyY2hDb250cm9sJGluY0FsdFRpdGxlc9w2PHAIPZEL3/Eqv6jInnuHo99a9y+cUFvVK5wCGZE/
# __VIEWSTATEGENERATOR: 8F40308D
# __EVENTVALIDATION: /wEdAA1fC0ZKvzxcu9+Ay/nIxhLx+iqCfGAVb9IaCP9f+m3b/ROPvN/tv8IBQ0iMU+5v7+Oj7g65cpzjJxVNF61gO8f+fLV5h6EJcNtWGYRiq7bleGIu0aYwTGe6fnmp4NvoPWmQTEwGAQTU+6fvs344AiYPUmfXu65Jux6BBvm44JilASsdXEYGzTDdUppjByIUeD/aj1Jm5SajLts7Znb9rVGiEXE7TtG9fBp/8t5aluvwykGZM6HUDKePEtYijMlTH4euDIPj5rgad2GgCD16XDAL8yqjXEA6kS4gKcP1tb+G9HrK6iFyIRGmQSXnHz2UMsM=
# searchControl$ddlTypeOfSearch: titleid
# searchControl$txtSearchFor: 24348968                                                        
# searchControl$btnSubmit: Search
# searchControl$incWriters: on
# searchControl$incPublishers: on

import requests
import json


url = "http://repertoire.bmi.com"
data = {
'__VIEWSTATE': ',/wEPDwUKLTk1NzQ1Mzc0Mw8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFhICBQ9kFgICAQ9kFgICBw8WAh4Fc3R5bGUFDGRpc3BsYXk6bm9uZRYCAgEPFgIeBWNsYXNzBRRjb250ZW50LWRpc3BsYXktZGFya2QCBw8WAh4HVmlzaWJsZWhkAgkPFgIfA2hkAgsPFgIfA2hkAg0PFgIeBFRleHQFAzFYMWQCDw8WAh4JaW5uZXJodG1sBQVUaXRsZWQCEw8PFgIfA2hkZAIVD2QWAgIBD2QWAgIDD2QWAmYPZBYCZg8PFgIfBAUwPHN0cm9uZz5Ub3RhbCBDb250cm9sbGVkIGJ5IEJNSTo8L3N0cm9uZz4gNTUuMDAlZGQCGQ9kFgoCAQ8PFgIfBAUHOTAwLDAwMGRkAgMPDxYCHwQFEW5lYXJseSAxNCBtaWxsaW9uZGQCBQ8PFgIfBAUHOTAwLDAwMGRkAgcPDxYCHwQFEW5lYXJseSAxNCBtaWxsaW9uZGQCCQ8PFgIfBAUTQ29weXJpZ2h0IDE5OTQtMjAyMGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYEBRhzZWFyY2hDb250cm9sJGluY1dyaXRlcnMFG3NlYXJjaENvbnRyb2wkaW5jUHVibGlzaGVycwUYc2VhcmNoQ29udHJvbCRpbmNBcnRpc3RzBRpzZWFyY2hDb250cm9sJGluY0FsdFRpdGxlc9w2PHAIPZEL3/Eqv6jInnuHo99a9y+cUFvVK5wCGZE/',
'__VIEWSTATEGENERATOR': '8F40308D',
'__EVENTVALIDATION': '/wEdAA1fC0ZKvzxcu9+Ay/nIxhLx+iqCfGAVb9IaCP9f+m3b/ROPvN/tv8IBQ0iMU+5v7+Oj7g65cpzjJxVNF61gO8f+fLV5h6EJcNtWGYRiq7bleGIu0aYwTGe6fnmp4NvoPWmQTEwGAQTU+6fvs344AiYPUmfXu65Jux6BBvm44JilASsdXEYGzTDdUppjByIUeD/aj1Jm5SajLts7Znb9rVGiEXE7TtG9fBp/8t5aluvwykGZM6HUDKePEtYijMlTH4euDIPj5rgad2GgCD16XDAL8yqjXEA6kS4gKcP1tb+G9HrK6iFyIRGmQSXnHz2UMsM=',
'searchControl$ddlTypeOfSearch': 'titleid',
'searchControl$txtSearchFor': '24348968',
'searchControl$btnSubmit': 'Search',
'searchControl$incWriters': 'on',
'searchControl$incPublishers': 'on'
}

params = {
	'blnWriter': 'True',
	'blnPublisher': 'True',
	'blnArtist': 'False',
	'blnAltTitles': 'False'
}

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '1453',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': '_ga=GA1.2.1283436025.1580411406; _gid=GA1.2.1473456406.1591559101; ASP.NET_SessionId=qaeozr0uvarmsk1i430ishwm; TiPMix=57.2779644081732; x-ms-routing-name=self; ARRAffinity=10576f13315c7f895b39b3667462633b4324d833d0d593e15abdaef9f894ec2e; __utma=112510103.1283436025.1580411406.1591559910.1591559910.1; __utmc=112510103; __utmz=112510103.1591559910.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=112510103.1.10.1591559910; _gat_UA-136722-12=1; __unam=73f8473-16ff7dc4ab6-e2ac25a-16',
'Host': 'repertoire.bmi.com',
'Origin': 'null',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36' 
}

#r = requests.post(url, data=json.dumps(data), headers=headers)
r = requests.post(url, params=params, data=data, headers=headers)

print (r.status_code)
print (r.content)

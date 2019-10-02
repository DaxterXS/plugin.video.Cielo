import re
import xbmcgui
import requests

url = 'https://videoplatform.sky.it/player/json/get_livestream_2.json?callback=getLive&_=1570036301745'
res = requests.get(url)

try:
	streaming_url = 'https://' + re.findall('"streaming_url":"https{0,1}://(.*?)"', res.text)[0]
	thumb_url = 'https://' + re.findall('"img":"https{0,1}://(.*?)"', res.text)[1]
	listitem = xbmcgui.ListItem('Cielo TV')
	listitem.setInfo('video', {'Title': 'Cielo TV'})
	listitem.setArt({ 'thumb': thumb_url})
	xbmc.Player().play(streaming_url, listitem)

except Exception as ex:
	message = 'Eccezione: %s' % ex
	listitem = xbmcgui.ListItem('Cielo - Errore')
	listitem.setInfo('video', {'Title': 'Errore nell\' avvio del plugin Cielo'})
	listitem.setInfo('video', { 'plot': message })

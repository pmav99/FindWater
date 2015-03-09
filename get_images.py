from PIL import Image
import urllib2 as urllib
import cStringIO

origin1 = 3.0
origin2 = 36.0
for i in range(0,5):
	for j in range(0,5):
		lon = origin1 + i*0.1;
		lat = origin2 + j*0.1;
		url = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(lon) + "," + str(lat) + "&zoom=12&size=400x400&style=feature:water|color:0xFF0066&key=AIzaSyDzWmvcVKeyoDgyvnLgHpVnCLpypWLrkPY"
		f = cStringIO.StringIO(urllib.urlopen(url).read())
		img = Image.open(f)
		url_satellite = url + "&maptype=satellite"
		f_satellite = cStringIO.StringIO(urllib.urlopen(url_satellite).read())
		img_satellite = Image.open(f_satellite)
		rgb = img.convert('RGB')
		(width, height) = img.size
		w = 10
		h = 10
		yes = 0
		while w+10 < width:
			h = 10
			while h+10 < height:
				r, g, b = rgb.getpixel((w - 5,h))
				if r <= 260 and r >= 250 and g <= 5 and b <= 107 and b >= 95:
					r, g, b = rgb.getpixel((w + 5,h))
					if r <= 260 and r >= 250 and g <= 5 and b <= 107 and b >= 95:
						r, g, b = rgb.getpixel((w,h + 5))
						if r <= 260 and r >= 250 and g <= 5 and b <= 107 and b >= 95:
							r, g, b = rgb.getpixel((w,h - 5))
							if r <= 260 and r >= 250 and g <= 5 and b <= 107 and b >= 95:
								img_satellite.save("yesNeal/" + str(lon) + "_" + str(lat) + ".bmp")
								w = width
								h = height
								yes = 1
				h = h + 11
			w = w + 11
		if yes == 0:
			img_satellite.save("noNeal/" + str(lon) + "_" + str(lat) + ".bmp")

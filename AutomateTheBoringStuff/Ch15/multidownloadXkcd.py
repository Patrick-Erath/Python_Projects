# multidownloadXkcd.py - Downloads XKCD comics using multiple threads
import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd


def download_xkcd(start_comic, end_comic):
	for url_number in range(start_comic, end_comic+1):
		# Download the page
		print('Downloading the page...')
		res = requests.get('https://xkcd.com/%s' %(url_number))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text, features='lxml') # gets HTML code of URL 

		# Find the URL of the comic image
		comic_elem = soup.select('#comic img') # gets HTML IMG tag
		if comic_elem == []:
			print('Could not find comic image')
		else:
			comic_url = 'http:'+comic_elem[0].get('src') # gets URL tag of comicElem list
			# Download the image
			print('Downloading the image of comic #%s' %(url_number))
			res = requests.get(comic_url)
			res.raise_for_status()		
			
			# Save image to ./xkcd
			image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
			for chunk in res.iter_content(10000):
				image_file.write(chunk)
			image_file.close()

			
#download_xkcd(1,3)
# Create and start the Thread objects
download_threads = [] # a list of all Thread objects
for i in range(0, 50, 10):
	download_thread = threading.Thread(target=download_xkcd, args=(i, i+9))
	# Create 14 threads, each thread gets images from range (i, i+9) seperately
	download_threads.append(download_thread)
	download_thread.start()

# Wait for all threads to end
for download_thread in download_threads:
	download_thread.join()
print('Done')
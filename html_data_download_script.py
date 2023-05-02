import os
import time
import requests
import sys

'''
https://en.tutiempo.net/climate/ws-722310.html 
Climate New Orleans, New Orleans International Airport
Climate data: 1945 - 2023 
'''
CLIMATE_CITY_CODE = 421820


def download_data_as_html_files():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month < 10):
                download_url = 'http://en.tutiempo.net/climate/0{}-{}/ws-{}.html'.format(month,year, CLIMATE_CITY_CODE)
            else:
                download_url = 'http://en.tutiempo.net/climate/0{}-{}/ws-{}.html'.format(month,year, CLIMATE_CITY_CODE)
            
            texts = requests.get(download_url)
            text_utf = texts.text.encode('utf=8')
            
            # create the data directory if not present
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
                
            # download the data as html files and save them in directory
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
        
if __name__ == "__main__":

    start_time=time.time()
    
    # download the html files
    download_data_as_html_files()
    
    stop_time=time.time()
    print("Time taken to download files {}".format(stop_time-start_time))

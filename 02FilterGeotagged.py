'''
    Muhammad Nur Yasir Utomo (yasirutomo@gmail.com)
'''

# Simpan file ini di ../json/ sebelum di eksekusi
import re
import json
import time
import random
from collections import Counter
# from geopy.geocoders import Nominatim
import geopip

# geolocator = Nominatim(user_agent="specify_your_app_name_here")

def txt_norm(text):
    text = text.replace("\n", " ")
    text = text.replace("'", " ")
    text = text.replace('"', " ")
    text = re.sub(' +', ' ', text)
    return text


def main():
    i = 1
    totaldata = 0
    awal = 0
    iterasi = 10000

    file_concern = "stream_sampleoutputstream"

    with open('dataset/' + file_concern + '.json', 'r') as f:

        output = open('geotagged/' + file_concern + '.csv', 'a')
        output.write('"idtweet,"datecreated","username","text","lang","location","lat","lng"' + "\n")

        for line in f:

            if i == iterasi:
                print('Iterasi ke:')
                print(i)
                iterasi = iterasi + 10000

            if line not in ['\n', '\r\n']:
                if '{"limit":{"track":' not in line:
                    if '{"delete":{"status":{"id":' not in line:  # hilang
                        tweet = json.loads(line)
                        text_check = json.dumps(tweet['text'])

                        totaldata += 1

                        if tweet['coordinates']:  # filter geotagged
                            idtweet = tweet['id']
                            datecreated = tweet['created_at']
                            username = txt_norm(tweet['user']['screen_name'])
                            text = txt_norm(tweet['text'])
                            lang = tweet['lang']
                            lat = tweet['coordinates']['coordinates'][1]
                            lng = tweet['coordinates']['coordinates'][0]

                            location = geopip.search(lng=lng, lat=lat)

                            if location:
                                country = location['NAME']
                                tweet['location'] = country
                                location = txt_norm(tweet['location'])
                            else:
                                location = 'Undefined'

                            # S: json form
                            form = {
                                "idtweet": idtweet,
                                "datecreated": datecreated,
                                "username": username,
                                "text": text,
                                "lang": lang,
                                "location": location,
                                "lat": lat,
                                "lng": lng
                            }

                            with open('geotagged/' + file_concern + '.json', 'a') as outfile:
                                json.dump(form, outfile)
                                outfile.write('\n')
                                outfile.close()
                            # E: json form

                            # S: csv form
                            form_csv = '"'+str(idtweet)+'","'+str(datecreated)+'","'+str(username)+'","'+str(text)+'","'+str(lang)+'","'+str(location)+'","'+str(lat)+'","'+str(lng)+'"'
                            output = open('geotagged/' + file_concern + '.csv', 'a')
                            output.write(form_csv + "\n")
                            # E: csv form

                            awal += 1

                            # print('data: '), awal
                            # print(idtweet)
                            # print(country)
                            # print(text.encode("utf-8"))
            i += 1
            # print('')

    print('')
    print('total data: ')
    print(totaldata)
    print('')
    print('total data geotagged: ')
    print(awal)


if __name__ == '__main__':
    main()
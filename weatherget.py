#!/usr/bin/env python3

import os
import datetime
import requests
import csv

ERRLOG = open('errors/errors.txt','a')    # the Python logging module is too complex

def logerror(s):
    now = datetime.datetime.now()
    nows = str(now)[:-1] + ' '   # remove the final newline
    print(nows + s)
    ERRLOG.write(nows + s + '\n')
                                   # for this little example

IDEEZ = [         # from the openweather api city list:
                  #  99  city IDs surrounding my home city of Issaquah WA
                  # ... and one BAD one and one super-long number bad ID to test with
    5729080,
    5729485,
    5730675,
    5731070,
    5731371,
    5734711,
    5735724,
    5736218,
    5736378,
    5740099,
    5740900,
    5742726,
    5743731,
    5744253,
    5745380,
    5746545,
    5750162,
    5751632,
    5756758,
    5757477,
    5757506,
    5760009,
    5761287,
    5761708,
    5771826,
    5771960,
    5772654,
    5772959,
    5773001,
    5773304,
    5774001,
    "BAD",
    5774215,
    5774301,
    5774662,
    5775782,
    5775863,
    5776008,
    5776715,
    5776727,
    5777107,
    5777224,
    5777544,
    5777793,
    5778244,
    5778352,
    5778755,
    5779036,
    9999999999999999,
    5779068,
    5779206,
    5779334,
    5779816,
    5780026,
    5780557,
    5780802,
    5780993,
    5781087,
    5781765,
    5781770,
    5781783,
    5781794,
    5781860,
    5781993,
    5782391,
    5782476,
    5783695,
    5784549,
    5784607,
    5785243,
    5785657,
    5785868,
    5785965,
    5786485,
    5786882,
    5786899,
    5787776,
    5787829,
    5788054,
    5788516,
    5788822,
    5789683,
    5790971,
    5791159,
    5792244,
    5793427,
    5793933,
    5794097,
    5794245,
    5794559,
    5795011,
    5795906,
    5796984,
    5798487,
    5799587,
    5799610,
    5799625,
    5799841,
    5800112,
    5800317,
    5800420
]

APIKEY = os.environ['API_KEY']   # the API Key from openweathermap

with open('output/weather.csv', 'a') as csvfile:
    weatherwriter = csv.writer(csvfile)
    for myid in IDEEZ:
        try:
            r = requests.get(
                'https://api.openweathermap.org/data/2.5/weather?id=%d&APPID=%s' % (myid, APIKEY))

            print(r.content)
            dtofobs = datetime.datetime.fromtimestamp(r.json()['dt'])
            j = r.json()
            weatherwriter.writerow([myid, j['name'], j['weather'][0]['main'], dtofobs])
        except:
            logerror("Can't get ID %s " % myid)

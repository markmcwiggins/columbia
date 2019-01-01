# columbia
An interview problem for Columbia Sportswear of Portland OR


The program weatherget.py will download about 100 current Pacific Northwest weather readings from openweather.org.




The station list is in the directory **resources**.

The program was developed using Python 3.6.1 on my trusty 2013 Macbook Pro,
so you'll need Python on your system to run it. It needs the nonstandard module**requests** added by **pip** or direct download ...

To use this you need an environment variable:

**API_KEY**

 ... that stores the API Key you get when registering with openweather.org.

Store it like this:

    export API_KEY=my_api_key
    
 Then to run (on Linux or Macintosh):
 
     while true
     do
       ./weatherget.py
       sleep 300
     done
 
 
 This will run the readings every five minutes until you interrupt it.
 
 Timings of readings is imprecise for some stations, so sometimes you'll come up with duplicates. The
 output file is in **output/weather.csv** ... you can eliminate duplicates with
 
     sort -u output/weather.csv >output/weather.unique.csv
 
 Errors go to **errors/errors.txt**.
 
 questions?
 
 Email me: mark@pythonsoftwarewa.com
 
 Thanks!
 

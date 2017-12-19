import requests
import csv
import time
import json
import cPickle as pickle

def makeApiCall(longOrigin, latOrigin, longDest, latDest):
    # test code for api
    orig = longOrigin+","+latOrigin
    dest = longDest+","+latDest
    print ("Origin: "+ orig+", Destination: "+dest)
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {"origin": orig,
              "destination": dest,
              "alternatives": "true",
              "key": "AIzaSyAb32ykWTCmkW0qPailxaolpBqnlh8FfcA"
              }
    r = requests.get(url, params)
    response_object = json.loads(r.text)

    # print(response_object)
    # print(response_object["routes"][0]["legs"][0]["distance"]["value"])
    # print(response_object["routes"][0]["legs"][0]["duration"]["value"])
    return response_object["routes"]





#create object with all nodes
dic = dict()
with open('stations_velib.csv', 'rb') as csvfile:
     reader = csv.reader(csvfile, delimiter=';')
     reader.next()
     for row in reader:
         if int(row[3])<50:
            dic[int(row[3])]=(row[0], row[1], row[2])
print len(dic)
#get edges in combinatory manner: every point to every point
edges = dict()
counter = 0
for source in dic:
    for destination in dic:
        if source is not destination:
            #make API call
            arrayIterinaries = makeApiCall(dic[source][0], dic[source][1], dic[destination][0], dic[destination][1])
            #save result
            edges[(source, destination)]=(arrayIterinaries)
            counter+=1
            #wait not to overdo the api calls per second
            time.sleep(0.04)
            print (str(counter))
            #if counter>1:
              #  break

    #if counter>1:
      #  break
#print counter
#print edges
#serialize

pickle.dump( edges, open( "edgesSer.dat", "wb" ) )

#save to file
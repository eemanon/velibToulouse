import cPickle as pickle

data = pickle.load( open( "edgesSer.dat", "rb" ) )
print (data[(1,2)][0]["legs"][0]["distance"]["value"])
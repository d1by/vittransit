import firebase_admin
from firebase_admin import credentials, db
import folium

cred = credentials.Certificate("bus--tracker-firebase-adminsdk-bd7k8-6fc1410e93.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://bus--tracker-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')
data = ref.get()

m = folium.Map()
for coords in data:
    for key in coords:
        if(key == 'latitude'):
            lat = coords[key]
        elif(key == 'longitude'):
            lon = coords[key]
        else:
            index = coords[key]
    
    folium.Marker(location = [lat, lon], 
                  popup = "<i>Next stop: Lorem ipsum</i>", 
                  tooltip=f"Bus {index}"
                  ).add_to(m)

m.save("map.html")
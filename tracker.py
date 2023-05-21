import firebase_admin
from firebase_admin import credentials, db
import folium
from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

cred = credentials.Certificate("bus--tracker-firebase-adminsdk-bd7k8-ef933504c7.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bus--tracker-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')

@app.route('/')
def display_map():
    data = ref.get()
    m = folium.Map()
    
    for coords in data:
        for key in coords:
            if key == 'Latitude':
                lat = coords[key]
            elif key == 'Longitude':
                lon = coords[key]
            else:
                index = coords[key]
        
        folium.Marker(
            location=[lat, lon],
            popup="<i>ETA: Lorem Ipsum</i>",
            tooltip=f"Bus {index}"
        ).add_to(m)
    
    m.save("templates/map.html")
    
    return render_template("map.html")


if __name__ == '__main__':
    app.run(debug=True)
# vittransit
codechef internal hackathon, may 2023

### To do
- [ ] Push location data to Firebase Realtime Database using android app
- [x] Retreive information from Firebase Realtime Database
- [x] Display map updates dynamically using Flask 
- [ ] Show time until arrival of bus at a location specified via menu 

### To run for yourself:
1. clone repo
2. generate firebase database private key (`https://console.firebase.google.com/u/project/<PROJECT_NAME>/settings/serviceaccounts/adminsdk`)
3. place private key .json file in the same directory as repo
4. create virtual env (optional, recommended): `py -3 -m venv env` and run it: `env\scripts\activate`
6. run flask app with `python tracker.py`
7. navigate to server (default: `http://127.0.0.1:5000`) in your web browser
 
## Images
###### Flask, displaying map generated via Folium 
![image](https://github.com/d1by/vittransit/assets/108338649/d56d700d-5ed1-4131-bae1-96c00fa3848d)
###### Initial Figma design
![image](https://github.com/d1by/vittransit/assets/108338649/2e3ae239-24c0-4048-9034-15e117321bce)
###### Rudimentary app UI
![image](https://github.com/d1by/vittransit/assets/108338649/44721e44-aec4-45f4-9f71-bdbaa1d06222)
![image](https://github.com/d1by/vittransit/assets/108338649/67b462d8-f8a4-4256-9edd-0dc63b465ba2)

### Contributors:
##### [Jayantika](https://github.com/Jayantika1610) 
###### Android app (Kotlin) to push location data to Firebase Realtime Database
##### [Aaryan](https://github.com/Aaryan-Poria)
###### UI for Android app (XML), presentations
##### [Aryaman](https://github.com/Unusedkeys)
###### Presentations
##### [Diby](https://github.com/d1by)
###### Python script to retreive data from Firebase Realtime Database, generate map data (Folium), dynamically display map on local server (Flask), Figma

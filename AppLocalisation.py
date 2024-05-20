
#Importation des bibliothèques
import phonenumbers as ph
from phonenumbers import geocoder
import folium as fl
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import streamlit as st
key="3060ff26a85bf4d55aff9fcf8562d2792"
#Construire le numero de téléphone
numero="+22376675002"
#Instancier le numero
MonNum=ph.parse(numero)
# Localisation du numero
localisation= geocoder.description_for_number(MonNum,"fr")
print(localisation)

#Trouver l'opérateur du nemero téléphonique
operateur=ph.parse(numero)
carr=carrier.name_for_number(operateur,'fr')

# Trouver la longititude et la latitude
#key="7f3d21e467ab4133b125ef36c8f08e56"
coord=OpenCageGeocode(key)
requete= str(localisation)
reponse=coord.geocode(requete)
print(reponse)
lat= reponse[0]["geometry"]["lat"]
lng= reponse[0]["geometry"]["lng"]
#Creation du Map
Map=fl.Map(location=[lat, lng],zoom_start=12)
fl.Marker([lat,lng],popup=localisation).add_to(Map)
Map.save("map.html")

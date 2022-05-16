#python app.py pour ecexuter le code
#utiliser postman pour tester + wamp/phpmyadmin
from flask import request
from models import * 
from init import create_app
from route import *

# Init app
app = create_app()

#Init Schema
temperature_schema = TemperatureSchema()
temperatures_schema = TemperatureSchema(many=True)
dioxyde_schema = DioxydeSchema()
dioxydes_schema = DioxydeSchema(many=True)
humidity_schema = HumiditySchema()
humidities_schema = HumiditySchema(many=True)
potentielHydrogene_schema = PotentielHydrogeneSchema()
potentielHydrogenes_schema = PotentielHydrogeneSchema(many=True)
nutriement_schema = NutriementSchema()
nutriements_schema = NutriementSchema(many=True)
luminosity_schema = LuminositySchema()
luminosities_schema = LuminositySchema(many=True)
temperatureEau_schema = TemperatureEauSchema()
temperatureEaux_schema = TemperatureEauSchema(many=True)
quantityEau_schema = QuantityEauSchema()
quantityEaux_schema = QuantityEauSchema(many=True)

#####################################################
#                    Get Single                     #
#####################################################
## Temperature
@app.route('/temperature/<id>', methods=['GET'])
def get_temperature(id):
    return get_single(Temperature,temperature_schema,id)
## Dioxyde
@app.route('/CO2/<id>', methods=['GET'])
def get_dioxyde(id):
    return get_single(Dioxyde,dioxyde_schema,id)
## Humidité
@app.route('/humidity/<id>', methods=['GET'])
def get_humidity(id):
    return get_single(Humidity,humidity_schema,id)
## PotentielHydrogène
@app.route('/PH/<id>', methods=['GET'])
def get_PH(id):
    return get_single(PotentielHydrogene,potentielHydrogene_schema,id)
## Nutriement
@app.route('/nutriement/<id>', methods=['GET'])
def get_nutriement(id):
    return get_single(Nutriement,nutriement_schema,id)
## Luminosité
@app.route('/luminosity/<id>', methods=['GET'])
def get_luminosity(id):
    return get_single(Luminosity,luminosity_schema,id)
## Température eau
@app.route('/temperatureEau/<id>', methods=['GET'])
def get_temperatureEau(id):
    return get_single(TemperatureEau,temperatureEau_schema,id)
## Quantité eau
@app.route('/quantityEau/<id>', methods=['GET'])
def get_quantityEau(id):
    return get_single(QuantityEau,quantityEau_schema,id)


#######################################################
#                   Get all                           #
#######################################################
## Temperatures
@app.route("/temperature", methods=['GET'])
def get_temperatures():
    return get_all(Temperature,temperatures_schema)
## Dioxydes
@app.route("/dioxyde", methods=['GET'])
def get_dioxydes():
    return get_all(Dioxyde,dioxydes_schema)
## Humidités
@app.route("/humidity", methods=['GET'])
def get_humidities():
    return get_all(Humidity,humidities_schema)
## PotentielHydrogène
@app.route("/PH", methods=['GET'])
def get_PHs():
    return get_all(PotentielHydrogene,potentielHydrogenes_schema)
## Nutriements
@app.route("/nutriement", methods=['GET'])
def get_nutriements():
    return get_all(Nutriement,nutriements_schema)
## Luminosités
@app.route("/luminosity", methods=['GET'])
def get_luminosities():
    return get_all(Luminosity,luminosities_schema)
## Températures eau
@app.route("/temperatureEau", methods=['GET'])
def get_temperatureEaux():
    return get_all(TemperatureEau,temperatureEaux_schema)
## Quantité eau
@app.route("/quantityEau", methods=['GET'])
def get_quantityEaux():
    return get_all(QuantityEau,quantityEaux_schema)

#########################################################
#                      Create                           #
#########################################################
## Temperature
@app.route("/temperature", methods=['POST'])
def add_temperature():
    return create(Temperature,temperature_schema)
## Dioxyde
@app.route("/CO2", methods=['POST'])
def add_dioxyde():
    return create(Dioxyde,dioxyde_schema)
## Humidité
@app.route("/humidity", methods=['POST'])
def add_humidity():
    return create(Humidity,humidity_schema)
## PotentielHydrogène
@app.route("/PH", methods=['POST'])
def add_PH():
    return create(PotentielHydrogene,potentielHydrogene_schema)
## Nutriement
@app.route("/nutriement", methods=['POST'])
def add_nutriement():
    return create(Nutriement,nutriement_schema)
## Luminosité
@app.route("/luminosity", methods=['POST'])
def add_luminosity():
    return create(Luminosity,luminosity_schema)
## Température eau
@app.route("/temperatureEau", methods=['POST'])
def add_temperatureEau():
    return create(TemperatureEau,temperatureEau_schema)
## Quantité eau
@app.route("/quantityEau", methods=['POST'])
def add_quantityEau():
    return create(QuantityEau,quantityEau_schema)

########################################################
#                       Update                         #
########################################################
## Temperature
@app.route("/temperature/<id>", methods=['PUT'])
def update_temperature(id):
    return update(Temperature,temperature_schema, id)
## Dioxyde
@app.route("/dioxyde/<id>", methods=['PUT'])
def update_dioxyde(id):
    return update(Dioxyde,dioxyde_schema, id)
## Humidité
@app.route("/humidity/<id>", methods=['PUT'])
def update_humidity(id):
    return update(Humidity,humidity_schema, id)
## PotentielHydrogène
@app.route("/PH/<id>", methods=['PUT'])
def update_PH(id):
    return update(PotentielHydrogene,potentielHydrogene_schema, id)
## Nutriement
@app.route("/nutriement/<id>", methods=['PUT'])
def update_nutriement(id):
    return update(Nutriement,nutriement_schema, id)
## Luminosité
@app.route("/luminosity/<id>", methods=['PUT'])
def update_luminosity(id):
    return update(Luminosity,luminosity_schema, id)
## Température eau
@app.route("/temperatureEau/<id>", methods=['PUT'])
def update_temperatureEau(id):
    return update(TemperatureEau,temperatureEau_schema, id)
## Quantité eau
@app.route("/quantityEau/<id>", methods=['PUT'])
def update_quantityEau(id):
    return update(QuantityEau,quantityEau_schema, id)

#######################################################
#                        Delete                       #
#######################################################
## Temperature
@app.route('/temperature/<id>', methods=['DELETE'])
def delete_temperature(id):
    return delete(Temperature,temperature_schema, id)
## Dioxyde
@app.route('/dioxyde/<id>', methods=['DELETE'])
def delete_dioxyde(id):
    return delete(Dioxyde,dioxyde_schema, id)
## Humidité
@app.route('/humidity/<id>', methods=['DELETE'])
def delete_humidity(id):
    return delete(Humidity,humidity_schema, id)
## PotentielHydrogene
@app.route('/PH/<id>', methods=['DELETE'])
def delete_PH(id):
    return delete(PotentielHydrogene,potentielHydrogene_schema, id)
## Nutriement
@app.route('/nutriement/<id>', methods=['DELETE'])
def delete_nutriement(id):
    return delete(Nutriement,nutriement_schema, id)
## Luminosité
@app.route('/luminosity/<id>', methods=['DELETE'])
def delete_luminosity(id):
    return delete(Luminosity,luminosity_schema, id)
## TemperatureEau
@app.route('/temperatureEau/<id>', methods=['DELETE'])
def delete_temperatureEau(id):
    return delete(TemperatureEau,temperatureEau_schema, id)
## QuantityEau
@app.route('/quantityEau/<id>', methods=['DELETE'])
def delete_quantityEau(id):
    return delete(QuantityEau,quantityEau_schema, id)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
import flask_sqlalchemy
import flask_marshmallow

db = flask_sqlalchemy.SQLAlchemy()
ma = flask_marshmallow.Marshmallow()

####################################################
#             Temperature Extérieure               #
####################################################
# Temperature Class/model
class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    valeur = db.Column(db.String(10))

    def __init__(self, date, valeur):
        self.date = date
        self.valeur = valeur

# Temperature Schema
class TemperatureSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'valeur')

####################################################
#                     CO2                          #
####################################################
# Dioxyde Class/model
class Dioxyde(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    valeur = db.Column(db.String(10))

    def __init__(self, date, valeur):
        self.date = date
        self.valeur = valeur

# Dioxyde Schema
class DioxydeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'valeur')

####################################################
#                     Humidité                     #
####################################################
# Humidité Class/model
class Humidity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    valeur = db.Column(db.String(10))

    def __init__(self, date, valeur):
        self.date = date
        self.valeur = valeur

# Humidité Schema
class HumiditySchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'valeur')

####################################################
#          PH - Potentiel Hydrogène                #
####################################################
# PotentielHydrogène Class/model
class PotentielHydrogene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    valeur = db.Column(db.String(10))

    def __init__(self, date, valeur):
        self.date = date
        self.valeur = valeur

# PotentielHydrogène Schema
class PotentielHydrogeneSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'valeur')

####################################################
#                 Nutriement                       #
####################################################
# Nutriement Class/model
class Nutriement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    valeur = db.Column(db.String(10))

    def __init__(self, date, valeur):
        self.date = date
        self.valeur = valeur

# Nutriement Schema
class NutriementSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'valeur')

####################################################
#                 Luminosité                       #
####################################################
# Luminosité Class/model
class Luminosity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    valeur = db.Column(db.String(10))

    def __init__(self, date, valeur):
        self.date = date
        self.valeur = valeur

# Luminosité Schema
class LuminositySchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'valeur')

####################################################
#                 Température eau                  #
####################################################
# Température eau Class/model
class TemperatureEau(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    valeur = db.Column(db.String(10))

    def __init__(self, date, valeur):
        self.date = date
        self.valeur = valeur

# Température eau Schema
class TemperatureEauSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'valeur')

####################################################
#                 Quantité eau                  #
####################################################
# Quantité eau Class/model
class QuantityEau(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    valeur = db.Column(db.String(10))

    def __init__(self, date, valeur):
        self.date = date
        self.valeur = valeur

# Quantité eau Schema
class QuantityEauSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'valeur')
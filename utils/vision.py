import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model("model/constellation_model.h5")
labels = ["Andromeda", "Antlia", "Apus", "Aquarius", "Aquila", "Ara", "Aries", "Auriga",
    "Boötes", "Caelum", "Camelopardalis", "Cancer", "Canes Venatici", "Canis Major",
    "Canis Minor", "Capricornus", "Carina", "Cassiopeia", "Centaurus", "Cepheus",
    "Cetus", "Chamaeleon", "Circinus", "Columba", "Coma Berenices", "Corona Australis",
    "Corona Borealis", "Corvus", "Crater", "Crux", "Cygnus", "Delphinus", "Dorado",
    "Draco", "Equuleus", "Eridanus", "Fornax", "Gemini", "Grus", "Hercules",
    "Horologium", "Hydra", "Hydrus", "Indus", "Lacerta", "Leo", "Leo Minor", "Lepus",
    "Libra", "Lupus", "Lynx", "Lyra", "Mensa", "Microscopium", "Monoceros", "Musca",
    "Norma", "Octans", "Ophiuchus", "Orion", "Pavo", "Pegasus", "Perseus", "Phoenix",
    "Pictor", "Pisces", "Piscis Austrinus", "Puppis", "Pyxis", "Reticulum", "Sagitta",
    "Sagittarius", "Scorpius", "Sculptor", "Scutum", "Serpens", "Sextans", "Taurus",
    "Telescopium", "Triangulum", "Triangulum Australe", "Tucana", "Ursa Major",
    "Ursa Minor", "Vela", "Virgo", "Volans", "Vulpecula"]

def predict_constellation(frame):
    img = cv2.resize(frame, (128, 128))
    img = img.astype("float") / 255.0
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0]
    return labels[np.argmax(prediction)]

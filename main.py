from models import *
from test import *
from utils import *
#No se enoje por esto, Evan, solo ando haciendo pruebas

Gold = Ore("Gold", "100", 1000)
Silver = Ore("Silver", "100", 500)
Bronze = Ore("Bronze", "100", 100)
Earth = Planet("Earth", 100, 1000000, 12756, [Gold, Silver, Bronze], 1, "Milky Way")
Evan = Human("Evan", 17, 100, Earth, [], [], 100)
Evan.show_atributes()

# if __name__ == "__main__":
#     pass
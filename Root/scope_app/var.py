GENDER = (
    ("Male","Male"),
    ("Female","Female"),
)

LOCATION_GRID = tuple([
    (f"{char}{number}", f"{char}{number}") for number in range(0, 14) for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
])


DINO_TYPE = [
    ("Tyrannosaurus", "Tyrannosaurus"), 
    ("Velociraptor","Velociraptor"), 
    ("Apatosaurus", "Apatosaurus"), 
    ("Stegosaurus","Stegosaurus"),  
    ("Triceratops","Triceratops")
]

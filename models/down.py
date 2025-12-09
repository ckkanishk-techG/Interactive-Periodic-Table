import os
import requests

# Element names indexed by atomic number (1–118)
ELEMENT_NAMES = [
    "hydrogen", "helium", "lithium", "beryllium", "boron",
    "carbon", "nitrogen", "oxygen", "fluorine", "neon",
    "sodium", "magnesium", "aluminum", "silicon", "phosphorus",
    "sulfur", "chlorine", "argon", "potassium", "calcium",
    "scandium", "titanium", "vanadium", "chromium", "manganese",
    "iron", "cobalt", "nickel", "copper", "zinc",
    "gallium", "germanium", "arsenic", "selenium", "bromine",
    "krypton", "rubidium", "strontium", "yttrium", "zirconium",
    "niobium", "molybdenum", "technetium", "ruthenium", "rhodium",
    "palladium", "silver", "cadmium", "indium", "tin",
    "antimony", "tellurium", "iodine", "xenon", "cesium",
    "barium", "lanthanum", "cerium", "praseodymium", "neodymium",
    "promethium", "samarium", "europium", "gadolinium", "terbium",
    "dysprosium", "holmium", "erbium", "thulium", "ytterbium",
    "lutetium", "hafnium", "tantalum", "tungsten", "rhenium",
    "osmium", "iridium", "platinum", "gold", "mercury",
    "thallium", "lead", "bismuth", "polonium", "astatine",
    "radon", "francium", "radium", "actinium", "thorium",
    "protactinium", "uranium", "neptunium", "plutonium", "americium",
    "curium", "berkelium", "californium", "einsteinium", "fermium",
    "mendelevium", "nobelium", "lawrencium", "rutherfordium",
    "dubnium", "seaborgium", "bohrium", "hassium", "meitnerium",
    "darmstadtium", "roentgenium", "copernicium", "nihonium",
    "flerovium", "moscovium", "livermorium", "tennessine", "oganesson"
]

# Output folder
os.makedirs("models", exist_ok=True)

for i in range(1, 119):
    name = ELEMENT_NAMES[i-1]
    padded = str(i).zfill(3)  # 001, 002, ...
    
    url = f"https://storage.googleapis.com/search-ar-edu/periodic-table/element_{padded}_{name}/element_{padded}_{name}.glb"
    save_path = f"models/{i}.glb"

    print(f"Downloading {url}")

    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"✔ Saved as {save_path}")
    else:
        print(f"❌ Failed for {i}: {response.status_code}")

print("\nDONE!")

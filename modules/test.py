from modules.database import *
import datetime

db = Database(dbtype='sqlite', dbname='../ockovani.db')

vakcina = Vakcina()
vakcina.nazev_firmy = "Pfizer/BioNTech"
vakcina.ucinnost_vakciny = 95
vakcina.cena_vakciny = 309
vakcina.typ_vakciny = "mRNA"
vakcina.pocet_davek = 2
vakcina.schvalena_v_EU = True
db.create_vakcina(vakcina)

povolani = Povolani()
povolani.nazev_povolani = "učitel"
db.create_povolani(povolani)

ockovani = Ockovani()
ockovani.jmeno = "Jan"
ockovani.prijmeni = "Novák"
ockovani.datum_narozeni = datetime.date(1978, 5, 2)
ockovani.vakciny_id = 1
ockovani.povolani_id = 1
db.create_ockovani(ockovani)
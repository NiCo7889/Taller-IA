import csv
import os

def load_population(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def save_population(filename, population):
    fieldnames = ['identificador', 'nombre', 'dias_en_lab', 'sexo', 'peso', 'temperatura', 'genotipo_x', 'genotipo_y', 'fecha_nacimiento']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for raton in population.ratones:
            writer.writerow(raton.to_dict())

def save_as_population(new_filename, population):
    save_population(new_filename, population)

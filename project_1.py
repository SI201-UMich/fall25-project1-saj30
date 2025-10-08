# project_1.py
# Name: Sajjad Majeed
# Email: sajjadma@umich.edu
# Date: 2025-10-06
# UM_ID: 39020780
"""Project 1 Overview
This script summarizes the dataset and outlines the planned analyses.
Dataset: penguins.csv

Columns used:
    - species
    - island
    - bill_length_mm
    - bill_depth_mm
    - flipper_length_mm
    - body_mass_g
    - sex
    - year

Planned analyses:
    • Calculate average bill length by species
    • Calculate percentage of males and females by species

Function structure:

main()
  - load_data(filepath)
      - Reads CSV file manually using csv.reader
      - Cleans data (removes index column, trims spaces)
      - Builds and returns:
          - header (list of column names)
          - records (list of dicts)
          - by_index (dict[int, dict])
          - by_species (dict[str, list[dict]])
  - analyze(records)
      - avg_bill_length_by_species(records)
          - Calculates average bill length per species
      - count_sex_by_species(records)
          - Counts number of males and females per species
  - Prints results from analyze()
"""

import csv

DATAFILE = 'penguins.csv'

COLUMNS = [
    'species', 'island', 'bill_length_mm', 'bill_depth_mm',
    'flipper_length_mm', 'body_mass_g', 'sex', 'year'
]


def load_data(filepath: str = DATAFILE):
    """Load the CSV into a structured dictionary and return header (manual version)."""
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        # If the first column is just an empty string (like ""), skip it.
        if header and header[0] == '':
            header = header[1:]

        records = []
        by_index = {}
        by_species = {}

        count = 0
        for row in reader:
            # Skip the first element if it's just the index number
            if row and row[0].isdigit():
                row = row[1:]

            # Stop if row is shorter than expected (to avoid index errors)
            if len(row) < len(header):
                continue

            # Build a dictionary manually: {header[i]: row[i]}
            record = {}
            for i in range(len(header)):
                record[header[i]] = row[i].strip()

            # Add record to collections
            records.append(record)
            by_index[count] = record

            species = record.get('species', '').strip()
            if species:
                if species not in by_species:
                    by_species[species] = []
                by_species[species].append(record)

            count += 1

        return header, {'records': records, 'by_index': by_index, 'by_species': by_species}


def avg_bill_length_by_species(records):
    """Compute average bill length (mm) grouped by species."""
    totals = {}
    counts = {}

    for rec in records:
        sp = rec.get('species', '').strip()
        bill = rec.get('bill_length_mm', '').strip()

        if not sp or bill in ('', 'NA'):
            continue
        try:
            bill_val = float(bill)
        except ValueError:
            continue

        totals[sp] = totals.get(sp, 0) + bill_val
        counts[sp] = counts.get(sp, 0) + 1

    avgs = {sp: round(totals[sp] / counts[sp], 2) for sp in totals if counts[sp] > 0}
    return avgs


def count_sex_by_species(records):
    """Count male and female records for each species."""
    counts = {}

    for rec in records:
        sp = rec.get('species', '').strip()
        sex = rec.get('sex', '').strip().lower()

        if not sp or sex in ('', 'na'):
            continue

        if sp not in counts:
            counts[sp] = {'male': 0, 'female': 0}
        if sex in counts[sp]:
            counts[sp][sex] += 1

    return counts


def analyze(records):
    """Perform analyses."""
    sex_species_counts = count_sex_by_species(records)
    avg_bill_length = avg_bill_length_by_species(records)
    return {
        'sex_by_species': sex_species_counts,
        'avg_bill_length_by_species': avg_bill_length
    }


def main():
    header, data = load_data()

    if data and data['records']:
        records = data['records']

        results = analyze(records)
        print("\nAnalysis Results ---\n")

        print("Average Bill Length by Species:")
        for sp, avg in results['avg_bill_length_by_species'].items():
            print(f"  - {sp}: {avg} mm")

        print("\nSex Distribution by Species:")
        for sp, counts in results['sex_by_species'].items():
            print(f"  - {sp}: male={counts['male']}, female={counts['female']}")
    else:
        print('load_data() not yet implemented or dataset empty.')


if __name__ == '__main__':
    main()

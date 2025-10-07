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
    • Count records by species and island
    • Compute summary statistics (mean, median, std) for numeric columns by species

Function structure:

main()
  - get_header(filepath): Reads and returns CSV column names
  - load_data(filepath): Loads CSV into records, cleans numeric fields, builds:
      - records (list of dicts)
      - by_index (dict)
      - by_species (dict)
  - analyze()
      - count_by_species()
      - count_by_island()
      - summary_stats_by_species()
"""

import csv

DATAFILE = 'penguins.csv'

# List of columns to load and analyze from the penguins dataset
COLUMNS = [
    'species', 'island', 'bill_length_mm', 'bill_depth_mm',
    'flipper_length_mm', 'body_mass_g', 'sex', 'year'
]


def get_header(filepath=DATAFILE):
    """Return the CSV header as a list of column names."""
    file = open(filepath, 'r')
    reader = csv.reader(file)
    header = next(reader)
    file.close()
    # Remove first column if it's empty
    if header and (header[0] == ''):
        header = header[1:]
    return header


def load_data(filepath: str = DATAFILE):
    """Load the CSV into a structured dictionary.

    (To be implemented)
    Expected return:
        {
            'records': list of dicts,
            'by_index': dict[int, dict],
            'by_species': dict[str, list[dict]]
        }
    """
    return {'records': [], 'by_index': {}, 'by_species': {}}


def avg_bill_length_by_species(records):
    """Step 1: Compute average bill length (mm) grouped by species.

    Args:
        records: list of dicts
    Returns:
        dict: {species: average_bill_length_mm}

    (To be called by analyze() once implemented)
    """
    pass


def count_sex_by_species(records):
    """Step 2: Count male and female records for each species.

    Args:
        records: list of dicts
    Returns:
        dict: {species: {'male': count, 'female': count}}

    Iterates through the records, grouping by species and counting
    the number of 'male' and 'female' entries for each species.
    """
    pass



def analyze(records):
    """Perform analyses: count sex by species and average bill length by species."""
    sex_species_counts = count_sex_by_species(records)
    avg_bill_length = avg_bill_length_by_species(records)
    return {
        'sex_by_species': sex_species_counts,
        'avg_bill_length_by_species': avg_bill_length
    }


def main():
    header = get_header()
    print('Detected header:')
    print(header)
    print('\n--- Plan ---')

    data = load_data()
    if data and data['records']:
        records = data['records']
        by_species = data['by_species']
        print('\nLoaded {} records'.format(len(records)))
        print('Counts by species:')
        for sp, items in by_species.items():
            print(f' - {sp}: {len(items)}')
    else:
        print('load_data() not yet implemented or dataset empty.')


if __name__ == '__main__':
    main()
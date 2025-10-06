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
  - count_by_species(records): Counts records by species
  - count_by_island(records): Counts records by island
  - summary_stats_by_species(records, numeric_columns): Computes summary stats for numeric columns
"""

import csv

DATAFILE = 'penguins.csv'

# Columns of interest
COLUMNS = [
    'species', 'island', 'bill_length_mm', 'bill_depth_mm',
    'flipper_length_mm', 'body_mass_g', 'sex', 'year'
]


def get_header(filepath: str = DATAFILE) -> list[str]:
    """Return the CSV header as a list of column names (normalized).

    If the CSV has an initial unnamed index column, drop it.
    """
    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
    header = [h.strip('"') for h in header]
    # Drop a leading empty/unnamed column if present
    if header and (header[0] == '' or header[0].lower().startswith('unnamed')):
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


def count_by_species(records):
    """Step 1: Count records grouped by species.

    Args:
        records: list of dicts
    Returns:
        dict: {species: count}

    (To be called by analyze() once implemented)
    """
    pass


def count_by_island(records):
    """Step 2: Count records grouped by island.

    Args:
        records: list of dicts
    Returns:
        dict: {island: count}

    (To be called by analyze() once implemented)
    """
    pass


def summary_stats_by_species(records, numeric_columns=None):
    """Compute summary statistics (mean, median, std, count) for numeric columns grouped by species.

    Args:
        records: list of dicts
        numeric_columns: list of column names to summarize (defaults to numeric columns in COLUMNS)
    Returns:
        dict: {species: {col: {mean, median, std, count}}}
    """
    pass


def main() -> None:
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
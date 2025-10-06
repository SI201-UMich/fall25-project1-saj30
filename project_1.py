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
  - print_plan(): Prints dataset summary and planned analyses
  - load_data(filepath): Loads CSV into records, cleans numeric fields, builds:
      - records (list of dicts)
      - by_index (dict)
      - by_species (dict)
  - clean_data(df): Reports and handles missing data, standardizes categories
  - analyze(df): Performs counts and summary statistics by species
  - save_or_plot(results): Saves summary tables or creates visualizations
"""

import csv

DATAFILE = 'penguins.csv'

# A short, explicit list of columns we'll focus on in the project.
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


def print_plan() -> None:
    """Print a short summary of the dataset and planned calculations."""
    print('Dataset: penguins.csv')
    print('Columns we will use:')
    print(', '.join(COLUMNS))
    print('\nPlanned calculations:')
    print('- Counts by species and island')
    print('- Summary stats (mean, median, std) for numeric columns by species')


def load_data(filepath: str = DATAFILE):
    """Load the CSV into a DataFrame-like structure.
    1. We'll load the CSV into a list of records (dicts) and also build
    2. Convenient nested indexes:
     - records: list[dict]
     - by_index: dict[int, dict]  (row number / original index -> record)
     - by_species: dict[str, list[dict]]"""
    import csv

    numeric_cols = {'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'}
    records = []
    by_index = {}
    by_species = {}

    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            rec = {k.strip('"'): v for k, v in row.items()}
            # convert numeric columns
            for c in numeric_cols:
                val = rec.get(c)
                if val is None:
                    rec[c] = None
                    continue
                s = val.strip()
                if s == '' or s.upper() == 'NA':
                    rec[c] = None
                else:
                    try:
                        if '.' in s:
                            rec[c] = float(s)
                        else:
                            rec[c] = int(s)
                    except ValueError:
                        try:
                            rec[c] = float(s)
                        except ValueError:
                            rec[c] = None

            # normalize categorical fields
            if 'sex' in rec and rec['sex'] is not None:
                rec['sex'] = rec['sex'].strip().lower() if rec['sex'].strip() != '' else None
            if 'species' in rec and rec['species'] is not None:
                rec['species'] = rec['species'].strip()

            records.append(rec)
            by_index[i] = rec
            sp = rec.get('species') or 'Unknown'
            by_species.setdefault(sp, []).append(rec)

    return {'records': records, 'by_index': by_index, 'by_species': by_species}


def analyze(df):
    """Perform the planned calculations and return results.

    Steps this function will perform when implemented:
    1. Counts by species and island (groupby + size).
    2. Summary statistics for numeric columns grouped by species
       (mean, median, std, count).
    3. Return a dict with results for easy printing or saving.

    Args:
        df: pandas.DataFrame
    Returns:
        dict
    """
    pass




def main() -> None:
    header = get_header()
    print('Detected header:')
    print(header)
    print('\n--- Plan ---')
    print_plan()

    # Smoke test: load CSV into dict structures and print simple counts
    data = load_data()
    records = data['records']
    by_species = data['by_species']
    print('\nLoaded {} records'.format(len(records)))
    print('Counts by species:')
    for sp, items in by_species.items():
        print(' - {}: {}'.format(sp, len(items)))


if __name__ == '__main__':
    main()

import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Convert Excel to CSV.')
parser.add_argument('input_file', type=str, help='Input Excel file')
parser.add_argument('output_file', type=str, help='Output CSV file')
parser.add_argument('--skip-header', action='store_true', help='Skip the header row')
parser.add_argument('--columns', nargs='*', type=int, help='Columns to extract (0-based index)')

args = parser.parse_args()

try:
    if args.skip_header:
        df = pd.read_excel(args.input_file, header=None, skiprows=1)  # Skip header
    else:
        df = pd.read_excel(args.input_file)

    # fetch only specified columns
    if args.columns:
        df = df.iloc[:, args.columns]

    df.to_csv(args.output_file, index=False, header=not args.skip_header) # Write csv
    print(f'Successfully converted {args.input_file} to {args.output_file}.')
except Exception as e:
    print(f'An error occurred: {e}')


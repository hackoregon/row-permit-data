"""
Author: Travis Hathaway <travis.j.hathaway@gmail.com>

Description:
    This file loads the data from the ROW CSV file in to a database of your
    choice by specifying the DSN

Example Usage:
    python load_db_from_csv.py <csv_file>
"""
import psycopg2
import csv
import sys

# PostgreSQL DSN (e.g. 'postgresql://user@localhost:5432/row_permit_data')
DSN = 'postgresql://travishathaway@localhost:5432/row_permit_data'


# Indexes of the fields that are numeric
NUMERIC_FIELDS = (
    35, 34, 33, 32, 29, 28, 27, 23, 21, 20, 19, 18, 17, 11,
    2, 1, 0
)


def main():
    """
    Load data in to table
    """
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()

    if len(sys.argv) < 2:
        print('Please provide csv file as first argument')
        sys.exit(1)

    cur.execute('TRUNCATE row_permit_data')

    with open(sys.argv[1]) as f:
        f_reader = csv.reader(f)
        for idx, row in enumerate(f_reader):
            conv_row = []
            if idx > 0:
                for s_idx, value in enumerate(row):
                    if value == 'NULL' or value == 'n/a':
                        value = None
                    elif s_idx in NUMERIC_FIELDS:
                        value = value.replace(',', '')
                    conv_row.append(value)
                cur.execute('''
                    INSERT INTO row_permit_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', conv_row)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()

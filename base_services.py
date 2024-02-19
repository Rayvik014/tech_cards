import pandas as pd
import random

def read_excel_file():
    excel_data = pd.ExcelFile('files/names_base.xlsx')
    tech_civil = excel_data.parse('civil')
    tech_comm = excel_data.parse('commercial')
    tech_mil = excel_data.parse('military')
    tech_aero = excel_data.parse('aero')
    tech_manuf = excel_data.parse('manufacturers')
    tech_country = excel_data.parse('countries')
    return [tech_civil, tech_comm, tech_mil, tech_aero, tech_manuf, tech_country]


def pick_record_from_table(table):
    available_rows = table[table['is_used'].isna()]
    count_rows = len(available_rows)
    random_row = available_rows.loc[random.randrange(count_rows-1)]
    manufacturer = random_row['manufacturer']
    model = random_row['model']
    return manufacturer, model


def get_new_tech(_type, database):
    if _type == 'civil':
        manufacturer, model = pick_record_from_table(database[0])
    if _type == 'commercial':
        manufacturer, model = pick_record_from_table(database[1])
    if _type == 'military':
        manufacturer, model = pick_record_from_table(database[2])
    if _type == 'aero':
        manufacturer, model = pick_record_from_table(database[3])
    manufacture_row = database[4].loc[database[4]['manufacture_name'] == manufacturer]
    emblem_file = manufacture_row.iloc[0]['emblem_file']
    country = manufacture_row.iloc[0]['country']
    country_row = database[5].loc[database[5]['country'] == country]
    flag_file = country_row.iloc[0]['flag_file']
    return (manufacturer, model, emblem_file, flag_file)
    
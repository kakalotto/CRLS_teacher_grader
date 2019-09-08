import os
import delegator
import re

from CRLS_APCSP_autograder.app.hardware_esd_expansion_cards_cases import docs_feedback_hardware_esd_formfactors_cards
from helper_functions.generate_sheets_credential import generate_sheets_credential

# Pass these in as parameters
fulltext_search = 'ESD'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Hardware_',r'Hardware - ', rubric_name)
    p_rubric_name = re.sub(r'ESD_Expansion_cards_cases_lab', r'ESD_cases_expansion_cards - rubric', rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B6', 'B7', 'B8', 'B9', 'B10', 'B12', 'B14',  'F3', 'F4', 'F6']
sheet_name = 'Sheet1'


def get_gdrive_cmd(*, fulltext_search='', mimetype=''):
    # Create the gdrive command and run it
    gdrive_list = 'gdrive list -m 0 --name-width 0 '
    gdrive_query = '--query "not fullText contains \'Template\' and  modifiedTime > \'2019-08-01T00:00:00\' and' \
                   ' \'me\' in owners '
    if fulltext_search:
        gdrive_query += ' and fullText contains \'' + fulltext_search + '\'  '
    else:
        gdrive_query += ' '
    if mimetype:
        gdrive_query += ' and mimeType = \'' + mimetype + "'" 
    else:
        gdrive_query += ' '
    gdrive_query += ' " '
    gdrive_cmd = gdrive_list + gdrive_query
    return gdrive_cmd


service_sheets = generate_sheets_credential()

gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search, mimetype='application/vnd.google-apps.document')
print(gdrive_cmd)
c = delegator.run(gdrive_cmd)
print(c.out)


# Download all the files
lines = c.out.split('\n')
for line in lines:
    if line:
        columns = line.split()
        doc_id = columns[0]
        if doc_id == 'Id':
            continue
        print("doc id")
        print(doc_id)
        
        # From doc_name get rubric_name 
        match = re.search(r'.+? \s+ (.+?) doc', line, re.X | re.M | re.S)
        doc_name = match.group(1)
        doc_name = doc_name.rstrip()
        rubric_name = doc_name_to_rubric_name(doc_name)
        print("doc name")
        print(doc_name)

        # From rubric_name get rubric_id
        gdrive_cmd = get_gdrive_cmd(fulltext_search=rubric_name, mimetype='application/vnd.google-apps.spreadsheet')
        c = delegator.run(gdrive_cmd)
        lines2 = c.out.split('\n')
        rubric_id = lines2[1].split()[0]
        print("rubric_id")
        print(rubric_id)

        # Score?
        datapoints = []
        tests = docs_feedback_hardware_esd_formfactors_cards(doc_id)
        for i, test in enumerate(tests):
            
            print(test)
            print(type(test['pass']))
            if test['pass'] is True:
                value = '0'
            else:
                match = re.search(r'.+? \(([0-9]+) \s* point s* \)', test['name'], re.X | re.M | re.S)
                if match:
                    print("oo oo match" + str(match.group(1)) + "ffff")
                    value = str(-1 * float(match.group(1)))
                else:
                    raise Exception("No match")
                print("YE SYES VALUE " + str(value))
            print(value, value_cells[i])
            range_name = sheet_name + '!' + value_cells[i]
            datapoint = {'range': range_name,
                         'values': [[value]]
            }
            datapoints.append(datapoint)

        body = {'valueInputOption': 'USER_ENTERED',
                'data':datapoints}
        result = service_sheets.spreadsheets().values().batchUpdate(spreadsheetId=rubric_id,
                                                                    body=body).execute()

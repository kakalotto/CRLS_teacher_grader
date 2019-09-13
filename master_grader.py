import os
from CRLS_APCSP_autograder.app.hardware_esd_expansion_cards_cases import docs_feedback_hardware_esd_formfactors_cards

# Pass these in as parameters
#fulltext_search = 'ESD'


# def doc_name_to_rubric_name(p_doc_name):
#     import re
#     p_rubric_name = p_doc_name
#     p_rubric_name = re.sub(r'Hardware_',r'Hardware - ', p_rubric_name)
#     p_rubric_name = re.sub(r'ESD_Expansion_cards_cases_lab', r'ESD_cases_expansion_cards - rubric', p_rubric_name)
#     return p_rubric_name


#value_cells = ['B3', 'B4', 'B6', 'B7', 'B8', 'B9', 'B10', 'B12', 'B14',  'F3', 'F4', 'F6']
# sheet_name = 'Sheet1'


def get_gdrive_cmd(*, fulltext_search='', mimetype='', extra_fulltext=''):
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
    if extra_fulltext:
        gdrive_query += ' and ' + extra_fulltext + ' '
    gdrive_query += ' " '
    p_gdrive_cmd = gdrive_list + gdrive_query
    print("query is " + p_gdrive_cmd)
    return p_gdrive_cmd


def master_grader(fulltext_search_term, doc_name_to_rubric_name, value_cells, *, sheet_name='Rubric', scorer='',
                  rubric_extra_fulltext='', match_cells=[]):
    import delegator
    import re
    from helper_functions.generate_sheets_credential import generate_sheets_credential

    service_sheets = generate_sheets_credential()
    gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document')
    print(gdrive_cmd)
    c = delegator.run(gdrive_cmd)
    print(c.out)

    # Download all the doc files
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
            print("rubric name")
            print(rubric_name)
            match = re.search(r'-\s', doc_name, re.X| re.M | re.S)
            if not match:
                continue
            # From rubric_name get rubric_id
            if rubric_extra_fulltext:
                gdrive_cmd = get_gdrive_cmd(fulltext_search=rubric_name,
                                            mimetype='application/vnd.google-apps.spreadsheet',
                                            extra_fulltext=rubric_extra_fulltext)
            else:
                gdrive_cmd = get_gdrive_cmd(fulltext_search=rubric_name,
                                            mimetype='application/vnd.google-apps.spreadsheet')

            print(gdrive_cmd)
            c = delegator.run(gdrive_cmd)
            print(c)
            lines2 = c.out.split('\n')
            if lines2[1]:
                rubric_id = lines2[1].split()[0]

                print("rubric_id")
                print(rubric_id)
            else:
                print("no rubric, have to skip")
                continue
            
            # Score?
            datapoints = []
#            tests = docs_feedback_hardware_esd_formfactors_cards(doc_id)
            tests = scorer(doc_id)
            match_counter = 0
            for i, test in enumerate(tests):
                if test['pass'] is True:
                    value = '0'
                else:
                    print(test['name'])
                    match = re.search(r'.+? \(([0-9]+\.*[0-9]*) \s* point s* \)', test['name'], re.X | re.M | re.S)
                    if match:
                        value = str(-1 * float(match.group(1)))
                    else:
                        raise Exception("No match couldn't find value of problem ")
                if match_cells:
                    if 'match' in test:
                        text_value = test['match']
                        range_name = sheet_name + '!' + match_cells[match_counter]
                        match_counter += 1
                        datapoint = {'range': range_name, 'values': [[text_value]]}
                        datapoints.append(datapoint)
                print("a " + str(i))
                range_name = sheet_name + '!' + value_cells[i]
                datapoint = {'range': range_name, 'values': [[value]]}
                datapoints.append(datapoint)

            body = {'valueInputOption': 'USER_ENTERED', 'data': datapoints}
            result = service_sheets.spreadsheets().values().batchUpdate(spreadsheetId=rubric_id, body=body).execute()
            print("match_counter" + str(match_counter))

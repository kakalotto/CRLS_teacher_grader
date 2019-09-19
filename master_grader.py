import os

from name_dictionary import names


def get_gdrive_cmd(*, fulltext_search='', mimetype='', extra_fulltext='', python_lab=False):
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
                  rubric_extra_fulltext='', lab_extra_fulltext='', match_cells=[], python_lab_num='',
                  python_rubric_suffix=''):
    import delegator
    import re
    from helper_functions.generate_sheets_credential import generate_sheets_credential

    service_sheets = generate_sheets_credential()
    if lab_extra_fulltext:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document',
                                    extra_fulltext=lab_extra_fulltext)
    else:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document')
    if python_lab_num:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    python_lab=True)
    print(gdrive_cmd)
    c = delegator.run(gdrive_cmd)
    print(c.out)

    # Download all the doc  or PDF filesfiles
    lines = c.out.split('\n')
    for line in lines:
        if line:
            columns = line.split()
            doc_id = columns[0]
            if doc_id == 'Id':
                continue
            print("doc id")
            print(doc_id)

            if python_lab_num:
                # from python lab, get rubric name
#                print("columns[1] " + str(columns[1]))
#                print("lab " + str(python_lab_num))
                python_filename = columns[1]
                found_lab = re.search(python_lab_num, python_filename)
                if found_lab:
                    print("do this: " + str(columns[1]))
                    gdrive_cmd = 'gdrive download ' + str(doc_id)
                    print("gddrive_cmd is this {}".format(gdrive_cmd))
                    c = delegator.run(gdrive_cmd)
                    if c.err:
                        raise Exception("Tried to download python file, failed.")
                    found = 0
                    for key in names.keys():
                        if re.search(key, python_filename):
                            print("Do this one! {}".format(python_filename))
                            rubric_name = names[key] + python_rubric_suffix
                            print("Rubric name {}".format(rubric_name))
                            found = 1
                            break
                    if found == 0:
                        raise Exception("Could not find name {} ".format(python_filename))

                else:
                    print('skip this: ' + str(columns[1]))
                    continue
            else:
                # From doc_name get rubric_name
                match = re.search(r'.+? \s+ (.+?) doc', line, re.X | re.M | re.S)
                doc_name = match.group(1)
                doc_name = doc_name.rstrip()
                rubric_name = doc_name_to_rubric_name(doc_name)
                print("doc name")
                print(doc_name)
                print("rubric name")
                print(rubric_name)
                match = re.search(r'-\s', doc_name, re.X | re.M | re.S)
                if not match:
                    continue
            # From rubric_name get rubric_id
            if rubric_extra_fulltext:  # Doc file here with extra rubric text
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
            if python_lab_num: # python file
                print("python file. filename is {}".format(python_filename))
                tests = scorer(python_filename)
            else:  # doc here
                tests = scorer(doc_id)
            match_counter = 0
            skipped_tests = 0
            # print("xxx tests: {}".format(tests))
            for i, test in enumerate(tests):
                # print('xxx test : {}'.format(test))
                if 'name' in test:
                    if re.search(r'that \s file \s is \s named \s correctly', test['name'], re.X | re.S | re.M):
                        skipped_tests += 1
                        continue
                if test['pass'] is True:
                    value = '0'
                else:
                    # print(test['name'])
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
                # print("a " + str(i))
                range_name = sheet_name + '!' + value_cells[i - skipped_tests]
                datapoint = {'range': range_name, 'values': [[value]]}
                datapoints.append(datapoint)

            body = {'valueInputOption': 'USER_ENTERED', 'data': datapoints}
            result = service_sheets.spreadsheets().values().batchUpdate(spreadsheetId=rubric_id, body=body).execute()
            print("match_counter" + str(match_counter))

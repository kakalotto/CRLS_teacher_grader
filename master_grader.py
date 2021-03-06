import os
import time

from name_dictionary import names
from scratch_names import scratch_names


def get_gdrive_cmd(*, fulltext_search='', mimetype='', extra_fulltext='', extra_nottext='',
                   python_lab=False, scratch_lab=False, person='', lab_name=''):

    # Create the gdrive command and run it
    gdrive_list = 'gdrive list -m 0 --name-width 0 '
    gdrive_query = '--query "not fullText contains \'Template\' and  modifiedTime > \'2020-06-15T00:00:00\' and' \
                   '  \'me\' in owners  '
#                   ' ( \'Kann\' in owners or  \'me\' in owners ) '
#                   '  \'me\' in owners  '
#                   ' ( \'Kann\' in owners or  \'me\' in owners ) '
#                   '  \'me\' in owners  '
#                   ' ( \'Kann\' in owners or  \'me\' in owners ) '
         #          '  \'me\' in owners  '
    print("LAB NAME IS " + str(lab_name))
    if lab_name:
        gdrive_query += ' and name contains \'' + lab_name + '\' '
    elif fulltext_search:
        gdrive_query += ' and fullText contains \'' + fulltext_search + '\'  '
    else:
        gdrive_query += ' '
    if mimetype:
        gdrive_query += ' and mimeType = \'' + mimetype + "'"
    else:
        gdrive_query += ' '
    # print("blahb alh " + extra_fulltext)
    if extra_fulltext:
        gdrive_query += ' and fullText contains \'' + extra_fulltext + '\' '
    if scratch_lab:
        gdrive_query += ' and fullText contains \'sb3\'  '
    if person:
        gdrive_query += ' and fullText contains \'' + person + '\'  '
    gdrive_query += ' " '
    p_gdrive_cmd = gdrive_list + gdrive_query
    print("query is " + p_gdrive_cmd)
    return p_gdrive_cmd


def master_grader(fulltext_search_term, doc_name_to_rubric_name, value_cells, *, sheet_name='Rubric', scorer='',
                  rubric_extra_fulltext='', lab_extra_fulltext='', match_cells=[], python_lab_num='',
                  python_rubric_suffix='', scratch_file=False, scratch_lab_num='', scratch_rubric_suffix='', person='',
                  lab_name=''):
    import delegator
    import re
    from helper_functions.generate_sheets_credential import generate_sheets_credential

    service_sheets = generate_sheets_credential()
    print("ASDF LABNAME " + str(lab_name))
    if lab_name and not person:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document',
                                    extra_fulltext=lab_extra_fulltext, lab_name=lab_name)
    elif lab_name and person:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document',
                                    extra_fulltext=lab_extra_fulltext, person=person, lab_name=lab_name)

    elif lab_extra_fulltext and not person:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document',
                                    extra_fulltext=lab_extra_fulltext)
    elif lab_extra_fulltext and person:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document',
                                    extra_fulltext=lab_extra_fulltext, person=person)
    elif person:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document', person=person)
    else:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    mimetype='application/vnd.google-apps.document')

    if python_lab_num and not person:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    python_lab=True)
    elif python_lab_num and person:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    python_lab=True, person=person)

    elif scratch_file and not person:
        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    scratch_lab=True)
        gdrive_cmd += ' | grep ' + scratch_lab_num
    elif scratch_file and person:
        print("Scratch and person")

        gdrive_cmd = get_gdrive_cmd(fulltext_search=fulltext_search_term,
                                    scratch_lab=True, person=person)
        gdrive_cmd += ' | grep ' + "_" + scratch_lab_num

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
                print("Trying file {} looking for this python number {}".format(python_filename, python_lab_num))

                if re.search(r'extra', python_filename) or re.search(r'startercode', python_filename):
                    continue
                # if re.search(r'jones', python_filename):
                #     continue
                found_lab = re.search(python_lab_num, python_filename)
                if found_lab:
                    print("do this: " + str(columns[1]))
                    gdrive_cmd = 'gdrive download ' + str(doc_id)
                    print("Found lab! gdrive_cmd running is this {}".format(gdrive_cmd))
                    c = delegator.run(gdrive_cmd)
                    #if c.err:
                    #    raise Exception("Tried to download python file, failed." + c.err)
                    found = 0
                    for key in names.keys():
                        print(key)
                        if re.search(key, python_filename):
                            print("Do this one! {}".format(python_filename))
                            rubric_name = names[key] + python_rubric_suffix
                            print("Rubric name {}".format(rubric_name))
                            found = 1
                            break
                    if found == 0:
                        raise Exception("Could not find this name in the name_dictionary file: {} ".format(python_filename))

                else:
                    print('skip this: ' + str(columns[1]))
                    continue
            elif scratch_lab_num:
                columns = line.split()
                doc_id = columns[0]
                if doc_id == 'Id':
                    continue
                print("doc id")
                print(doc_id)
                # from scratch lab, get rubric name
                print("columns[1] " + str(columns[1]))
                print("lab " + str(python_lab_num))

                scratch_filename = columns[1]
                #if re.search(r'finn', scratch_filename):
                #     continue

#                if re.search(r'justin', scratch_filename):
#                    continue

                found_lab = re.search(scratch_lab_num, scratch_filename)
                if found_lab:
                    print("do this: " + str(columns[1]))
                    gdrive_cmd = 'gdrive download ' + str(doc_id)
                    print("Running this : " + str(gdrive_cmd))
                    c = delegator.run(gdrive_cmd)
                    #                    if c.err:
                    #                        raise Exception("Tried to download scratch file, failed. {} asdf".format(c.err))
                    for key in names.keys():
                        if re.search(key, scratch_filename):
                            print("Do this one! {}".format(scratch_filename))
                            rubric_name = names[key] + scratch_rubric_suffix
                            print("Rubric name {}".format(rubric_name))
                else:
                    print('skip this: ' + str(columns[1]))
                    continue

            else:
                # From doc_name get rubric_name
                match = re.search(r'.+? \s+ (.+?) doc', line, re.X | re.M | re.S)
                doc_name = match.group(1)
                doc_name = doc_name.rstrip()
                rubric_name = doc_name_to_rubric_name(doc_name)
                #                rubric_extra_fulltext = rubric_name
                if re.search(r'JULIAN', line, re.X | re.M | re.S):
                    print("YESYES")
                    continue 
                print("doc name")
                print(doc_name)
                print("rubric name rubric extra")
                print(rubric_name)
                match = re.search(r'-\s', doc_name, re.X | re.M | re.S)
                if not match:
                    continue
            # From rubric_name get rubric_i

            #print("yesyesyes")

            if rubric_extra_fulltext:  # Doc file here with extra rubric text
                gdrive_cmd = get_gdrive_cmd(fulltext_search=rubric_name,
                                            mimetype='application/vnd.google-apps.spreadsheet',
                                            extra_fulltext=rubric_extra_fulltext)
            else:
                gdrive_cmd = get_gdrive_cmd(fulltext_search=rubric_name,
                                            mimetype='application/vnd.google-apps.spreadsheet')

            print(' Running this to find rubric:\n ' + gdrive_cmd)
            print("\n\n")
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
            if python_lab_num:  # python file
                print("python file. filename is {}".format(python_filename))
                [_, tests, _] = scorer(python_filename)
            elif scratch_lab_num:
                print("scratch file. filename is {}".format(scratch_filename))
                [_, tests, _] = scorer(scratch_filename)

            else:  # doc here
                tests = scorer(doc_id)
                if 'username' in tests[0]:
                    tests.pop()
                    tests.pop(0)
                    tests = tests[0]
            match_counter = 0
            skipped_tests = 0
            # print("xxx tests: {}".format(tests))
            for i, test in enumerate(tests):
                print("test here")
                print('xxx test : {}'.format(test))

                if 'name' in test:
                    # print("NAME IS")
                    if re.search(r'that \s file \s is \s named \s correctly', test['name'], re.X | re.S | re.M):
                        print("SKIP THIS")
                        skipped_tests += 1
                        continue
                    if re.search(r'that \s Scratch \s variables \s have \s no \s spaces', test['name'], re.X | re.S | re.M):
                        print("SKIP THIS")
                        skipped_tests += 1
                        continue
                    if re.search(r'\s the \s number \s of \s \(non-background\) \s sprite \s is \s equal', test['name'], re.X | re.S | re.M):
                        print("SKIP THIS")
                        skipped_tests += 1
                        continue
                    if re.search(r'different \s names \s than \s regular \s variables', test['name'], re.X | re.S | re.M):
                        print("SKIP THIS")
                        skipped_tests += 1
                        continue
                    # if re.search(r'Checking \s the  \s number \s of \s \(non-background\) \s sprite',
                    #              test['name'], re.X | re.S | re.M):
                    #     print("SKIP THIS")
                    #     skipped_tests += 1
                    #     continue
                if 'username' in test:
                    continue
                print(test)
                if test['pass'] is True:
                    value = '0'
                else:
                    # print(test['name'])
                    match = re.search(r'.+? \(([0-9]+\.*[0-9]*) \s* point s* \s* \)', test['name'], re.X | re.M | re.S)
                    if match:
                        value = str(-1 * float(match.group(1)))
                    else:
                        value = 0
#                        raise Exception("No match couldn't find value of problem ")
                if match_cells:
                    if 'match' in test:
                        # print("MaTCH in this test " + str(match_cells[match_counter]))
                        text_value = test['match']
                        range_name = sheet_name + '!' + match_cells[match_counter]
                        match_counter += 1
                        datapoint = {'range': range_name, 'values': [[text_value]]}
                        datapoints.append(datapoint)
                range_name = sheet_name + '!' + value_cells[i - skipped_tests]
                # print(str(i - skipped_tests) + '  range ' + range_name)

                datapoint = {'range': range_name, 'values': [[value]]}
                datapoints.append(datapoint)

            body = {'valueInputOption': 'USER_ENTERED', 'data': datapoints}
            # print(body)
            result = service_sheets.spreadsheets().values().batchUpdate(spreadsheetId=rubric_id, body=body).execute()
            # print("match_counter" + str(match_counter))
            time.sleep(6.5)

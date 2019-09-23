def feedback_2040(filename):

    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_all_strings, find_questions, find_if, find_elif, find_else
    from CRLS_APCSP_autograder.app.python_labs.python_2_040 import python_2_040
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test

    tests = list()

    filename = './' + filename
    test_filename = filename_test(filename, '2.040')
    tests.append(test_filename)
    if not test_filename['pass']:
        return tests
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Test for prize variables
        test_prizes = find_all_strings(filename_data, [r'prize1 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize2 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize3 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize4 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+', ], 6)
        test_prizes['name'] += "Testing for 4 variables names prize1, prize2, prize3, prize4 (not prize_1, prize_2..." \
                               " <br>"
        tests.append(test_prizes)
        if not test_prizes['pass']:
            test_prizes['fail_message'] += 'Be sure you have 4 variables called  prize1, prize2, prize3, prize4. <br>' \
                                           'Be sure to set their values to be prizes'
            return tests
        else:
            test_question = find_questions(filename_data, 1, 6)
            tests.append(test_question)
            if not test_question['pass']:
                test_question['fail_message'] += "You need to ask the user a question about which door to pick. <br>"
                return tests
            else:
                # test if, check for at least 1 if statement
                test_ifs = find_if(filename_data, 1, 6)
                tests.append(test_ifs)

                # test else check for at least 1 else statement
                test_else = find_else(filename_data, 1, 6)
                tests.append(test_else)

                # look for 3 elifs
                test_elif = find_elif(filename_data, 3, 6)
                tests.append(test_elif)

                test_correct_prizes = python_2_040(filename, filename_data)
                if not test_correct_prizes['pass']:
                    test_correct_prizes['fail_message'] += test_correct_prizes['debug']
                tests.append(test_correct_prizes)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                return tests
            

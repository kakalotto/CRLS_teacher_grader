def feedback_6011(filename):
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, find_elif, find_dictionary
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents

    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '6.011')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:

        test_find_function = find_function(filename, 'bob_kraft_translator', 2, points=5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return tests
        else:

            # Test for dictionary with 3+ items
            filename_data = read_file_contents(filename)

            test_dictionary = find_dictionary(filename_data, num_items=3, points=10)
            tests.append(test_dictionary)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            test_function_1 = run_unit_test('6.011', 1, 10)
            test_function_1['name'] += " (Sent in dictionary  {'wth': 'What the heck'}, search for 'wth', " \
                                       "returned 'what the heck') <br>"
            tests.append(test_function_1)

            test_function_2 = run_unit_test('6.011', 2, 10)
            test_function_2['name'] += " (Sent in dictionary  {'wth': 'What the heck', 'aymm': 'Ay yo my man',}, " \
                                       "looking for aymm, should receive 'Ay yo my man'. <br>"
            tests.append(test_function_2)

            test_function_3 = run_unit_test('6.011', 3, 10)
            test_function_3['name'] += " (Sent in dictionary  {'wth': 'What the heck','aymm': 'Ay yo my man',}, " \
                                       "asdfasdf, received something with 'do not know''. <br>"
            tests.append(test_function_3)

            # Check for 3 ifs on different lines
            test_elifs = find_elif(filename_data, 3, 5, minmax='max')
            tests.append(test_elifs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            return tests
        

def feedback_4023(filename):
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, function_called, find_loop
    from CRLS_APCSP_autograder.app.python_labs.function_test import run_unit_test, extract_all_functions, \
        extract_single_function, create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    test_filename = filename_test(filename, '4.023')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:


        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        test_function_1 = run_unit_test('4.023', 1, 5)
        tests.append(test_function_1)
        test_function_2 = run_unit_test('4.023', 2, 2.5)
        tests.append(test_function_2)
        test_function_3 = run_unit_test('4.023', 3, 2.5)
        tests.append(test_function_3)
        test_function_4 = run_unit_test('4.023', 4, 2.5)
        tests.append(test_function_4)
        test_function_5 = run_unit_test('4.023', 5, 2.5)
        tests.append(test_function_5)
        test_function_6 = run_unit_test('4.023', 6, 2.5)
        tests.append(test_function_6)
        test_function_7 = run_unit_test('4.023', 7, 2.5)
        tests.append(test_function_7)
        test_function_8 = run_unit_test('4.023', 8, 2.5)
        tests.append(test_function_8)
        test_function_9 = run_unit_test('4.023', 9, 2.5)
        tests.append(test_function_9)



        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        return tests
    

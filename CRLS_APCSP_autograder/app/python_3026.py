def feedback_3026(filename):
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_string, find_function, function_called, find_loop
    from CRLS_APCSP_autograder.app.python_labs.function_test import run_unit_test, create_testing_file, extract_all_functions, \
        extract_single_function
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8

    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '3.026')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        # Check for function return_min
        test_find_function = find_function(filename, 'return_min', 1, points=5)
        tests.append(test_find_function)

        # Only continue if you have a return_min_function
        if test_find_function['pass'] is False:
            return tests
        else:
            extract_all_functions(filename)
            create_testing_file(filename)

            return_min_function = extract_single_function(filename, 'return_min')

            # Check that function is called 1x
            test_function_run = function_called(filename, 'return_min', 1, points=5)
            tests.append(test_function_run)

            # find string return (return in the function)
            test_return = find_string(return_min_function, r'return \s .+', 1, points=2.5)
            test_return["name"] += " (There is a return in the function)"
            test_return["fail_message"] += " (There is a return in the function)"
            tests.append(test_return)

            # find loop in function
            test_loop = find_loop(return_min_function, 2.5)
            test_loop["name"] += " (There is a loop in the code)"
            test_loop["fail_message"] += " (There is a loop in the function)"
            tests.append(test_loop)
         # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('3.026', 1, 5)
            test_function_1['name'] += " (return_min with list [-1, 3, 5, 99] returns -1) "
            tests.append(test_function_1)

            # function test 2
            test_function_2 = run_unit_test('3.026', 2, 5)
            test_function_2['name'] += " (return_min with list [-1, 3, 5, -99] returns -99) "
            tests.append(test_function_2)

            # function test 3
            test_function_3 = run_unit_test('3.026', 3, 5)
            test_function_3['name'] += " (return_min with list [5] returns 5) "
            tests.append(test_function_3)

            # function test 4
            test_function_4 = run_unit_test('3.026', 4, 5)
            test_function_4['name'] += " (return_min with list [5, 4, 99, -11, 44, -241, -444, -999, 888, -2] " \
                                       "returns -444) "
            tests.append(test_function_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            return tests
        

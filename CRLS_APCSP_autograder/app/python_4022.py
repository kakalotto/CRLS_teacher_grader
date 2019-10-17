def feedback_4022(filename):
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, function_called, find_loop
    from CRLS_APCSP_autograder.app.python_labs.function_test import run_unit_test, extract_all_functions, \
        extract_single_function, create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8

    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '4.022')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        # Check for function
        test_find_function = find_function(filename, 'bad_lossy_compression', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return tests
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'bad_lossy_compression')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 2.5)
            test_loop['name'] += "Testing there is a loop in the bad_lossy_compression function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return tests
            else:
                test_function_run = function_called(filename, 'bad_lossy_compression', 3, points=5)
                tests.append(test_function_run)

                # test1
                test_function_1 = run_unit_test('4.022', 1, 5)
                test_function_1['name'] += " (Testing calling bad_lossy_compression with 'The rain in spain falls " \
                                           "mainly in the plain' returns 'The ain n spin flls ainl in he pain') "
                tests.append(test_function_1)

                # test2 for the_rock_says
                test_function_2 = run_unit_test('4.022', 2, 5)
                test_function_2['name'] += " (Testing calling bad_lossy_compression with " \
                                           "'I am sick and tired of these darned snakes on this darned plane'" \
                                           " returns 'I a sik ad tredof hes danedsnaes n tis arnd pane' <br> "
                tests.append(test_function_2)

                # test3 for the_rock_says
                test_function_3 = run_unit_test('4.022', 3, 5)
                test_function_3['name'] += "Testing calling bad_lossy_compression with 'Madness?!?!?!?!" \
                                           " THIS IS SPARTA!!!!'" \
                                           " returns 'Madess!?!!?!THI ISSPATA!!!' <br> "
                tests.append(test_function_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

            return tests
        

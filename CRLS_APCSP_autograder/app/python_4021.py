def feedback_4021(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, function_called, find_loop
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.function_test import run_unit_test, extract_all_functions, extract_single_function, \
        create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8

    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '4.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function the_rock_says
        test_find_function = find_function(filename, 'the_rock_says', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return tests
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)
            function_data = extract_single_function(filename, 'the_rock_says')

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 2.5)
            test_loop['name'] += "Testing there is a loop in the the_rock_says function.<br>"
            tests.append(test_loop)

            # Check that function is called 3x
            test_function_run = function_called(filename, 'the_rock_says', 3, points=5)
            
            tests.append(test_function_run)
            
            # test1 for the_rock_says
            test_function_1 = run_unit_test('4.021', 1, 5)
            test_function_1['name'] += " (Testing calling the_rock_says with list ['eggs', 'apple'] returns a " \
                                       "list ['The Rock says eggs', 'The Rock says apple']) (caps unimportant)"
            tests.append(test_function_1)
            
            # test2 for the_rock_says
            test_function_2 = run_unit_test('4.021', 2, 5)
            test_function_2['name'] += " (Testing calling the_rock_says with list ['eggs', 'smell'] returns " \
                                       "['The Rock says eggs', 'Do you smell what The Rock is cooking'] (caps unimportant) <br>"
            tests.append(test_function_2)
            
            # test3 for the_rock_says
            test_function_3 = run_unit_test('4.021', 3, 5)
            test_function_3['name'] += " (Testing calling the_rock_says with list " \
                                       "['eggs', 'what should I think'] returns ['The Rock says eggs', 'It doesn't matter what you think' (caps unimportant) "
            tests.append(test_function_3)
            
            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)
            return tests
            

def feedback_4012(filename):
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, find_loop, function_called, find_if
    from CRLS_APCSP_autograder.app.python_labs.function_test import run_unit_test, extract_single_function,\
        extract_all_functions, create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8

    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '4.012')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:

        # Check for function
        test_find_function = find_function(filename, 'samuel_l_algorithm', 1, points=5)
        tests.append(test_find_function)

        extract_all_functions(filename)
        function_data = extract_single_function(filename, 'samuel_l_algorithm')
        create_testing_file(filename)
        
        # Check for a loop of some sort (for or while)
        test_loop = find_loop(function_data, 5)
        test_loop['name'] += "Testing there is a loop in the samuel_l_algorithm function.<br>"
        tests.append(test_loop)
        
        # Check that function is called 3x
        test_function_run = function_called(filename, 'samuel_l_algorithm', 3, points=5)
        tests.append(test_function_run)
        
        test_ifs = find_if(function_data, 3, 5, minmax='max')
        tests.append(test_ifs)
        
        test_function_1 = run_unit_test('4.012', 1, 10)
        test_function_1['name'] += " (samuel_l_algorithm with 'Birdman or (The Unexpected Virtue of Ignorance)'" \
                                   " returns 'bad) "
        tests.append(test_function_1)
        
        test_function_2 = run_unit_test('4.012', 2, 10)
        test_function_2['name'] += " (samuel_l_algorithm with 'Snakes on a plane' returns 'good') "
        tests.append(test_function_2)
        test_function_3 = run_unit_test('4.012', 3, 10)
        test_function_3['name'] += " (samuel_l_algorithm with 'aladdin' returns 'maybe') "
        tests.append(test_function_3)
        
        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 14)
        tests.append(test_pep8)
        test_help = helps(filename, 5)
        tests.append(test_help)
        
        return tests
            

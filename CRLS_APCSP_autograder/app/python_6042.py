def feedback_6042(filename):
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, find_loop, find_dictionary, function_called
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test, \
        extract_single_function
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.python_6_041 import five_loop
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents

    tests = list()
    test_filename = filename_test(filename, '6.042')
    tests.append(test_filename)
    if not test_filename['pass']:
        return tests
    else:
        filename_data = read_file_contents(filename)

        # Check for function add with 1 inputs
        test_find_function = find_function(filename, 'worst_hit', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return tests
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)
            # unit tests
            test_function_1 = run_unit_test('6.042', 1, 5)
            tests.append(test_function_1)
            test_function_2 = run_unit_test('6.042', 2, 5)
            tests.append(test_function_2)

            # Check for function 2 inputs
            test_find_function_2 = find_function(filename, 'top_hits', 1, points=5)
            tests.append(test_find_function_2)

            run_simulation_function = extract_single_function(filename, 'top_hits')
            test_run_sim = find_loop(run_simulation_function, 5)
            test_run_sim['name'] = "Looking for loop in the run_simulation function (5 points).<br>"
            tests.append(test_run_sim)

            # unit tests
            test_function_3 = run_unit_test('6.042', 3, 5)
            tests.append(test_function_3)
            test_function_4 = run_unit_test('6.042', 4, 5)
            tests.append(test_function_4)

            test_dictionary = find_dictionary(filename_data, num_items=6, points=5)
            tests.append(test_dictionary)
            test_function_run = function_called(filename, 'worst_hit', 3, points=5)
            tests.append(test_function_run)
            test_function_run = function_called(filename, 'top_hits', 3, points=5)
            tests.append(test_function_run)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)
            return tests
 

def feedback_6031(filename):
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, run_unit_test, create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, find_loop, find_dictionary
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '6.031')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        filename_data = read_file_contents(filename)

        test_dictionary = find_dictionary(filename_data, num_items=0, points=5)
        tests.append(test_dictionary)
        if test_dictionary['pass'] is False:
            return tests
        else:

            # Check for function add with 3 inputs
            test_find_function = find_function(filename, 'add', 3, points=5)
            tests.append(test_find_function)
            if test_find_function['pass'] is False:
                return tests
            else:

                extract_all_functions(filename)
                create_testing_file(filename)

                # function test 1
                test_function_1 = run_unit_test('6.031', 1, 5)
                tests.append(test_function_1)
                # function test 2
                test_function_2 = run_unit_test('6.031', 2, 10)
                tests.append(test_function_2)

                # Check for function add with 2 inputs
                test_find_function = find_function(filename, 'get', 2, points=5)
                tests.append(test_find_function)
                if test_find_function['pass'] is False:
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)
                else:
                    # function test 3
                    test_function_3 = run_unit_test('6.031', 3, 5)
                    tests.append(test_function_3)

                    # function test 3
                    test_function_4 = run_unit_test('6.031', 4, 10)
                    tests.append(test_function_4)

                    # Check for a loop of some sort (for or while)
                    test_loop = find_loop(filename_data, 5)
                    tests.append(test_loop)

                    # Find number of PEP8 errors and helps
                    test_pep8 = pep8(filename, 14)
                    tests.append(test_pep8)
                    test_help = helps(filename, 5)
                    tests.append(test_help)

                    return tests
                

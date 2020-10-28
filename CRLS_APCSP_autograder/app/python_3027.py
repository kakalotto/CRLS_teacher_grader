def route_python_3_027(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_string, find_function, function_called, find_loop
    from CRLS_APCSP_autograder.app.python_labs.function_test import run_unit_test, create_testing_file, extract_all_functions, \
        extract_single_function
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=44.5, score_manual=11)
    test_filename = filename_test(filename, '3.027')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        tests.append(find_function(filename, 'longest_reception', 1, points=5))
        extract_all_functions(filename)
        create_testing_file(filename)
        longest_reception_function = extract_single_function(filename, 'longest_reception')
        tests.append(function_called(filename, 'longest_reception', 1, points=5))

        # find string return (return in the function)
        return_link = ''
        tests.append(find_string(longest_reception_function, r'return \s .+', 1, points=2.5,
                                 description='Testing that there is a string "return" in the function',
                                 help_link=return_link))

        loop_link = 'https://docs.google.com/presentation/d/1jfcPojBgjVXL2ql2kN-FW2ML6yVzE2H67cc9UO4yKzo/e' \
                    'dit#slide=id.g8cb34fff74_0_0'
        tests.append(find_loop(longest_reception_function, 2.5,
                               description='There is a loop in the function',
                               help_link=loop_link))
        extract_all_functions(filename)
        create_testing_file(filename)
        run_link = 'https://docs.google.com/presentation/d/1jfcPojBgjVXL2ql2kN-FW2ML6yVzE2H67cc9UO4yKzo/' \
                   'edit#slide=id.g8cf0cdf918_0_0'
        tests.append(run_unit_test('3.027', 1, 5,
                                   description='Calling longest_reception with list [0, 40, 80, 10, 13.5]; '
                                               'should return 80',
                                   help_link=run_link))
        tests.append(run_unit_test('3.027', 2, 5,
                                   description='Calling longest_reception with list [-1, 3, 5, 3]; should return 5',
                                   help_link=run_link))
        tests.append(run_unit_test('3.027', 3, 5,
                                   description='Calling longest_reception with list [5]; should return 5',
                                   help_link=run_link))
        tests.append(run_unit_test('3.027', 4, 5,
                                   description='Calling longest_reception with list '
                                               '[5, 4, 9, -1, 44, 55, 66, 8, -2]; should return 66',
                                   help_link=run_link))
        tests.append(pep8(filename, 7))
        tests.append(helps(filename, 2.5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]
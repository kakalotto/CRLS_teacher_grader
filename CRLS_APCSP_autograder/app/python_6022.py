def route_python_6_022(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, function_called, find_dictionary
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, extract_single_function, \
        create_testing_file, run_unit_test
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=69, score_manual=11)
    test_filename = filename_test(filename, '6.022')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        extract_all_functions(filename)
        create_testing_file(filename)
        test_find_function = find_function(filename, 'dr_lam_workout_counter', 1, points=10)
        tests.append(test_find_function)
        test_function_run = function_called(filename, 'dr_lam_workout_counter', 3, points=10)
        tests.append(test_function_run)
        dr_lam_function = extract_single_function(filename, 'dr_lam_workout_counter')
        test_dictionary = find_dictionary(dr_lam_function, num_items=0, points=10)
        tests.append(test_dictionary)
        test_function_1 = run_unit_test('6.022', 1, 10,
                                        help_link='https://drive.google.com/file/d/1Ohm2eMdFdRLbSMMH8mCMXVBQJRalqC4h/'
                                                  'view?usp=sharing')
        tests.append(test_function_1)
        test_function_2 = run_unit_test('6.022', 2, 10,
                                        help_link='https://docs.google.com/presentation/d/1-Us-Uaf_59FoYxVwcXCX'
                                                  '1JpgcqGb6w1EHsHkfLTFazo/edit#slide=id.g90b2ba3b83_0_0')
        tests.append(test_function_2)
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]
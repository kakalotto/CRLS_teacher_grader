def route_python_4_028(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_loop, find_string
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, create_testing_file, extract_single_function, \
        run_unit_test
    # from app.python_labs.python_4_025 import win_all, win_most
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    from app.python_labs.python_4_028 import full_run

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=84, score_manual=11)
    test_filename = filename_test(filename, '4.028')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        extract_all_functions(filename)
        create_testing_file(filename)
        help_link = 'https://drive.google.com/file/d/1pcgQnkjbwZtqFiaUa0PjyY9vNGsvxZUQ/view?usp=sharing'
        tests.append(run_unit_test('4.028', 1, 10,
                                   description="Testing round_result function - 10000 runs with 90% win should "
                                               "give between 8850 and 9150 wins", help_link=help_link))
        tests.append(run_unit_test('4.028', 2, 5,
                                   description="Testing round_result - 10000 runs with 0% win should give 0 wins",
                                   help_link=help_link))
        tests.append(run_unit_test('4.028', 3, 5,
                                   description="Testing game function - 10000 runs with "
                                               "100% win should give 10000 wins",
                                   help_link=help_link))
        loop_link = 'https://docs.google.com/presentation/d/1zUYcVIBO2oIIa_rLWB2ODthLvTBWXc9b2ITCDbrHYBw/' \
                    'edit#slide=id.ga461190e43_1_0'
        match_result_function = extract_single_function(filename, 'match_result')
        tests.append(find_loop(match_result_function, 5,
                               description='There is a loop in the match_result function', help_link=loop_link))
        tests.append(run_unit_test('4.028', 4, 5,
                                   description="Testing match_result function.  If I call match_result with "
                                               "input parameter (75), and run 10,000 matches, I  "
                                               "should have between   and  (10points).<br>",
                                   help_link=help_link))
        tests.append(run_unit_test('4.028', 5, 5,
                                   description="Testing match_result function.  If I call match_result with "
                                               "input parameter (0), and run 10,000 matches, I  "
                                               "should win 0 times (5 points).<br>",
                                   help_link=help_link))
        tests.append(run_unit_test('4.028', 6, 10,
                                   description="Testing match_result function.  If I call match_result with "
                                               "input parameter (75), and run 10,000 matches, I "
                                               "should have 10,000 wins (5 points).<br>",
                                   help_link=help_link))
        tests.append(find_string(match_result_function, 'round_result', 1, points=5,
                                 description='match_result calls round_result'))
        tests.append(full_run(filename, 75))
        tests.append(full_run(filename, 100))
        tests.append(full_run(filename, 0))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]

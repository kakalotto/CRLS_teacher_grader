def route_python_4_021(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, function_called, find_loop
    from CRLS_APCSP_autograder.app.python_labs.function_test import run_unit_test, extract_all_functions, extract_single_function, \
        create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=37, score_manual=11)
    test_filename = filename_test(filename, '4.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        test_find_function = find_function(filename, 'the_rock_says', 1, points=5)
        tests.append(test_find_function)
        extract_all_functions(filename)
        create_testing_file(filename)
        function_data = extract_single_function(filename, 'the_rock_says')
        loop_link = 'https://docs.google.com/presentation/d/1j2hs8-LijkXe6E-9idSnbbsr3l6ql0SzbWlhDMzCGUU/' \
                    'edit#slide=id.g40e52091b3_0_38'
        tests.append(find_loop(function_data, 2.5,
                               description='There is a loop in the function',
                               help_link=loop_link))
        tests.append(function_called(filename, 'the_rock_says', 3, points=5))
        run_link = 'https://docs.google.com/presentation/d/1w2XmELIdscPcIk1ddPEg6gAtBUcwn_5ocLV2PSsGB_E/' \
                   'edit#slide=id.g8cf0cdf918_0_0'
        tests.append(run_unit_test('4.021', 1, 2.5,
                                   description="Calling the_rock_says with list ['eggs', 'apple'] returns a "
                                               "list ['The Rock says eggs', 'The Rock says apple']) "
                                               "(caps unimportant, spacing unimportant)",
                                   help_link=run_link))
        tests.append(run_unit_test('4.021', 2, 2.5,
                                   description="Calling the_rock_says with list ['eggs', 'apple'] returns a "
                                               "list ['The Rock says eggs', 'The Rock says apple']) "
                                               "(caps unimportant, but spacing counts!!)",
                                   help_link=run_link))
        tests.append(run_unit_test('4.021', 3, 5,
                                   description="Calling the_rock_says with list ['eggs', 'smell'] returns "
                                               "['The Rock says eggs', 'Do you smell what The Rock is cooking'] "
                                               "(caps unimportant) <br>",
                                   help_link=run_link))
        tests.append(run_unit_test('4.021', 4, 5,
                                   description="Calling the_rock_says with list ['eggs', 'what should I think'] "
                                               "returns ['The Rock says eggs', 'It doesn't matter what you think' ]"
                                               "(caps unimportant) ",
                                   help_link=run_link))
        tests.append(pep8(filename, 7))
        tests.append(helps(filename, 2.5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]
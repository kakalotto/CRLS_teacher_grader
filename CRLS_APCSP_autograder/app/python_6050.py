
def route_python_6_050(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, find_loop, find_string, function_called
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test, \
        extract_single_function
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test

    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=69, score_manual=11)
    test_filename = filename_test(filename, '6.050')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        test_find_function = find_function(filename, 'honest_johnny_time', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return [user, tests, score_info]
        else:
            extract_all_functions(filename)
            create_testing_file(filename)
            tests.append(function_called(filename, 'homework_times', 1, points=5))
            honest_johnny_function = extract_single_function(filename, 'honest_johnny_time')
            loop_link = 'https://docs.google.com/presentation/d/1jWHQTT5G6B1XqfpUlYaWHXqNhKco2ehIAzdbJnngaXs/' \
                        'edit#slide=id.ga13fe700cb_0_0'
            tests.append(find_loop(honest_johnny_function, 5,
                                   description='There is a loop in the honest_johnny_time function',
                                   help_link=loop_link))
            tests.append(run_unit_test('6.050', 1, 10,
                                       description='Checking honest_johnny works.<br>   Input dictionary: '
                                                   '{0: 10, 1: 20, 2: 5, 3: 2} should give a time of 37 minutes ',
                                       help_link=loop_link))
            test_find_function = find_function(filename, 'cheating_johnny_time', 1, points=5)
            tests.append(test_find_function)
            if test_find_function['pass'] is False:
                return [user, tests, score_info]
            else:
                cheating_johnny_function = extract_single_function(filename, 'cheating_johnny_time')
                cheating_help_link = 'https://docs.google.com/presentation/d/1jWHQTT5G6B1XqfpUlYaWHXqNhKco2eh' \
                                     'IAzdbJnngaXs/edit#slide=id.ga13fe700cb_0_5'
                tests.append(find_string(cheating_johnny_function,
                                         r'(for .*? in|while) .*? (for .*? in|while)', 1, points=5,
                                         description="Checking that cheating johnny function has a double loop.<br>",
                                         help_link=cheating_help_link))
                tests.append(run_unit_test('6.050', 2, 5,
                                           description='Checking cheating_johnny works.<br>   '
                                                       'If Johnny has homework that is broken up like so: <br>'
                                                       '[{0:10, 1:20, 2: 30}, {3: 40, 4: 5, 5: 10}, '
                                                       '{6: 0, 7: 2, 8:, 9},'
                                                       ' {10: 12, 12: 13, 13: 14}] <br>'
                                                       'and there is a 100 minute penalty'
                                                       ' for sorting and '
                                                       'distributing, the total time it will take Johnny and friends '
                                                       'to do homework'
                                                       'is 160 minutes ',
                                           help_link=cheating_help_link))
                tests.append(run_unit_test('6.050', 3, 5,
                                           description='Checking cheating_johnny works.<br>   '
                                                       'If Johnny has homework that is broken up like so: <br>'
                                                       '[{0: 6, 1: 6, 2: 4, 3: 12, 4: 2, 5: 19, 6: 20, 7: 5, 8: 16, '
                                                       '9: 1, 10: 7, 11: 1, '
                                                       '12: 20, 13: 16, 14: 2, 15: 19, 16: 17}, '
                                                       '{17: 10, 18: 14, 19: 5, 20: 17, 21: 4, '
                                                       '22: 15, 23: 5, 24: 7, 25: 8, 26: 7, 27: 14, 28: 16, '
                                                       '29: 17, 30: 10, 31: 11, '
                                                       '32: 9, 33: 15}, '
                                                       '{34: 12, 35: 12, 36: 7, 37: 13, 38: 20, 39: 18, 40: 11, '
                                                       '41: 18, 42: 17, '
                                                       '43: 3, 44: 3, 45: 9, 46: 2, 47: 13, 48: 12, 49: 16}] '
                                                       'and there is a 100 minute penalty for sorting and '
                                                       'distributing, the total time it will take Johnny and '
                                                       'friends to do homework'
                                                       'is 286 minutes ',
                                           help_link=cheating_help_link))
                tests.append(io_test(filename, r'speed \s* up .*? 2 .*? friends .*? speed \s* up .*? 5 .*? friends .*?'
                                               r'speed \s* up .*? 25 .*? friends', 1,
                                     points=5,
                                     description='Ran the code.  Expected to find the string "speedup for 2 friends is"'
                                                 '..."speedup for 5 friends is"...."speedup for 25 friends is"',
                                     help_link='https://docs.google.com/document/d/1sRN7tX5eTM9ePYPyvs-Y7VubdXO6H3A0u'
                                               'i19oVOhvl4/edit#bookmark=id.c4f9hepoo2k0'))
                tests.append(pep8(filename, 14))
                tests.append(helps(filename, 5))
                score_info['finished_scoring'] = True
                score_info = sum_score(tests, score_info)
                return [user, tests, score_info]
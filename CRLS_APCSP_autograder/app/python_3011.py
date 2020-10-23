def route_python_3_011(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions, find_list, find_random, find_print
    from CRLS_APCSP_autograder.app.python_labs.python_3_011 import python_3_011_2, python_3_011_1
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=64, score_manual=11)
    test_filename = filename_test(filename, '3.011')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        filename_data = read_file_contents(filename)
        tests.append(find_list(filename_data, num_items=6, list_name='houses', points=10,
                               description='Looking for list named exactly "houses" with 6+ items<br>'))
        tests.append(find_questions(filename_data, 1, 5,
                                    description='Ask user a question to influence the hat.<br>This question is ignored '
                                                'but please save it to a variable anyway '
                                                '(i.e. question = input(stuff)'))
        tests.append(find_random(filename_data, 5))
        print_help = 'https://docs.google.com/presentation/d/1u-Qw_AOBVPfLxKBlT-aBAkSb1Sn3SFLYRyF37GMVcKA/' \
                     'edit#slide=id.g43f58452bd_1_0'
        tests.append(find_print(filename_data, 1, 5, description='Print out the random house that is picked.',
                                help_link=print_help))
        tests.append(find_random(filename_data, 5, randint=True))
        tests.append(python_3_011_1(filename_data, 5))
        tests.append(python_3_011_2(filename, filename_data, 10))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]

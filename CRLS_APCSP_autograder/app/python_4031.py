def route_python_4_031(filename):
    from CRLS_APCSP_autograder.app.python_labs.function_test import create_testing_file, extract_all_functions, run_unit_test
    from CRLS_APCSP_autograder.app.python_labs.python_4_03x import python_4_031_double_loops, python_4_031_good_prints
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=64, score_manual=11)
    test_filename = filename_test(filename, '4.031')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        extract_all_functions(filename)
        create_testing_file(filename)
        help_link = 'https://drive.google.com/file/d/1ufkJolgWSd-uxQZ1eIaAE4iwAvaTz6nY/view'
        loop6_link = 'https://drive.google.com/file/d/1ufkJolgWSd-uxQZ1eIaAE4iwAvaTz6nY/view?t=14m30s'
        tests.append(run_unit_test('4.031', 1, 2.5, description='loop1 looks correct', help_link=help_link))
        tests.append(run_unit_test('4.031', 2, 2.5, description='loop2 looks correct', help_link=help_link))
        tests.append(run_unit_test('4.031', 3, 2.5, description='loop3 looks correct', help_link=help_link))
        tests.append(run_unit_test('4.031', 4, 5, description='loop4 looks correct', help_link=help_link))
        loop5_help = 'https://docs.google.com/presentation/d/1rKJ4N7jcsWYseB-JghW1a-Qf7kHtuCfQ-I80MSU2WpU/' \
                     'edit#slide=id.g910a641c3e_0_l0'
        tests.append(run_unit_test('4.031', 5, 5, description='loop5 looks correct', help_link=loop5_help))
        tests.append(run_unit_test('4.031', 6, 5, description='loop6 looks correct', help_link=loop6_link))
        loop7_link = 'https://docs.google.com/presentation/d/1rKJ4N7jcsWYseB-JghW1a-Qf7kHtuCfQ-I80MSU2WpU/' \
                     'edit#slide=id.g910a641c3e_1_6'
        tests.append(run_unit_test('4.031', 7, 5, description='loop7 looks correct', help_link=loop7_link))
        loop8_link = 'https://docs.google.com/presentation/d/1rKJ4N7jcsWYseB-JghW1a-Qf7kHtuCfQ-I80MSU2WpU/' \
                     'edit#slide=id.g910a641c3e_1_11'
        tests.append(run_unit_test('4.031', 8, 7.5, description='loop8 looks correct', help_link=loop8_link))
        tests.append(python_4_031_double_loops(filename))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]
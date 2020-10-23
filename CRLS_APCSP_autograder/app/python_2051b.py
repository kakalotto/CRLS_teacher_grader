
def route_python_2_051b(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_if, find_questions, find_list, find_elif, find_else
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=32.5, score_manual=11)
    test_filename = filename_test(filename, '2.051b')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        filename_data = read_file_contents(filename)
        tests.append(find_list(filename_data, num_items=4, list_name='learning_communities', points=3,
                               description='Looking for list named exactly "learning_communities" with 4 items<br>'
                                           "List items should be 'C', 'R', 'L', and 'S' (this is not tested)."))
        tests.append(find_list(filename_data, num_items=4, list_name='scores', points=3,
                               description='Looking for list named exactly "scores" with 4 items<br>'
                                           'All list items should be zero at first (this is not tested).'))
        tests.append(find_questions(filename_data, 1, 1,
                                    description='You must ask the user a question about which LC to vote for'))
        tests.append(find_if(filename_data, 1, 1))
        tests.append(find_else(filename_data, 1, 4))
        elif_help = 'https://docs.google.com/presentation/d/1uH-3Md7NZ3GJHEH0J7UNUlw9tXyyAh_om4gux_2rV2U/' \
                    'edit#slide=id.g338c39f182_0_58'
        tests.append(find_elif(filename_data, 3, 1, help_link=elif_help))
        tests.append(io_test(filename, r'\[\s*2\s*,\s*1\s*,\s*1\s*,\s*1\s*\]', 1,
                             points=5,
                             description='Ran the code and answered C, C, R, L, S.  Program should '
                                         'print [2, 1, 1, 1]',
                             help_link='https://docs.google.com/document/d/1I078s2LQeYGYSFGqc'
                                       'MyB5a1DM4UnCMrHqp0ZyXGfhkY/edit#bookmark=id.yrgfnbdq760i'))
        tests.append(io_test(filename, r'\[\s*1\s*,\s*1\s*,\s*1\s*,\s*1\s*\]', 2,
                             points=5,
                             description='Ran the code and answered C, R, L, S, blahblah.  Program should '
                                         'print [1, 1, 1, 1]',
                             help_link='https://docs.google.com/document/d/1I078s2LQeYGYSFGqcMyB5a1DM4Un'
                                       'CMrHqp0ZyXGfhkY/edit#bookmark=id.v4kazwxsmt90'))
        tests.append(pep8(filename, 7))
        tests.append(helps(filename, 2.5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]


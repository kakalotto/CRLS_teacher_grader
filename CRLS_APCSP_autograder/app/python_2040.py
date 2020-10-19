def route_python_2_040(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_all_strings, find_questions, find_if, find_elif, find_else
    from CRLS_APCSP_autograder.app.python_labs.python_2_040 import python_2_040
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=61, score_manual=11)
    test_filename = filename_test(filename, '2.040')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        filename_data = read_file_contents(filename)
        prize_help = 'https://docs.google.com/presentation/d/1Uh_zlH-FUgYJaEW1fA3YOxQNfWver55g_EncWLVJ3-0/' \
                     'edit#slide=id.g8c389caccd_3_0'
        tests.append(find_all_strings(filename_data, [r'prize1 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                      r'prize2 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                      r'prize3 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                      r'prize4 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+', ], 6,
                                      description='Testing for 4 variables names prize1, prize2, prize3, prize4',
                                      help_link=prize_help))
        tests.append(find_questions(filename_data, 1, 6, description='Ask user a question about which door to pick'))
        tests.append(find_if(filename_data, 1, 6))
        tests.append(find_else(filename_data, 1, 6))
        elif_help = 'https://docs.google.com/presentation/d/1uH-3Md7NZ3GJHEH0J7UNUlw9tXyyAh_om4gux_2rV2U/' \
                    'edit#slide=id.g338c39f182_0_58'
        tests.append(find_elif(filename_data, 3, 6, help_link=elif_help))
        tests.append(python_2_040(filename, filename_data))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]
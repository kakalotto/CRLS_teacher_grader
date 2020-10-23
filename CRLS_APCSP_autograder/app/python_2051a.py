def route_python_2_051a(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_string, find_questions
    from CRLS_APCSP_autograder.app.python_labs.python_2_05x import python_2_051a, efficiency
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=32.5, score_manual=11)
    test_filename = filename_test(filename, '2.051a')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        filename_data = read_file_contents(filename)
        tests.append(find_string(filename_data, r'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]', 1, points=5,
                                 description='Testing for list prizes.  prizes is a list with exactly 4 items.'
                                             'Prizes needs to be named exactly "prizes"',
                                 help_link='https://docs.google.com/presentation/d/115yqVHY0APEvQFTQ0fGNbw81pX4gv4kfl'
                                           'TUfco1E_Q8/edit#slide=id.g3fda053d45_1_2'))
        tests.append(find_questions(filename_data, 1, 5,
                                    description='Ask user a question about which door to pick'))
        tests.append(python_2_051a(filename, filename_data))
        tests.append(efficiency(filename_data, 5))
        tests.append(pep8(filename, 7))
        tests.append(helps(filename, 2.5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]





def route_python_1_040(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test
    from CRLS_APCSP_autograder.app.python_labs.python_1_040 import statement_variables
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=34.5, score_manual=5.5)
    print("starting")
    test_filename = filename_test(filename, '1.040')
    tests.append(test_filename)
    print("one")
    if test_filename['pass'] is False:
        return tests
    else:
        filename_data = read_file_contents(filename)
        tests.append(find_questions(filename_data, 3, 5))
        help_link = 'https://docs.google.com/presentation/d/1R1jJfHfXgtZAjrYpC8lKL7uG4VW5Ujy8h3TawLWab3A/' \
                    'edit#slide=id.g8669460cfd_6_0'
        tests.append(io_test(filename, r'.+ wish1 .+ wish2 .+ wish3 ', 1, points=5,
                             description='Check things are in correct order in output - '
                                         'wishing for wish1, wish2, wish3 '
                                         ' should print \'your wishes are wish1, wish2, and wish3, '
                                         'with correct spacing\' <br>" ',
                             help_link=help_link))
        tests.append(find_questions(filename_data, 6, 5))
        tests.append(statement_variables(filename_data, 5))
        tests.append(io_test(filename, r'.+ wish1 .+ wish2 .+ wish3 .+ wishb .+ wishc .+ wisha ', 1, points=5,
                             description='Check things are in correct order in output - '
                                         'wishing for wish1, wish2, wish3 then'
                                         'wisha, wishb, and wishc should print out \'your wishes are wish1, wish2,'
                                         'and wish3 , then print out wishb, wishc, and wisha with '
                                         'correct spacing\' <br>" ',
                             help_link=help_link))
        tests.append(pep8(filename, 7))
        tests.append(helps(filename, 2.5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return tests

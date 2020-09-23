def route_python_2_021(filename):

    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions, find_string
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=55, score_manual=11)
    test_filename = filename_test(filename, '2.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        filename_data = read_file_contents(filename)
        tests.append(find_questions(filename_data, 1, 5))
        tests.append(find_string(filename_data, r'( int\(1 | float\( )', 1, points=5,
                                 description='Checking that there is casting of any sort to either int or float'))
        help_link = 'https://docs.google.com/document/d/16b7Rv3g0jQtTxcMBvflu1hGST-z2KxMbjPvedfIsE0Y/' \
                    'edit#bookmark=id.x3i91ba2p0lc'
        tests.append(io_test(filename, r'3\.14', 1, points=10,
                             description='Checking calculation of circumference.  If I input 1, '
                                         'program should printout 3.14....', help_link=help_link))
        tests.append(io_test(filename, r'[^0-9]3$', 1, points=5,
                             description='Checking calculation of circumference rounded down.  If I input 1, '
                                         'program should printout 3', help_link=help_link))
        tests.append(io_test(filename, r'5\.34', 2, points=5,
                             description='Checking calculation of circumference.  If I input 1.7, '
                                         'program should printout 5.34....', help_link=help_link))
        tests.append(io_test(filename, r'[^0-9]5$', 2, points=6,
                             description='Checking calculation of circumference rounded down.  If I input 1.7, '
                                         'program should printout 5', help_link=help_link))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return tests

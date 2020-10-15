def route_docs_python_2021(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    expected = 'https://docs.google.com/presentation/d/12hooQ6UZPh7P2TgoLw-Rj_UJaFrP0q4Qe88lIyLHHL0/' \
               'edit#slide=id.g5304dafeb6_0_0'
    to_float = 'https://docs.google.com/presentation/d/1YhZ7u37vRQHPMnx_XJgV_BDvBocQL9Y5VLWOQ2Zeleo/' \
               'edit#slide=id.g8c6e751a19_0_0'
    no_float_string = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
                      'edit#slide=id.g1ccdc42220236e58_89'
    errors = 'https://docs.google.com/presentation/d/1YhZ7u37vRQHPMnx_XJgV_BDvBocQL9Y5VLWOQ2Zeleo/' \
             'edit#slide=id.g8c6e751a19_1_0'
    double_cast = 'https://docs.google.com/presentation/d/1YhZ7u37vRQHPMnx_XJgV_BDvBocQL9Y5VLWOQ2Zeleo/' \
                  'edit#slide=id.g20957deb5ef4f55d_27'
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=14, score_manual=0)
    text = get_text(link)
    tests.append(check_answer('1a', 'expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=1))
    tests.append(check_answer('1b', 'actual', text, {'answers': r'1\.0', 'help_link': to_float}, points=1))
    tests.append(check_answer('2a', 'expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=1))
    tests.append(check_answer('2b', 'actual', text, {'answers': r'error', 'help_link': no_float_string}, points=1))
    tests.append(check_answer('3a', 'expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=1))
    tests.append(check_answer('3b', 'actual', text, {'answers': r'2', 'help_link': no_float_string}, points=1))
    tests.append(check_answer('4a', 'expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=1))
    tests.append(check_answer('4b', 'actual', text, {'answers': r'error', 'help_link': errors}, points=1))
    tests.append(check_answer('5a', 'expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=1))
    tests.append(check_answer('5b', 'actual', text, {'answers': r'1', 'help_link': double_cast}, points=1))
    tests.append(check_answer('6a', 'expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=1))
    tests.append(check_answer('6b', 'actual', text, {'answers': r'1\.0', 'help_link': double_cast}, points=1))
    tests.append(check_answer('7a', 'expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=1))
    tests.append(check_answer('7b', 'actual', text, {'answers': r'1\.0', 'help_link': double_cast}, points=1))
    score_info = sum_score(tests, score_info)
    return tests


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
        return [score_info, tests, score_info]
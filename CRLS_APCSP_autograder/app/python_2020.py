# noinspection SpellCheckingInspection
def route_docs_python_2021(link):
    from app.docs_labs.docs import get_text, check_answer
    from app.routes import initialize_scoring, sum_score
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
    return [user, tests, score_info]


def feedback_2020(filename):

    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test, io_test_find_all
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions, find_string
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test

    tests = list()
    filename = './' + filename
    test_filename = filename_test(filename, '2.020')
    tests.append(test_filename)

    if not test_filename['pass']:
        return tests
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there is 1 input questions
        test_find_question = find_questions(filename_data, 1, 5)
        test_find_question['name'] += " Checking for at least 1 question. <br> " + \
                                      " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_question)
        if not test_find_question['pass']:
            return tests
        else:
            # Test for casting of any sort
            test_find_casting = find_string(filename_data, r'( int\( | float\( )', 1, points=5)
            test_find_casting['name'] += 'Checking that there is some casting of any sort to either integer or float.'
            tests.append(test_find_casting)

            # Test for casting of initial value to float.  Will crash with unknown errors later if casted to int.
            test_find_casting_2 = find_string(filename_data, r'float\( ', 1)
            test_find_casting_2['name'] += 'Test your program by manually running it and typing in 55.5 for your ' \
                                           'number. <br> If you  get an error<br>' \
                                           'ValueError: invalid literal for int() with base 10:<br>' \
                                           'This error means you are trying to convert a string that looks like' \
                                           ' a float into an integer.  ' \
                                           '<br> If you really want an integer you have to cast the string' \
                                           ' to a float first. <br> Or else if you are OK with float, cast to float ' \
                                           'instead of integer.<br> '
            tests.append(test_find_casting_2)
            if not test_find_casting_2['pass']:
                return tests
            else:
                # Check that input1 is good (input / 2) 99 / 2 = 49.5
                test_io_1 = io_test(filename, '49.5', 1, points=10)
                test_io_1['name'] += "Checks that the number divides by 2 and prints out.  Input 99, " \
                                     "expected 49.5 and 49 in output. <br>"
                tests.append(test_io_1)

                # Check input2 is good (int(input / 2))
                test_io_2 = io_test(filename, '49$', 1, points=10)
                test_io_2['name'] += "Checks that the number divides by 2 and prints out the INTEGER only answer. " \
                                     " Input 99, expected 49 in output. <br>"
                tests.append(test_io_2)

                # Check input2 is good (int(input / 2))
                test_io_3 = io_test_find_all(filename, ['49.75', '49$'], 2, points=6)
                test_io_3['name'] += "Checks that the program works for non-whole inputs. " \
                                     " Input 99.5, expected 49.75 and 49 in output. <br>"
                tests.append(test_io_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                return tests
            


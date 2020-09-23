def route_python_1_060(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions, find_string
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test_find_all, io_test
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=69, score_manual=11)
    test_filename = filename_test(filename, '1.060')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        filename_data = read_file_contents(filename)
        tests.append(find_questions(filename_data, 5, 5))
        help_link = 'https://docs.google.com/presentation/d/1a2a4z0Hli9uj5utJkP_Le0MzhS4NCDUEgJ6A4dbffKs/' \
                    'edit#slide=id.g8c389cadc7_0_0'
        tests.append(find_string(filename_data,
                                 r'(verb|noun|name|adjective|adverb|preposition|place) _* [0-9]* \s* = \s* input\(',
                                 5, points=5, description='Testing that variables are named after parts of speech'
                                                          ' (i.e. noun1, verb2, adjective3).  Convention is lowercase',
                                 help_link=help_link))
        help_link = 'https://docs.google.com/presentation/d/1a2a4z0Hli9uj5utJkP_Le0MzhS4NCDUEgJ6A4dbffKs/' \
                    'edit#slide=id.g8c389cadc7_0_7'
        tests.append(find_string(filename_data, r'print \s* \(', 1, points=5,
                                 description='Testing for at least one print statement', help_link=help_link))
        tests.append(find_string(filename_data, r'print \s \(', 3, points=5, minmax='max',
                                 description='Testing for maximum of 3 print statements', help_link=help_link))

        # answer 5 questions, they should all show up in printout
        output_link = 'https://docs.google.com/presentation/d/1a2a4z0Hli9uj5utJkP_Le0MzhS4NCDUEgJ6A4dbffKs/' \
                      'edit#slide=id.g8c389cadc7_5_0'
        tests.append(io_test_find_all(filename, [r'fake1', r'fake2', r'fake3', r'fake4', r'fake5'], 1,
                                      points=15, description="Ran the code and answered fake1, fake2, "
                                                             "fake3, fake4, and fake5.  All of these answers "
                                                             "should show up in the printout", help_link=output_link))

        help_link = 'https://docs.google.com/presentation/d/1a2a4z0Hli9uj5utJkP_Le0MzhS4NCDUEgJ6A4dbffKs/' \
                    'edit#slide=id.g8c389caccd_3_0'
        tests.append(io_test(filename, r'(\? | ! | \.) ', 1, points=5, occurrences=3,
                             description='Testing for at least 3 punctuations in printout (. ? or !)',
                             help_link=help_link))
        tests.append(io_test_find_all(filename, [r'(\^ | \s+ ) fake2 (\s+ | \? | \. | , | ! | \n)',
                                                 r'(\^ | \s+ ) fake3 (\s+ | \? | \. | , | ! | \n)',
                                                 r'(\^ | \s+ ) fake4 (\s+ | \? | \. | , | ! | \n)',
                                                 r'(\^ | \s+ ) fake5 (\s+ | \? | \. | , | ! | \n)'],
                                      1, points=10, description='Testing for spacing and punctuation.  Ran the code'
                                                                'and answered fake1, fake2, fake3, fake4, fake5.'
                                                                'Each of these should have spaces or punctuations '
                                                                'after them, and spaces before them in the printout',
                                      help_link=output_link))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return tests
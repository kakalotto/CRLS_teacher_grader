def route_python_3_020(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, function_called, find_list
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, extract_single_function, run_unit_test, \
        create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.python_3_020 import check_random
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=69, score_manual=11)
    test_filename = filename_test(filename, '3.020')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        tests.append(find_function(filename, 'birthday_song', 1, points=4))
        tests.append(function_called(filename, 'birthday_song', 1, points=4))

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)
        help_link = 'https://docs.google.com/presentation/d/1WJmH2p5iqk1j53E5PZ5KHDCvt18dqxqQOd-SQ5nPomY/' \
                    'edit#slide=id.g8cb34fff74_0_0'
        tests.append(run_unit_test('3.020', 1, 4, description='happy_birthday function should print "happy birthday"',
                                   help_link=help_link))
        tests.append(run_unit_test('3.020', 2, 5, description='happy birthday function should print out the input '
                                                              'parameter (i.e. if you call function with argument '
                                                              '"Abel", it prints out "Abel"',
                                   help_link=help_link))
        tests.append(run_unit_test('3.020', 3, 8,
                                   description='happy_birthday function should print out "happy birthday to you" '
                                               'twice and "happy birthday dear (argument) once',
                                   help_link=help_link
                                   ))
        test_find_function_2 = find_function(filename, 'pick_card', 0, points=4)
        tests.append(test_find_function_2)

        cards_function = extract_single_function(filename, 'pick_card')
        card_help = 'https://docs.google.com/presentation/d/1WJmH2p5iqk1j53E5PZ5KHDCvt18dqxqQOd-SQ5nPomY/' \
                    'edit#slide=id.g8c389caccd_3_0'
        tests.append(find_list(cards_function, num_items=4, list_name='cards', points=2,
                               description='Looking for list named exactly cards with 13 items.<br>'
                                           'See help link if it still fails.',
                               help_link=card_help))
        tests.append(find_list(cards_function, num_items=4, list_name='suits', points=2,
                               description='Looking for list named exactly suits with 4 items.<br>'
                                           'See help link if it still fails.',
                               help_link=card_help))

        help_one_card = 'https://docs.google.com/presentation/d/1WJmH2p5iqk1j53E5PZ5KHDCvt18dqxqQOd-SQ5nPomY/' \
                        'edit#slide=id.g8cb34fff74_2_0'
        tests.append(run_unit_test('3.020', 4, 5,
                                   description='Function picks exactly one card', help_link=help_one_card))
        tests.append(function_called(filename, 'pick_card', 1, points=4))
        tests.append(check_random(filename, 4))
        help_link = 'https://docs.google.com/document/d/1e9AjniHMvdG9gAyc8m0GPhyPoMPdHLMJ8IjvlveY2zI/' \
                    'edit#bookmark=id.ef0zr7na59o9'
        tests.append(io_test(filename, r'\s of \s', 2, occurrences=10, points=4,
                             description='Running entire code, should draw 10 cards.  Looking for printout'
                                         ' like this: (card) of (suit) (ten times)" ',
                             help_link=help_link))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]

def feedback_3020(filename):

    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, function_called, find_list
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, extract_single_function, run_unit_test, \
        create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.python_3_020 import ten_runs, check_random

    tests = list()
    test_filename = filename_test(filename, '3.020')
    if not test_filename['pass']:
        return tests
    else:
        test_find_function_1 = find_function(filename, 'birthday_song', 1, points=4)
        tests.append(test_find_function_1)

        # Only continue if you have a birthday_song_function
        if not test_find_function_1['pass']:
            return tests
        else:
            # Check that function is called once
            test_birthday_song_run = function_called(filename, 'birthday_song', 1, points=4)
            tests.append(test_birthday_song_run)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('3.020', 1, 4)
            test_function_1['name'] += " (prints out 'birthday' somewhere) "
            tests.append(test_function_1)

            # function test 2
            test_function_2 = run_unit_test('3.020', 2, 5)
            test_function_2['name'] += " (prints out input parameter somewhere) "
            tests.append(test_function_2)
           # function test 3
            test_function_3 = run_unit_test('3.020', 3, 8)
            test_function_3['name'] += " (output looks good) "
            tests.append(test_function_3)

            test_find_function_2 = find_function(filename, 'pick_card', 0, points=4)
            tests.append(test_find_function_2)

            # Only continue if you have a birthday_song_function
            if not test_find_function_2['pass']:
                return tests
            else:

                cards_function = extract_single_function(filename, 'pick_card')

                test_find_cards = find_list(cards_function, num_items=4, list_name='cards', points=2)
                tests.append(test_find_cards)

                test_find_suits = find_list(cards_function, num_items=4, list_name='suits', points=2)
                tests.append(test_find_suits)

                # function test 4
                test_function_4 = run_unit_test('3.020', 4, 5)
                test_function_4['name'] += " (function picks 1 card) "
                tests.append(test_function_4)

                # Check that function is called once
                test_pick_card_run = function_called(filename, 'pick_card', 1, points=4)
                tests.append(test_pick_card_run)

                # Check that random is random
                test_random = check_random(filename)
                tests.append(test_random)

                # check that pick_card prints out 10 cards (looks for 'of' 10x)
                test_run_ten_cards = ten_runs(filename)
                tests.append(test_run_ten_cards)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)
                return tests


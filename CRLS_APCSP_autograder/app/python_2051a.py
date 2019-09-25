def feedback_2051a(filename):

    from CRLS_APCSP_autograder.app.python_labs.find_items import find_string, find_questions, find_all_strings
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.python_2_05x import python_2_051a
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test

    tests = list()

    test_filename = filename_test(filename, '2.051a')
    tests.append(test_filename)
    if not test_filename['pass']:
        return tests
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 4 items
        test_prizes = find_string(filename_data, r'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]', 1, points=5)
        test_prizes['name'] += "Testing that there is a variable prizes.  Prizes is a list with exactly 4 items.<br>" \
                               "Prizes is a named exactly 'prizes' and not something else."
        tests.append(test_prizes)
        if not test_prizes['pass']:
            test_prizes['fail_message'] += r"Looking for variable prizes that is a list with 4 items.  We name lists " \
                                           r"plural to help keep track of what is what.<br>  " \
                                           r"Looked for 'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]' " \
                                           r"in this string: <br>" + filename_data
            return tests
        else:

            # Check for question
            test_find_input = find_questions(filename_data, 1, 5)
            tests.append(test_find_input)

            # Test input gives output
            test_runs = python_2_051a(filename, filename_data)
            tests.append(test_runs)

            # Test efficiency
            test_efficiency = find_all_strings(filename_data, [r'prizes\[0\]', r'prizes\[1\]',
                                                               r'prizes\[2\]', r'prizes\[3\]'], 5)
            test_efficiency['name'] += "Testing efficiency.  Do NOT want to have a big if/elif/else.<br>" \
                                       "If you have a variable x which is a number of item in list," \
                                       " list[x-1] will get you the correct item.<br>" \
                                       "<br>  This technique saves a lot of lines of code over a big if/elif  " \
                                       "and scales to big numbers.  " \
                                       "<br>That is, a list with 10,000 items will need " \
                                       "just one line to print out the list item whereas with a big if/else, " \
                                       "you will need 20,000 lines of code.<br>" \
                                       " If this does not make sense, ask a neighbor or the teacher."
            if test_efficiency['pass']:
                test_efficiency['pass'] = False
                test_efficiency['points'] = 0
                test_efficiency['fail_message'] += "You want to use a variable for the list index of prizes."
            else:
                test_efficiency['pass'] = True
                test_efficiency['pass_message'] += "(actually, did NOT find prizes[0], prizes[1] prizes[2] prizes[3]"
                test_efficiency['points'] = 5
            tests.append(test_efficiency)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)
            return tests





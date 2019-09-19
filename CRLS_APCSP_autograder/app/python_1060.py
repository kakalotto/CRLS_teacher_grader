def feedback_1060(filename):

    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions, find_string
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test_find_all, io_test
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test

    tests = list()
    test_filename = filename_test(filename, '1.060')
    tests.append(test_filename)

    if not test_filename['pass']:
        return tests
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)
        # Check that there are 5 input questions
        test_find_five_questions = find_questions(filename_data, 5, 5)
        test_find_five_questions['name'] += " Checking for at least 5 questions. <br> " + \
                                            " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_five_questions)
        if not test_find_five_questions['pass']:
            return tests
        else:

            # Check that inputs are named after part of speech
            test_find_parts_of_speech = find_string(filename_data,
                                                    r'(verb|noun|name|adjective|adverb|preposition|place) _* [0-9]* \s* = '
                                                    r'\s* input\(',
                                                    5, points=5)
            test_find_parts_of_speech['name'] += "Testing that variables are named after parts of speech. <br>"\
                                                 "If this test fails, rename variables to parts of speech " \
                                                 "per instructions.<br>" \
                                                 "Also note, Python variable name convention is LOWERCASE, so this " \
                                                 "test will flunk variables like 'Noun1' or 'Verb2'<br>"
            tests.append(test_find_parts_of_speech)

            # Check for at least 1 print statement
            test_find_print = find_string(filename_data, r'print \s* \(', 1, points=5)
            test_find_print['name'] += "Testing for at least one print statement. <br>"
            tests.append(test_find_print)

            # Check for less than 3 print statements
            test_find_three_print = find_string(filename_data, r'print \s \(', 3, points=5, minmax='max')
            test_find_three_print['name'] += "Testing for at maximum of three print statements. <br>"
            tests.append(test_find_three_print)

            # answer 5 questions, they should all show up in printout
            test_io_five_inputs = io_test_find_all(filename, [r'a1', r'a2', r'a3', r'b1', r'b2'], 1, points=15)
            test_io_five_inputs['name'] += 'Testing for first 5 things you answered questions to show in output.<br>' \
                                           'For example, if you typed in noun1, verb1, noun2, verb2, and adjective' \
                                           '<br> noun1, verb1, noun2, verb2, and adjective should all appear ' \
                                           'in the printout. <br>'
            tests.append(test_io_five_inputs)

            # Check for 3 punctuations
            test_puncts = io_test(filename, r'(\? | ! | \.) ', 1, points=5, occurrences=3)
            test_puncts['name'] += "Testing for at least 3 punctuations.<br>"
            tests.append(test_puncts)

            # Test second 4 inputs for correct spacing
            test_io_spacing = io_test_find_all(filename, [r'(\^ | \s+ ) a2 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) a3 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) b1 (\s+ | \? | \. | , | !)',
                                                          r'(\^ | \s+ ) b2 (\s+ | \? | \. | , | !)'],
                                               1, points=10)
            test_io_spacing['name'] += 'Testing for spacing.  Things you enter should have spaces or punctuations<br>' \
                                       'after them and spaces before them in the printout. <br>'
            tests.append(test_io_spacing)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)


            return tests

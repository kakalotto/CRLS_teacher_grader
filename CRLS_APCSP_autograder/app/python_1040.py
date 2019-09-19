def feedback_1040(filename):

    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test
    from CRLS_APCSP_autograder.app.python_labs.python_1_040 import statement_variables
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps

    tests = list()

    # Test file name
    filename = './' + filename
    test_filename = filename_test(filename, '1.040')
    tests.append(test_filename)

    if test_filename['pass'] is False:
        return tests
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there are 3 input questions
        test_find_three_questions = find_questions(filename_data, 3, 5)
        test_find_three_questions['name'] += " Checking that Genie asks at least 3 questions. <br> " + \
                                             " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_three_questions)
        if not test_find_three_questions['pass']:
            return tests
        else:
            # io test 1- a b c
            test_io_1 = io_test(filename, r'.+ a1 .+ a2 .+ a3 ', 1, points=5)
            test_io_1['name'] += "Check things are in correct order - wishing for a, b, c " +\
                                 " should print 'your wishes are a, b, and c.' <br>" \
                                 "You must have at least 1 character of some sort between your wishes.<br>"
            tests.append(test_io_1)

            # Check that there are 6 total questions (3 part 1, 3 part 2)
            test_find_six_questions = find_questions(filename_data, 6, 5)
            test_find_six_questions['name'] += " Checking that Genie asks at least 6 questions (you need 3 for" \
                                               " part 1 and 3 for part 2) (5 points). <br>"
            tests.append(test_find_six_questions)

            # Check that repeated questions put into variables.
            test_input_variable = statement_variables(filename_data, 5)
            tests.append(test_input_variable)

            # io test 2 - a b c, b2, b3, b1
            test_io_2 = io_test(filename, r'.+ a1 .+ a2 .+ a3 .+ b2 .+ b3 .+ b1 ', 1, points=5)
            test_io_2['name'] += "Check things are in correct order - wishing for a, b, c, d, e, f " + \
                                 " should print 'your wishes are a, b, and c' <br>" +\
                                 " and 'your wishes are e, f, and d' <br>" \
                                 "You must have at least 1 character of some sort between your wishes.<br>"
            tests.append(test_io_2)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            return tests

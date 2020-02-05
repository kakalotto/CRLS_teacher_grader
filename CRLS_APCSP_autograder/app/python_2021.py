def feedback_2021(filename):

    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test, io_test_find_all
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions, find_string
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test

    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '2.021')
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
            test_io_1 = io_test(filename, r'3\.14', 1, points=5)
            test_io_1['name'] += "case 1: Checks that circumference is calculated.  Input 1, " \
                                 "expected 3.14 in output. <br>"
            tests.append(test_io_1)
            test_io_2 = io_test(filename, r'[^0-9]3$', 1, points=5)
            test_io_2['name'] += "case 1: Checks that circumference is calculated, rounded.  Input 1, " \
                                 "expected 3 in output. <br>"
            tests.append(test_io_2)
            test_io_3 = io_test(filename, r'5\.34', 2, points=5)
            test_io_3['name'] += "case2: Checks that circumference is calculated.  Input 1.7, " \
                                 "expected 5.34 in output (be sure pi has enough digits) <br>"
            tests.append(test_io_3)
            test_io_4 = io_test(filename, r'[^0-9]5$', 2, points=5)
            test_io_4['name'] += "case2: Checks that circumference is calculated, rounded.  Input 1.7, " \
                                 "expected 5 in output. <br>"
            tests.append(test_io_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            return tests
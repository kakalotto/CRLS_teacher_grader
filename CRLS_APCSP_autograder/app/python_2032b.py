def feedback_2032b(filename):

    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_if
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.python_2_03x import python_2_032b
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps

    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '2.032b')
    tests.append(test_filename)
    if not test_filename['pass']:
        return tests
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check for ifs
        test_ifs = find_if(filename_data, 0, 5, minmax='max')
        test_ifs['name'] += 'Testing for ifs.  There should be zero ifs in the code. <br>' \
                            'For example, print(1==1) NOT if (1 == 1): print("True") <br>' \
                            'If you think this should pass, control-F and search for "if" in your code'
        tests.append(test_ifs)

        # test all 8 cases
        debug_statement = 'Program asks for if you are Yuka Kinoshita, your stomach size, and money in that order <br>'\
                          'If you are failing 2 tests, read example 8 from the presentation.'
        test_runs = python_2_032b(filename, filename_data, debug_statement=debug_statement)
        tests.append(test_runs)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        return tests
    

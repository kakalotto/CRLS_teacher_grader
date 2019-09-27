def feedback_3011(filename):

    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions, find_list, find_random, find_print
    from CRLS_APCSP_autograder.app.python_labs.python_3_011 import python_3_011_2, python_3_011_1
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test

    tests = list()

    test_filename = filename_test(filename, '3.011')
    tests.append(test_filename)
    if not test_filename['pass']:
        return tests
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 6 items
        test_houses = find_list(filename_data, num_items=6, list_name='houses', points=10)
        tests.append(test_houses)
        if not test_houses['pass']:
            return tests
        else:
            # Asks a question, but that is ignore
            test_question = find_questions(filename_data, 1, 5)
            if not test_question['pass']:
                test_question['fail_message'] += "You need to ask the user a question to try to influence the hat. <br>"
            tests.append(test_question)

            # test for importing random
            test_random = find_random(filename_data, 5)
            tests.append(test_random)
            if not test_random['pass']:
                return tests
            else:
                # test for importing randint
                test_randint = find_random(filename_data, 5, randint=True)
                tests.append(test_randint)

                # Check for at least 1 print statement
                test_find_print = find_print(filename_data, 1, 5)
                tests.append(test_find_print)
                # Test efficiency
                test_efficiency = python_3_011_1(filename_data, 5)
                tests.append(test_efficiency)

                test_runs = python_3_011_2(filename, filename_data, 10)
                tests.append(test_runs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)
            return tests
        

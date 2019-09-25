def feedback_2051b(filename):

    from CRLS_APCSP_autograder.app.python_labs.find_items import find_if, find_questions, find_list, find_elif, find_else
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.python_2_05x import python_2_051b_1, python_2_051b_2
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test

    tests = list()
    test_filename = filename_test(filename, '2.051b')
    tests.append(test_filename)
    if not test_filename['pass'] is True:
        return tests
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 4 items
        test_lcs = find_list(filename_data, num_items=4, list_name='learning_communities', points=3)
        tests.append(test_lcs)
        if not test_lcs['pass']:
            return tests
        else:
            # Read in the python file to filename_data
            filename_data = read_file_contents(filename)

            test_scores = find_list(filename_data, num_items=4, list_name='scores', points=3)
            test_scores['name'] += "All items should be initially all zero (which we do not check right now).<br>"
            tests.append(test_scores)
            if not test_scores['pass']:
                return tests
            else:
                test_question = find_questions(filename_data, 1, 1)
                if not test_question['pass']:
                    test_question['fail_message'] += "You need to ask the user a question about which " \
                                                     "LC to vote for. <br>"
                tests.append(test_question)

                # test if, check for at least 1 if statement
                test_if = find_if(filename_data, 1, 1)
                tests.append(test_if)

                # test else check for at least 1 else statement
                test_else = find_else(filename_data, 1, 4)
                tests.append(test_else)

                # test elif check for at least 3
                test_elif = find_elif(filename_data, 3, 1)
                tests.append(test_elif)
                # Try C C R L S, should get 2, 1, 1, 1
                test_1_io = python_2_051b_1(filename, 5)
                tests.append(test_1_io)

                # Try C R L S blah blah blah, should get 1, 1, 1, 1
                test_2_io = python_2_051b_2(filename, 5)
                tests.append(test_2_io)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

                return tests

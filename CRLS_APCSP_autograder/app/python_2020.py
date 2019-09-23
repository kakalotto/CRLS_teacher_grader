def docs_feedback_python_2020(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    text = get_text(link)
     
    tests = list()
    test1a = exact_answer('1a expected', [r'1a\. .+? tabledata \s* [0-9a-zA-Z] .+? 1b\.'], text, points=1)
    test1b = exact_answer('1b expected', [r'1b\. .+? tabledata \s* 1\.0 \s* tabledata .+? 2a\.'], text, points=1)
    test2a = exact_answer('2a expected', [r'2a\. .+? tabledata \s* [0-9a-zA-Z] .+? 2b\.'], text, points=1)
    test2b = exact_answer('2b expected', [r'2b\. .+? tabledata \s* error \s* tabledata .+? 3a\.'], text, points=1)
    test3a = exact_answer('3a expected', [r'3a\. .+? tabledata \s* [0-9a-zA-Z] .+? 3b\.'], text, points=1)
    test3b = exact_answer('3b expected', [r'2b\. .+? tabledata \s* 2 \s* tabledata .+? 4a\.'], text, points=1)
    test4a = exact_answer('4a expected', [r'4a\. .+? tabledata \s* [0-9a-zA-Z] .+? 4b\.'], text, points=1)
    test4b = exact_answer('4b expected', [r'4b\. .+? tabledata \s* error \s* tabledata .+? 5a\.'], text, points=1)
    test5a = exact_answer('5a expected', [r'5a\. .+? tabledata \s* [0-9a-zA-Z] .+? 5b\.'], text, points=1)
    test5b = exact_answer('5b expected', [r'5b\. .+? tabledata \s* 1 \s* tabledata .+? 6a\.'], text, points=1)
    test6a = exact_answer('6a expected', [r'6a\. .+? tabledata \s* [0-9a-zA-Z] .+? 6b\.'], text, points=1)
    test6b = exact_answer('6b expected', [r'6b\. .+? tabledata \s* 1\.0 \s* tabledata .+? 7a\.'], text, points=1)
    test7a = exact_answer('7a expected', [r'7a\. .+? tabledata \s* [0-9a-zA-Z] .+? 7b\.'], text, points=1)
    test7b = exact_answer('7b expected', [r'7b\. .+? tabledata \s* 1\.0 \s* .+? $'], text, points=1)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test5b, test6a, test6b,
                  test7a, test7b,])
    return tests 

def feedback_2020(filename):

    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test, io_test_find_all
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_questions, find_string
    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test

    tests = list()
    filename = './' + filename
    test_filename = filename_test(filename, '2.020')
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

            # Test for casting of initial value to float.  Will crash with unknown errors later if casted to int.
            test_find_casting_2 = find_string(filename_data, r'float\( ', 1)
            test_find_casting_2['name'] += 'Test your program by manually running it and typing in 55.5 for your ' \
                                           'number. <br> If you  get an error<br>' \
                                           'ValueError: invalid literal for int() with base 10:<br>' \
                                           'This error means you are trying to convert a string that looks like' \
                                           ' a float into an integer.  ' \
                                           '<br> If you really want an integer you have to cast the string' \
                                           ' to a float first. <br> Or else if you are OK with float, cast to float ' \
                                           'instead of integer.<br> '
            tests.append(test_find_casting_2)
            if not test_find_casting_2['pass']:
                return tests
            else:
                # Check that input1 is good (input / 2) 99 / 2 = 49.5
                test_io_1 = io_test(filename, '49.5', 1, points=10)
                test_io_1['name'] += "Checks that the number divides by 2 and prints out.  Input 99, " \
                                     "expected 49.5 and 49 in output. <br>"
                tests.append(test_io_1)

                # Check input2 is good (int(input / 2))
                test_io_2 = io_test(filename, '49$', 1, points=10)
                test_io_2['name'] += "Checks that the number divides by 2 and prints out the INTEGER only answer. " \
                                     " Input 99, expected 49 in output. <br>"
                tests.append(test_io_2)

                # Check input2 is good (int(input / 2))
                test_io_3 = io_test_find_all(filename, ['49.75', '49$'], 2, points=6)
                test_io_3['name'] += "Checks that the program works for non-whole inputs. " \
                                     " Input 99.5, expected 49.75 and 49 in output. <br>"
                tests.append(test_io_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                return tests
            


def efficiency(p_filename_data, p_points):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_string

    p_test = {"name": "Test that code is efficient (" + str(p_points) + " points) <br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>Code prints answer with efficient code",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>Code does not print answer with efficient code"
                              "<br>",
              "points": 0,
              }
    print_prizes = find_string(p_filename_data, r'prizes\[[^0123]', 1)   # Looks for prizes[  but not prizes[0] etc...
    if_if = find_string(p_filename_data, r'if .*? if .*?', 1)  # finds if if or if elif
    if print_prizes['pass'] and if_if['pass'] is False:
        p_test['pass'] = True
        p_test['points'] += p_points
        return p_test
    if print_prizes['pass'] is False:
        presentation = 'https://docs.google.com/presentation/d/115yqVHY0APEvQFTQ0fGNbw81pX4gv4kflTUfco1E_Q8/' \
                       'edit#slide=id.g41529343e1_0_35'
        p_test['fail_message'] += "<br><h5 style=\"color:purple;\"> " \
                                  'Code does not use a variable to represent list item<br>' \
                                  "<br>See this link for help " \
                                  "answering this question: " \
                                  ' <a href="' + presentation + '" target="_blank">link</a><br>'
    if if_if['pass']:
        presentation = 'https://docs.google.com/presentation/d/115yqVHY0APEvQFTQ0fGNbw81pX4gv4kflTUfco1E_Q8/' \
                       'edit#slide=id.g8c7a63841e_2_0'
        p_test['fail_message'] += "<br><h5 style=\"color:purple;\"> " \
                                  'Code has an if/(el)if/(el)if and is inefficient.<br>' \
                                  "<br>See this link for help answering this question: " \
                                  ' <a href="' + presentation + '" target="_blank">link</a>'
    return p_test


def python_2_051a(p_filename, p_filename_data):
    """
    Does the tests for 2.051a
    :param p_filename: filename (string)
    :param p_filename_data: contents of the filename (string)
    :return: A dictionary of test info
    """
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_list_items, find_string
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test

    p_pass_tests = {"name": "2 test cases for 2.051a work (8 points) <br>",
                    "pass": True,
                    "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  2 test cases work",
                    "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  Check your 2 test cases.<br>"
                                    "If you run the program, and I type '1', it should print out 0th element of prizes "
                                    "list."
                                    " <br> "
                                    "Same for prize2, prize3, and prize4. <br>"
                                    "User should input '1', '2', '3', or '4', not 'door1', 'prize1' or anything like "
                                    "that",
                    "points": 0,
                    }

    test = find_string(p_filename_data, r'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]', 1, points=5,
                       description='Testing for list prizes.  prizes is a list with exactly 4 items.'
                                   'Prizes needs to be named exactly "prizes"',
                       help_link='https://docs.google.com/presentation/d/115yqVHY0APEvQFTQ0fGNbw81pX4gv4kfl'
                                 'TUfco1E_Q8/edit#slide=id.g3fda053d45_1_2')
    if test['pass'] is False:
        p_pass_tests['pass'] = False
        p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\">You did not have a list name prizes with ' \
                                        '4 items. ' \
                                        'Test aborted early.<br>' \
                                        'Set a list named prizes with 4 items and try again please.<br> </h5> '
        return p_pass_tests

    prizes = find_list_items(p_filename_data, 'prizes')
    prizes[1] = prizes[1].replace(' ', r'\s')
    prizes[2] = prizes[2].replace(' ', r'\s')

    test_2 = io_test(p_filename, prizes[1], 2)
    test_3 = io_test(p_filename, prizes[2], 3)

    test_prizes = find_string(p_filename_data, r'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]', 1, points=5,
                              description='Testing for list prizes.  prizes is a list with exactly 4 items.'
                                          'Prizes needs to be named exactly "prizes"',
                              help_link='https://docs.google.com/presentation/d/115yqVHY0APEvQFTQ0fGNbw81pX4gv4kfl'
                                        'TUfco1E_Q8/edit#slide=id.g3fda053d45_1_2')
    if test_prizes['pass'] is False:
        p_pass_tests['pass'] = False
        p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\">You did not a list prizes with 4 items. ' \
                                        'Test aborted early.<br>' \
                                        'Create list prizes with 4 itemsand try again please.<br> </h5> '
        return p_pass_tests
    debug_string = ''

    if test_2['pass']:
        p_pass_tests['points'] += 4
        debug_string += ' 2 prize passed '
    else:
        p_pass_tests['fail_message'] += test_2['fail_message'] + "<br> This was result after entering " \
                                                                 "'2' at keyboard.<br>"
    if test_3['pass']:
        p_pass_tests['points'] += 4
        debug_string += ' 3 prize passed'
    else:
        p_pass_tests['fail_message'] += test_3['fail_message'] + "<br> This was result after entering " \
                                                                 "'3' at keyboard.<br>"
    if p_pass_tests['points'] != 8:
        p_pass_tests['pass'] = False
        p_pass_tests['debug'] = debug_string
        help_link = 'https://docs.google.com/presentation/d/1Uh_zlH-FUgYJaEW1fA3YOxQNfWver55g_EncWLVJ3-0/' \
                    'edit#slide=id.g8dcab25422_1_0'
        p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\">' \
                                        '<br>See this link for help answering this question: ' \
                                        ' <a href="' + help_link + '" target="_blank">link</a></h5>'
    return p_pass_tests


if __name__ == "__main__":
    from app.python_labs.read_file_contents import read_file_contents

    print("yes")
    #    filename = '/home/ewu/abc/2.040/2019_mayasater_2.040.py'
    filename = '/Users/dimmyfinster/PycharmProjects/untitled5/2019_anais_2.050a.py'
    filename_data = read_file_contents(filename)
    bbb = python_2_051a(filename, filename_data)
    print(bbb)

def python_2_040(p_filename, p_filename_data):

    import re
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test
    match_obj_prize1 = re.search(r'prize1 \s* = \s* (\'|") ([\[\]a-zA-Z0-9!-\.\$\+\s\(\)]+) (\'|")',
                                 p_filename_data, re.X | re.M | re.S)
    match_obj_prize2 = re.search(r'prize2 \s* = \s* (\'|") ([\[\]a-zA-Z0-9!-\.\$\+\s\(\)]+) (\'|")',
                                 p_filename_data, re.X | re.M | re.S)
    match_obj_prize3 = re.search(r'prize3 \s* = \s* (\'|") ([\[\]a-zA-Z0-9!-\.\$\+\s\(\)]+) (\'|")',
                                 p_filename_data, re.X | re.M | re.S)
    match_obj_prize4 = re.search(r'prize4 \s* = \s* (\'|") ([\[\]a-zA-Z0-9!-\.\$\+\s\(\)]+) (\'|")',
                                 p_filename_data, re.X | re.M | re.S)

    prize1 = ' NOT FOUND '
    prize2 = ' NOT FOUND '
    prize3 = ' NOT FOUND '
    prize4 = ' NOT FOUND '
    debug_string = '<br> These are the prizes we found:<br>'
    if match_obj_prize1:
        prize1 = match_obj_prize1.group(2)
        debug_string += prize1 + "<br>"
    if match_obj_prize2:
        prize2 = match_obj_prize2.group(2)
        debug_string += prize2 + "<br>"
    if match_obj_prize3:
        prize3 = match_obj_prize3.group(2)
        debug_string += prize3 + "<br>"
    if match_obj_prize4:
        prize4 = match_obj_prize4.group(2)
        debug_string += prize4 + "<br>"

    # quit = True
    # if not match_obj_prize1:
    #     raise Exception("Did not find a prize after prize1 variable")
    # if not match_obj_prize2:
    #     raise Exception("Did not find a prize after prize2 variable")
    # if not match_obj_prize3:
    #     raise Exception("Did not find a prize after prize3 variable")
    # if not match_obj_prize4:
    #     raise Exception("Did not find a prize after prize4 variable")

    p_pass_tests = {"name": "4 test cases for 2.040 work (12 points) <br>",
                    "pass": True,
                    "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  All 4 test cases work",
                    "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  Check your 4 test cases.<br>"
                                    "If you run the program, and I type '1', it should print out prize1 somehow."
                                    " <br> "
                                    "Same for prize2, prize3, and prize4. <br>"
                                    "User should input '1', '2', '3', or '4', not 'door1', 'prize1' or anything like "
                                    "that",
                    "points": 0,
                    }
    if not match_obj_prize1 or not match_obj_prize2 or not match_obj_prize3 or not match_obj_prize4:
        p_pass_tests['pass'] = False
        p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\">You did not have 4 prizes. ' \
                                        'Test aborted early.<br>' \
                                        'Set 4 prizes and try again please.<br> </h5> '
        if not match_obj_prize1:
            p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\"> ' \
                                            'Did not find a prize after prize1 variable</h5>'
        if not match_obj_prize2:
            p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\"> ' \
                                            'Did not find a prize after prize2 variable</h5>'
        if not match_obj_prize3:
            p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\"> ' \
                                            'Did not find a prize after prize3 variable</h5>'
        if not match_obj_prize4:
            p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\"> ' \
                                            'Did not find a prize after prize4 variable</h5>'

        return p_pass_tests
    prize1 = prize1.replace(' ', r'\s')
    prize2 = prize2.replace(' ', r'\s')
    prize3 = prize3.replace(' ', r'\s')
    prize4 = prize4.replace(' ', r'\s')
    prize1 = prize1.replace(r'$', r'\$')
    prize2 = prize2.replace(r'$', r'\$')
    prize3 = prize3.replace(r'$', r'\$')
    prize4 = prize4.replace(r'$', r'\$')
    prize1 = prize1.replace(r'(', r'\(')
    prize2 = prize2.replace(r'(', r'\(')
    prize3 = prize3.replace(r'(', r'\(')
    prize4 = prize4.replace(r'(', r'\(')
    prize1 = prize1.replace(r')', r'\)')
    prize2 = prize2.replace(r')', r'\)')
    prize3 = prize3.replace(r')', r'\)')
    prize4 = prize4.replace(r')', r'\)')
    prize1 = prize1.replace(r'[', r'\[')
    prize2 = prize2.replace(r'[', r'\[')
    prize3 = prize3.replace(r'[', r'\[')
    prize4 = prize4.replace(r'[', r'\[')
    prize1 = prize1.replace(r']', r'\]')
    prize2 = prize2.replace(r']', r'\]')
    prize3 = prize3.replace(r']', r'\]')
    prize4 = prize4.replace(r']', r'\]')

    print("here are prizes {} {} {} {}".format(prize1, prize2, prize3, prize4))
    test_1 = io_test(p_filename, prize1, 1)
    test_2 = io_test(p_filename, prize2, 2)
    test_3 = io_test(p_filename, prize3, 3)
    test_4 = io_test(p_filename, prize4, 4)

    if test_1['pass']:
        p_pass_tests['points'] += 3
        debug_string += ' <br>1  prize passed '
    if test_2['pass']:
        p_pass_tests['points'] += 3
        debug_string += ' 2 prize passed '
    if test_3['pass']:
        p_pass_tests['points'] += 3
        debug_string += ' 3 prize passed'
    if test_4['pass']:
        p_pass_tests['points'] += 3
        debug_string += ' 4 prize pass'
    if p_pass_tests['points'] != 12:
        p_pass_tests['pass'] = False
        p_pass_tests['debug'] = debug_string
        p_pass_tests['fail_message'] += debug_string

        help_link = 'https://docs.google.com/presentation/d/1Uh_zlH-FUgYJaEW1fA3YOxQNfWver55g_EncWLVJ3-0/' \
                    'edit#slide=id.g8dcab25422_1_0'
        p_pass_tests['fail_message'] += '<h5 style=\"color:purple;\">' \
                                        '<br>See this link for help answering this question: ' \
                                        ' <a href="' + help_link + '" target="_blank">link</a></h5>'
    return p_pass_tests


if __name__ == "__main__":
    from app.python_labs.read_file_contents import read_file_contents
    print("yes")
    filename = '/home/ewu/abc/2.040/2019_mayasater_2.040.py'
    filename_data = read_file_contents(filename)
    bbb = python_2_040(filename, filename_data)
    print(bbb)

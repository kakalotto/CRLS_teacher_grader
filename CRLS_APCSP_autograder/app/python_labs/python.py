def filename_test(p_filename, p_lab):
    """
    Tests the filename is followed convention
    :param p_filename: filename to check (str)
    :param p_lab: the lab number(str)
    :return:
    """
    import re
    from CRLS_APCSP_autograder.app.python_labs import YEAR, LAST_YEAR
    # from CRLS_APCSP_autograder.app.python_labs.name_dictionary import names
    find_year = re.search(YEAR, p_filename)
    find_last_year = re.search(LAST_YEAR, p_filename)
    import sys
    import socket
    if sys.platform == 'darwin':
        heroku = False
    else:
        if len(socket.gethostname()) > 25:
            heroku = True
        else:
            heroku = False
    find_lab = re.search(p_lab, p_filename)
    find_all = re.search(YEAR + r"_ .+ _ " + p_lab + r".py", p_filename, re.X | re.M | re.S)
    find_all_last = re.search(LAST_YEAR + r"_ .+ _ " + p_lab + r".py", p_filename, re.X | re.M | re.S)

    classroom_test = re.search('classroom', p_filename, re.X | re.M | re.S)
    autograder_name = re.search(r'20(19|20)_(.+?)_[0-9]\.[0-9][0-9][0-9]', p_filename, re.X | re.M | re.S)
    found_name = ''
    if autograder_name:
        found_name = autograder_name.group(2)

    found_name_passed = True
    if heroku is False:
        from CRLS_APCSP_autograder.app.python_labs.name_dictionary import names
        if found_name in names.keys():
            found_name_passed = True
        else:
            found_name_passed = False
        print("HEROKU  +" + str(found_name_passed))
    else:
        names = {}
    p_test_filename = {"name": "Testing that file is named correctly",
                       "pass": find_year and find_lab and find_all,
                       "pass_message": "<h5 style=\"color:green;\">Pass!</h5> File name looks correct "
                                       "(i.e. something like 2020_goku_" + p_lab +
                                       ".py)",
                       "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                       "File name of submitted file does not follow required convention. "
                                       " Rename and resubmit.<br>"
                                       "File name should be like this: <br> <br>"
                                       "2020_goku_" + p_lab + ".py <br><br>"
                                       "File must be python file (ends in .py).<br>" 
                                       "A Google doc with Python code copy+pasted in is not accepted <br>"
                                       "Filename must not have capital letters. <br>"
                                       " Other tests not run. They will be run after filename is fixed.<br>",
                       'points': 0,
                       }
    if heroku:
        p_test_filename['pass_message'] += "<h5 style=\"color:purple;\">Note! This version of autograder does not" \
                                           " check that you are using the correct autograder name. <br> " \
                                           "Please be sure" \
                                           "to re-check file at school.<br>"

    if classroom_test:
        p_test_filename['fail_message'] += '<br>Link is Google classroom link.  Open up the doc and get that link.<br>'
    if found_name_passed is False:
        p_test_filename['fail_message'] += '<br><h5 style=\"color:purple;\"> Your autograder name was not ' \
                                           'found in the ' \
                                           'list of autograder names.<br></h5>' \
                                           'The found autograder name was this: ' + found_name + \
            "<br>The list of names is this:<br>" + str(names.keys())

    if p_filename.islower() is False:
        p_test_filename['fail_message'] += '<br>Filename had an upper case letter.  Rename and resubmit.<br>'
    if (find_year or find_last_year) and find_lab and (find_all or find_all_last) and p_filename.islower() and not \
            classroom_test and found_name_passed:
        p_test_filename['pass'] = True
    else:
        p_test_filename['pass'] = False
    return p_test_filename


def helps(p_filename, p_points):
    """
    Function figures out how many points to give for helps.
    :param p_filename: name of python file with code to grade
    :param p_points: points to give if there is a help
    :return: a dictionary containing the test info
    """
    import delegator

    # Check for help comment
    cmd = 'grep "#" ' + p_filename + ' | grep -i help | grep -vi wu|grep -vi martinez |grep -vi atwood|  wc -l  '
    c = delegator.run(cmd)
    help_comments = int(c.out)
    p_test_help = {"name": "Testing that you got a help and documented it as a comment (" + str(p_points) + " points)",
                   "pass": True,
                   "pass_message": "<h5 style=\"color:green;\">Pass (for now).<h5>"
                                   "  You have a comment with 'help' in it.  <br>"
                                   "Be sure your comment is meaningful, otherwise this can be overturned "
                                   "on review.",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5>"
                                   "  Did not find a comment in your code with the word 'help' describing"
                                   " how somebody helped you with your code.  <br>"
                                   "This must be a MEANINGFUL help.<br>"
                                   "This translates to " + str(p_points) +
                                   " points deduction.<br>"
                                   "Your help can NOT be from a teacher <br><br> See this link for help answering this"
                                   ' question:  <a href="https://docs.google.com/presentation/d/1d1DS-OWpD5QXUIStPkAQr'
                                   'MtNk1tH7nAsWOYSHbOllqo/edit#slide=id.g8c389caccd_3_0" ' 
                                   'target="_blank">link</a>',
                   'points': 0
                   }
    if help_comments == 0:
        p_test_help['pass'] = False
    else:
        p_test_help['points'] += p_points
    return p_test_help


def pep8(p_filename, p_max_points):
    """
    This module fines the number of PEP8 errors
    :param p_filename: Name of the python file
    :param p_max_points: maximum number of points you can get for 0 pep8 errors or warnings
    :return: dictionary with test info
    """
    import delegator
    import sys
    import socket

    ignore_codes = 'E226,E241,W504,W293,E126,W503'
    if sys.platform == 'darwin':
        pycodestyle_file = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/venv1/bin/pycodestyle'
        # This is Eric's home computer
    else:
        if len(socket.gethostname()) > 25:
            pycodestyle_file = '/app/.heroku/python/bin/pycodestyle'
        else:
            pycodestyle_file = '/home/ewu/CRLS_APCSP_autograder/venv1/bin/pycodestyle'
    try:
        fh = open(pycodestyle_file, 'r')
    except FileNotFoundError:
        raise Exception("Could not find pycodestyle file " + pycodestyle_file)
    fh.close()

    cmd = pycodestyle_file + ' --ignore=' + ignore_codes + ' --max-line-length=120 ' + p_filename + ' | wc -l '
    c = delegator.run(cmd)
    if c.err:
        raise Exception(c.err)
    side_errors = int(c.out)
    error_msg = 'NONE'
    if side_errors != 0:
        cmd = pycodestyle_file + ' --ignore=' + ignore_codes + ' --max-line-length=120 ' + p_filename
        print(cmd)
        c = delegator.run(cmd)
        error_msg = c.out
        error_msg = error_msg.replace(p_filename, '<br>' + p_filename)
    test_pep8 = {"name": "Testing for PEP8 warnings and errors (" + str(p_max_points) + " points)",
                 "pass": True,
                 "pass_message": "You have " + str(side_errors) + " PEP8 warning(s) or error(s). <br>" +
                                 "This translates to -" +
                                 str(min(p_max_points, side_errors)) +
                                 " point(s) deduction.<br>" +
                                 " Warnings/Errors are:" + error_msg +
                                 ".<br> ",
                 "pep8_errors": 0,
                 'points': 0,
                 }

    if side_errors != 0:
        test_pep8['pep8_errors'] = side_errors
        test_pep8['pass_message'] += '<br> See this link for help answering this question: ' \
                             ' <a href="https://docs.google.com/presentation/d/' \
                             '1d1DS-OWpD5QXUIStPkAQrMtNk1tH7nAsWOYSHbOllqo/edit#slide=id.g8c389caccd_0_6" ' \
                             'target="_blank">link</a>'
    test_pep8['fail_message'] = test_pep8['pass_message']
    test_pep8['points'] = max(0, int(p_max_points) - test_pep8['pep8_errors'])
    return test_pep8


def read_file_contents(p_filename):
    """ This function reads in contents of a file.
    Input: filename (string).
    Output: Filename contents (string)
    """
    with open(p_filename, 'r', encoding='utf8') as myfile:
        p_filename_data = myfile.read()
    return p_filename_data

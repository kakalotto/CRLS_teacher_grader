def _var_dir():  # TODO add some way to test on my machine instead of making blind edits (i'm sorry if i cause any bugs)
    """
    This helper function returns the var dir, depending on if code is run at CRLS or at Eric's Mac
    :return:The var dir for the CRLS autograder
    """
    import sys
    import os
    import socket

    if sys.platform == 'darwin':
        var_dir = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/var'  # This is Eric's home computer
    else:
        if len(socket.gethostname()) > 25:
            var_dir = '/app/var'  #assume heroku here
        else:
            var_dir = '/home/ewu/CRLS_APCSP_autograder/var'
    if os.path.isdir(var_dir) is False:
        raise Exception("Cannot find the var dir" + var_dir)
    return var_dir


def _var_filename(p_filename, p_test_num):
    """ This helper function returns the var filename, depending on if the code is run on Unix or Eric's Mac
    :param p_filename: The filename to evaluate
    :param p_test_num: the IO input test number
    :return: The var filename for the CRLS autograder
    """
    import re
    from CRLS_APCSP_autograder.app.python_labs import YEAR

    p_var_filename = re.sub(r'/tmp/', '', p_filename)
    p_var_filename = re.sub(YEAR + '_', '', p_var_filename)
    p_var_filename = re.sub(r'.py', '.in', p_var_filename)
    p_var_filename = re.sub(r'.+_', '', p_var_filename)
    p_var_filename = re.sub(r'\.in', '-' + str(p_test_num) + '.in', p_var_filename)

    return p_var_filename

# Input parameters: p_filename - filename (string)
#                   p_test - the number of test to run
#                   p_string - regex string you are going to search the output for (string)
#                   p_occurrences - number of times you want this string to show up (int)
#                   p_points - the number of points this test is worth
# Output: Dictionary of test_list_created
# This module runs tests and tries to find all strings in output


def io_test_find_string(p_filename, p_string, p_test_num, p_occurrences, p_points):
    import delegator
    import re

    var_dir = _var_dir()  # TODO should this be _var_dir()?
    var_filename = _var_filename(p_filename, p_test_num)

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + var_filename
    c = delegator.run(cmd)
    if c.err:
        raise Exception('Failed, trying to run ' + cmd)
    outfile_data = c.out
    p_string = p_string.replace(' ', r'\s')
    p_string = p_string.replace('$', r'\$')
    p_string = p_string.replace('+', r'\+')

    p_matches = len(re.findall(p_string, outfile_data, re.X | re.M | re.S))

    p_test_io = {"name": "Testing input/output  (" + str(p_points) + " points).<br>" +
                         "In output, looking for " + str(p_string) + " " + str(p_occurrences) + " times. <br>",
                 "pass": True,
                 "pass_message": "Pass! Input/output gave expected result. <br>",
                 "fail_message": "Fail. Input/output gave unexpected result. <br>" +
                                 "Looked for this: " + str(p_string) + "<br>" +
                                 " in this: " + str(outfile_data) + ".<br>"
                                 "Found it " + str(p_matches) + " times.<br>",
                 }
    if p_matches < p_occurrences:
        p_test_io['pass'] = False
        p_test_io['occurrences'] = p_matches
    return p_test_io


def io_test(p_filename, p_string, p_test_num, *, points=0, occurrences=1, help_link='', description=''):
    """
    This function runs a python program with a piped in file.  Then looks for certain strings.
    Returns a test dictionary.
    :param p_filename: filename of python code (string)
    :param p_string: regex string you are going to search the output for (string)
    :param p_test_num: the number of test to run (basically the input file for test)
    :param points: the number of points this test is worth
    :param occurrences: how many times you want the string to show up in the code output
    :param description: a description for the test (str)
    :param help_link: a link to help file
    :return: Dictionary containing info for this test.
    """
    import delegator
    import re

    var_dir = _var_dir()
    var_filename = _var_filename(p_filename, p_test_num)
    p_test_io = {"name": "Testing input/output  (" + str(points) + " points).<br>" +
                         "In output, looking for " + str(p_string) + "<br>",
                 "pass": True,
                 "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Input/output gave expected result. <br>",
                 "fail_message": "<h5 style=\"color:red;\">Fail.</h5> Input/output gave unexpected result. <br>",
                 "output": '',
                 "points": 0,
                 }

    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + var_filename
    print("Running this now" + str(cmd))
    c = delegator.run(cmd)
    if c.err:
        print("CERR" + str(c.err))
        print("COUT" + str(c.out))
        syntax_error = re.search(r'SyntaxError:', c.err, re.X | re.M | re.S)
        if syntax_error:
            p_test_io['fail_message'] += "<h5 style=\"color:purple;\"><br><br>" \
                                           "Your function has a syntax error somewhere<br>" \
                                           "Please run your code manually, correct the error, and try again.<br>" \
                                           "Syntax errors means the a mistake in typing (rather than logic) : " \
                                           "Things like missing comma, quotation mark, bracket." \
                                           " Or else just a typo.<br></h5>" \
                                           "<br>Code output was this:<br>" + str(c.err)
        p_test_io['pass'] = False
        p_test_io['fail_message'] += 'Failed, trying to run ' + cmd + \
                                     '. <br>  Try running the program manually with input specified in test' \
                                     ' to see what is wrong.'
        return p_test_io

    outfile_data = c.out
    print("WUT WUT WUT \n " + outfile_data)
    print("end outfile data\n ")

    print("p_string")
    print(p_string)
    print("outfile_data")
    print(outfile_data)
    print("end outfile data")
    p_matches = len(re.findall(p_string, outfile_data, re.X | re.M | re.S))

    if p_matches < occurrences:
        p_test_io['pass'] = False
        p_test_io['fail_message'] += "Looked for this regex in output:" + str(p_string) + "<br>" + \
                                     "Program output was this:<br> " + str(outfile_data) + "<br>"
        p_test_io['fail_message'] += "Found this many matches: " + str(p_matches)
    else:
        p_test_io['points'] += points

    if description:
        p_test_io['name'] = 'Input/output test: ' + description + ' (' + str(points) + ' points)'
    if help_link:
        p_test_io['fail_message'] += '<h5 style=\"color:purple;\">' \
                                     '.<br><br> See this link for help answering this question: ' \
                                     ' <a href="' + help_link + '" target="_blank">link</a>'
    p_test_io['output'] = outfile_data
    return p_test_io


def io_test_find_all(p_filename, p_strings, p_test_num, *, points=0, description='', help_link=''):
    """
    This function runs a python program with a piped in file.  Then looks for certain strings X times, using io_test.
    :param p_filename: Filename of python code (strong)
    :param p_strings: regex strings you are going to search the output for (string)
    :param p_test_num: the number of test to run (basically the input file for test)
    :param points: Points this test is worth
    :param description: description of the test (str)
    :param help_link: link to help (str)
    :return: Dictionary containing info for this test.
    """

    p_test_io = {"name": "Testing input/output  (" + str(points) + " points).<br>" +
                         "In output, looking for " + str(p_strings) + "<br>",
                 "pass": True,
                 "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                                 " Input/output gave expected result. <br>",
                 "fail_message": "<h5 style=\"color:red;\">Fail</h5>."
                                 " Input/output gave unexpected result. <br>",
                 'points': 0
                 }

    for this_test in [io_test(p_filename, regex_string, p_test_num) for regex_string in p_strings]:
        if not this_test['pass']:
            p_test_io['pass'] = False
            p_test_io['fail_message'] += this_test['fail_message']
    if p_test_io['pass']:
        p_test_io['points'] += points
    if description:
        p_test_io['name'] = 'Input/output test (looking for everything): ' + description + ' (' + str(points) + \
                            'points)'
    if help_link:
        p_test_io['fail_message'] += '<h5 style=\"color:purple;\">' \
                                     '<br><br> See this link for help answering this question: ' \
                                     ' <a href="' + help_link + '" target="_blank">link</a>'

    return p_test_io


if __name__ == "__main__":
    print("yes")
    #  abc = io_test('/Users/dimmyfinster/PycharmProjects/untitled5/2019_ewu_1.040.py', 1, 'asdfsdf', 5)
    #  print(abc)
    # abc = io_test_find_all ('/Users/dimmyfinster/PycharmProjects/untitled5/2019_ewu_1.060.py',

    #                        ['(\^ | \s+ ) b2 (\s+ | \? | \. | , | !)'], 1, 5)
    # abc = io_test_find_all('/home/ewu/CRLS_APCSP_Mac_Autograder/2.051/2019_ewu_1.040.py',
    #                        [r'(\^ | \s+ ) b2 (\s+ | \? | \. | , | !)'], 1, 5)

    #print(abc)

def run_unit_test(p_lab, p_test_number, p_points, description='', help_link=''):
    """
    unit test runs the unit tests.  It assumes that there is a file /tmp/<lab number>.test.py and runs one test
    :param p_lab: lab number (str) i.e. 4.021
    :param p_test_number: test number within the test suite to run
    :param description: description of the problem (str)
    :param help_link: link to help in case of fail
    :param p_points: number of points this is worth
    :return: test dictionary
    """
    import delegator
    import re
    import os.path

    p_unit_test = {"name": "Testing calling functions, test " + str(p_test_number) + ".  (" + str(p_points) +
                           " points )",
                   "pass": True,
                   "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Test number " + str(p_test_number) +
                                   " gave expected result. <br>",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5> Test number " + str(p_test_number) +
                                   " gave unexpected result. <br>",
                   "output": '',
                   'points': 0
                   }
    if description:
        p_unit_test['name'] = 'Running unit test ' + str(p_test_number) + ': ' + description + \
                              ' (' + str(p_points) + ' points)'

    test_filename = '/tmp/' + str(p_lab) + '.test.py'
    if not os.path.exists(test_filename):
        p_unit_test['pass'] = False
        p_unit_test['fail_message'] += "Testing file " + test_filename + " doesn't exist.  Bug somewhere?<br>"
        return p_unit_test

    cmd = 'python3 /tmp/' + str(p_lab) + '.test.py testAutograde.test_' + str(p_test_number) + " 2>&1 "
    c = delegator.run(cmd)

    error = re.search('Error', c.out, re.X | re.M | re.S)
    failed_assertion_equal = re.search('AssertionError: (.+?) != (.+?)$', c.out, re.X | re.M | re.S)
    failed_assertion_regex = re.search('AssertionError: \s Regex .*? match: (.+?) not \s found \s in  (.+?) :',
                                       str(c.out), re.X | re.M | re.S)
    p_unit_test['fail_message'] += 'Ran this command: ' + str(cmd)
    print("c.out" + str(c.out))
    print("c.out done")
    print("c.err " + str(c.err))
    print("c.err done")
    syntax_error = re.search(r'SyntaxError:', c.out, re.X | re.M | re.S)
    name_error = re.search(r'NameError:', c.out, re.X | re.M | re.S)
    if syntax_error:
        p_unit_test['pass'] = False
        p_unit_test['fail_message'] += "<h5 style=\"color:purple;\"><br><br>" \
                                       "Your function has a syntax error somewhere<br>" \
                                       "Please run your code manually, correct the error, and try again.<br>" \
                                       "Syntax errors means the a mistake in typing (rather than logic) : " \
                                       "Things like missing comma, quotation mark, bracket." \
                                       " Or else just a typo.<br></h5>" \
                                       "<br>Code output was this:<br>" + str(c.out)
        p_unit_test['output'] = c.out
        return p_unit_test
    if name_error:
        p_unit_test['pass'] = False
        p_unit_test['fail_message'] += "<h5 style=\"color:purple;\"><br><br>" \
                                       "Your function has a name error somewhere<br>" \
                                       "Please run your code manually, correct the error (if it is obvious)" \
                                       ", and try again.<br>" \
                                       "name errors can mean a few things. <br><br> One possibility is using " \
                                       "a variable that is not declared.  " \
                                       "<br>If this is the case, your program should " \
                                       "fail to run if you run it manually.<br>" \
                                       "  <br>A second possibility is that you are using a variable " \
                                       "from the main program, not from the function. " \
                                       '<br>This problem is explained here (see note on right about autograder): ' \
                                       '<a href="https://docs.google.com/presentation/d/1WJmH2p5iqk1j53E5PZ5KHDCv' \
                                       't18dqxqQOd-SQ5nPomY/edit#slide=id.g8caecfd5e9_0_1" ' \
                                       'target="_blank">link</a><br><br>' \
                                       'A third possibility is that you are calling a ' \
                                       'function that does not exist or that the autograder is calling' \
                                       'a function you have not written yet.</h5><br>' \
                                       "<br>Code output was this:<br>" + str(c.out)
        p_unit_test['output'] = c.out
        return p_unit_test

    true_false = re.search(r'(True|False)', c.out, re.X| re.M | re.S)
    ok = re.search(r'^OK$', c.out, re.X | re.M | re.S)

    no_return = re.search(r'AssertionError: .*?  (None|none) .*? !=', c.out, re.X | re.M | re.S)

    if no_return:
        return_link = 'https://docs.google.com/presentation/d/1jfcPojBgjVXL2ql2kN-FW2ML6yVzE2H67cc9UO4yKzo/' \
                      'edit#slide=id.g8cf0cdf918_2_0'
        p_unit_test['fail_message'] += "<h5 style=\"color:purple;\"><br><br>" \
                                       "Looks like function is supposed to have a return, but does not. <br><br>" \
                                       "If you think you did this function correctly, usually it " \
                                       "is because you printed " \
                                       "instead. <br>Please  double check the instructions to see what <br>" \
                                       "function is supposed to return (if anything).<br>" \
                                       '<br>Sometimes this error happens because you aren not done yet' \
                                       '<br>See this link for help about returns/no return: ' \
                                       ' <a href="' + return_link + '" target="_blank">link</a><br></h5>'

    formatted_cout = re.sub(r"\n", "<br>", c.out)
    if failed_assertion_equal and not no_return:
        p_unit_test['pass'] = False
        p_unit_test['fail_message'] += "<h5 style=\"color:purple;\"><br><br>" \
                                       "Function ran but gave the wrong result. <br>" \
                                       "Your function returns this:" + failed_assertion_equal.group(1) + \
                                       "<br>Correct function expects this: " + failed_assertion_equal.group(2) + \
                                       "</h5><br><br>"
        p_unit_test['fail_message'] += formatted_cout + "<br>"
    elif failed_assertion_regex and not no_return:
        p_unit_test['pass'] = False
        return_text = failed_assertion_regex.group(1)
        p_unit_test['fail_message'] += return_text

        return_text = return_text.replace('(?xms) ', '')
        return_text = return_text.replace('\\\s', '')

        p_unit_test['fail_message'] += "<h5 style=\"color:purple;\"><br><br>" \
                                       "Function ran but gave the wrong result. <br>" \
                                       "Your function needs to find this string:" + return_text + \
                                       "<br>Inside of this string: " + failed_assertion_regex.group(2) + \
                                       "</h5><br><br>"
        p_unit_test['fail_message'] += formatted_cout + "<br>"
    elif error:
        p_unit_test['pass'] = False
        p_unit_test['fail_message'] += "This is the output of the test:<br> <br>"
        p_unit_test['fail_message'] += formatted_cout + "<br>"
    else:
        p_unit_test['points'] += p_points
    if help_link:
        p_unit_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                  '<br>See this link for help answering this question: ' \
                                  ' <a href="' + help_link + '" target="_blank">link</a>'
    return p_unit_test


# Inputs: p_filename, filename with python in it
# This module creates a testing file to run unit tests
def create_testing_file(p_filename):
    import delegator
    import sys
    import os
    import re
    import socket

    from CRLS_APCSP_autograder.app.python_labs import YEAR

    if sys.platform == 'darwin':
        var_dir = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/var'
        # This is Eric's home computer
    else:
        if len(socket.gethostname()) > 25:
            var_dir = '/app/var'
        else:
            var_dir = '/home/ewu/CRLS_APCSP_autograder/var'
    if os.path.isdir(var_dir) is False:
        raise Exception("Cannot find the var dir " + str(var_dir))

    p_functions_filename = p_filename.replace('.py', '.functions.py')

    p_var_filename = re.sub('/tmp/', '', p_filename)
    p_var_filename = re.sub(YEAR + '_', '', p_var_filename)
    p_var_filename = re.sub('.py', '.test.py', p_var_filename)
    p_var_filename = re.sub('.+_', '', p_var_filename)
    cmd = ' cat ' + p_functions_filename + " " + var_dir + "/" + p_var_filename + "  > /tmp/" + p_var_filename
    c = delegator.run(cmd)

    if c.err:
        raise Exception("There as a problem creating the python test file " + cmd
                        + "\nOne possible reason is there is nothing in the main part of the code.  If this"
                          "is the case, add a dummy line there (like a print('hello') or something like that.\n"
                          "Another possible reason is that you don't have any functions.\n"
                          "Another reason is that you are running as user and can't overwrite a root file.")


def extract_all_functions_2(orig_file):
    """
    Extracts all functions from the file, hopefully this one works with spaces
    :param orig_file: Name of the python file (str)
    :return: Nothing.  It writes everything to the file /tmp/<python_file>.functions.py
    """
    import re
    with open(orig_file, 'r', encoding='utf8') as infile:
        all_lines = infile.readlines()
    infile.close()
    file_contents = ''.join([str(elem) for elem in all_lines])  # converts the list into a single string
    outfile_name = orig_file.replace('.py', '.functions.py')
    outfile = open(outfile_name, 'w')
    delimiter = r'def'
    items = file_contents.split(delimiter)
    keep_functions = [line for line in items if re.search(r'^\s', line)]
    almost_functions = [delimiter + line for line in keep_functions.split(delimiter) if line]  # sticks 'def' back in


def extract_all_functions(orig_file):
    """
    Extracts all functions
    :param orig_file: The name of the python file (string)
    :return: Nothing. It writes everything to the file <python file>.functions.py
    """
    import re
    outfile_name = orig_file.replace('.py', '.functions.py')
    outfile = open(outfile_name, 'w')

    with open(orig_file, 'r', encoding='utf8') as infile:
        line = True

        while line:
            line = infile.readline()
            start_def = re.search(r"^(def|class) \s+ .+ ", line, re.X | re.M | re.S)
            # print(start_def)
            empty_counter = 0
            if start_def:

                outfile.write(line)
                in_function = True
                # counter = 0
                while in_function:
                    # counter += 1
                    # print("counter " + str(counter))
                    # if counter == 15:
                    #     raise Exception("what the heck")
                    line = infile.readline()
                    if line == '':
                        break
                    # print("aaa next line " + line)
                    end_of_function = re.search(r"^[a-zA-Z]", line, re.X | re.M | re.S)
                    new_function = re.search(r"^(def|class) \s+ .+ ", line, re.X | re.M | re.S)
                    # print("end? " + str(end_of_function))
                    # print("new?" + str(new_function))
                    if end_of_function and not new_function:
                        in_function = False
                        start_def = False
                    elif end_of_function and new_function:
                        in_function = True
                        start_def = True
                        outfile.write(line)
                    else:
                        outfile.write(line)
                    # print("aaa this line still " + str(line))
                    # print("in function start_def " + str(in_function) + " " + str(start_def))


def extract_single_function(p_orig_file, p_function):
    import re
    function_file = p_orig_file.replace('.py', '.functions.py')
    extracted_function = ''
    with open(function_file, 'r', encoding='utf8') as infile:
        line = True
        while line:
            # print("looking for this function : " + p_function)
            line = infile.readline()
            start_def = re.search(r"^(def|class) \s+ " + p_function, line, re.X | re.M | re.S)
            if start_def:
                # print("entering function!")
                # print('writing this' + str(line))
                extracted_function += line
                # print("reading this" + str(line))
                inside_function = True
                x = 0
                while inside_function:
#                    print('reading this ' + str(line))
                    line = infile.readline()
                    # (^(\s+ | \# ) .+  | ^\s*$)
                    #  r"^(\s+ | \# ) .+
                    inside_function = re.search(r"(^(\s+ | \# ) .+  | ^\s*$)", line, re.X | re.M | re.S)
                    if inside_function:
                        # print("writing this inside function " + str(line))
                        extracted_function += line
                    quitnow = re.search(r"^([a-zA-Z]+ | def | class)", line, re.X | re.M | re.S)
                    if quitnow and x != 0:
                        inside_function = False
                    x += 1
                    if x > 100:
                        inside_function = False
                extracted_function += line
    # print(extracted_function)
    return extracted_function

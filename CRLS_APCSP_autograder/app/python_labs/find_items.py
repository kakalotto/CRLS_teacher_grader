def find_list(p_filename_data, *, num_items=0, list_name='', points=0, description='', help_link=''):
    """
    find_list finds that there is a list with exactly p_num_items items
    :param p_filename_data: larger string, usually containing the contents of the python file
    :param num_items: number of items we are looking for (int)
    :param list_name: Name of list we are looking for (int)
    :param description: Description of the test (str)
    :param points: points you can earn (int)
    :param help_link: link describing help (str)
    :return: a dictionary of the test
    """
    import re

    search_string = ''
    if num_items == 0:
        search_string = list_name + r" \s* = \s* \[ ?\]"
    elif num_items == 4:
        search_string = list_name + r" \s* = \s* \[ [^\]]+ , [^\]]+ , [^\]]+ , [^\]]+ .? \]"
    elif num_items == 6:
        search_string = list_name + r" \s* = \s* \[ [^\]]+ , [^\]]+ , [^\]]+ , [^\]]+ , [^\]]+, [^\]]+ .? \]"

    # test for a list that is created (i.e. abc = [asdf]
    p_search_object = re.search(search_string, p_filename_data, re.X | re.M | re.S)

    p_test_list = {"name": "Testing that there is a list named " + list_name + " with " + str(num_items) + " items ("
                           + str(points) + " points). <br>",
                   "pass": bool(p_search_object),
                   "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Submitted string has something"
                                   " that looks like "
                                   "a list being created with correct name and number of items.",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5>Submitted string does not look like it has list"
                                   " being created with correct name and number of items.  String is the following:<br>"
                                   + p_filename_data +
                                   "<h5 style=\"color:purple;\">"
                                   "<br> List must be named <b><i>exactly</b></i> according to instructions <br></h5>",
                   'points': points if bool(p_search_object) else 0
                   }

    if description:
        prefix = 'Find list '
        if num_items != 0:
            prefix += ' with ' + str(num_items) + ' items '
        prefix += ' test: '
        p_test_list['name'] = prefix + description + ' (' + str(points) + ' points)'
    if help_link:
        p_test_list['fail_message'] += '<h5 style=\"color:purple;\">' \
                                       '<br>See this link for help answering this question: ' \
                                       ' <a href="' + help_link + '" target="_blank">link</a>'
    return p_test_list


def find_dictionary(p_filename_data, *, num_items=0, dict_name='', points=0, help_link=''):
    """
    find_dictionary finds that there is a dictionary with  p_num_items items
    :param p_filename_data: larger string, usually containing the contents of the python file
    :param num_items: number of items we are looking for (int)
    :param dict_name: Name of list we are looking for (int)
    :param points: points you can earn (int)
    :param help_link: link describing help (str)
    :return: a dictionary of the test
    """
    import re

    search_string = ''
    if num_items == 0:
        search_string = dict_name + r"{ \s* }"
    elif num_items == 3:
        search_string = dict_name + r"{ [^:},]+ : .+ , [^:},]+ : .+ , [^:},]+ : .+ [^}]+}"

    # test for a dictionary that is created (i.e. abc = [asdf]
    p_search_object = re.search(search_string, p_filename_data, re.X | re.M | re.S)

    p_test_dictionary = {"name": "Testing that there is a dictionary named " + dict_name + " with " +
                                 str(num_items) + " items (" + str(points) + " points). <br>",
                         "pass": bool(p_search_object),
                         "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Submitted string has something"
                                         " that looks like "
                                         "a dictionary being created with correct name and number of items.",
                         "fail_message": "<h5 style=\"color:red;\">Fail.</h5>Submitted string does not look "
                                         "like it has a dictionary"
                                         " being created with correct name and number of items.  String is the "
                                         "following:<br>"
                                         + p_filename_data + "<br> Dictionary must given the name in the instructions "
                                                             "EXACTLY."
                                                             "<br>",
                         'points': points if bool(p_search_object) else 0
                         }
    if help_link:
        p_test_dictionary['fail_message'] += '<h5 style=\"color:purple;\">' \
                                       '<br>See this link for help answering this question: ' \
                                       ' <a href="' + help_link + '" target="_blank">link</a>'
    return p_test_dictionary


def find_if(p_filename_data, p_num, p_points, *, minmax='min', description='', help_link=''):
    """
    function finds ifs
    :param p_filename_data: large string with data (usually the python file)
    :param p_num: number of times we are looking for ifs
    :param p_points: points
    :param minmax: minimum or maximum matches
    :param description: description of the problem (str)
    :param help_link: link to help in case of fail

    :return: a dictionary of the test
    """
    import re

    matches = len(re.findall(r"[^l]if \s", p_filename_data, re.X | re.M | re.S))

    p_test = {"name": "Testing that there are least " + str(p_num) + " ifs (" + str(p_points) +
                      " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We matched " + str(matches) + " ifs ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> ",
              "points": 0
              }
    if minmax == 'max':
        p_test['name'] = "Testing that there is MAX  " + str(p_num) + " ifs (" + str(p_points) + \
                         " points)<br>"
        print(p_test['name'])
        print(matches)
        if matches > p_num:
            p_test['pass'] = False
            p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                      "Code has over " + str(p_num) + " ifs.<br></h5>" + \
                                      "Searched for ifs in this string:<br> " + p_filename_data + \
                                      "<br>  If you think this should pass, control-F and search for " \
                                      "'if' in your code""<br>  Found this many ifs: " + \
                                      str(matches) + ".<br>"
    elif minmax == 'min':
        if matches < p_num:
            p_test['pass'] = False
            p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                      "Code does not have at least " + str(p_num) + " ifs.<br></h5>" + \
                                      "Searched for ifs in this string:<br> " + p_filename_data + \
                                      "<br>" + \
                                      "If you think this should pass, control-F and search for " + \
                                      "'if' in your code" + \
                                      "<br>  Found this many ifs: " + str(matches) + ".<br>"

    if description:
        p_test['name'] = 'Find string in code test: ' + description + ' (' + str(p_points) + ' points)'
    if help_link:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                  '<br>See this link for help answering this question: ' \
                                  ' <a href="' + help_link + '" target="_blank">link</a></h5>'

    if p_test['pass']:
        p_test['points'] = p_points
    return p_test


def find_elif(p_filename_data, p_num, p_points, *, minmax='min', help_link=''):
    """
    function finds elifs
    :param p_filename_data: large string with data (usually the python file)
    :param p_num: number of times we are looking for ifs
    :param p_points: points
    :param help_link: html link to help (str)
    :param minmax: minimum or maximum matches
    :return: a dictionary of the test
    """
    import re

    matches = len(re.findall(r"elif \s", p_filename_data, re.X | re.M | re.S))

    p_test_find_questions = {"name": "Testing that there are least " + str(p_num) + " elifs (" + str(p_points) +
                                     " points)<br>",
                             "pass": True,
                             "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                                             "We matched " + str(matches) + " elifs ",
                             "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                             '<h5 style=\"color:purple;\">'
                                             "Code does not have at least " + str(p_num) + " elifs.<br></h5>" +
                                             "Searched for elifs in this string:<br> " + p_filename_data + "<br>" +
                                             "If you think this should pass, control-F and search for "
                                             "'elif' in your code<br>",
                             "points": 0
                             }
    if minmax == 'max':
        p_test_find_questions['name'] = "Testing that there is MAX  " + str(p_num) + " elifs (" + str(p_points) + \
                                        " points)<br>"
        if matches > p_num:
            p_test_find_questions['pass'] = False
            p_test_find_questions['fail_message'] += "<h5 style=\"color:red;\">Fail.</h5> " \
                                                     "Code does not have at least " + str(p_num) + " elifs.<br>" + \
                                                     "Searched for elifs in this string:<br> " + p_filename_data + \
                                                     "<br>  If you think this should pass, control-F and search for " \
                                                     "'elif' in your code""<br>  Found this many elifs: " + \
                                                     str(matches) + ".<br>"
    elif minmax == 'min':
        if matches < p_num:
            p_test_find_questions['pass'] = False
            p_test_find_questions['fail_message'] += "<br>  Found this many elifs: " + str(matches) + ".<br>"

    if help_link:
        p_test_find_questions['fail_message'] += '<h5 style=\"color:purple;\">' \
                                                 '<br>See this link for help answering this question: ' \
                                                 ' <a href="' + help_link + '" target="_blank">link</a>'
    if p_test_find_questions['pass']:
        p_test_find_questions['points'] = p_points
    return p_test_find_questions


def find_else(p_filename_data, p_num, p_points, *, minmax='min'):
    """
    function finds elses
    :param p_filename_data: large string with data (usually the python file)
    :param p_num: number of times we are looking for ifs
    :param p_points: points
    :param minmax: minimum or maximum matches
    :return: a dictionary of the test
    """
    import re

    matches = len(re.findall(r"else:", p_filename_data, re.X | re.M | re.S))

    p_test_find_questions = {"name": "Testing that there are least " + str(p_num) + " elses (" + str(p_points) +
                                     " points)<br>",
                             "pass": True,
                             "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                                             "We matched " + str(matches) + " elses ",
                             "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                             '<h5 style=\"color:purple;\">'
                                             "Code does not have at least " + str(p_num) + " elses.<br></h5>" +
                                             "Searched for elses in this string:<br> " + p_filename_data + "<br>" +
                                             "If you think this should pass, control-F and search for "
                                             "'elses' in your code<br>"
                                             "Elses take care of the scenario where we don't match any if or elif.<br>",
                             "points": 0
                             }
    if minmax == 'max':
        p_test_find_questions['name'] = "Testing that there is MAX  " + str(p_num) + " elses (" + str(p_points) + \
                                        " points)<br>"
        if matches > p_num:
            p_test_find_questions['pass'] = False
            p_test_find_questions['fail_message'] += "<h5 style=\"color:red;\">Fail.</h5> " \
                                                     "Code does not have at least " + str(p_num) + " elses.<br>" + \
                                                     "Searched for elses in this string:<br> " + p_filename_data + \
                                                     "<br>  If you think this should pass, control-F and search for " \
                                                     "'else' in your code""<br>  Found this many elses: " + \
                                                     str(matches) + ".<br>"
    elif minmax == 'min':
        if matches < p_num:
            p_test_find_questions['pass'] = False
            p_test_find_questions['fail_message'] += "<br>  Found this many elses: " + str(matches) + ".<br>"

    if p_test_find_questions['pass']:
        p_test_find_questions['points'] = p_points
    return p_test_find_questions


def find_print(p_filename_data, p_num, p_points, *, minmax='min', description='', help_link=''):
    """
    function finds prints
    :param p_filename_data: large string with data (usually the python file)
    :param p_num: number of times we are looking for prints
    :param p_points: points
    :param minmax: minimum or maximum matches
    :param description: Description of what you are printing (str)
    :param help_link: link to help in case of fail (str)
    :return: a dictionary of the test
    """
    import re

    matches = len(re.findall(r"print\(", p_filename_data, re.X | re.M | re.S))

    p_test = {"name": "Testing that there are least " + str(p_num) + " prints (" + str(p_points) +
                      " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We matched " + str(matches) + " prints ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have at least " + str(p_num) + " prints.<br>" +
                              "Searched for prints in this string:<br> " + p_filename_data + "<br>" +
                              "If you think this should pass, control-F and search for "
                              "'print' in your code",
              "points": 0
              }
    if minmax == 'max':
        p_test['name'] = "Testing that there is MAX  " + str(p_num) + " prints (" + str(p_points) + \
                         " points)<br>"

        if matches > p_num:
            p_test['pass'] = False
            p_test['fail_message'] += "<h5 style=\"color:red;\">Fail.</h5> " \
                                      "Code does not have at least " + str(p_num) + " prints.<br>" + \
                                      "Searched for prints in this string:<br> " + p_filename_data + \
                                      "<br>  If you think this should pass, control-F and search for " \
                                      "'print' in your code""<br>  Found this many prints: " + \
                                      str(matches) + ".<br>"
    elif minmax == 'min':
        if matches < p_num:
            p_test['pass'] = False
            p_test['fail_message'] += "<br>  Found this many prints: " + str(matches) + ".<br>"

    if p_test['pass']:
        p_test['points'] = p_points
    if description:
        p_test['name'] = 'Find print in code test: ' + description + ' (' + str(p_points) + ' points)'
    if help_link:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                  '<br>See this link for help answering this question: ' \
                                  ' <a href="' + help_link + '" target="_blank">link</a>'

    return p_test


def find_random(p_filename_data, p_points, *, randint=False):
    """
    find_random - looks for importing random or else from random import.  I
    :param p_filename_data: string usually containing the python code
    :param p_points: number of points this is worth
    :param randint: whether we are looking for randint also
    :return:
    """
    import re

    matches = len(re.findall(r"(import\s+random|from\s+random\s+import)", p_filename_data, re.X | re.M | re.S))

    help_link = 'https://docs.google.com/presentation/d/1u-Qw_AOBVPfLxKBlT-aBAkSb1Sn3SFLYRyF37GMVcKA/' \
                'edit#slide=id.g41529343e1_0_4'
    p_test_random = {"name": "Testing that random is imported (" + str(p_points) + " points)<br>",
                     "pass": True,
                     "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  We found that random was imported ",
                     "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                     "Code does not import random.<br>"
                                     "<h5 style=\"color:purple;\">"
                                     '<br>See this link for help answering this question: '
                                     ' <a href="' + help_link + '" target="_blank">link</a>',
                     "points": 0
                     }
    if matches < 1:
        p_test_random['pass'] = False

    if randint:
        matches = len(re.findall(r"randint\(", p_filename_data, re.X | re.M | re.S))
        p_test_random['name'] += 'AND that randint is used.<br>'
        p_test_random['pass_message'] += '  AND randint is used.<br>'
        p_test_random['fail_message'] += '  Or else randint is not used.<br>'
        if matches < 1:
            p_test_random['pass'] = False
    if p_test_random['pass']:
        p_test_random['points'] = p_points
    return p_test_random


# Inputs: p_filename_data, contents of the file (string).
# Output: Dictionary of test_loop, created
# This module finds if there is a loop


def find_loop(p_filename_data, p_points, description='', help_link=''):
    """
    find_loop - looks for a loop in a string
    :param p_filename_data: string with code in it (string)
    :param p_points: number of points this is worth
    :param description: description of the problem (str)
    :param help_link: link to help in case of fail (str)
    :return: a test dictionary
    """
    import re

    # test for a list that is created (i.e. abc = [asdf]
    p_search_object = re.search(r"(for|while)", p_filename_data, re.X | re.M | re.S)

    p_test_loop = {"name": "Testing that there is a loop. (" + str(p_points) + " points)<br>",
                   "pass": True,
                   "pass_message": "<h5 style=\"color:green;\">Pass!</h5> There is a loop in the code selection",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5> There is not a loop in the selected code.  "
                                   "Selected code is this:<br>"
                                   "" + p_filename_data,
                   'points': 0
                   }
    if p_search_object:
        p_test_loop['points'] += p_points
    else:
        p_test_loop['pass'] = False
    if description:
        p_test_loop['name'] = 'Find string in code test: ' + description + ' (' + str(p_points) + ' points)'
    if help_link:
        p_test_loop['fail_message'] += '<h5 style=\"color:purple;\">' \
                                       '<br>See this link for help answering this question: ' \
                                       ' <a href="' + help_link + '" target="_blank">link</a>'
    return p_test_loop


def find_string(p_filename_data, p_search_string, p_num, *, points=0, minmax='min', description='', help_link=''):
    """
    This function looks for a regex string within a larger string X times
    :param p_filename_data: The larger string to search
    :param p_search_string: The regex to look for
    :param p_num: number of times you require regex to appear in larger string
    :param points: points this is worth (int)
    :param minmax: whether you want p_num to be MIN or MAX times string can appear.  Default is min.
    :param description: description of the problem (str)
    :param help_link: link to help in case of fail (str)
    :return: dictionary of test info
    """
    import re

    p_matches = len(re.findall(p_search_string, p_filename_data, re.X | re.M | re.S))
    p_test_find_string = {"name": "Testing that this string is there: " + p_search_string + " at least " +
                                  str(p_num) + " times (" + str(points) +
                                  " points) <br>",
                          "pass": True,
                          "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Found this string: "
                                          + p_search_string + " at least " +
                                          str(p_num) + " times.<br>",
                          "fail_message": "<h5 style=\"color:red;\">Fail.</h5>  Didn't find this regex string:"
                                          + p_search_string + " at least " +
                                          str(p_num) + " times.<br>",
                          'points': 0
                          }
    if minmax == 'max':
        passed = p_matches <= p_num
    elif minmax == 'min':
        passed = p_matches >= p_num
    else:
        raise Exception("variable minmax must be either 'min' or 'max'")
    if not passed:
        p_test_find_string['pass'] = False
        p_test_find_string['fail_message'] += "Found match " + str(p_matches) + " times in this string:. <br>" + \
                                              p_filename_data
    else:
        p_test_find_string['points'] += points
    if description:
        p_test_find_string['name'] = 'Find string in code test: ' + description + ' (' + str(points) + ' points)'
    if help_link:
        p_test_find_string['fail_message'] +=  '<h5 style=\"color:purple;\">' \
                                               '<br>See this link for help answering this question: ' \
                                               ' <a href="' + help_link + '" target="_blank">link</a>'
    return p_test_find_string


# Inputs: p_filename_data, contents of the file (string).
#         p_search_strings, list of what you are looking for, literally (string)
#         p_points, number of points this test is worth (int)
# Output: Dictionary of test_find_all_strings
# This module finds if all strings are there


def find_all_strings(p_filename_data, p_search_strings, p_points, *, description='', help_link=''):
    """
    function looks for all strings
    :param p_filename_data: The larger string to search
    :param p_search_strings: The regexes (PLURAL) to look for (string)
    :param p_points:  points this is worth (int)
    :return: dictionary of test info
    """
    # passed = []
    # debug = []
    # for p_search_string in p_search_strings:
    #     test_find_string = find_string(p_filename_data, p_search_string, 1, points=0)
    #     if test_find_string['pass']:
    #         passed.append(p_search_string)
    #         debug.append(test_find_string)
    passed = [p_search_string for p_search_string in p_search_strings
              if find_string(p_filename_data, p_search_string, 1, points=0)['pass']]

    p_test_find_strings = {"name": "Testing that ALL of these strings are there: " + str(p_search_strings) +
                                   " (" + str(p_points) + " points) <br>",
                           "pass": passed == p_search_strings,
                           "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Found ALL of these these strings: "
                                           "" + str(p_search_strings) + ".<br>",
                           "fail_message": "<h5 style=\"color:red;\">Fail.</h5> Didn't find all strings in "
                                           "" + str(p_search_strings) + ". <br" +
                                           " But did find these strings: " + str(passed) + ". <br>",
                           'points': p_points if passed == p_search_strings else 0
                           }
    if passed != p_search_strings:
        p_test_find_strings['pass'] = False
    else:
        p_test_find_strings['points'] = p_points
    if description:
        p_test_find_strings['name'] = 'Find all strings test: ' + description + ' (' + str(p_points) + ' points)'
    if help_link:
        p_test_find_strings['fail_message'] += '<h5 style=\"color:purple;\">' \
                                               '<br>See this link for help answering this question: ' \
                                               ' <a href="' + help_link + '" target="_blank">link</a></h5>'
    return p_test_find_strings


def find_function(p_filename, p_function_name, p_num_parameters, *, points=0):
    """
    find function finds if a particular function exists
    :param p_filename: name of python file to check
    :param p_function_name: function to find
    :param p_num_parameters: number of parameters this function should have
    :param points: number points this test is worth
    :return:
    """
    import delegator

    # Check for function return_min
    cmd_string = ''
    if p_num_parameters == 0:
        cmd_string = r'grep "^def ' + p_function_name + r'(\s*):"'
    elif p_num_parameters == 1:
        cmd_string = r'grep "^def ' + p_function_name + r'(\s*[a-zA-Z_][^,]*\s*)"'
    elif p_num_parameters == 2:
        cmd_string = r'grep "^def ' + p_function_name + r'(\s*[a-zA-Z_][a-zA-Z0-9_]*,\s*[a-zA-Z_][^,]*\s*)"'
    elif p_num_parameters == 3:
        cmd_string = r'grep "^def ' + p_function_name + r'(\s*[a-zA-Z_][a-zA-Z0-9_]*,' \
                                                        r'\s*[a-zA-Z_][a-zA-Z0-9_]*,\s*[a-zA-Z_][^,]*\s*)"'
    p_test_function_exists = {"name": "Testing that there is a function " + p_function_name +
                                      " with " + str(p_num_parameters) + " input parameters. (" + str(points) +
                                      " points). <br>",
                              "pass": True,
                              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                                              " There is a function " + p_function_name +
                                              " with " + str(p_num_parameters) + " input parameters. <br>",
                              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>"
                                              "There is NOT a function " + p_function_name +
                                              " with " + str(p_num_parameters) + " input parameters. <br>",
                              'points': 0
                              }

    cmd = cmd_string + ' ' + p_filename
    c = delegator.run(cmd)
    if c.err:
        p_test_function_exists['pass'] = False
        p_test_function_exists['fail_message'] += "Error message: " + c.err
    elif c.out:
        p_test_function_exists['pass_message'] += "Found this: " + c.out
        p_test_function_exists['points'] += points
    else:
        p_test_function_exists['pass'] = False
        cmd = 'grep "def" ' + p_filename
        c = delegator.run(cmd)
        p_test_function_exists['fail_message'] += "The file " + p_filename + " has these functions: <br> " + \
                                                  c.out + "<br>" + " Autograder did not find " +\
                                                  p_function_name + " with" + \
                                                  " exactly " + str(p_num_parameters) + " input parameter(s). <br>"
    help_link = 'https://docs.google.com/presentation/d/1cAr1bVWWGVcDKuEqSCYBbla7_pglpbt-5hsFOxPcmE8/' \
                'edit#slide=id.g8e77a2c1ac_0_0'
    p_test_function_exists['fail_message'] += '<h5 style=\"color:purple;\">' \
                                              '<br>See this link for help answering this question: ' \
                                              ' <a href="' + help_link + '" target="_blank">link</a>'
    return p_test_function_exists


# Inputs: p_filename_data, contents of the file (string).
#         p_class_name, function name I am looking for (string)
#         p_parent, number of parameters I expect (integer)
#         p_points, points this is worth (int)
# Output: Dictionary of test_class_exists
# This module finds if there is a class with a certain name and certain parameters

def find_class(p_filename, p_class_name, p_parent, *, points=0):
    """
    find class finds if a particular class with a particular name is there
    :param p_filename: name of the python code file
    :param p_class_name:  name of class you are looking for
    :param p_parent: parent (object, or else the parent class)
    :param points: points this is worth
    :return: dictionary of test info
    """
    import delegator
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents

    filename_data = read_file_contents(p_filename)

    cmd_string = 'grep "^class ' + p_class_name + r"(" + p_parent + r')"'

    cmd = cmd_string + ' ' + p_filename
    c = delegator.run(cmd)
    p_test_class_exists = {"name": "Looking for this class " + p_class_name + " with this parent " + " p_parent (" +
                                   str(points) + " points). ",
                           "pass": True,
                           'pass_message': "<h5 style=\"color:green;\">Pass!</h5>",
                           'fail_message': "<h5 style=\"color:red;\">Fail.</h5>",
                           'points': 0}
    if c.err:
        p_test_class_exists['pass'] = False
        p_test_class_exists['fail_message'] += "Error message: " + c.err
    elif c.out:
        p_test_class_exists['pass_message'] += "Found this: " + c.out
        p_test_class_exists['points'] = points
    else:
        p_test_class_exists['pass'] = False
        cmd = 'grep "class" ' + p_filename
        c = delegator.run(cmd)
        p_test_class_exists['fail_message'] += "The file " + p_filename + " contents is this: : <br> " + \
                                               filename_data + "<br>" + " but not " + p_class_name + "("\
                                               + str(p_parent) + "). <br>" \
                                                                 "All classes should have a parent" \
                                                                 " (something in parentheses, if this is an early lab" \
                                                                 "that should be (object) as in class(object)).<br> "\
                                                                 "For example: def ExampleClass(object): <br><br>"
    return p_test_class_exists


def object_created(p_filename, p_class_name, p_times, *, points=0):
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    import re
    p_test_function_called = {"name": "Testing that there are objects of type  " + p_class_name +
                                      " that gets created in the main program at least " +
                                      str(p_times) + " times.  (" + str(points) + " points).<br>"
                                      + "). <br>",
                              "pass": False,
                              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> There is object of type " + p_class_name +
                                              " that gets created enough times "
                                              "<br>",
                              "fail_message": "<h5 style=\"color:red;\">Fail</h5>  The class " + p_class_name +
                                              " does NOT have enough objects of that type in the program. <br>"
                                              " If this doesn't make sense, look at the presentations for help"
                                              " <br>",
                              "points": points
                              }
    regex = r"[a-zA-Z0-9]\s*=\s*" + p_class_name
    with open(p_filename) as infile:
        matches = len([1 for line in infile.readlines() if re.search(regex, line, re.X | re.M | re.S)])
    infile.close()
    if matches >= p_times:
        p_test_function_called['pass'] = True
    else:
        p_test_function_called['points'] = 0  # ???
        p_filename_data = read_file_contents(p_filename)
        p_test_function_called["fail_message"] += "Found this many matches: " + str(matches) + \
                                                  " of objects of class type:" + p_class_name + \
                                                  " in file with this data: <br> " + p_filename_data
    return p_test_function_called


def function_called(p_filename, p_function_name, p_times, *, points=0):
    """
    tests to see if function is called p_num of times
    :param p_filename: contents of python code
    :param p_function_name: function name to look for
    :param p_times: number of times you are calling
    :param points:  points it is worth
    :return:
    """
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    import re
    p_test = {"name": "Testing that there is a function " + p_function_name +
                      " that gets called in the main program at least " +
                      str(p_times) + " times.  (" + str(points) + " points).<br>"
                      + " <br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>"
                              " There is a function " + p_function_name +
                              " that gets called in the main program (i.e. not part of a function). "
                              "<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5>"
                              "  The function " + p_function_name +
                              " is NOT called in the main program enough times. <br>"
                              " If this doesn't make sense, look in the presentation for 3.020, "
                              "examples 1-6 to see calling functions in action.  <br>",
              "score": points
              }
    regex = r"(?<!def \s)" + p_function_name
    with open(p_filename) as infile:
        matches = len([1 for line in infile.readlines() if re.search(regex, line, re.X | re.M | re.S)])
    infile.close()

    if matches >= p_times:
        p_test['pass'] = True
        p_test['points'] = points
    else:
        p_test['score'] = 0
        p_filename_data = read_file_contents(p_filename)
        p_test["fail_message"] += "Found this many function calls: " + str(matches) + \
                                  " <br>of " + p_function_name + \
                                  " in file with this data: <br> " + p_filename_data
    help_link = 'https://docs.google.com/presentation/d/1cAr1bVWWGVcDKuEqSCYBbla7_pglpbt-5hsFOxPcmE8/' \
                'edit#slide=id.g8e77a2c1ac_0_0'
    p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                              '<br>See this link for help answering this question: ' \
                              ' <a href="' + help_link + '" target="_blank">link</a>'

    return p_test


def find_questions(p_filename_data, p_num, p_points, description='', help_link=''):
    """
    Finds number of questions in code
    :param p_filename_data: contains the entire python file (string)
    :param p_num: minimum number of times you want to find a question (int).
                              i.e. you require minimum 3 strings that look like blah = input('question here')
    :param p_points: - number of points this question is worth
    :param description: description of the problem (str)
    :param help_link: link to help in case of fail
    :return: test dictionary
    """

    import re

    matches = len(re.findall(r".{1,2} \s* = \s* \(* input\(", p_filename_data, re.X | re.M | re.S))
    matches_int = len(re.findall(r".{1,2} \s* = \s* \(* int\( input\(", p_filename_data, re.X | re.M | re.S))
    matches_float = len(re.findall(r".{1,2} \s* = \s* \(* float\( input\(", p_filename_data, re.X | re.M | re.S))

    p_test_find_questions = {"name": "Testing that there are least " + str(p_num) + " question(s) (" + str(p_points) +
                                     " points)<br>",
                             "pass": True,
                             "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                                             "Code asks at least " + str(p_num) + " questions ",
                             "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                             "Code does not ask at least " + str(p_num) + " questions .<br>" +
                                             "You need to save your answer in a variable.  That is, "
                                             "input('my question') will not score, you need"
                                             " answer = input('my question')<br>",
                             "points": 0
                             }
    if matches < p_num and matches_int < p_num and matches_float < p_num:
        p_test_find_questions['pass'] = False
        p_test_find_questions['fail_message'] += "<br>  Found this many questions: " + \
                                                 str(matches) + \
                                                 '.<br><br> See this link for help answering this question: ' \
                                                 ' <a href="https://docs.google.com/presentation/' \
                                                 'd/1R1jJfHfXgtZAjrYpC8lKL7uG4VW5Ujy8h3TawLWab3A/' \
                                                 'edit#slide=id.g3fba4a57ae_0_0" target="_blank">link</a>'

    else:
        p_test_find_questions['points'] = p_points
    if description:
        p_test_find_questions['name'] = 'Find question test: ' + description + ' (' + str(p_points) + ' points)'
    if help_link:
        p_test_find_questions['fail_message'] += '<h5 style=\"color:purple;\">' \
                                                 '<br>See this link for help answering this question: ' \
                                                 ' <a href="' + help_link + '" target="_blank">link</a></h5>'
    return p_test_find_questions


def find_list_items(p_filename_data, p_string):
    """
    Looks for a string
    :param p_filename_data: contains the entire python file (string)
    :param p_string: The list you are looking for (string)
    :return: A list, items are items in the list you are searching for
    """
    import re
    find_this_list = p_string + r' \s* = \s* \[ ([^\]]+) \] '
    print(find_this_list)
    print(p_filename_data)
    p_search_object = re.search(find_this_list, p_filename_data, re.X | re.M | re.S)
    match = p_search_object.group(1)
    print('initial match ' + str(match))
    new_item = ''
    on_off = -1
    reconstructed_list = []
    quotation = ''

    for letter in str(match):  # TODO consider using ast.literal_eval()?
        if letter == '"' or letter == "'":
            if on_off == -1:
                on_off *= -1  # turn on
                quotation = letter
                new_item = ''
            else:
                if quotation == letter:
                    on_off *= -1  # turn off
                    reconstructed_list.append(new_item)
                else:
                    new_item += letter
        else:
            new_item += letter

    print("reconstructed list")
    print(reconstructed_list)

    return reconstructed_list


if __name__ == "__main__":
    # find_function('/tmp/abc.py', 'hello', 3)
    # asdf = "[a-z]{1,2} \s* = \s* input \( [^']+ \) "
    # m_filename_data = '# print("yes") abc  = input(asdf) input(asdf) wish1 =' \
    #                 ' input("give me wish")n wish2 = input("give me wish")n wish3 = input("give me wish")  ' \
    #                 'print("your wishes are " + wish1 + ", " + wish2 + ", " + wish3)# Joe helped me'
    #
    # abc = find_string(m_filename_data, asdf, 1, 0)
    # print(abc)
    # asdf = '(verb|noun|adjective|adverb|preposition) .+ \s* = \s* input\('
    # m_filename_data = 'print("asdf") verb = input("yes") noun = input("yes") adjective = input("yes") ' \
    #                 'noun3 = input("yes") adjective10 = input("yes") print(verb + " " + ' \
    #                 'noun + " .?! " + adjective + " noun" + noun3 + " " + adjective10) # joe helped me '
    # abc = find_string(m_filename_data, asdf, 5, 0)
    # print(abc)
    m_filename_data = "hello world    prizes = [\"asdf\", '23', 'llll']"
    # abc = find_list_items('prizes \s* = \s* \[ (.+) \]', m_filename_data)
    abc = find_list_items(m_filename_data, r'prizes \s* = \s* \[ (.+) \]')

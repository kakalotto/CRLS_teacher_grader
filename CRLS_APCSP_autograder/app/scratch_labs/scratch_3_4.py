def find_day_of_week(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import one_custom_block
    p_test = {"name": "Checking that there is a custom block called 'day_of_week' with one input parameter"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'day_of_week' with one input parameter named 'day'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'day_of_week' with one input parameter named 'day'."
                              "<br>"
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    [test_block, custom_block_name] = one_custom_block(p_scripts, 'day_of_week')
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    key_ok = True
    for key in custom_block_name.keys():
        if len(re.findall(r'VARIABLE', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Custom block 'day_of_week' needs to have exactly one input parameter.  <br>" \
                                      "Found this many: " + str(len(re.findall(r'VARIABLE', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
        if len(re.findall(r'VARIABLE_day', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Custom block 'day_of_week' needs to have exactly one input parameter named " \
                                      "<i> exactly </i>'day'." \
                                      " <br>" \
                                      "Found this many: " + str(len(re.findall(r'VARIABLE_day', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
    if test_block['pass'] and key_ok:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def if_ifelse(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import one_custom_block

    p_test = {"name": "Checking that the day_of_week custom block with one argument has good use of if/ifelse"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The day_of_week custom block with one argument has good use of if/ifelse.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The day_of_week custom block with one argument does not appear to have good use "
                              "of if/ifelse, which leads to inefficient code.<br>",
              "points": 0
              }
    [test_block, custom_block_dict] = one_custom_block(p_scripts, 'day_of_week')
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    pass_ifelse = False
    for key in custom_block_dict.keys():
        script = custom_block_dict[key]
        match_ifelse = re.findall(r"control_if_else'", str(script), re.X | re.M | re.S)
        num_ifelses = len(match_ifelse)
        if num_ifelses < 6:
            match_if = re.findall(r"control_if'", str(script), re.X | re.M | re.S)
            num_ifs = len(match_if)
            if num_ifs >= 6:  # did it all with ifs
                p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                          'There are 6 or more if statements.  ' \
                                          'This block can be written more efficiently ' \
                                          'with if/elses. <br>' \
                                          'See presentation for an example of nested if/elses: ' \
                                          '<a href="https://docs.google.com/presentation/d/1hub7R1qTCGTqgKRP_gz' \
                                          'Z-j9dJ3st7HM4_hmeBJlxkds/edit#slide=id.g739f674ef6_2_27">' \
                                          'link to page in presentation</a><br>' \
                                          'Found many ifs (of any type including if/else): ' + str(num_ifs) + '<br>' \
                                          "Found this many if/else: " + str(num_ifelses) + '</h5>'
            else:  # less than 6 ifelse, less than6 if.  Fail.
                p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                          'Expect to see at least 6 if/elses - one for each of Su - F and ' \
                                          'the else for Saturday.<br>' \
                                          'See presentation for an example of nested if/elses: ' \
                                          '<a href="https://docs.google.com/presentation/d/1hub7R1qTCGTqgKRP_gz' \
                                          'Z-j9dJ3st7HM4_hmeBJlxkds/edit#slide=id.g739f674ef6_2_27">' \
                                          'link to page in presentation</a><br>' \
                                          'Found many ifs (of any type including if/else): ' + str(num_ifs) + '<br>' \
                                          "Found this many if/else: " + str(num_ifelses) + \
                                          '<br></h5>'
        else:  # more than 6 if/else.  Good
            pass_ifelse = True
    if pass_ifelse:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


# This can be refactored along with find_triangle and happy_birthday from 3.2
def find_min(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import one_custom_block
    p_test = {"name": "Checking that there is a custom block called 'min' with two input parameters named exactly "
                      "'number1' an 'number2'"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'min' with two input parameters named 'number1' and"
                              " 'number2'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'min' with two input parameters named 'number1' "
                              "and 'number2'."
                              "<br>"
                              "The script must be named EXACTLY 'min' with exactly two input parameters named "
                              "'number1' and 'number2'.<br>"
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    [test_block, custom_block_name] = one_custom_block(p_scripts, 'min')
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    key_ok = True
    for key in custom_block_name.keys():
        if len(re.findall(r'VARIABLE', key)) != 2:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Custom block 'min' needs to have exactly two input parameters.  <br>" \
                                      "Found this many: " + str(len(re.findall(r'VARIABLE', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
        if len(re.findall(r'VARIABLE_number1', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Custom block 'min' needs to have exactly two input parameters. " \
                                      "The first one must be named <i> exactly </i>number1" \
                                      " <br>" \
                                      "Found this many of number1: " + \
                                      str(len(re.findall(r'VARIABLE_number1', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
        if len(re.findall(r'VARIABLE_number2', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Custom block 'min' needs to have exactly two input parameters. " \
                                      "The sedond one must be named <i> exactly </i>number2" \
                                      " <br>" \
                                      "Found this many of number2: " + \
                                      str(len(re.findall(r'VARIABLE_number2', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
    if test_block['pass'] and key_ok:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def minif_ifelse(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import one_custom_block

    p_test = {"name": "Checking that the min custom block with two input parameters named exactly"
                      "'number1' and 'number2' has good use of if/ifelse"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The the min custom block with two input parameters named exactly"
                              "'number1' and 'number2' has good use of if/ifelse.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The the min custom block with two input parameters 'number1' and 'number2'"
                              "does not appear to have good use "
                              "of if/ifelse.<br>",
              "points": 0
              }
    [test_block, custom_block_dict] = one_custom_block(p_scripts, 'min')
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    pass_ifelse = False
    for key in custom_block_dict.keys():
        script = custom_block_dict[key]
        match_ifelse = re.findall(r"control_if_else'", str(script), re.X | re.M | re.S)
        num_ifelses = len(match_ifelse)
        if num_ifelses < 2:
            match_if = re.findall(r"control_if'", str(script), re.X | re.M | re.S)
            num_ifs = len(match_if)
            if num_ifs >= 2:  # did it all with ifs
                p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                          'There are 2 or more if statements.  ' \
                                          'This block can be written more efficiently ' \
                                          'with if/elses. <br>' \
                                          'See presentation for an example of nested if/elses: ' \
                                          '<a href="https://docs.google.com/presentation/d/1hub7R1qTCGTqgKRP_gz' \
                                          'Z-j9dJ3st7HM4_hmeBJlxkds/edit#slide=id.g739f674ef6_2_27">' \
                                          'link to page in presentation</a><br>' \
                                          'Found many ifs (of any type including if/else): ' + str(num_ifs) + '<br>' \
                                          "Found this many if/else: " + str(num_ifelses) + '</h5>'
            else:  # less than 3 ifelse, less than6 if.  Fail.
                p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                          'Expect to see at least 2 if/elses - one if for number1 is the minimum,' \
                                          'one if for number2 is the minimum, and the ' \
                                          'else for if number1 = number2.<br>' \
                                          'See presentation for an example of nested if/elses: ' \
                                          '<a href="https://docs.google.com/presentation/d/1hub7R1qTCGTqgKRP_gz' \
                                          'Z-j9dJ3st7HM4_hmeBJlxkds/edit#slide=id.g739f674ef6_2_27">' \
                                          'link to page in presentation</a><br>' \
                                          'Found many ifs (of any type including if/else): ' + str(num_ifs) + '<br>' \
                                          "Found this many if/else: " + str(num_ifelses) + \
                                          '<br></h5>'
        else:  # more than 3 if/else.  Good
            pass_ifelse = True
    if pass_ifelse:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_distance(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import one_custom_block
    p_test = {"name": "Checking that there is a custom block called 'distance' with two input parameters"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'distance' with two input parameters named 'x2' and"
                              " 'y2'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'distance' with two input parameters named 'y2' "
                              "and 'y22'."
                              "<br>"
                              "The script must be named EXACTLY 'distance' with exactly two input parameters named "
                              "'x2' and 'y2'.<br>"
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    [test_block, custom_block_name] = one_custom_block(p_scripts, 'distance')
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    key_ok = True
    for key in custom_block_name.keys():
        if len(re.findall(r'VARIABLE', key)) != 2:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Custom block 'distance' needs to have exactly two input parameters.  <br>" \
                                      "Found this many: " + str(len(re.findall(r'VARIABLE', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
        if len(re.findall(r'VARIABLE_x2', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Custom block 'distance' needs to have exactly two input parameters. " \
                                      "The first one must be named <i> exactly </i>x2" \
                                      " <br>" \
                                      "Found this many of x2: " + \
                                      str(len(re.findall(r'VARIABLE_x2', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
        if len(re.findall(r'VARIABLE_y2', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Custom block 'distance' needs to have exactly two input parameters. " \
                                      "The second one must be named <i> exactly </i>y2" \
                                      " <br>" \
                                      "Found this many of y2: " + \
                                      str(len(re.findall(r'VARIABLE_y2', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
    if test_block['pass'] and key_ok:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


# def find_between(p_scripts, p_points):
#     """
#     :param p_scripts: json data from file, which is the code of the scratch file. (dict)
#     :param p_points: Number of points this test is worth (int)
#     :return: The test dictionary
#     """
#     from CRLS_APCSP_autograder.app.scratch_labs.scratch import procedure_exists
#     p_test = {"name": "Checking that there is a custom block called 'between' with three input parameters"
#                       " (" + str(p_points) + " points)<br>",
#               "pass": False,
#               "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
#                               "There is a custom block called 'between' with three input parameters named 'number1' and"
#                               " 'number2' and 'number3'.<br>",
#               "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
#                               "There is not a custom block called 'between' with three input parameters named"
#                               " 'number1' "
#                               "and 'number2' and 'number3'."
#                               "<br>"
#                               "The script must be named EXACTLY between with exactly three input parameters named "
#                               "'number1' and 'number2' and 'number3'."
#                               "Capitalization and using the underscore matter.<br>",
#               "points": 0
#               }
#     test_procedure = procedure_exists('between %s %s %s', p_scripts)
#     if test_procedure:
#         p_test['pass'] = True
#         p_test['points'] += p_points
#     return p_test


def between_works_equal(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the between custom block with three input parameters works when number1 "
                      "is EQUAL to number2 or number3"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The between custom block with three input parameters works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The between custom block with three input parameters does not appear to work in this "
                              "scenario.<br>"
                              "Is the input parameters named 'number1', 'number2', 'number3'?<br>"
                              "BE SURE INPUT PARAMETER IS NAMED CORRECTLY  OTHERWISE THIS TEST BREAKS.<br>"
                              "The script must say 'True' exactly (capital T, lowercase everything else).<br>",
              "points": 0
              }
    if 'between %s %s %s' in p_scripts.keys():
        print("ppp STARTING")
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 5, "number2": 5, "number3": 2})
        script = p_scripts['between %s %s %s']
        day_success_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1 = match_string(r'^True', sprite.say_history)
        if test_1['pass'] is False:
            p_test['fail_message'] += "Called custom block 'between' with number1 = 5, number2 = 5, number3 = 2<br>" \
                                      "Expect 'True', got this:<br>" + sprite.say_history

        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 5, "number2": 6665, "number3": 5})
        day_success_2 = do_sprite(sprite, script, True)

        test_2 = match_string(r'^True', sprite.say_history)
        if test_2['pass'] is False:
            p_test['fail_message'] += "Called custom block 'between' with number1 = 5, " \
                                      "number2 = 6665, number3 = 5<br>" \
                                      "Expect 'True', got this:<br>" + sprite.say_history
        if day_success_1 and day_success_2 and test_1['pass'] and test_2['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points
    return p_test


def between_works_unequal(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from app.scratch_labs.scratch_2_2 import brickLayer, do_sprite
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string

    p_test = {"name": "Checking that the between custom block with three input parameters works when number1 "
                      "is NOT equal to number2 or number3"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The between custom block with three input parameters works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The between custom block with three input parameters does not appear to work in this "
                              "scenario.<br>"
                              "Is the input parameters named 'number1', 'number2', 'number3'?<br>"
                              "BE SURE INPUT PARAMETER IS NAMED CORRECTLY  OTHERWISE THIS TEST BREAKS.<br>"
                              "The script must say 'True' exactly (capital T, lowercase everything else)"
                              "or else 'False' exactly (capital F, lowercase everything else).<br>",
              "points": 0
              }
    if 'between %s %s %s' in p_scripts.keys():
        print("ppp STARTING")
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 1, "number2": 2, "number3": 3})
        print("aaa test 1 unequals variables {}".format(sprite.variables))

        script = p_scripts['between %s %s %s']
        between_success_1 = do_sprite(sprite, script, True)
        print("VALHALLA {}".format(sprite.say_history))
        test_1 = match_string(r'^False', sprite.say_history)
        if test_1['pass'] is False:
            p_test['fail_message'] += "Called custom block 'between' with number1 = 1, number2 = 2, number3 = 3<br>" \
                                      "Expect 'False', got this:<br>" + sprite.say_history + "<br>"

        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 1, "number2": 3, "number3": 2})
        print("aaa test 2 unequals variables {}".format(sprite.variables))

        between_success_2 = do_sprite(sprite, script, True)
        test_2 = match_string(r'^False', sprite.say_history)
        if test_2['pass'] is False:
            p_test['fail_message'] += "Called custom block 'between' with number1 = 1, number2 = 3, number3 = 2<br>" \
                                      "Expect 'False', got this:<br>" + sprite.say_history + "<br>"

        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 2, "number2": 1, "number3": 3})
        print("aaa test 3 unequals variables {}".format(sprite.variables))
        between_success_3 = do_sprite(sprite, script, True)
        test_3 = match_string(r'^True', sprite.say_history)
        if test_3['pass'] is False:
            p_test['fail_message'] += "Called custom block 'between' with number1 = 2, number2 = 1, number3 = 3<br>" \
                                      "Expect 'True', got this:<br>" + sprite.say_history + "<br>"

        print("test4")
        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 2, "number2": 3, "number3": 1})
        print("aaa test 4 unequals variables {}".format(sprite.variables))
        between_success_4 = do_sprite(sprite, script, True)
        test_4 = match_string(r'^True', sprite.say_history)
        print("test4 say history {}".format(sprite.say_history))
        if test_4['pass'] is False:
            p_test['fail_message'] += "Called custom block 'between' with number1 = 2, number2 = 3, number3 = 1<br>" \
                                      "Expect 'True', got this:<br>" + sprite.say_history + "<br>"

        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 3, "number2": 1, "number3": 2})
        print("aaa test 5 unequals variables {}".format(sprite.variables))
        between_success_5 = do_sprite(sprite, script, True)
        test_5 = match_string(r'^False', sprite.say_history)
        if test_5['pass'] is False:
            p_test['fail_message'] += "Called custom block 'between' with number1 = 3, number2 = 1, number3 = 2<br>" \
                                      "Expect 'True', got this:<br>" + sprite.say_history + "<br>"

        sprite = brickLayer(0, 0, 0, pendown=False, variables={"number1": 3, "number2": 2, "number3": 1})
        print("aaa test 6 unequals variables {}".format(sprite.variables))
        between_success_6 = do_sprite(sprite, script, True)
        test_6 = match_string(r'^False', sprite.say_history)
        if test_6['pass'] is False:
            p_test['fail_message'] += "Called custom block 'between' with number1 = 3, number2 = 2, number3 = 1<br>" \
                                      "Expect 'True', got this:<br>" + sprite.say_history + "<br>"

        if between_success_1 and between_success_2 and between_success_3 and between_success_4 and \
            between_success_5 and between_success_6 and test_1['pass'] and test_2['pass'] and test_3['pass'] and \
                test_4['pass'] and test_5['pass'] and test_6['pass']:
            p_test['pass'] = True
            p_test['points'] += p_points

    return p_test
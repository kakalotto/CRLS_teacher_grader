def python_3_011_1(p_filename_data, p_points):
    """
    Tests to see if there are ifs or elifs (more than 3) in code.  If so, not efficient.
    :param p_filename_data: large string with data (usually the python file)
    :param p_points: Number of points for this test (int)
    :return:  a dictionary of the test
    """
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_if

    # test if, check for max 3 if statement
    test_if = find_if(p_filename_data, 3, 1, minmax='max')

    # test elif, check for max 3 if statement
    test_elif = find_if(p_filename_data, 3, 1, minmax='max')

    test = {'name': "Testing efficiency.  Do NOT want to have a big if/elif/else.<br>"
                    "If you have a variable x which is a number of item in list,"
                    " printing list[x-1] directly will get you the correct item.<br>"
                    "A big if/elif/elif/elif etc.... will scale poorly as your list gets huge."
                    "<br>  If this does not make sense, ask a neighbor or the teacher.",
            "pass": True,
            "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  Did not find a ton of ifs or elifs.<br>",
            'fail_message': "<h5 style=\"color:red;\">Fail.</h5> "
                            "Code has more than 3 ifs or elifs.<br>" +
                            "Searched for ifs/elifs in this string:<br> " + p_filename_data + "<br>",
            'points': 0
            }
    if not test_if['pass'] or not test_elif['pass']:
        test['pass'] = False
        help_link = 'https://docs.google.com/presentation/d/115yqVHY0APEvQFTQ0fGNbw81pX4gv4kflTUfco1E_Q8/edit' \
                    '#slide=id.g8c7a63841e_2_0'
        test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                '<br>See this link for help answering this question: ' \
                                '<a href="' + help_link + '" target="_blank">link</a>'
    else:
        test['points'] += p_points
    return test


def python_3_011_2(p_filename, p_filename_data, p_points):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_list_items
    from CRLS_APCSP_autograder.app.python_labs.io_test import _var_filename, _var_dir

    import delegator
    import re

    var_dir = _var_dir()
    var_filename = _var_filename(p_filename, 1)
    cmd = 'python3 ' + p_filename + ' < ' + var_dir + '/' + var_filename

    p_io_test = {"name": "Run the code 300 times.  Through 120 runs, should get at least one of each house "
                         "(10 points) <br>",
                 "pass": True,
                 "pass_message": "<h5 style=\"color:green;\">Pass!</h5> After 120 runs, got at least one of each house",
                 "fail_message": "<h5 style=\"color:red;\">Fail.</h5> Autograder ran the code 120 times "
                                 "and expects to see each of the houses at least once.<br>"
                                 "For example, if you have 7 houses in your list, after 120 runs, every house should "
                                 "print at least once. <br>",
                 "points": 0,
                 }

    houses = find_list_items(p_filename_data, 'houses')

    answers = []
    # print("STARTING")
    for x in range(110):

        c = delegator.run(cmd)
        print("run " + c.out)
        if c.err:
            p_io_test["fail_message"] += "<h5 style=\"color:purple;\">A run crashed." \
                                         "<br>Error given was this: " + str(c.err) + "</h5>"
            break

        for house in houses:
            if re.search(house, c.out):
                answers.append(house)

    #  print("houses " + str(houses))
    #  print("answers" + str(answers))
    for house in houses:
        if house not in answers:
            p_io_test['pass'] = False
            if not c.err:
                p_io_test['fail_message'] += "Did not find this house in 120 runs of answers: " + house + ". <br>"
    if p_io_test['pass']:
        p_io_test['points'] += p_points
    help_link = 'https://docs.google.com/presentation/d/18ubdbsuqCXeJLhD-CrW-AzjJ-5sNT9TMHs1NUqQhXZ4/' \
                'edit#slide=id.g8c389caccd_3_0'
    p_io_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                 '<br>See this link for help answering this question: ' \
                                 ' <a href="' + help_link + '" target="_blank">link</a>'
    return p_io_test

# at some point, refactor find_happy_birthday, find_draw_triangle, find_day_of_week, find_min


def press_one(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string, unique_coordinates, is_square, one_event
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2  import brickLayer, do_sprite

    p_test = {"name": "Checking that there is a script that has 'when 1 key is pressed' that draws a square"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when 1 key is pressed' that draws a "
                              "square using repeats.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when 1 key is pressed' that draws a "
                              "square using repeats.<br>",
              "points": 0
              }
    [test_one_one, one_script] = one_event(p_scripts, r"'event_whenkeypressed',\s'1'")
    if test_one_one['pass'] is False:
        p_test['fail_message'] += test_one_one['fail_message']
        return p_test
    test_repeat = match_string(r"'control_repeat',\s'4'", one_script)
    if test_repeat['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">Did not find a repeat block that repeats the expected " \
                                  "number of times for a square.<br>" \
                                  'It will look a little like this: <a href=' \
                                  '"https://docs.google.com/presentation/d/1W3bmLtRCv99HlsSGPZmGUvDcBEbi334iwh' \
                                  'AGibJD7aY/edit#slide=id.g3f255390c6_0_0">link</a></h5><br>'
    sprite = brickLayer(0, 0, 0, pendown=True)
    move_success = do_sprite(sprite, one_script, True)
    coords = unique_coordinates(sprite.move_history)
    if len(coords) != 4:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "After pressing 1, sprite should land on 4 unique coordinates, but does not.</h5><br>"
    square = is_square(coords)
    if square is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Failed test for square: " \
                                  "Code expects that you drew a square (4 coordinates, with certain distances apart)" \
                                  "<br></h5>"
    if test_repeat['pass'] and square and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_two(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string, unique_coordinates, is_equilateral_triangle, one_event
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2  import brickLayer, do_sprite

    p_test = {"name": "Checking that there is a script that has 'when 2 key is pressed' that draws an "
                      "equilateral triangle with repeats. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when 2 key is pressed' that draws an "
                              "equilateral triangle with repeats.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when 2 key is pressed' that draws an "
                              "equilateral triangle with repeats.<br>",
              "points": 0
              }
    [test_one_two, two_script] = one_event(p_scripts, "'event_whenkeypressed',\s'2'")
    if test_one_two['pass'] is False:
        p_test['fail_message'] += test_one_two['fail_message']
        return p_test
    test_repeat = match_string(r"'control_repeat',\s'3'", two_script)
    sprite = brickLayer(0, 0, 0, pendown=True)
    if test_repeat['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a repeat block that repeats the expected number of times" \
                                  " for a triangle.<br>" \
                                  'It will look a little like this: <a href=' \
                                  '"https://docs.google.com/presentation/d/1W3bmLtRCv99HlsSGPZmGUvDcBEbi334iwhAGib' \
                                  'JD7aY/edit#slide=id.g806810a5d0_2_0">link</a></h5><br>'
    move_success = do_sprite(sprite, two_script, True)
    coords = unique_coordinates(sprite.move_history)
    if len(coords) != 3:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "After pressing 2, sprite should land on 3 unique coordinates, but does not." \
                                  "</h5><br>"
    equilateral = is_equilateral_triangle(coords)
    if equilateral is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Failed test for equilateral triangle (all sides equal length). <br><br>" \
                                  "</h5>"
    if test_repeat['pass'] and equilateral and move_success:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_draw_triangle(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import one_custom_block
    p_test = {"name": "Checking that there is a custom block called 'draw_triangle' with one input parameter.  Input "
                      "parameter must be named 'size'."
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'draw_triangle' with one input parameter;   "
                              "input parameter must be named exactly 'size'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'draw_triangle' with one input parameter named size."
                              "<br> "
                              "Capitalization and using the underscore matter.<br>"
                              "<h5 style=\"color:purple;\"> "
                              'Link to a similar example: <a href="https://docs.google.com/presentation/d/14BGDnhzYy'
                              'NK6ON0ouAyyo3Q-T7VpJO2FLC0iD_0p53U/edit#slide=id.g45e5e0afb0_0_0" target="_blank">'
                              'link to page in presentation</a><br></h5>',
              "points": 0
              }
    [test_block, custom_block_name] = one_custom_block(p_scripts, 'draw_triangle')
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    key_ok = True
    for key in custom_block_name.keys():
        if len(re.findall(r'VARIABLE', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "custom block 'draw_triangle' needs to have exactly one input parameter.  <br>" \
                                      "Found this many input parameters: " + str(len(re.findall(r'VARIABLE', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
        if len(re.findall(r'VARIABLE_size', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "custom block 'draw_triangle' needs to have exactly one input parameter named " \
                                      "<i> exactly </i>'size'." \
                                      " <br>" \
                                      "Found this many input parameters named 'size': " \
                                      "" + str(len(re.findall(r'VARIABLE_size', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
    if test_block['pass'] and key_ok:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def draw_triangle_works(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2  import brickLayer, do_sprite
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import unique_coordinates, is_equilateral_triangle, distance

    p_test = {"name": "Checking that the draw_triangle custom block with one input parameter named exactly 'size' works"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The draw_triangle custom block with one input parameter named exactly 'size' works.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The draw_triangle custom block with one input parameter named exactly 'size' "
                              "does not appear to work.",
              "points": 0
              }

    test_run_one = False
    test_run_two = False
    move_success_1 = False
    move_success_2 = False
    found_custom_block = False
    for key in p_scripts.keys():
        search_this = r"^draw_triangle \s VARIABLE_size ($|\s)"
        if re.search(search_this, key, re.X | re.M | re.S):
            found_custom_block = True
            sprite = brickLayer(0, 0, 0, pendown=True, variables={"size": 60})
            script = p_scripts[key]
            print("iii script {}".format(script))
            move_success_1 = do_sprite(sprite, script, True)
            coords = unique_coordinates(sprite.move_history)
            print("YES COCORDS" + str(coords))
            if len(coords) != 3:
                p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                          "draw_triangle custom block should move and land on 3 unique coordinates," \
                                          " but does not.  <br>" \
                                          "Found this many coordinates: " + str(len(coords)) + \
                                          "<br>If your angles are incorrect for a triangle, you will not end up" \
                                          "where you started and it will land on 4 coordinates.</h5>"
                print("COORDS" + str(coords))
                return p_test
            equilateral = is_equilateral_triangle(coords)
            if equilateral is False:
                p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                          "draw_triangle custom block should create equilateral triangle but does " \
                                          "not.<br></h5>"
            first_move_distance = distance(coords[0], coords[1])
            if abs(60 - first_move_distance) > 60 * 0.01:
                p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                          "Distance between first and second move should be around 60 steps if I call" \
                                          " block with input of 60. <br> Instead, it's " \
                                          "this distance: " + str(first_move_distance) + \
                                          "<br>This can happen if you hard-coded your move instead of " \
                                          "using the size variable.<br>" \
                                          "See this link: " \
                                          '<a href="https://docs.google.com/presentation/d/14BGDnhzYyNK6ON0ouAy' \
                                          'yo3Q-T7VpJO2FLC0iD_0p53U/edit#slide=id.g45e5e0afb0_0_0" target="_blank">' \
                                          ' Link to Google slide with square example.</a></h5>'
            else:
                test_run_one = True
                sprite = brickLayer(0, 0, 0, pendown=True, variables={"size": 100})
                script = p_scripts[key]
                move_success_2 = do_sprite(sprite, script, True)
                coords = unique_coordinates(sprite.move_history)
                second_move_distance = distance(coords[0], coords[1])
                if abs(100 - second_move_distance) > 100 * 0.01:
                    p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                              "Distance between first and second move should be around 100 steps if" \
                                              " I call" \
                                              "block with input of 100. <br> Instead, it's " \
                                              "this distance:" + str(second_move_distance) + \
                                              "<br>This can happen if you hard-coded your move instead of " \
                                              "using the size variable.<br>" \
                                              " See this link:  " \
                                              '<a href="https://docs.google.com/presentation/d/14BGDnhzYyNK6ON0' \
                                              'ouAyyo3Q-T7VpJO2FLC0iD_0p53U/edit#slide=id.g45e5e0afb0_0_0" ' \
                                              'target="blank">' \
                                              'Link to Google slide with square example.</a></h5>'
                else:
                    test_run_two = True
    if found_custom_block is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\"> " \
                                  "Does not look like there is a custom block draw_triangle with one input parameter " \
                                  "named exactly 'size'.</h5>"
    if move_success_1 and move_success_2 and equilateral and test_run_one and test_run_two:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_three(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string, one_event
    p_test = {"name": "Checking that there is a script 'when 3 key is pressed' that calls draw_triangle custom block "
                      "with one argument. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script 'when 3 key is pressed' that calls draw_triangle custom block "
                              "with one argument.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script 'when 3 key is pressed' that calls draw_triangle custom block "
                              "with one argument.<br>"
                              "The script must be named EXACTLY draw_triangle with exactly one argument.<br>",
              "points": 0
              }
    [test_one_three, three_script] = one_event(p_scripts, r"'event_whenkeypressed',\s'3'")
    if test_one_three['pass'] is False:
        p_test['fail_message'] += test_one_three['fail_message']
        return p_test
    test_three = match_string(r"'event_whenkeypressed', \s* '3'], .*? 'draw_triangle .*? ([0-9]|VARIABLE|sensing)",
                              three_script)
    if test_three['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a 'when 3 pressed' followed by a 'draw_triangle'.<br>" \
                                  "draw_triangle needs to have an argument (i.e. draw_triangle 50 not " \
                                  "draw_triangle (blank) )<br>" \
                                  "See presentation for an example of using a custom block: " \
                                  '<a href=' \
                                  '"https://docs.google.com/presentation/d/14BGDnhzYyNK6ON0ouAyyo3Q-' \
                                  'T7VpJO2FLC0iD_0p53U' \
                                  '/edit#slide=id.g7363a6f889_0_0">link</a> </h5>'
    if test_three['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_happy_birthday(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import one_custom_block
    p_test = {"name": "Checking that there is a custom block called 'happy_birthday' with one input parameter."
                      "Input parameter must be named exactly 'name' "
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called 'happy_birthday' with one input parameter;"
                              "Input parameter must be named exactly 'name'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a custom block called 'happy_birthday' with exactly one input parameter "
                              "named 'name'."
                              "Capitalization and using the underscore matter.<br>",
              "points": 0
              }
    [test_block, custom_block_name] = one_custom_block(p_scripts, 'happy_birthday')
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    key_ok = True
    for key in custom_block_name.keys():
        if len(re.findall(r'VARIABLE', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "custom block 'happy_birthday' needs to have exactly one input parameter  <br>" \
                                      "Found this many: " + str(len(re.findall(r'VARIABLE', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
        if len(re.findall(r'VARIABLE_name', key)) != 1:
            key_ok = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "custom block 'happy_birthday' needs to have exactly one input parameter named " \
                                      "<i> exactly </i>'name'." \
                                      " <br>" \
                                      "Found this many: " + str(len(re.findall(r'VARIABLE_size', key))) + \
                                      "<br>Please edit custom block and resubmit.</h5>"
    if test_block['pass'] and key_ok:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_four(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string, one_event
    p_test = {"name": "Checking that there is a script 'when 4 key is pressed' that calls happy birthday custom block "
                      "with one argument. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script 'when 4 key is pressed' that calls happy_birthday custom block "
                              "with one argument.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script 'when 4 key is pressed' that calls happy_birthday custom block "
                              "with one argument.<br>"
                              "The script must be named EXACTLY happy_birthday with exactly one input parameter.",
              "points": 0
              }
    [test_one_four, four_script] = one_event(p_scripts, "'event_whenkeypressed',\s'4'")
    if test_one_four['pass'] is False:
        p_test['fail_message'] += test_one_four['fail_message']
        return p_test
    test_four = match_string(r"'event_whenkeypressed', \s* '4'], .*? 'happy_birthday .*? [a-zA-Z?\.!]",
                             four_script)
    print("four script {} ".format(four_script))
    if test_four['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a 'when 4 pressed' followed by a 'happy_birthday'.<br>" \
                                  "happy_birthday needs to have an argument (i.e. happy_birthday Mr. Kann not " \
                                  "happy_birthday(blank) )<br>" \
                                  "See presentation for an example of using a custom block: " \
                                  '<a href=' \
                                  '"https://docs.google.com/presentation/d/14BGDnhzYyNK6ON0ouAyyo3Q-' \
                                  'T7VpJO2FLC0iD_0p53U' \
                                  '/edit#slide=id.g7363a6f889_0_0">link</a> </h5>'
    if test_four['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test

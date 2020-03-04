def min_two_sprites(p_json, p_points):
    """
    Checks that there are at least two sprites in the code
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: number of points this is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import count_sprites
    num_sprites = count_sprites(p_json)
    p_test = {"name": "Checking that there is at least two sprites (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found at least two sprites in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have at least two sprites.<br>",
              "points": 0
              }
    if num_sprites >= 2:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
        p_test['fail_message'] += "Found this many sprites: " + str(num_sprites)
    return p_test


def show_and_hide(p_json, p_points):
    """
    Checks that there is a sprite that hides and shoes
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: number of points this is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that there is hiding and showing of sprites going on (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found hiding and showing of sprites!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have hiding and showing of sprites.<br>",
              "points": 0
              }
    test_show = match_string(r'looks_show', p_json)
    if test_show['pass'] is False:
        p_test['fail_message'] +=  "<h5 style=\"color:purple;\">Did not find a show block anywhere in the code,</h5> "
    test_hide = match_string(r'looks_hide', p_json)
    if test_hide['pass'] is False:
        p_test['fail_message'] +=  "<h5 style=\"color:purple;\">Did not find a hide block anywhere in the code.</h5> "
    if test_show['pass'] and test_hide['pass']:
        p_test['points'] += p_points
    else:
        p_test['pass'] = False
    return p_test


def find_move(p_json, p_points):
    """
    Checks that there is a sprite that moves
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: number of points this is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that there is a sprite that moves (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found a sprite that moves!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have a sprite that moves.<br> ",
              "points": 0
              }
    test_find_move = match_string(r'(motion_movesteps|motion_glide)', p_json, points=5)
#    print("test move is this")
    print(test_find_move)
    if test_find_move['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">  You need to have either a move or else a glide in the code for one of the sprites</h5>"
        p_test['pass'] = False
#        print("FAILED!!!!")0
    else:
        p_test['points'] += p_points
    return p_test


def find_rotate(p_json, p_points):
    """
    Checks that there is a sprite that rotates or ate least turns
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: number of points this is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that there is a sprite that rotates (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found a sprite that rotates!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have a sprite that rotates.<br> ",
              "points": 0
              }
    test_find_rotate = match_string(r'(motion_turnleft|motion_turnright)', p_json, points=5)
    print(test_find_rotate)
    if test_find_rotate['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">  You need to have a rotate (turn left or turn right)</h5>"
        p_test['pass'] = False
    else:
        p_test['points'] += p_points
    return p_test


def find_changecostume(p_json, p_points):
    """
    Checks that there is a sprite that changes costumes
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: number of points this is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import match_string
    p_test = {"name": "Checking that there is a sprite that changes costume (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found a sprite that changes costume!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not have a sprite that changes costume.<br> ",
              "points": 0
              }
    test_find_costume = match_string(r'(looks_nextcostume|looks_switchcostumeto)', p_json)
    if test_find_costume['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">  You need to have a costume change in a sprite (next costume or switch costume)</h5>"
        p_test['pass'] = False
    else:
        p_test['points'] += p_points
    return p_test



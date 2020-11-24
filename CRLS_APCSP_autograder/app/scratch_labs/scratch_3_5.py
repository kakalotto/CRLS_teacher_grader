def find_hero(p_json, p_points):
    """
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary and scripts of that ditionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_sprite_name, arrange_blocks_v2

    p_test = {"name": "Checking that there is a sprite named exactly 'hero' "
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a sprite named exactly 'hero'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not is a sprite named exactly 'hero'<br>"
                              "See this link for example of how to do it: <a href="
                              '"https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                              'edit#slide=id.g883030db0b_0_14">link</a>',
              "points": 0,
              }
    p_scripts = {}
    if find_sprite_name(p_json, 'hero'):
        p_scripts = arrange_blocks_v2(p_json,  only_this_sprite='hero')
        p_test['pass'] = True
        p_test['points'] += p_points
    return [p_test, p_scripts]


def turn_right(p_scripts, p_points):
    """
    :param p_scripts: Scripts for the hero sprite (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    test1 = find_string_in_script(p_scripts, '35_turn_right_1', p_points)
    test2 = find_string_in_script(p_scripts, '35_turn_right_2', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    else:
        if re.search(r'ou \s are \s supposed \s to \s have \s exactly \s one \s of', test2['fail_message'],
                     re.X | re.M | re.S):
            return test2
        else:
            return test1


def turn_left(p_scripts, p_points):
    """
    :param p_scripts: Scripts for the hero sprite (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    test1 = find_string_in_script(p_scripts, '35_turn_left_1', p_points)
    test2 = find_string_in_script(p_scripts, '35_turn_left_2', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    else:
        if re.search(r'ou \s are \s supposed \s to \s have \s exactly \s one \s of', test2['fail_message'],
                     re.X | re.M | re.S):
            return test2
        else:
            return test1


def animated_walk(p_scripts, p_sprite_name, p_points):
    """
    :param p_scripts: scripts for hero, sprite which is the code of the scratch file. (dict)
    :param p_sprite_name: name of sprite. (string)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    if p_sprite_name == 'hero':
        test1 = find_string_in_script(p_scripts, '35_animated_walk_1', p_points)
        test2 = find_string_in_script(p_scripts, '35_animated_walk_2', p_points)
        test3 = {'pass': False}

    else:
        test1 = find_string_in_script(p_scripts, '35_enemy_animated_walk_1', p_points)
        test2 = find_string_in_script(p_scripts, '35_enemy_animated_walk_2', p_points)
        test3 = find_string_in_script(p_scripts, '35_enemy_animated_walk_3', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    elif test3['pass']:
        return test3
    else:
        if re.search(r'ou \s are \s supposed \s to \s have \s exactly \s one \s of', test2['fail_message'],
                     re.X | re.M | re.S):
            return test2
        else:
            return test1


def layers(p_scripts, p_points):
    """
    :param p_scripts: Scripts for the hero sprite (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    test1 = find_string_in_script(p_scripts, '35_layers_1', p_points)
    test2 = find_string_in_script(p_scripts, '35_layers_2', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    else:
        if re.search(r'ou \s are \s supposed \s to \s have \s exactly \s one \s of', test2['fail_message'],
                     re.X | re.M | re.S):
            return test2
        else:
            return test1


def jumps(p_scripts, p_points):
    """
    :param p_scripts: scripts for hero, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    test1 = find_string_in_script(p_scripts, '35_jump_1', p_points)
    test2 = find_string_in_script(p_scripts, '35_jump_2', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    else:
        return test1


def find_scenery(p_json, p_points):
    """
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_sprite_name, arrange_blocks_v2

    p_test = {"name": "Checking that there is 2 sprites named exactly 'scenery1' and 'scenery2'"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a sprites named exactly 'scenery1' and 'scenery2'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not is sprites named exactly 'scenery1' and 'scenery2'<br>"
                              "See this link for example of how to do it: <a href="
                              '"https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                              'edit#slide=id.g883030db0b_0_14">link</a>',
              "points": 0,
              }
    p_scripts_1 = {}
    p_scripts_2 = {}
    if find_sprite_name(p_json, 'scenery1'):
        p_scripts_1 = arrange_blocks_v2(p_json,  only_this_sprite='scenery1')
    if find_sprite_name(p_json, 'scenery2'):
        p_scripts_2 = arrange_blocks_v2(p_json,  only_this_sprite='scenery2')
    if find_sprite_name(p_json, 'scenery1') and find_sprite_name(p_json, 'scenery2'):
        p_test['pass'] = True
        p_test['points'] += p_points
    return [p_test, p_scripts_1, p_scripts_2]


def sprite2_moves(p_scripts, p_test_name, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_test_name: name of test to run
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    # scenarios:
    # _1 - when key pressed + move X/changex by x
    # _2 - forever + if key pressed + move X/changex by x
    # _3 - when event received +  move X/changex by x
    if p_test_name == '35_scenery1_1':
        test1 = find_string_in_script(p_scripts, '35_scenery1_1', p_points)
        test2 = find_string_in_script(p_scripts, '35_scenery1_2', p_points)
        test3 = find_string_in_script(p_scripts, '35_scenery1_3', p_points)
    elif p_test_name == '35_scenery1_2':
        test1 = find_string_in_script(p_scripts, '35_scenery1_4', p_points)
        test2 = find_string_in_script(p_scripts, '35_scenery1_5', p_points)
        test3 = find_string_in_script(p_scripts, '35_scenery1_6', p_points)
    elif p_test_name == '35_scenery2_1':
        test1 = find_string_in_script(p_scripts, '35_scenery2_1', p_points)
        test2 = find_string_in_script(p_scripts, '35_scenery2_2', p_points)
        test3 = find_string_in_script(p_scripts, '35_scenery2_3', p_points)
    else:
        # p_test_name == '35_scenery2_2':
        test1 = find_string_in_script(p_scripts, '35_scenery2_4', p_points)
        test2 = find_string_in_script(p_scripts, '35_scenery2_5', p_points)
        test3 = find_string_in_script(p_scripts, '35_scenery2_6', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    elif test3['pass']:
        return test3
    else:
        return test2


def scenery_moves_different_rate(p_scripts_scenery1, p_scripts_scenery2, p_points):
    """
    Finds out if scenery moves at different rate
    :param p_scripts_scenery1: scripts from scenery1 (dict)
    :param p_scripts_scenery2: scripts from scenery 2(dict)
    :param p_points: points this is worth (int)
    :return: test dictionary
    """
    import re
    p_test = {"name": "Checking that there is 2 scenery sprites move different rates (only checked move right)'"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is 2 scenery sprites move different rates (only checked move right)<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not 2 sprites moving right at different rates"
                              "<br>",
              "points": 0,
              }

    match_1 = r"(event_whenkeypressed .+? right \s arrow | " \
              r"control_repeat .+? 150 .+? control_if .+? sensing_keypressed .+? sensing_keyoptions .+?" \
              r" right \s arrow|" \
              r"event_whenbroadcastreceived) " \
              r".*? (motion_movesteps|motion_changexby) .*? ([0-9]+) "
    script1_found = False
    scenery1_move = 999
    for script in p_scripts_scenery1:
        match_obj = re.search(match_1, str(p_scripts_scenery1[script]), re.X | re.M | re.S)
        if match_obj:
            script1_found = True
            scenery1_move = match_obj.group(1)
            break

    script2_found = False
    scenery2_move = 999
    for script in p_scripts_scenery2:
        match_obj = re.search(match_1, str(p_scripts_scenery2[script]), re.X | re.M | re.S)
        if match_obj:
            script2_found = True
            scenery2_move = match_obj.group(1)
            break
    if script1_found is False or script2_found is False:
        if script1_found is False:
            p_test['fail_message'] += "<h5 style=\"color:purple;\"> Did not find a move when right arrow pressed for " \
                                      "scenery 1.<br></h5> "
        if script2_found is False:
            p_test['fail_message'] += "<h5 style=\"color:purple;\"> Did not find a move when right arrow pressed for " \
                                      "scenery 2.<br></h5> "
    else:
        if scenery1_move == scenery2_move:
            p_test['pass'] = True
        else:
            p_test['fail_message'] += "<h5 style=\"color:purple;\"> Found that scenery1 and scenery2 did not move" \
                                      " different amounts when right arrow pressed.  <br>" \
                                      "Found this move for scenery1:  " + str(scenery1_move) +\
                                      "Found this move for scenery2:  " + str(scenery2_move) +\
                                      "/h5> "
    return p_test


def rollover_check(p_scripts, p_test_name, p_points):
    """

    :param p_scripts: Scripts from just the sprite of interest
    :param p_test_name: name of the test
    :param p_points: Points that this is worth
    :return: list - test dictionary and the number
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    # scenarios:
    # _1 - when key pressed + move X/changex by x
    # _2 - forever + if key pressed + move X/changex by x
    # _3 - broadcast +  move X/changex by x
    if p_test_name == '35_scenery1_rollover_left':
        test1 = find_string_in_script(p_scripts, '35_scenery1_rollover_1', p_points)
        test2 = find_string_in_script(p_scripts, '35_scenery1_rollover_2', p_points)
        test3 = find_string_in_script(p_scripts, '35_scenery1_rollover_3', p_points)
    elif p_test_name == '35_scenery1_rollover_right':
        test1 = find_string_in_script(p_scripts, '35_scenery1_rollover_4', p_points)
        test2 = find_string_in_script(p_scripts, '35_scenery1_rollover_5', p_points)
        test3 = find_string_in_script(p_scripts, '35_scenery1_rollover_6', p_points)
    elif p_test_name == '35_scenery2_rollover_left':
        test1 = find_string_in_script(p_scripts, '35_scenery2_rollover_1', p_points)
        test2 = find_string_in_script(p_scripts, '35_scenery2_rollover_2', p_points)
        test3 = find_string_in_script(p_scripts, '35_scenery2_rollover_3', p_points)
    elif p_test_name == '35_scenery2_rollover_right':
        test1 = find_string_in_script(p_scripts, '35_scenery2_rollover_4', p_points)
        test2 = find_string_in_script(p_scripts, '35_scenery2_rollover_5', p_points)
        test3 = find_string_in_script(p_scripts, '35_scenery2_rollover_6', p_points)
    else:
        # p_test_name == '35_enemy_rollover_left':
        test1 = find_string_in_script(p_scripts, '35_enemy_rollover_1', p_points)
        test2 = find_string_in_script(p_scripts, '35_enemy_rollover_2', p_points)
        test3 = find_string_in_script(p_scripts, '35_enemy_rollover_3', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    elif test3['pass']:
        return test3
    else:
        return test2


def find_enemy(p_json, p_points):
    """
    :param p_json: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary and scripts of that ditionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_sprite_name, arrange_blocks_v2

    p_test = {"name": "Checking that there is a sprite named exactly 'enemy' "
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a sprite named exactly 'enemy'.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not is a sprite named exactly 'enemy'<br>"
                              "See this link for example of how to do it: <a href="
                              '"https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                              'edit#slide=id.g883030db0b_0_14">link</a>',
              "points": 0
              }
    p_scripts = {}
    if find_sprite_name(p_json, 'enemy'):
        p_scripts = arrange_blocks_v2(p_json,  only_this_sprite='enemy')
        p_test['pass'] = True
        p_test['points'] += p_points
    return [p_test, p_scripts]


def touch_stop(p_scripts_hero, p_scripts_enemy, p_points):
    """
    :param p_scripts_hero: scripts of the hero, which is the code of the scratch file. (dict)
    :param p_scripts_enemy: scripts of the hero, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dic tionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    test1 = find_string_in_script(p_scripts_hero, '35_stop_1', p_points)
    test2 = find_string_in_script(p_scripts_enemy, '35_stop_2', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    else:
        return test1

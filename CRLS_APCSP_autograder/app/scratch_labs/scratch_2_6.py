
def test_top(p_scripts, p_points):
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script, one_event

    test1 = find_string_in_script(p_scripts, '26_top_1', p_points)
    test2 = find_string_in_script(p_scripts, '26_top_2', p_points)
    y = -300  # no pass
    [_, script] = one_event(p_scripts, 'event_whenflagclicked')
    if test1['pass']:
        test_high_enough = re.search(r"'motion_sety', \s+ '(-?[0-9]+)'", str(script), re.X | re.M | re.S)
        if test_high_enough:
            y = test_high_enough.group(1)
        test = test1
    elif test2['pass']:
        test_high_enough = re.search(r"'motion_gotoxy',  .+? ,\s+ '([0-9]+)", str(script), re.X | re.M | re.S)
        if test_high_enough:
            y = test_high_enough.group(1)
        test = test2
    else:
        test3 = test1
        test3['fail_message'] += ' OR ' + test2['fail_message'] + '<br> <h5 style=\"color:purple;\">' \
                                                                  'You only need one of these to pass.<br></h5>'
        return test3
    try:
        int(y)
        if int(y) < 125:
            test['fail_message'] += '<h5 style=\"color:purple;\">Y position of sprite at beginning of code ' \
                                    'needs to be higher than 125.  <br>' \
                                    'Your y was set to this: ' + str(y) + '</h5>'
            test['pass'] = False
    except ValueError:
        test['fail_message'] += 'Broken somehow.  Found a y value of this:' + str(y)
    return test


def test_hit_ground(p_scripts, p_points):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    test1 = find_string_in_script(p_scripts, '26_ground_1', p_points)
    test2 = find_string_in_script(p_scripts, '26_ground_2', p_points)
    test3 = find_string_in_script(p_scripts, '26_ground_3', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    elif test3['pass']:
        return test3
    else:
        test4 = test1
        test4['fail_message'] += ' OR ' + test2['fail_message'] + ' OR ' + test3['fail_message'] +\
                                 '<br> <h5 style=\"color:purple;\"> You only need one of these to pass.<br></h5>'
        return test3


def test_random_x(p_scripts, p_points):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    test1 = find_string_in_script(p_scripts, '26_random_x_1', p_points)
    test2 = find_string_in_script(p_scripts, '26_random_x_2', p_points)
    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    else:
        test3 = test1
        test3['fail_message'] += ' OR ' + test2['fail_message'] + '<br> <h5 style=\"color:purple;\">' \
                                                                  'You only need one of these to pass.<br></h5>'
        return test3


def platform_or_ground(p_scripts, p_points):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_string_in_script

    test1 = find_string_in_script(p_scripts, '26_platform_or_ground_1', p_points)
    test2 = find_string_in_script(p_scripts, '26_platform_or_ground_2', p_points)
    test3 = find_string_in_script(p_scripts, '26_platform_or_ground_3', p_points)

    if test1['pass']:
        return test1
    elif test2['pass']:
        return test2
    elif test3['pass']:
        return test3
    else:
        test = test1
        return test
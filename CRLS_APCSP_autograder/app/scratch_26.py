def route_scratch_2_6(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, find_help, variable_check_no_space, \
        find_string_in_script
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_6 import test_top,  test_hit_ground, test_random_x, \
        platform_or_ground
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=70, score_manual=10)
    test_filename = scratch_filename_test(filename, '2.6')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        [json_data, scripts] = get_scripts_wrapper(filename)
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        if test_spaces['pass'] is False:
            return [user, tests, score_info]
        else:
            tests.append(find_string_in_script(scripts, '26_greenflag_forever', 15))
            tests.append(find_string_in_script(scripts, '26_test_fall', 10))
            tests.append(test_top(scripts, 10))
            tests.append(test_random_x(scripts, 5))
            tests.append(test_hit_ground(scripts, 20))
            tests.append(platform_or_ground(scripts, 5))
            tests.append(find_help(json_data, 5))
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]

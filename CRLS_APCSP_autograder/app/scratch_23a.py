def route_scratch_23a(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, check_num_sprites, find_help, variable_check_no_space, \
        press_greenflag, find_string_in_script, run_script_check_say
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=40, score_manual=10)
    test_filename = scratch_filename_test(filename, '2.3a')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        [json_data, scripts] = get_scripts_wrapper(filename)
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        test_one_sprite = check_num_sprites(json_data, 1)
        tests.append(test_one_sprite)
        if test_spaces['pass'] is False or test_one_sprite['pass'] is False:
            return [user, tests, score_info]
        else:
            tests.append(press_greenflag(scripts, 5))
            tests.append(find_string_in_script(scripts, '23name', 5))
            tests.append(run_script_check_say(scripts, '23a_name_reply', 5))
            tests.append(find_string_in_script(scripts, '23triangle', 5))
            tests.append(find_string_in_script(scripts, '23a_draw_triangle', 5))
            tests.append(find_string_in_script(scripts, '23feel', 5))
            tests.append(run_script_check_say(scripts, '23a_feel_reply', 5))
            tests.append(find_help(json_data, 5))
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]

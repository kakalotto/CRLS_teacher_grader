def route_scratch_3_4(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, find_help, variable_check_no_space, \
        one_sprite, check_straggler_variable_no_space, run_custom_block_check_say
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_3_4  import find_day_of_week, if_ifelse, \
        find_min, find_distance, minif_ifelse
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=70, score_manual=10)
    test_filename = scratch_filename_test(filename, '3.4')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        [json_data, scripts] = get_scripts_wrapper(filename)
        test_one_sprite = one_sprite(json_data)
        tests.append(test_one_sprite)
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        if test_spaces['pass'] is False or test_one_sprite['pass'] is False:
            return [user, tests, score_info]
        else:
            test_straggler_spaces = check_straggler_variable_no_space(scripts)
            tests.append(test_straggler_spaces)
            if test_straggler_spaces['pass'] is False:
                return [user, tests, score_info]
            tests.append(find_day_of_week(scripts, 10))
            tests.append(run_custom_block_check_say('34_1', scripts, 15))
            tests.append(if_ifelse(scripts, 5))
            tests.append(find_min(scripts, 10))
            tests.append(run_custom_block_check_say('34_2', scripts, 10))
            tests.append(minif_ifelse(scripts, 5))
            tests.append(find_distance(scripts, 5))
            tests.append(run_custom_block_check_say('34_3', scripts, 5))
            tests.append(find_help(json_data, 5))
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]
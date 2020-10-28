def route_scratch_2_2(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, find_help, find_string_in_script, check_num_sprites
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2 import press_one, press_two, press_three, press_four

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=70, score_manual=10)
    test_filename = scratch_filename_test(filename, '2.2')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        [json_data, scripts] = get_scripts_wrapper(filename)
        test_one_sprite = check_num_sprites(json_data, 1)
        tests.append(test_one_sprite)
        if test_one_sprite['pass'] is False:
            return [user, tests, score_info]
        else:
            tests.append(find_string_in_script(scripts, '22_press_zero', 15))
            tests.append(press_one(scripts, 15))
            tests.append(press_two(scripts, 15))
            tests.append(press_three(scripts, 10))
            tests.append(press_four(scripts, 10))
            tests.append(find_help(json_data, 5))
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]
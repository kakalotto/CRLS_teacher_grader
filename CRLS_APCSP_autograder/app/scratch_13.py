def route_scratch_1_3(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, find_help, check_num_sprites, press_zero
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_1_3 import press_number
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=70, score_manual=10)
    test_filename = scratch_filename_test(filename, '1.3')
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
            tests.append(press_zero(scripts, 15))
            tests.append(press_number(scripts, 1, 15))
            tests.append(press_number(scripts, 2, 15))
            tests.append(press_number(scripts, 3, 10))
            tests.append(press_number(scripts, 4, 10))
            tests.append(find_help(json_data, 5))
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]




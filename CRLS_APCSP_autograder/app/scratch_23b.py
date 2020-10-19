def route_scratch_2_3b(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, check_num_sprites, find_help, \
        find_question, variable_check_no_space, find_block_in_sprite, find_string_in_script
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=35, score_manual=15)
    test_filename = scratch_filename_test(filename, '2.3b')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        [json_data, scripts] = get_scripts_wrapper(filename)
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        test_one_sprite = check_num_sprites(json_data, 1)
        tests.append(test_one_sprite)
        tests.append(find_block_in_sprite(json_data, 'green_flag', 5))
        tests.append(find_question(json_data, 'color', 2.5))
        tests.append(find_string_in_script(scripts, '23b_color_change_1', 5))
        tests.append(find_question(json_data, 'school', 2.5))
        tests.append(find_string_in_script(scripts, '23b_costume_change', 5))
        tests.append(find_string_in_script(scripts, '23b_question_ifelse', 5))
        tests.append(find_string_in_script(scripts, '23b_two_question', 5))
        tests.append(find_help(json_data, 5))
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]

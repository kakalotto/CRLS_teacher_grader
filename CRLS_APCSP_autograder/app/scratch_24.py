def route_scratch_2_4(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, check_num_sprites, find_help, find_string_in_script,\
        find_variable, find_question, variable_check_no_space, run_script_check_say
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=60, score_manual=10)
    test_filename = scratch_filename_test(filename, '2.4')
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
            tests.append(find_string_in_script(scripts, '24_green_flag', 2.5))
            tests.append(find_variable(json_data, 'name', 2.5))
            tests.append(find_question(json_data, r'(name|Name)', 2.5))
            tests.append(find_string_in_script(scripts, '24_name_variable_to_answer', 2.5))
            tests.append(find_variable(json_data, 'number', 5))
            tests.append(find_string_in_script(scripts, '24_set_random', 10))
            tests.append(find_question(json_data, r'(guess|Guess)', 5))
            tests.append(find_string_in_script(scripts, '24_ifelse', 5))
            tests.append(run_script_check_say(scripts, '24_correct', 10))
            tests.append(run_script_check_say(scripts, '24_wrong', 10))
            tests.append(find_help(json_data, 5))
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]

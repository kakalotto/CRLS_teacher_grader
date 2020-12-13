
def route_scratch_4_3a(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, find_help, variable_check_no_space, \
        check_straggler_variable_no_space, check_num_sprites, find_string_in_script, run_script_check_say,\
        variable_check_list_different_name_than_regular
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_4_3  import songs_list, songs_list_min_items
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=60, score_manual=10)
    test_filename = scratch_filename_test(filename, '4.3a')
    tests.append(test_filename)
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        [json_data, scripts] = get_scripts_wrapper(filename)
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        test_one_sprite = check_num_sprites(json_data, 1)
        tests.append(test_one_sprite)
        test_straggler_variable = check_straggler_variable_no_space(scripts)
        tests.append(test_straggler_variable)
        test_different_variables = variable_check_list_different_name_than_regular(json_data['monitors'])
        tests.append(test_different_variables)

        tests.append(songs_list(json_data, 10))
        tests.append(songs_list_min_items(json_data, 5))
        tests.append(find_string_in_script(scripts, '43a_1', 5))
        tests.append(run_script_check_say(scripts, '43a_2', 5))
        tests.append(find_string_in_script(scripts, '43a_3', 5))
        tests.append(run_script_check_say(scripts, '43a_4', 5))
        tests.append(find_string_in_script(scripts, '43a_5', 5))
        tests.append(run_script_check_say(scripts, '43a_6', 5))
        tests.append(find_string_in_script(scripts, '43a_7', 5))
        tests.append(run_script_check_say(scripts, '43a_8', 5))
        # tests.append(find_help(json_data, 5))
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]

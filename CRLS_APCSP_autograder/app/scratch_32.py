
def route_scratch_3_2(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, find_help, variable_check_no_space, one_sprite,\
        press_zero, run_custom_block_check_say
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_3_2  import press_one, press_two, press_three, press_four, \
        find_draw_triangle, find_happy_birthday, draw_triangle_works
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=50, score_manual=10)
    test_filename = scratch_filename_test(filename, '3.2')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        [json_data, scripts] = get_scripts_wrapper(filename)
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        test_one_sprite = one_sprite(json_data)
        tests.append(test_one_sprite)
        if test_spaces['pass'] is False or test_one_sprite['pass'] is False:
            return [user, tests, score_info]
        else:
            tests.append(press_zero(scripts, 5))
            tests.append(press_one(scripts, 5))
            tests.append(press_two(scripts, 5))
            tests.append(find_draw_triangle(scripts, 5))
            tests.append(draw_triangle_works(scripts, 5))
            tests.append(press_three(scripts, 5))
            tests.append(find_happy_birthday(scripts, 5))
            tests.append(run_custom_block_check_say('32_1', scripts, 5))
            tests.append(press_four(scripts, 5))
            tests.append(find_help(json_data, 5))
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]
def route_scratch_3_5(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, find_help, variable_check_no_space, \
        check_straggler_variable_no_space, find_block_in_sprite, find_variable, find_change_variable, \
        find_string_in_script
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_3_5 import find_hero, turn_right, turn_left, animated_walk, jumps, find_scenery, \
        sprite2_moves, rollover_check, find_enemy, touch_stop, scenery_moves_different_rate, layers
    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=100, score_manual=100)
    test_filename = scratch_filename_test(filename, '3.5')
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
            test_straggler_spaces = check_straggler_variable_no_space(scripts)
            tests.append(test_straggler_spaces)
            [test_find_hero, scripts_hero] = find_hero(json_data, 0)
            tests.append(test_find_hero)
            tests.append(find_block_in_sprite(json_data, 'green_flag', 5))
            tests.append(find_variable(json_data, 'score', 5))
            tests.append(find_change_variable(json_data, 'score', points=5))
            tests.append(turn_right(scripts_hero, 5))
            tests.append(turn_left(scripts_hero, 5))
            tests.append(animated_walk(scripts_hero, 'hero', 5))
            tests.append(jumps(scripts_hero, 5))
            tests.append(layers(scripts_hero, 5))
            [test_find_scenery, scripts_scenery1, scripts_scenery2] = find_scenery(json_data, 10)
            tests.append(test_find_scenery)
            tests.append(sprite2_moves(scripts_scenery1, '35_scenery1_1', 2.5))
            tests.append(sprite2_moves(scripts_scenery1, '35_scenery1_2', 2.5))
            tests.append(sprite2_moves(scripts_scenery1, '35_scenery2_1', 2.5))
            tests.append(sprite2_moves(scripts_scenery1, '35_scenery2_2', 2.5))
            tests.append(rollover_check(scripts_scenery1, '35_scenery1_rollover_left', 2.5))
            tests.append(rollover_check(scripts_scenery1, '35_scenery1_rollover_right', 2.5))
            tests.append(rollover_check(scripts_scenery2, '35_scenery2_rollover_left', 2.5))
            tests.append(rollover_check(scripts_scenery2, '35_scenery2_rollover_right', 2.5))
            tests.append(scenery_moves_different_rate(scripts_scenery1, scripts_scenery2, 5))
            [test_find_enemy, scripts_enemy] = find_enemy(json_data, 5)
            tests.append(test_find_enemy)
            tests.append(animated_walk(scripts_enemy, 'enemy', 5))
            tests.append(find_string_in_script(scripts_enemy, '35_enemy_move', 5))
            tests.append(rollover_check(scripts_enemy, '35_enemy_rollover_left', 5))
            tests.append(touch_stop(scripts_hero, scripts_enemy, 5))
            tests.append(find_help(json_data, 5))
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]
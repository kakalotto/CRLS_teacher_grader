def scratch_feedback_35(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help,\
        arrange_blocks_v2, variable_check_no_space, every_sprite_green_flag, find_variable, find_change_variable
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_3_5 import turn_right, turn_left, animated_walk, jumps, find_scenery, find_enemy, \
        check_layers, scenery_moves, scenery_moves_different_rate, enemy_moves, enemy_rollover, enemy_animated,\
        scenery1_scenery2_rollover, touch_stop, find_hero

    tests = list()
    test_filename = scratch_filename_test(filename, '3.5')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        test_find_hero = find_hero(json_data, 0)
        tests.append(test_find_hero)
        if test_spaces['pass'] is False or test_find_hero['pass'] is False:
            return tests
        else:
            scripts = arrange_blocks_v2(json_data)
            print('scripts')
            for key in scripts:
                    print("key {}  script {} ".format(key, scripts[key]))

            print("DONE WITH SCRIPTS")
            test_every_sprite_green_flag = every_sprite_green_flag(json_data, 5)
            tests.append(test_every_sprite_green_flag)
            test_find_variable = find_variable(json_data, 'score', 5)
            tests.append(test_find_variable)
            test_change_variable = find_change_variable(json_data, 'score', points=5)
            tests.append(test_change_variable)
            test_turn_right = turn_right(json_data, 10)
            tests.append(test_turn_right)
            test_turn_left = turn_left(json_data, 10)
            tests.append(test_turn_left)
            test_animate_walk = animated_walk(json_data, 10)
            tests.append(test_animate_walk)
            test_jumps = jumps(json_data, 10)
            tests.append(test_jumps)

            test_find_scenery = find_scenery(json_data, 10)
            tests.append(test_find_scenery)
            if test_find_scenery['pass'] is False:
                return tests
            else:
                test_check_layer = check_layers(scripts, 10)
                tests.append(test_check_layer)
                test_scenery_moves = scenery_moves(json_data, 10)
                tests.append(test_scenery_moves)
                test_scenery_moves_rate = scenery_moves_different_rate(json_data, 10)
                tests.append(test_scenery_moves_rate)
                test_scenery_rollover = scenery1_scenery2_rollover(json_data, 10)
                tests.append(test_scenery_rollover)
                test_find_enemy = find_enemy(json_data, 5)
                tests.append(test_find_enemy)
                if test_find_enemy['pass'] is False:
                    return tests
                else:
                    test_enemy_moves = enemy_moves(json_data, 10)
                    tests.append(test_enemy_moves)
                    test_enemy_rollover = enemy_rollover(json_data, 10)
                    tests.append(test_enemy_rollover)
                    test_enemy_animated = enemy_animated(json_data, 5)
                    tests.append(test_enemy_animated)
                    test_touch_stop = touch_stop(json_data, 10)
                    tests.append(test_touch_stop)
                    test_help = find_help(json_data, 10)
                    tests.append(test_help)
                    return tests

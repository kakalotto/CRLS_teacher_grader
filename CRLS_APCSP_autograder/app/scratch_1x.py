def route_scratch_1_x(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, find_help, check_num_sprites, find_block_in_sprite
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, get_scripts_wrapper, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scratch Scholar', score_max=45, score_manual=35)
    test_filename = scratch_filename_test(filename, '1.x')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        [json_data, _] = get_scripts_wrapper(filename)
        tests.append(check_num_sprites(json_data, 2, eq_ge='greaterthanequal', points=5))
        tests.append(find_block_in_sprite(json_data, 'green_flag', 4))
        tests.append(find_block_in_sprite(json_data, 'broadcast', 5, min_sprites=2))
        tests.append(find_block_in_sprite(json_data, 'broadcast_received', 5, min_sprites=2))
        tests.append(find_block_in_sprite(json_data, 'any_move', 4, min_sprites=1))
        tests.append(find_block_in_sprite(json_data, 'rotate', 4, min_sprites=1))
        tests.append(find_block_in_sprite(json_data, 'change_costume', 4, min_sprites=1))
        tests.append(find_block_in_sprite(json_data, 'show_hide', 4, min_sprites=1, different_ok=True))
        tests.append(find_block_in_sprite(json_data, 'two_backgrounds', 5, min_sprites=1, check_all=True))
        tests.append(find_help(json_data, 5))
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]
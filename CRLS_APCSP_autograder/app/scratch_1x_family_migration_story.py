def scratch_feedback_1x_family_migration_story(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks, \
        match_string, every_sprite_green_flag, every_sprite_broadcast_and_receive
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_1_4_1_5 import min_two_sprites, show_and_hide
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_1x_family_migration_story import min_two_stages

    tests = list()
    
    # Test file name
    test_filename = scratch_filename_test(filename, '1.x_family_migration_story')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks(json_data)
        test_num_sprites = min_two_sprites(json_data, 5)
        tests.append(test_num_sprites)
        test_green_flag = every_sprite_green_flag(json_data, 4)
        tests.append(test_green_flag)
        test_broadcast_receive = every_sprite_broadcast_and_receive(json_data, 5)
        tests.append(test_broadcast_receive)
        if test_broadcast_receive['pass'] is False:
            return tests
        else:
            test_find_move = match_string(r'motion_movesteps', scripts, points=4)
            if test_find_move['pass'] is False:
                test_find_move['fail_message'] += 'At least one of the sprites should move. <br>'
            tests.append(test_find_move)
            test_find_rotate = match_string(r'(motion_turnleft|motion_turnright)', scripts, points=4)
            if test_find_rotate['pass'] is False:
                test_find_rotate['fail_message'] += 'At least one of the sprites should rotate. <br>'
            tests.append(test_find_rotate)
            test_change_costume = match_string(r'(looks_nextcostume|looks_switchcostumeto)', scripts, points=4)
            if test_change_costume['pass'] is False:
                test_change_costume['fail_message'] += 'At least one of the sprites should change a costume. <br>'
            tests.append(test_change_costume)
            test_show_and_hide = show_and_hide(scripts, 4)
            tests.append(test_show_and_hide)
            test_change_stage = min_two_stages(json_data, 5)
            tests.append(test_change_stage)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            return tests
        

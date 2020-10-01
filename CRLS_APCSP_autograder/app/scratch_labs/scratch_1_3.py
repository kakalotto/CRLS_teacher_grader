def press_number(p_scripts, number, p_points):
    """
    Runs all of the "press number" tests for scratch 1.3 drawing shapes.
    :param p_scripts: scripts for the sprite (sprite limited to one) (list of dict)
    :param number: the number I'm pressing (int)
    :param p_points: number of points this test is worth (int)
    :return: test dictionary (dict)
    """
    import re
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import one_event, unique_coordinates, is_equilateral_triangle, is_square, \
        is_pentagon, is_parallelogram
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2 import brickLayer, do_sprite

    shape_dict = {1: 'equilateral triangle', 2: 'square', 3: 'pentagon', 4: 'parallelogram', }
    sides_dict = {1: 3, 2: 4, 3: 5, 4: 4}
    p_test = {"name": "Checking that there is a script that has 'when " + str(number) +
                      " key is pressed' that draws a(n) " + str(shape_dict[number]) + ". (" +
                      str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a script that has 'when " + str(number) +
                              " key is pressed' that draws a(n) " + shape_dict[number] + ".<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "There is not a script that has 'when " + str(number) +
                              " key is pressed' that correctly draws a(n) " + shape_dict[number] + ".<br>",
              "points": 0
              }
    search_string = r"'event_whenkeypressed',\s'" + str(number) + "'"
    [test_one_press, script] = one_event(p_scripts, search_string)
    if test_one_press['pass'] is False:
        p_test['fail_message'] += test_one_press['fail_message']
        return p_test
    sprite = brickLayer(0, 0, 0, pendown=True)
    move_success = do_sprite(sprite, script, True)
    coords = unique_coordinates(sprite.move_history)
    drawn_sides = len(re.findall(r'motion_move', str(script), re.X | re.M | re.S))
    if re.search(r'control_repeat', str(script), re.X | re.M | re.S):
        drawn_sides = sides_dict[number]  # skip the check if there is a repeat
    if len(coords) != sides_dict[number] or (drawn_sides != sides_dict[number]):
        if len(coords) != sides_dict[number]:
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "After pressing " + str(number) + ", sprite should land on " +\
                                      str(sides_dict[number]) + \
                                      " unique coordinates, but instead lands on this many:<br>" + str(len(coords)) +\
                                      ".<br></h5>"
        if drawn_sides != sides_dict[number]:
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "Sprite should draw this many sides: " +\
                                      str(sides_dict[number]) + ", but instead draws this many: " + \
                                      str(drawn_sides) + ".<br></h5>"
    if number == 1:
        correct_shape = is_equilateral_triangle(coords)
    elif number == 2:
        correct_shape = is_square(coords)
    elif number == 3:
        correct_shape = is_pentagon(coords)
    elif number == 4:
        correct_shape = is_parallelogram(coords)
    else:
        correct_shape = False
    if correct_shape is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Tested the shape drawn by sprite.  Shape failed test for " +\
                                  str(shape_dict[number]) + ".</h5>"
    if correct_shape is False or (drawn_sides != sides_dict[number]):
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "See example of press 1 for equilateral triangle here: " \
                                  '<a href="https://docs.google.com/presentation/d/18HDDCHckIsuphA91LbFHyS272PIiG4f' \
                                  '5wxRQE3KRc2g/edit#slide=id.g74c3b39ec7_0_8" target="_blank">' \
                                  'link to page in presentation </a> <br><br>' \
                                  'See example of press 9 for rectangle (similar to parallelogram) here: ' \
                                  '<a href="https://docs.google.com/presentation/d/18HDDCHckIsuphA91LbFHy' \
                                  'S272PIiG4f5wxR' \
                                  'QE3KRc2g/edit#slide=id.g74c3b39ec7_0_15" target="_blank">' \
                                  'link to page in presentation </a></h5>'
    if test_one_press['pass'] and correct_shape and move_success and drawn_sides == sides_dict[number]:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test

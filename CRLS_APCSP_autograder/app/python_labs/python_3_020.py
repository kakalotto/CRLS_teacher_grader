def check_random(p_filename, p_points):
    from app.python_labs.io_test import io_test

    p_test = {"name": "The code should draw a random card each time."
                      "(4 points) <br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> The code drew different cards in three runs.",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> The code does not draw different cards. <br>",
              "points": 0,
              }

    p_unit_test1 = io_test(p_filename, r'.', 3)
    p_unit_test2 = io_test(p_filename, r'.', 3)
    p_unit_test3 = io_test(p_filename, r'.', 3)
    if p_unit_test1['pass'] is False:
        p_test['fail_message'] = p_unit_test1['fail_message']
        return p_unit_test1
    if p_unit_test2['pass'] is False:
        p_test['fail_message'] = p_unit_test2['fail_message']
        return p_unit_test2
    if p_unit_test3['pass'] is False:
        p_test['fail_message'] = p_unit_test3['fail_message']
        return p_unit_test3
    out1 = p_unit_test1['output']
    out2 = p_unit_test2['output']
    out3 = p_unit_test3['output']
    if out1 != out2 and out2 != out3 and out1 != out3:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test

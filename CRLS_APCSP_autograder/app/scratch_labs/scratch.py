def scratch_filename_test(p_filename, p_lab):
    """
    Checks that the filename follows correct format i.e. 2019_ewu_1.3.sb3
    :param p_filename: the name of the file
    :param p_lab: the lab
    :return: a test dictionary
    """
    import re
    from CRLS_APCSP_autograder.app.python_labs import YEAR
    from CRLS_APCSP_autograder.app.python_labs import LAST_YEAR

    find_year = re.search(YEAR, p_filename)
    find_last_year = re.search(LAST_YEAR, p_filename)
    
    find_lab = re.search(p_lab, p_filename)
    find_caps = re.search(r'[A-Z]', p_filename)
    find_all = re.search(YEAR + r"_ .+ _ " + p_lab + r".sb3", p_filename, re.X | re.M | re.S)
    find_all_last = re.search(LAST_YEAR + r"_ .+ _ " + p_lab + r".sb3", p_filename, re.X | re.M | re.S)

    p_test_filename = {"name": "Testing that file is named correctly",
                       "pass": True,
                       "pass_message": "<h5 style=\"color:green;\">Pass!</h5> File name looks correct "
                                       "(i.e. something like 2019_luismartinez_" + p_lab +
                                       ".sb3).  Filename was this:" + p_filename,
                       "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                       "File name of submitted file does not follow required convention. "
                                       " Rename and resubmit.<br>"
                                       "File name should be like this: <br> <br>"
                                       "2019_luismartinez_" + p_lab + ".sb3 <br><br>"
                                       "<b>Your name should be in lowercase.</b><br>"
                                       "File must be scratch 3 file (ends in .sb3).<br>" 
                                       "A Google doc with code copy+pasted in is not accepted <br>"
                                       " Other tests not run. They will be run after filename is fixed.<br>",
                       'points': 0,
                       }
    if (find_year or find_last_year) and find_lab and (find_all or find_all_last) and not find_caps:
        p_test_filename['pass'] = True
    else:
        p_test_filename['pass'] = False
    return p_test_filename


def read_json_file():
    """
    Reads in json file
    :return: dictionary of what is in json file
    """
    import json

    with open('/tmp/project.json', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


def unzip_sb3(p_filename):
    """
    Unzips the file
    :param p_filename: name of file (string)
    :return: none
    """
    from zipfile import ZipFile
    with ZipFile(p_filename, 'r') as p_zip:
        p_zip.extractall('/tmp', )


def find_help(p_json, p_points):
    """
    Reads in json info (in dictionary form)
    :param p_json: json info (as dictionary)
    :param p_points: points this is worth
    :return: test dictionary
    """
    import re

    p_test_help = {"name": "Testing that you got a help and documented it as a comment (" + str(p_points) + " points)",
                   "pass": True,
                   "pass_message": "<h5 style=\"color:green;\">Pass (for now).<h5>"
                                   "  You have a comment with 'help' in it.  <br>"
                                   "Be sure your comment is meaningful, otherwise this can be overturned "
                                   "on review.",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5>"
                                   "  Did not find a comment in your code with the word 'help' describing"
                                   " how somebody helped you with your code.  <br>"
                                   "Your help can NOT be from teachers Atwood, Wu, or Martinez" 
                                   '<h5 style=\"color:purple;\">'
                                   'See example here: <a href="' +
                                   "https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m"
                                   "8QGkVhDJWf62lFVITA/edit#slide=id.g74d477a87c_0_0" 
                                   '" target="_blank">link to page in presentation</a></h5></br>',
                   'points': 0
                   }
    help_comments = 0
    for target in p_json['targets']:
        if target['comments']:
            for comment_id in target['comments']:
                helps = re.search(r'(help|Help)', target['comments'][comment_id]['text'], re.X | re.M | re.S)
                teacher = re.search('(Wu|Martinez|Atwood)', target['comments'][comment_id]['text'], re.X | re.M | re.S)
                if helps and not teacher:
                    help_comments += 1
    if help_comments == 0:
        p_test_help['pass'] = False
    else:
        p_test_help['points'] += p_points
    return p_test_help


def find_variable(p_json, variable_name, p_points):
    """
    Find a particular variable in scratch. Retruns True/False
    :param p_json: The json
    :param variable_name: variable nmae you are looking for
    :param p_points: Number of points this test is worth
    :return: test dictionary
    """
    p_test = {"name": "Testing that variable '" +
                      variable_name +
                      "' is in the Scratch program "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. </h5>"
                              "Variable '" +
                              variable_name +
                              "' is in the Scratch program. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "<h5 style=\"color:purple;\">"
                              "Did not find a variable '" +
                              variable_name +
                              "' in your code.  You must name the variable EXACTLY '" +
                              variable_name +
                              "' with correct spelling and capitalization.  </h5><br>",
              'points': 0
              }

    sprites = p_json['targets']
    for sprite in sprites:
        if 'variables' in sprite:
            variables = sprite['variables']
            for key in variables:
                variable_list = variables[key]
                if variable_name == variable_list[0]:
                    p_test['pass'] = True
    if p_test['pass']:
        p_test['points'] += p_points
    return p_test


def find_list(p_json, list_name, p_points, *, min_items=0):
    """
    Find a particular list in scratch. Retruns True/False
    :param p_json: The json
    :param list_name: list name you are looking for
    :param p_points: Number of points this test is worth
    :param min_items: minimum number of items in the list to pass
    :return: test dictionary
    """
    p_test = {"name": "Testing that list '" +
                      list_name +
                      "' is in the Scratch program "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "List '" +
                              list_name +
                              "' is in the Scratch program. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Did not find a list '" +
                              list_name +
                              "' in your code.  You must name the list EXACTLY '" +
                              list_name +
                              "' with correct spelling and capitalization.  <br>",
              'points': 0
              }

    sprites = p_json['targets']
    for sprite in sprites:
        if 'lists' in sprite:
            lists = sprite['lists']
            for key in lists:
                list_list = lists[key]
                if list_name == list_list[0]:
                    p_test['pass'] = True  # temporarily....see min_items test
                    if min_items >= 1:
                        if len(list_list[1]) < min_items:
                            p_test['pass'] = False
                            p_test['fail_message'] = "<h5 style=\"color:purple;\"> " \
                                                     "Found a list " +\
                                                     list_name + " in your code. <br> " + list_name +\
                                                     " had this many items: " + str(len(list_list[1])) + "</h5>"
    if p_test['pass']:
        p_test['points'] += p_points
    return p_test


def find_question(p_json, question_string, p_points):
    """
    Find a particular string in all of the questions being asked in scratch. Retruns True/False
    :param p_json: The json
    :param question_string: String you are going to regex search in
    :param p_points: Number of points this test is worth
    :return: test dictionary
    """
    import re
    p_test = {"name": "Testing that a question with the string '" +
                      question_string +
                      "' is in the Scratch program "
                      "(" + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Question with the string " +
                              question_string +
                              " is in the Scratch program. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "<h5 style=\"color:purple;\">"
                              "Did not find a question with the string '" +
                              question_string +
                              "' in your code. <br> "
                              'See example here: <a href="https://docs.google.com/presentation/d/1fM_9jw-XCvQxCdNCq'
                              '3GrIGdBns3MzpoK9EzcalRrH_k/edit#slide=id.g3f255390c6_0_26asdf">link to page in'
                              'presentation of asking a question</a></h5>',
              'points': 0
              }

    sprites = p_json['targets']
    for sprite in sprites:
        if 'blocks' in sprite:
            blocks = sprite['blocks']
            for block_id in blocks:
                block = blocks[block_id]
                if 'opcode' not in block:
                    continue
                if block['opcode'] == 'sensing_askandwait':
                    question = extract_value(block['inputs']['QUESTION'], blocks)
                    if re.search(question_string, str(question), re.X | re.M | re.S):
                        p_test['pass'] = True
    if p_test['pass']:
        p_test['points'] += p_points
    return p_test


def find_set_variable(p_json, variable, value, *, points=0):
    """
    Find a particular string in all of the questions being asked in scratch. Retruns True/False
    :param p_json: The json
    :param variable: the variable
    :param value: value
    :param p_points: Number of points this test is worth
    :return: test dictionary
    """
    p_test = {"name": "Testing that setting a variable '" +
              variable +
              "' to the value '" +
              value +
              "' is in the Scratch program  (" +
                      str(points) +
                      "  points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>" +
                              "A variable '" +
                              variable +
                              "' is set to the value '" +
                              value +
                              "' in the Scratch program  <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Did not find  a variable '" +
                              variable +
                              "' with the value '" +
                              value +
                              "' in the Scratch program  <br>",
              'points': 0
              }

    sprites = p_json['targets']
    for sprite in sprites:
        if 'blocks' in sprite:
            blocks = sprite['blocks']
            for block_id in blocks:
                block = blocks[block_id]
                if 'opcode' not in block:
                    continue
                if block['opcode'] == 'data_setvariableto':
                    block_variable = block['fields']['VARIABLE'][0]
                    if isinstance(block['inputs']['VALUE'][1], str):
                        value_block_id = block['inputs']['VALUE'][1]
                        if blocks[value_block_id]['opcode'] == 'sensing_answer':
                            block_value = 'answer'
                    else:
                        block_value = block['inputs']['VALUE'][1][1]
                    if block_variable == variable and block_value == value:
                        p_test['pass'] = True
    if p_test['pass']:
        p_test['points'] += points
    return p_test


def find_change_variable(p_json, variable, *, points=0):
    """
    Find a particular string in all of the questions being asked in scratch. Retruns True/False
    :param p_json: The json
    :param variable: the variable
    :param points: Number of points this test is worth
    :return: test dictionary
    """
    p_test = {"name": "Testing that variable " + variable + " is changed  in the Scratch program  (" +
                      str(points) + "  points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. </h5>" +
                              "A variable '" +
                              variable +
                              "' is changed in the Scratch program  <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Did not find  a variable '" +
                              variable +
                              "' that is changed in the Scratch program  <br>",
              'points': 0
              }

    sprites = p_json['targets']
    for sprite in sprites:
        if 'blocks' in sprite:
            blocks = sprite['blocks']
            for block_id in blocks:
                block = blocks[block_id]
                if 'opcode' not in block:
                    continue
                if block['opcode'] == 'data_changevariableby':
                    p_test['pass'] = True
    if p_test['pass']:
        p_test['points'] += points
    return p_test


def check_only_one_block(p_scripts, find_this, p_points):
    from app.scratch_labs.scratch import match_string

    p_test = {"name": "Testing only one block of a particular type (i.e. one flag)'(" +
                      str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "There is only one block of a particular type <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Found multiple blocks of this type!.<br>",
              'points': 0
              }
    count = 0
    block_dict = {'greenflag': 'event_whenflagclicked'}
    target = block_dict[find_this]

    for key in p_scripts:
        script = p_scripts[key]
        test_found_1 = match_string(target, script)
        if test_found_1['pass']:
            count += 1
    if count > 1:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">Found too many of " + str(target) + \
                                  ".<br>Expected 1 found " + str(count) + "</h5>"
        p_test['pass'] = False
    elif count != 1:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">Found wrong number of " + str(target) + \
                                  ".<br>Expected 1 found " + str(count) + "</h5>"
        p_test['pass'] = False
    else:
        p_test['pass'] = True
    return p_test


def _clean_block(block):
    """
    Helper function, gets rid of a bunch of keys to make more readable
    :param block is a scratch block (dictionary)
    :return: same block, but cleaned
    """

    if 'next' in block.keys():
        del block['next']
    if 'parent' in block.keys():
        del block['parent']
    del block['shadow']
    del block['topLevel']
    if 'x' in block.keys():
        del block['x']
        del block['y']
    return block


def _order_blocks(starting_block_id, p_target):
    """
    Called by arrange_blocks, to traverse a scratch block json, finding sequential blocks until it hits the end
    :param starting_block_id: Key of the block with which o start the script
    :param p_target: json info for block that is starting the script (value of dictionary with key starting_block-id)
    :return: list.   values is list of block JSON info for each item in the script
    """
    script = [p_target['blocks'][starting_block_id]]
    current_block_id = starting_block_id
    next_block_id = p_target['blocks'][current_block_id]['next']
    while next_block_id is not None:
        script.append(p_target['blocks'][next_block_id])
        current_block_id = next_block_id
        next_block_id = p_target['blocks'][current_block_id]['next']
    return script


def arrange_blocks(p_json):
    """
    Looks for a particular script in the code.  Algorithms:
    1. Find all the parents and populate new dictionary.
    2. Keys are keys of the parents.  Values are lists, each item is a block starting at the top of the tree.
    3. Look for "next" key and add that to the value list.

    :param p_json: json info (as dictionary)
    :return: scripts - dictionary of scripts.  Keys are block ID's of parent.  values are lists of individual blocks
    under the parent
    """

    scripts = {}
    for target in p_json['targets']:
        if target['blocks']:
            for block_id in target['blocks']:
                if 'parent' in target['blocks'][block_id]:  # Verify it hasn't been processed already
                    if target['blocks'][block_id]['parent'] is None:                   # Do parent blocks
                        script = _order_blocks(block_id, target)
                        scripts[block_id] = script
                    else:  # Do nested repeat blocks
                        parent_id = target['blocks'][block_id]['parent']
                        if target['blocks'][parent_id]['inputs']:
                            if 'SUBSTACK' in target['blocks'][parent_id]['inputs']:
                                if target['blocks'][parent_id]['inputs']['SUBSTACK'][1] == block_id:
                                    script = _order_blocks(block_id, target)
                                    for block in script:
                                        _clean_block(block)
                                    target['blocks'][parent_id]['inputs']['SUBSTACK'].append(script)

    for key in scripts:
        for block in scripts[key]:
            _clean_block(block)
    return scripts


def extract_value(block_portion, p_blocks):
    """
    Same as build karel script but copied over so I cdon't break that one
    :param block_portion: a portion of a block (like block['inputs']['MESSAGE']
    :param p_block_id: ID of this block
    :param p_blocks: al the blocks for this script
    :return: a combined script (dictionary)
    """
    if len(block_portion) == 2:
        return block_portion[1][1]  # length is 2, say it directly.
    else:
        if isinstance(block_portion[1], list):
            # i.e  message[1] is a list - variable.  Same as before, but  add VARIABLE_
            ret_val = block_portion[1][1]
            ret_val = 'VARIABLE_' + ret_val
            return ret_val
        else:
            # message[1] is a string and therefore references another block
            next_id = block_portion[1]
            ret_val = build_scratch_script(next_id, p_blocks)
            return ret_val


def build_scratch_script(starting_block_id, p_blocks):
    """
    Same as build karel script but copied over so I cdon't break that one
    :param starting_block_id:
    :param p_blocks: al the blocks for this script
    :return: a combined script (dictionary)
    """
    import re
    script = []
    if starting_block_id is None:
        return script
    print("starting block ID " + str(starting_block_id))
    temp_block = p_blocks[starting_block_id]
    temp_block['ID'] = starting_block_id
    current_block_id = starting_block_id
    next_block_id = "continue"
    while next_block_id is not None:
        current_block = p_blocks[current_block_id]
        print("building scratch script.  current id: {} opcode: {}".format(current_block_id, current_block['opcode']))
        if current_block['opcode'] == 'motion_movesteps':
            # print("XXX script {}".format(script))
            steps = extract_value(current_block['inputs']['STEPS'], p_blocks)
            script.append(['motion_movesteps', steps])  # had to use append in instance of 1 pressed, moe
        elif current_block['opcode'] == 'motion_turnleft':
            degrees = extract_value(current_block['inputs']['DEGREES'], p_blocks)
            script.append(['motion_turnleft', degrees])  # required append in test case
        elif current_block['opcode'] == 'motion_turnright':
            degrees = extract_value(current_block['inputs']['DEGREES'], p_blocks)
            script.append(['motion_turnright', degrees])
        elif current_block['opcode'] == 'motion_sety':
            y = extract_value(current_block['inputs']['Y'], p_blocks)
            script.append(['motion_sety', y])
        elif current_block['opcode'] == 'motion_setx':
            x = extract_value(current_block['inputs']['X'], p_blocks)  # test required append
            script.append(['motion_setx', x])
        elif current_block['opcode'] == 'motion_gotoxy':
            x = extract_value(current_block['inputs']['X'], p_blocks)
            y = extract_value(current_block['inputs']['Y'], p_blocks)
            script.append(['motion_gotoxy', x, y])  # tested used append
        elif current_block['opcode'] == 'motion_changeyby':
            dy = extract_value(current_block['inputs']['DY'], p_blocks)
            script.append(['motion_changeyby', dy])  # updated
        elif current_block['opcode'] == 'motion_changexby':
            dx = extract_value(current_block['inputs']['DX'], p_blocks)
            script.append(['motion_changexby', dx])  # tested
        elif current_block['opcode'] == 'motion_xposition':
            script.extend(['motion_xposition'])
        elif current_block['opcode'] == 'motion_yposition':
            script.extend(['motion_yposition'])  # 2.2 needs extend
        elif current_block['opcode'] == 'motion_pointindirection':
            direction = extract_value(current_block['inputs']['DIRECTION'], p_blocks)
            script.append(['motion_pointindirection', direction])
        elif current_block['opcode'] == 'motion_glidesecstoxy':
            secs = extract_value(current_block['inputs']['SECS'], p_blocks)
            x = extract_value(current_block['inputs']['X'], p_blocks)
            y = extract_value(current_block['inputs']['Y'], p_blocks)
            script.append(['motion_glidesecstoxy', secs, x, y])
        elif current_block['opcode'] == 'event_whenflagclicked':
            script.append('event_whenflagclicked')
        elif current_block['opcode'] == 'event_whenkeypressed':
            key = current_block['fields']['KEY_OPTION'][0]
            script.append(['event_whenkeypressed', key])
        elif current_block['opcode'] == 'event_broadcast':
            message = current_block['inputs']['BROADCAST_INPUT'][1][1]
            script.append(['event_broadcast', message])
        elif current_block['opcode'] == 'event_broadcastandwait':
            message = current_block['inputs']['BROADCAST_INPUT'][1][1]
            script.append(['event_broadcastandwait', message])
        elif current_block['opcode'] == 'event_whenbroadcastreceived':
            message = current_block['fields']['BROADCAST_OPTION'][0]
            script.append(['event_whenbroadcastreceived', message])
        elif current_block['opcode'] == 'control_repeat' or current_block['opcode'] == 'control_forever':
            print('aaa current block {}'.format(current_block))
            if 'SUBSTACK' not in current_block['inputs']:
                repeat_script = ['']
            elif current_block['inputs']['SUBSTACK'][1]:
                substack_id = current_block['inputs']['SUBSTACK'][1]
                repeat_script = build_scratch_script(substack_id, p_blocks)
            else:
                repeat_script = ['']
            if current_block['opcode'] == 'control_forever':
                times = 150
            else:
                #  oldtimes = current_block['inputs']['TIMES'][1][1]
                print('CURRENT BLOCK {}'.format(current_block['inputs']['TIMES']))
                times = extract_value(current_block['inputs']['TIMES'], p_blocks)
            script.append(['control_repeat', times, repeat_script])
        elif current_block['opcode'] == 'control_repeat_until':
            if 'SUBSTACK' not in current_block['inputs']:
                repeat_script = ['']
            elif current_block['inputs']['SUBSTACK'][1]:
                substack_id = current_block['inputs']['SUBSTACK'][1]
                repeat_script = build_scratch_script(substack_id, p_blocks)
            else:
                repeat_script = ['']
            if 'CONDITION' not in current_block['inputs']:
                condition_script = True
            elif current_block['inputs']['CONDITION'][1]:
                condition_id = current_block['inputs']['CONDITION'][1]
                condition_script = build_scratch_script(condition_id, p_blocks)
            else:
                condition_script = True
            script.append(['control_repeat_until', condition_script, repeat_script])
        elif current_block['opcode'] == 'control_stop':
            script.append(['control_stop'])
        elif current_block['opcode'] == 'control_wait':
            time = extract_value(current_block['inputs']['DURATION'], p_blocks)
            script.append(['control_wait', time])
        elif current_block['opcode'] == 'sensing_askandwait':
            question = extract_value(current_block['inputs']['QUESTION'], p_blocks)
            script.append(['sensing_askandwait', question])
        elif current_block['opcode'] == 'sensing_keypressed':
            sensing_keyoptions_id = current_block['inputs']['KEY_OPTION'][1]
            sensing_keyoptions_list = build_scratch_script(sensing_keyoptions_id, p_blocks)
            script.extend(['sensing_keypressed', sensing_keyoptions_list])
        elif current_block['opcode'] == 'sensing_keyoptions':
            key = current_block['fields']['KEY_OPTION'][0]
            script.extend(['sensing_keyoptions', key])
        elif current_block['opcode'] == 'sensing_touchingobject':
            touchingobjectmenu_id = current_block['inputs']['TOUCHINGOBJECTMENU'][1]
            touching_object_list = build_scratch_script(touchingobjectmenu_id, p_blocks)
            script.extend(['sensing_touchingobject', touching_object_list])
        elif current_block['opcode'] == 'sensing_touchingobjectmenu':
            touching_object = current_block['fields']['TOUCHINGOBJECTMENU'][0]
            script.extend(['sensing_touchingobjectmenu', touching_object])
        elif current_block['opcode'] == 'looks_sayforsecs':
            time = current_block['inputs']['SECS'][1][1]
            message = extract_value(current_block['inputs']['MESSAGE'], p_blocks)
            script.append(['looks_sayforsecs', message, time])
            # Needs the append # 7/31 try again extend 8/1 need append
            print("looks_sayforsecs script is this {}".format(script))
        elif current_block['opcode'] == 'looks_say':
            time = 1
            message = extract_value(current_block['inputs']['MESSAGE'], p_blocks)
            script.append(['looks_sayforsecs', message, time])  # no distinction beteen say and say for 1 second
            # 4.4 wants extend 4.3b wants append?
            print("looks_say script is this {}".format(script))
        elif current_block['opcode'] == 'looks_nextcostume':
            script.extend(['looks_nextcostume'])  # no distinction beteen say and say for 1 second
        elif current_block['opcode'] == 'looks_switchcostumeto':
            costume_id = current_block['inputs']['COSTUME'][1]
            costume_costume = build_scratch_script(costume_id, p_blocks)
            script.append(['looks_switchcostumeto', costume_costume])  # no distinction beteen say and say for 1 second
        elif current_block['opcode'] == 'looks_costume':
            costume = current_block['fields']['COSTUME'][0]
            script.append(['looks_costume', costume])
        elif current_block['opcode'] == 'looks_hide':
            script.extend(['looks_hide'])
        elif current_block['opcode'] == 'looks_show':
            script.extend(['looks_show'])
        elif current_block['opcode'] == 'looks_gotofrontback':
            frontback = current_block['fields']['FRONT_BACK'][0]
            script.append(['looks_gotofrontback', frontback])
        elif current_block['opcode'] == 'looks_goforwardbackwardlayers':
            num = extract_value(current_block['inputs']['NUM'], p_blocks)
            forwardbackwards = current_block['fields']['FORWARD_BACKWARD'][0]
            script.append(['looks_goforwardbackwardlayers', num, forwardbackwards])
            # no distinction beteen say and say for 1 second
        elif current_block['opcode'] == 'sensing_answer':
            return 'sensing_answer'
        elif current_block['opcode'] == 'data_setvariableto':
            value = extract_value(current_block['inputs']['VALUE'], p_blocks)
            variable = current_block['fields']['VARIABLE'][0]
            script.append(['data_setvariableto', variable, value])  # test used append
        elif current_block['opcode'] == 'data_changevariableby':
            variable_name = current_block['fields']['VARIABLE'][0]
            variable_name = 'VARIABLE_' + variable_name
            value = extract_value(current_block['inputs']['VALUE'], p_blocks)
            script.append(['data_changevariableby', variable_name, value])
        elif current_block['opcode'] == 'data_deletealloflist':
            listname = current_block['fields']['LIST'][0]
            script.append(['data_deletealloflist', listname])  # tested with append
        elif current_block['opcode'] == 'data_itemoflist':
            list_name = current_block['fields']['LIST'][0]
            index = extract_value(current_block['inputs']['INDEX'], p_blocks)
            script.extend(['data_itemoflist', index, list_name])  # tested with extend
        elif current_block['opcode'] == 'data_lengthoflist':
            list_name = current_block['fields']['LIST'][0]
            print("ccc length of list {}".format(list_name))
            script.extend(['data_lengthoflist', list_name])
        elif current_block['opcode'] == 'data_deleteoflist':
            list_name = current_block['fields']['LIST'][0]
            index = extract_value(current_block['inputs']['INDEX'], p_blocks)
            script.append(['data_deleteoflist', index, list_name])  # test used append
        elif current_block['opcode'] == 'data_addtolist':
            item = extract_value(current_block['inputs']['ITEM'], p_blocks)
            if len(current_block['fields']['LIST']) == 2:
                list_to_append = current_block['fields']['LIST'][0]
            script.append(['data_addtolist', item, list_to_append])  # testused append
        elif current_block['opcode'] == 'procedures_call':
            procedure_name = current_block['mutation']['proccode']
            procedure = re.sub(r"%s", "", procedure_name, re.X | re.M | re.S)
            procedure = re.sub(r"%b", "", procedure, re.X | re.M | re.S)
            arg_ids_str = current_block['mutation']['argumentids']
            print("args id_str {}".format(arg_ids_str))
            arg_ids_str = re.sub(r"^\[", "", arg_ids_str, re.X | re.M | re.S)
            arg_ids_str = re.sub(r"]$", "", arg_ids_str, re.X | re.M | re.S)
            arg_ids = arg_ids_str.split('","')
            if len(current_block['inputs']) != 0:
                print("procedure {} inputs {}".format(procedure, current_block['inputs']))
                for arg in arg_ids:
                    arg = re.sub(r'"', "", arg, re.X | re.M | re.S)
                    if len(current_block['inputs'][arg]) == 2:
                        procedure += " " + current_block['inputs'][arg][1][1]
                    elif len(current_block['inputs'][arg]) == 3:
                        procedure += " " + "VARIABLE_" + current_block['inputs'][arg][1][1]
            script.append(procedure)

        elif current_block['opcode'] == 'control_if':
            if 'SUBSTACK' not in current_block['inputs'].keys() or current_block['inputs']['SUBSTACK'][1] is None:
                script.append(['control_if', 'True', ['looks_sayforsecs',
                                                      'You have an if that is empty, please put something there',
                                                      '1']])  # need append
                # raise Exception("You have an if statement with nothing in it.  "
                #                "Add something inside it before autograding")
            elif 'CONDITION' not in current_block['inputs'].keys():
                script.append(['control_if', 'True', ['looks_sayforsecs',
                                                      'You have an if without a condition'], '1'])  # need append
                # raise Exception("You have an if statement with nothing in it.  "
                #                "Add something inside it before autograding")
            else:
                substack_1_id = current_block['inputs']['SUBSTACK'][1]
                condition_id = current_block['inputs']['CONDITION'][1]
                print("substack 1 id {} condition id {}".format(substack_1_id, condition_id))
                if_script = build_scratch_script(substack_1_id, p_blocks)
                condition_script = build_scratch_script(condition_id, p_blocks)
                script.append(['control_if', condition_script, if_script])  # need append
        elif current_block['opcode'] == 'control_if_else':
            if 'SUBSTACK' not in current_block['inputs'].keys() or 'SUBSTACK2' not in current_block['inputs'].keys()\
                    or current_block['inputs']['SUBSTACK'][1] is None or \
                    current_block['inputs']['SUBSTACK2'][1] is None:
                script.append(['control_if_else', 'True',
                               ['looks_sayforsecs', 'You have if/else that is blank in code.  Fix your code!',
                                '1', ],
                               ['looks_sayforsecs', 'You have if/else that is blank in code.  Fix your code!'
                                                    '', '1', ]])  # need append
            else:
                substack_1_id = current_block['inputs']['SUBSTACK'][1]
                substack_2_id = current_block['inputs']['SUBSTACK2'][1]
                condition_id = current_block['inputs']['CONDITION'][1]
                if_script = build_scratch_script(substack_1_id, p_blocks)
                else_script = build_scratch_script(substack_2_id, p_blocks)
                condition_script = build_scratch_script(condition_id, p_blocks)
                script.append(['control_if_else', condition_script, if_script, else_script])
        elif current_block['opcode'] == 'operator_not':
            # operand = extract_value(current_block['inputs']['OPERAND'], p_blocks)
            operand_id = current_block['inputs']['OPERAND'][1]
            operand = build_scratch_script(operand_id, p_blocks)
            script.extend(['operator_not', operand])
        elif current_block['opcode'] == 'operator_mod':
            num1 = extract_value(current_block['inputs']['NUM1'], p_blocks)
            num2 = extract_value(current_block['inputs']['NUM2'], p_blocks)
            script.extend(['operator_mod', num1, num2])

        elif current_block['opcode'] == 'operator_and':
            if 'OPERAND1' not in current_block['inputs'] or 'OPERAND2' not in current_block['inputs']:
                script.extend(['operator_and', 1, 1])
            else:
                operand1_id = current_block['inputs']['OPERAND1'][1]
                operand2_id = current_block['inputs']['OPERAND2'][1]
                if operand1_id is None:
                    operand1 = True
                else:
                    operand1 = build_scratch_script(operand1_id, p_blocks)
                if operand2_id is None:
                    operand2 = True
                else:
                    operand2 = build_scratch_script(operand2_id, p_blocks)
                print("asdfasdf {} {}".format(operand1, operand2))
                script.extend(['operator_and', operand1, operand2])
        elif current_block['opcode'] == 'operator_or':
            if 'OPERAND1' not in current_block['inputs'] or 'OPERAND2' not in current_block['inputs']:
                script.extend(['operator_or', 1, 1])
            else:
                operand1_id = current_block['inputs']['OPERAND1'][1]
                operand2_id = current_block['inputs']['OPERAND2'][1]
                if operand1_id is None:
                    operand1 = True
                else:
                    operand1 = build_scratch_script(operand1_id, p_blocks)
                if operand2_id is None:
                    operand2 = True
                else:
                    operand2 = build_scratch_script(operand2_id, p_blocks)

                print('OR {} {}'.format(operand1_id, operand2_id))
                # operand1 = build_scratch_script(operand1_id, p_blocks)
                # operand2 = build_scratch_script(operand2_id, p_blocks)
                # script.extend([operand1, 'or', operand2])
                script.extend(['operator_or', operand1, operand2])

        elif current_block['opcode'] == 'operator_length':
            operator_string = extract_value(current_block['inputs']['STRING'], p_blocks)
            script.extend(['operator_length', operator_string])
        elif current_block['opcode'] == 'operator_letter_of':
            letter = extract_value(current_block['inputs']['LETTER'], p_blocks)
            operator_string = extract_value(current_block['inputs']['STRING'], p_blocks)
            script.extend(['operator_letter_of', letter, operator_string])

        elif current_block['opcode'] == 'operator_subtract':
            num1 = extract_value(current_block['inputs']['NUM1'], p_blocks)
            num2 = extract_value(current_block['inputs']['NUM2'], p_blocks)
            script.extend(['operator_subtract', num1, num2])  # tested
        elif current_block['opcode'] == 'operator_add':
            num1 = extract_value(current_block['inputs']['NUM1'], p_blocks)
            num2 = extract_value(current_block['inputs']['NUM2'], p_blocks)
            print("hhh num1 {} num2 {}".format(num1, num2))
            script.extend(['operator_add', num1, num2])
        elif current_block['opcode'] == 'operator_divide':
            num1 = extract_value(current_block['inputs']['NUM1'], p_blocks)
            num2 = extract_value(current_block['inputs']['NUM2'], p_blocks)
            script.extend(['operator_divide', num1, num2])  # tested
        elif current_block['opcode'] == 'operator_multiply':
            num1 = extract_value(current_block['inputs']['NUM1'], p_blocks)
            num2 = extract_value(current_block['inputs']['NUM2'], p_blocks)
            print("hhh num1 {} num2 {}".format(num1, num2))
            script.extend(['operator_multiply', num1, num2])
        elif current_block['opcode'] == 'operator_equals':
            operand1 = extract_value(current_block['inputs']['OPERAND1'], p_blocks)
            operand2 = extract_value(current_block['inputs']['OPERAND2'], p_blocks)
            # script.extend([operand1, '=', operand2])
            script.extend(['operator_equals', operand1, operand2])
        elif current_block['opcode'] == 'operator_lt':
            operand1 = extract_value(current_block['inputs']['OPERAND1'], p_blocks)
            operand2 = extract_value(current_block['inputs']['OPERAND2'], p_blocks)
            script.extend(['operator_lt', operand1, operand2])
        elif current_block['opcode'] == 'operator_gt':
            operand1 = extract_value(current_block['inputs']['OPERAND1'], p_blocks)
            operand2 = extract_value(current_block['inputs']['OPERAND2'], p_blocks)
            # script.extend([operand1, '>', operand2])
            script.extend(['operator_gt', operand1, operand2])
        elif current_block['opcode'] == 'operator_join':
            string1 = extract_value(current_block['inputs']['STRING1'], p_blocks)
            string2 = extract_value(current_block['inputs']['STRING2'], p_blocks)
            script.extend(['join', string1, string2])  # extend tested
        elif current_block['opcode'] == 'operator_contains':
            string1 = extract_value(current_block['inputs']['STRING1'], p_blocks)
            string2 = extract_value(current_block['inputs']['STRING2'], p_blocks)
            script.extend(['operator_contains', string2, string1])
        elif current_block['opcode'] == 'operator_random':
            num_from = extract_value(current_block['inputs']['FROM'], p_blocks)
            num_to = extract_value(current_block['inputs']['TO'], p_blocks)
            script.extend(['operator_random', num_from, num_to])
        elif current_block['opcode'] == 'operator_mathop':
            operator = current_block['fields']['OPERATOR'][0]
            inputs = extract_value(current_block['inputs']['NUM'], p_blocks)
            print("baby snork operator {} inputs {}".format(operator, inputs))
            script.extend(['operator_mathop', operator, inputs])
        elif current_block['opcode'] == 'looks_switchbackdropto':
            backdrop_id = current_block['inputs']['BACKDROP'][1]
            backdrop = build_scratch_script(backdrop_id, p_blocks)
            script.extend(['looks_switchbackdropto', backdrop])
        elif current_block['opcode'] == 'looks_nextbackdrop':
            script.extend(['looks_nextbackdrop'])
        elif current_block['opcode'] == 'looks_backdrops':
            backdrop = current_block['fields']['BACKDROP'][0]
            return backdrop
#            script.append(backdrop)
        elif current_block['opcode'] == 'pen_penDown':
            print("fff pen down")
            script.append('pen_penDown')
        elif current_block['opcode'] == 'pen_penUp':
            print("fff pen up")
            script.append('pen_penUp')
        elif current_block['opcode'] == 'pen_clear':
            script.append('pen_clear')
        elif current_block['opcode'] == 'pen_setPenColorToColor':
            color = current_block['inputs']['COLOR'][1][1]
            script.append(['pen_setPenColorToColor', color])
        elif current_block['opcode'] == 'pen_setPenColorParamTo':
            color_param = current_block['inputs']['COLOR_PARAM'][1][1]
            script.append(['pen_setPenColorParamTo', color_param])
        elif current_block['opcode'] == 'argument_reporter_string_number':
            # script.extend(['VARIABLE_' + str(current_block['fields']['VALUE'][0])])
            return 'VARIABLE_' + str(current_block['fields']['VALUE'][0])
        elif current_block['opcode'] == 'argument_reporter_boolean':
            # script.extend(['VARIABLE_' + str(current_block['fields']['VALUE'][0])])
            return 'VARIABLE_' + str(current_block['fields']['VALUE'][0])

        elif 'opcode' in current_block.keys():
            print("This opcode not done in build_scratch_script" + current_block['opcode'])
        next_block_id = current_block['next']
        current_block_id = next_block_id
    return script


def arrange_blocks_v2(p_json, *, no_background=False, only_this_sprite=''):
    """
    More or less the same, but taking the lessons I learned from Karel.
    Looks for a particular script in the code.  Algorithms:
    :param p_json: json info (as dictionary)
    :param no_background: whether or not to include the backdrop scripts (boolean)
    :param only_this_sprite: If parameter set, only does the blocks for this sprite (string)
    :return: scripts - dictionary of scripts.  Keys are block ID's of parent.  values are lists of individual blocks
    under the parent
    """
    import re

    scripts = {}
    repeat_scripts = {}
    operator_scripts = {}
    if_scripts = {}
    sprites = p_json['targets']
    for sprite in sprites:
        if 'blocks' in sprite:
            if 'isStage' in sprite:
                if sprite['isStage'] is True and no_background is True:
                    continue
            if only_this_sprite:
                if sprite['name'] != only_this_sprite:
                    continue
            blocks = sprite['blocks']
            for block_id in blocks:
                block = blocks[block_id]
                print("uuu this is the block_id in arrange {}".format(block_id))
                if 'opcode' not in block:
                    continue
                if block['opcode'] == "control_repeat" or \
                        block['opcode'] == "control_forever" or \
                        block['opcode'] == "control_repeat_until":
                    if 'inputs' in block:
                        if 'SUBSTACK' in block['inputs']:
                            repeat_scripts[block_id] = [block['inputs']['SUBSTACK'][1]]
                elif block['opcode'] == "operator_equals":
                    if 'inputs' in block:
                        if 'OPERAND1' in block['inputs']:
                            operator_scripts[block_id] = [block['inputs']['OPERAND1'][1][1],
                                                          '=',
                                                          block['inputs']['OPERAND2'][1][1]]
                elif block['opcode'] == "control_if_else":
                    if 'inputs' in block:
                        if 'SUBSTACK' in block['inputs'] and 'SUBSTACK2' in block['inputs']:
                            if_scripts[block_id] = [block['inputs']['CONDITION'][1],
                                                    block['inputs']['SUBSTACK'][1],
                                                    block['inputs']['SUBSTACK2'][1]]
                elif block['opcode'] == "procedures_definition":  # tells what's in it
                    continue
                elif block['opcode'] == "procedures_prototype":  # start here. prototype has defintion as parent

                    default_moves = ['move', 'pickbeeper', 'putbeeper', 'turnleft', 'turnoff']
                    if 'parent' not in block and block['mutation']['proccode'] in default_moves:
                        continue   # Ignore blocks from scratch2 that are default
                    else:
                        procedures_definition_id = block['parent']
                        procedure_name = block['mutation']['proccode']
                        input_ids = block['inputs']
                        input_variables = []
                        for key in input_ids:
                            variable_key = block['inputs'][key][1]
                            print("checking this variable out " + str(variable_key))
                            if variable_key is not None:
                                temp_variable = build_scratch_script(variable_key, blocks)
                                input_variables.append(temp_variable)
                        print("INPUT VARIABLES IS THIS: " + str(input_variables))
                        for input_variable in input_variables:
                            print("input var {} procedure name {}".format(input_variable, procedure_name))
                            procedure_name = re.sub("(%s|%b)", input_variable, procedure_name, count=1)
                        print("NEW PROCEDURE NAME: " + str(procedure_name))
                        script = build_scratch_script(procedures_definition_id, blocks)
                        scripts[procedure_name] = script
                        print("aaa procedure name is this {}".format(procedure_name))
                        print("fff input args {} input_ids {} ".format(len(input_ids), input_ids))
                        print("aaa script for procedure is this {} ".format(script))
                        continue
                elif block['parent']:
                    parent_id = block['parent']
                    parent_block = blocks[parent_id]
                    if parent_block['inputs']:
                        if parent_block['opcode'] == 'control_repeat' or \
                                parent_block['opcode'] == 'control_forever':
                            if 'SUBSTACK' in parent_block['inputs']:
                                if parent_block['inputs']['SUBSTACK'][1] == block_id:
                                    script = build_scratch_script(block_id, blocks)
                                    temp_repeat_commands = []
                                    for item in script:
                                        temp_repeat_commands.append(item)
                                    repeat_scripts[block_id] = temp_repeat_commands
                elif block['parent'] is None:
                    print("yyyy {} doing things without parents now.".format(block_id))
                    script = build_scratch_script(block_id, blocks)
                    scripts[block_id] = script
            # print("All scripts " + str(scripts))
    return scripts


def match_string(regex, p_json, *, points=0, num_matches=1):
    """
    Tries to match regex inside the json.
    :param regex: Regex we are looking for
    :param p_json: json of all blocks in the code(dict).
    :param points: How many points this is worth (int).
    :param num_matches: how many times you want to match (int).
    :return: Dictionary of the test
    """
    import re
    # print("ooo yeah regex {} \njson {}".format(regex, p_json))
    found = len(re.findall(regex, str(p_json), re.X | re.M | re.S))
    p_test = {"name": "Looking for a string in code (" + str(points) + " points)<br>",
              "pass": found >= num_matches,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found this string in the code:  " + str(regex) + "<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Code does not find string we were looking for.<br>"
                              "Looked for this string: " + str(regex) + "<br>" +
                              "Looked in this code: " + str(p_json) + "<br>" +
                              "Found this many matches : " + str(found) + "<br>",
              "points": points if found >= num_matches else 0
              }
    return p_test


def extract_move_steps(p_json):
    """
    Extracts the steps inside the block.
    Will match the all integers.
    :param p_json:  - json of the block you are looking at
    :return: all matches, as a list of integers
    """
    import re
    regex = r"{'opcode':\s+'motion_movesteps',\s+'inputs':\s+{'STEPS':\s+\[1,\s+\[4,\s+'(\d+)']]}"
    matches = re.findall(regex, str(p_json), re.X | re.M | re.S)
    return matches if matches else []


def extract_turn_degrees(p_json):
    """
    Extracts the turn degrees inside the block.
    Will match the all integers integer.
    :param p_json:  - json of the block you are looking at
    :return: all matches, as a list of integers
    """
    import re

    regex = r"{'opcode':\s+'motion_turn(right|left)',\s+'inputs':\s+{'DEGREES':\s+\[1,\s+\[4,\s+'(\d+)']]}"
    matches = re.findall(regex, str(p_json), re.X | re.M | re.S)
    return matches if matches else []


def count_sprites(p_json):
    """
    Finds the number of sprites that are NOT background
    :param p_json:  - json of all code
    :return: all matches, as a list of integers
    """
    num_sprites = 0
    for target in p_json['targets']:
        if target['isStage'] is not True:
            num_sprites += 1
    return num_sprites


def check_num_sprites(p_json, wanted_sprites, *, eq_ge='equal', points=0):
    """
    Checks to see if number of nonbackground sprites is equal or equal/reater than a certain number
    :param p_json:  - json of all code
    :param wanted_sprites - number of sprites looking for (int)
    :param eq_ge: 'equal' or 'greaterthanequal' for equal or greater than/equal (string)
    :param points:  - points this is worth (int)
    :return: a dictionary with test info.
    """
    eq_ge_strings = {'equal': 'equal to',
                     'greaterthanequal': 'greater than or equal to',
                     }
    eq_ge_strings2 = {'equal': 'exactly',
                      'greaterthanequal': 'equal or more than'}
    p_test = {"name": "Checking the number of (non-background) sprite is " + eq_ge_strings[eq_ge] + " " +
                      str(wanted_sprites) + " (" + str(points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Code has correct number of sprites.<br>",
              "fail_message":  "<h5 style=\"color:red;\">Fail.</h5> Code has incorrect number of sprites.<br>",
              "points": 0
              }
    num_sprites = count_sprites(p_json)
    if eq_ge == 'equal':
        print()
        if num_sprites != wanted_sprites:
            p_test['pass'] = False
    elif eq_ge == 'greaterthanequal':
        if num_sprites < wanted_sprites:
            p_test['pass'] = False
    else:
        print("check_num_sprites has a bug")
    if p_test['pass'] is False:
        p_test['fail_message'] = "<h5 style=\"color:purple;\">" \
                                 "You are supposed to have " + eq_ge_strings2[eq_ge] + " " + str(wanted_sprites) + \
                                     " sprite(s).  You have " + str(num_sprites) + \
                                     " sprites.  Please merge code into " + str(wanted_sprites) +\
                                     " sprite(s).<br> </h5>"
    else:
        p_test['points'] += points
    return p_test


# To be deleted when check_num_sprites sed
def one_sprite(p_json, p_points=0):
    """
    Finds the number of sprites that are NOT background
    :param p_json:  - json of all code
    :param p_points:  - points this is worth (int)
    :return: a dictionary with test info.
    """
    p_test = {"name": "Checking there is only one (non-background) sprite (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Code has one (non-background) sprite.<br>",
              "points": 0
              }
    num_sprites = count_sprites(p_json)
    if num_sprites != 1:
        p_test['pass'] = False
        p_test['fail_message'] = "<h5 style=\"color:red;\">Fail.</h5> <br> " \
                                 "<h5 style=\"color:purple;\">You have too many sprites.  You are supposed to have " \
                                 "one sprite.  You have " + str(num_sprites) + \
                                 " sprites.  Please merge code into one sprite and recheck.<br> </h5>"
    return p_test


# To be deleted when check_num_sprites sed
def two_sprites(p_json, p_points=0):
    """
    Finds the number of sprites that are NOT background
    :param p_json:  - json of all code
    :param p_points:  - points this is worth (int)
    :return: a dictionary with test info.
    """
    p_test = {"name": "Checking there are exactly two (non-background) sprites (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Code has exactly two (non-background) sprites.<br>",
              "points": 0
              }
    num_sprites = count_sprites(p_json)
    if num_sprites != 2:
        p_test['pass'] = False
        p_test['fail_message'] = "<h5 style=\"color:red;\">Fail.</h5> <br> " \
                                 "<h5 style=\"color:purple;\">You have wrong number of sprites.  " \
                                 "You are supposed to have exactly " \
                                 "two sprites.  You have " + str(num_sprites) + \
                                 " sprites.  <br>Please use exactly two sprites for this lab.<br> </h5>"
    else:
        p_test['points'] += p_points
    return p_test


def press_zero(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary\
    """
    # from app.scratch_labs.scratch import match_string, one_event

    p_test = {"name": "Checking that there is a script that has 'when 0 key is pressed' along with a "
                      "pen down, goto 0 0, clear, and point 90. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found the strings in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "<h5 style=\"color:purple;\">"
                              'See example here: '
                              '<a href="https://docs.google.com/presentation/d/18HDDCHckIsuphA91LbFHyS272PIiG4f5wxRQE3K'
                              'Rc2g/edit#slide=id.g74c3b39ec7_0_0" target="_blank">link to page of presentation</a>.'
                              '</h5>',
              "points": 0
              }
    [test_one_zero, zero_script] = one_event(p_scripts, "'event_whenkeypressed',\s'0'")
    if test_one_zero['pass'] is False:
        p_test['fail_message'] += test_one_zero['fail_message']
        return p_test

    test_pendown = match_string(r"\['event_whenkeypressed', \s '0'] .+ 'pen_penDown'", zero_script)
    if test_pendown['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a 'when 0 pressed' followed by a 'pen down'.<br></h5>"
    test_clear = match_string(r"\['event_whenkeypressed', \s '0'] .+ 'pen_clear'", zero_script)
    if test_clear['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a 'when 0 pressed' followed by an 'erase all'.<br></h5>"
    test_point = match_string(r"\['event_whenkeypressed', \s '0'] .+ \['motion_pointindirection', \s '90']",
                              zero_script)
    if test_point['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a 'when 0 pressed' followed by a 'point in direction 90'.<br>" \
                                  "</h5>"
    test_goto = match_string(r"\['event_whenkeypressed', \s '0'] .+ \['motion_gotoxy', \s '0', \s '0'],",
                             zero_script)
    if test_goto['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a 'when 0 pressed' followed by 'goto 0 0'.<br>" \
                                  "</h5>"
    if test_pendown['pass'] and test_clear['pass'] and test_point['pass'] and test_goto['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_greenflag(p_scripts, p_points):
    """
    :param p_scripts: json data from file, which is the code of the scratch file. (dict)
    :param p_points: Number of points this test is worth (int)
    :return: The test dictionary\
    """
    # from app.scratch_labs.scratch import match_string, one_event

    p_test = {"name": "Checking that there is a script that has a green flag along with a "
                      "pen down, goto 0 0, clear, and point 90. (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "We found the strings in the code!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "<h5 style=\"color:purple;\">"
                              'See example here: '
                              '<a href="https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62l'
                              'FVITA/edit#slide=id.g842921740d_0_5" target="_blank">link to page of presentation</a>.'
                              '</h5>',
              "points": 0
              }
    [test_one_flag, flag_script] = one_event(p_scripts, "event_whenflagclicked")
    if test_one_flag['pass'] is False:
        p_test['fail_message'] += test_one_flag['fail_message']
        return p_test
    test_pendown = match_string(r"\['event_whenflagclicked' .+ 'pen_penDown'", flag_script)
    if test_pendown['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a green flag followed by a 'pen down'.<br></h5>"
    test_clear = match_string(r"\['event_whenflagclicked' .+ 'pen_clear'", flag_script)
    if test_clear['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a green flag followed by an 'erase all'.<br></h5>"
    test_point = match_string(r"\['event_whenflagclicked' .+ \['motion_pointindirection', \s '90']",
                              flag_script)
    if test_point['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a a green flag followed by a 'point in direction 90'.<br>" \
                                  "</h5>"
    test_goto = match_string(r"\['event_whenflagclicked' .+ \['motion_gotoxy', \s '0', \s '0'],",
                             flag_script)
    if test_goto['pass'] is False:
        p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                  "Did not find a green flag followed by 'goto 0 0'.<br>" \
                                  "</h5>"
    if test_pendown['pass'] and test_clear['pass'] and test_point['pass'] and test_goto['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_string_in_script(p_scripts, this_test, p_points):
    """
    Finds a string (multiple strings) in script.  Assumes one sprite.
    Similar to find_block_in_sprite except allows multiple searches and expects a certain event at top.
    More specific testing
    :param p_scripts: scripts from the sprite (dict)
    :param this_test: name of test (string)
    :param p_points: points (int)
    :return: Test dictionary
    """
    this_test_description = {'22_press_zero': [['press zero followed by pen clear',
                                                'pen_clear'],
                                               ['press zero followed by pen down',
                                                'pen_penDown'],
                                               ['press zero followed by point direction 90',
                                                'motion_pointindirection .*? \s \'90\''],
                                               ['press zero followed by goto -160, -180',
                                                "'motion_gotoxy', \s '-160', \s '-180'"],
                                               ['press zero followed by change of pen color',
                                                "(pen_setPenColorToColor|pen_setPenColorParamTo)"],
                                               ],
                             '22_1_1': [['draws a rectangle (using correct number of repeats)',
                                         " \['control_repeat', \s '2' .*? motion_movesteps .*? motion_turn .*? "
                                         ".*? motion_movesteps "],
                                        ],
                             '22_1_2': [['draws a rectangle but turns the wrong way ',
                                         " ('motion_turnright', \s '[0-9]+'|'motion_turnleft', \s '-[0-9]+')"],

                                        ],
                             '22_2_1': [['draws a rectangle (using correct number of repeats)',
                                         " \['control_repeat', \s '2' .*? motion_movesteps .*? motion_turn .*? "
                                         ".*? motion_movesteps "],
                                        ],
                             '22_2_2': [['draws a rectangle but turns the wrong way ',
                                         " ('motion_turnright', \s '[0-9]+'|'motion_turnleft', \s '-[0-9]+')"],
                                        ],
                             '22_2_3': [['draws two rectangle (using correct number of repeats for maximum efficiency)',
                                         "\['control_repeat', \s '2', \s \[\['control_repeat', \s '2' .*? "
                                         "motion_movesteps"
                                         " .*? motion_turn .*? .*? motion_movesteps "],
                                        ],
                             '22_3_1': [['draws a rectangle (using correct number of repeats)',
                                         " \['control_repeat', \s '2' .*? motion_movesteps .*? motion_turn .*? "
                                         ".*? motion_movesteps "],
                                        ],
                             '22_3_2': [['draws a rectangle but turns the wrong way ',
                                         " ('motion_turnright', \s '[0-9]+'|'motion_turnleft', \s '-[0-9]+')"],
                                        ],
                             '22_3_3': [['draws two rectangle (using correct number of repeats for maximum efficiency)',
                                         "\['control_repeat', \s '8', \s \[\['control_repeat', \s '2' .*?"
                                         " motion_movesteps"
                                         " .*? motion_turn .*? .*? motion_movesteps "],
                                        ],
                             '23name': [['green flag followed by asking a question with "name" in it',
                                         'event_whenflagclicked .+ sensing_askandwait'],
                                        ['question that has the word "name" in it',
                                         '(name|Name)']
                                        ],
                             '23triangle': [['green flag followed by asking a question with "triangle" in it',
                                             'event_whenflagclicked .+ sensing_askandwait'],
                                            ['question that has the word "triangle" in it',
                                             '(triangle|Triangle)']
                                            ],
                             '23feel': [['green flag followed by asking a question with "feel" in it',
                                         'event_whenflagclicked .+ sensing_askandwait'],
                                        ['question that has the word "feel" in it (i.e. how do you feel)',
                                         '(feel|Feel)']
                                        ],
                             '23a_draw_triangle': [['green flag followed by repeat 3',
                                                    "\'control_repeat\', \s \'3\'"],
                                                   ['repeat 3 followed by moving answer',
                                                    "control_repeat .*? 3 .*? \'motion_movesteps\',"
                                                    "\s \'sensing_answer\'"],
                                                   ['repeat 3 followed by turning correct angle for triangle',
                                                    "control_repeat .*? 3 .*? \'motion_turn .*? 120"]
                                                   ],
                             '23b_color_change_1': [['if sensing_answer = blue with something inside it',
                                                     'control_if .+? operator_equals .+?  sensing_answer .+? '
                                                     '(Blue|blue)'],
                                                    ['if sensing_answer = blue, switch backdrop (or next backdrop)',
                                                     'control_if .+? operator_equals .+? sensing_answer .+? '
                                                     'blue .+?'
                                                     '(looks_switchbackdropto|looks_nextbackdrop)']
                                                    ],
                             '23b_costume_change': [['if sensing_answer = CRLS with something inside it',
                                                     'control_if .+? operator_equals .+?  sensing_answer. +? CRLS'],
                                                    ['if sensing_answer = CRLS, change costume (or next costume)',
                                                     'control_if .+? operator_equals .+? sensing_answer .+? CRLS .+?'
                                                     '(looks_switchcostumeto|looks_nextcostume)']
                                                    ],
                             '23b_question_ifelse': [['asks question followed by if/else after color and costume '
                                                      'checks',
                                                      'sensing_askandwait .+? control_if_else'],
                                                     ['asks question followed by if/else with say inside if/else '
                                                      'after color and costume checks',
                                                      'sensing_askandwait .+? control_if_else .+? '
                                                      '\[. +? \[ .+? looks_say .+? ] .+?'
                                                      '\[ .+? looks_say .+? ] ']
                                                     ],
                             '23b_two_question': [['asks two questions, each followed by if/else with say inside '
                                                   '(all after color/costume checks)',
                                                   'sensing_askandwait .+? control_if_else .+ \[ .+? looks_say .+? ]'
                                                   ' .+? \[ .+ looks_say .+ ]  .+? '
                                                   'sensing_askandwait .+? control_if_else .+? \[ .+?  looks_say .+? ] '
                                                   '.+? \[ .+ looks_say .+? ] ']
                                                  ],
                             '24_green_flag': [['green flag followed by asking a question',
                                                'event_whenflagclicked .+? sensing_askandwait'],
                                               ['green flag followed by asking a question and setting a variable',
                                                'event_whenflagclicked .+? sensing_askandwait .+? data_setvariableto'],
                                               ],
                             '24_name_variable_to_answer': [['green flag followed by setting name variable to answer',
                                                             'data_setvariableto .*? name .*? sensing_answer'],
                                                            ],
                             '24_set_random': [['green flag followed by setting number variable to random number '
                                                'between 1-10.  Setting number to random number should be in 1 block.',
                                                'event_whenflagclicked .+? data_setvariableto .*? number .*? '
                                                'operator_random .*? 1 .*? 10']
                                               ],
                             '24_ifelse': [['green flag followed by asking a question followed by an if/else block',
                                            'event_whenflagclicked .+? sensing_askandwait .+? control_if_else'
                                            ]
                                           ],
                             '26_greenflag_forever': [['green flag followed by a forever under it',
                                                       'event_whenflagclicked .+? (control_repeat|control_forever)'],
                                                      ],
                             '26_test_fall': [['green flag followed by sprite forever falling (with a changey)',
                                               r"event_whenflagclicked .+? (control_repeat|control_forever) .+?"
                                               r" motion_changeyby', \s '(-[0-9]|VARIABLE) .*? ]", ]
                                              ],
                             '26_top_1': [['green flag IMMEDIATELY followed by sety to higher than 125 ',
                                           "'event_whenflagclicked' .+? 'motion_sety', \s+ '(-?[0-9]+)'", ]
                                          ],
                             '26_top_2': [['green flag IMMEDIATELY followed by gotoxy to y higher than 125 ',
                                           "'event_whenflagclicked' .+? 'motion_gotoxy',  .+? ,\s+ '([0-9]+)", ]
                                          ],
                             '26_random_x_1': [['green flag followed by goto xy with x being random number between '
                                                '-240 and 240',
                                                "'event_whenflagclicked' .+? 'motion_gotoxy', .+ 'operator_random', "
                                                "\s '-240', \s '240'", ]
                                               ],
                             '26_random_x_2': [['green flag followed by set x with x being random number between '
                                                '-240 and 240',
                                                "'event_whenflagclicked' .+? 'motion_setx', .+ 'operator_random', \s "
                                                " '-240', \s '240'", ]
                                               ],
                             '26_ground_1': [['sprite keeps moving if not touching ground',
                                              "(control_repeat|control_forever) .+ control_if .+ operator_not .+  "
                                              "'sensing_touchingobject' .+ 'sensing_touchingobjectmenu', \s* 'ground'",
                                              ]],
                             '26_ground_2': [['sprite stop if touching ground, else moves',
                                              "(control_repeat|control_forever) .+? control_if_else .+? "
                                              r"\[ 'sensing_touchingobject' .+? 'sensing_touchingobjectmenu', "
                                              r"\s* 'ground' .+? \]  .+? \[ 'motion_changeyby', \s '-",
                                              ]],
                             '26_ground_3': [['sprite moves until touching ground',
                                              " control_repeat_until .+? "
                                              r"'sensing_touchingobject' .+? 'sensing_touchingobjectmenu', "
                                              r"\s* 'ground' .+? 'motion_changeyby',\s'-",
                                              ]],
                             '26_platform_or_ground_1': [['sprite stops when touching platform OR ground',
                                                          "operator_or .+? sensing_touchingobject .+? "
                                                          "sensing_touchingobjectmenu "
                                                          ".+? ground  .+? 'sensing_touchingobject' .+? "
                                                          "'sensing_touchingobjectmenu .+? platform'", ]
                                                         ],
                             '26_platform_or_ground_2': [['sprite stop when touching platform OR ground',
                                                          "operator_or .+? sensing_touchingobject .+? "
                                                          "sensing_touchingobjectmenu "
                                                          ".+? platform  .+? 'sensing_touchingobject' .+? "
                                                          "'sensing_touchingobjectmenu .+? ground'", ]
                                                         ],
                             '26_platform_or_ground_3': [['sprite stop when touching platform OR ground',
                                                          "(control_if .+? sensing_touchingobject .+? "
                                                          "sensing_touchingobjectmenu .+? platform .+? "
                                                          "control_if .*? 'sensing_touchingobject' .+? "
                                                          "'sensing_touchingobjectmenu .+? ground' | "
                                                          "control_if .+? sensing_touchingobject .+? "
                                                          "sensing_touchingobjectmenu .+? ground .+? control_if .*?"
                                                          " 'sensing_touchingobject' .+? 'sensing_touchingobjectmenu "
                                                          ".+? platform' )", ]
                                                         ],
                             '35_turn_right_1': [[
                                 'Hero sprite turns right if right arrow pressed (forever+if key pressed)',
                                 "control_repeat \', \s 150 .+? control_if .+? \[\'sensing_keypressed .+? "
                                 "\[\'sensing_keyoptions .+? right \s arrow .+? motion_pointindirection\', \s \'90\'"]],
                             '35_turn_right_2': [[
                                 'Hero sprite turns right if right arrow pressed (When key pressed)',
                                 '\'motion_pointindirection\', \s \'90\']']],
                             '35_turn_left_1': [[
                                 'Hero sprite turns left if left arrow pressed (forever+if key pressed)',
                                 "control_repeat \', \s 150 .+? control_if .+? \[\'sensing_keypressed .+? "
                                 "\[\'sensing_keyoptions .+? left \s arrow .+?"
                                 " motion_pointindirection\', \s \'(270|-90)\'"]],
                             '35_turn_left_2': [[
                                 'Hero sprite turns left if left arrow pressed (When key pressed)',
                                 '\'motion_pointindirection\', \s \'(270|-90)\']']],
                             '35_animated_walk_1': [[
                                 'animated walk for hero when right arrow pressed',
                                 "control_repeat \', \s 150 .+? control_if .+? \[\'sensing_keypressed .+? "
                                 "\[\'sensing_keyoptions .+? right \s arrow .+?"
                                 " looks_(switchcostume|nextcostume)"],
                             ],
                             '35_animated_walk_2': [[
                                 'animated walk for hero when right arrow pressed',
                                 'looks_(switchcostume|nextcostume)']],
                             '35_jump_1': [[
                                 'jump when space pressed',
                                 "control_repeat \', \s 150 .+? control_if .+? \[\'sensing_keypressed .+? "
                                 "\[\'sensing_keyoptions .+? space .+?"
                                 " (motion_changeyby| motion_turn .+? motion_move .+? motion_turn .+?)"],
                             ],
                             '35_jump_2': [[
                                 'jump when space pressed',
                                 '(motion_changeyby| motion_turn .+? motion_move .+? motion_turn .+?)']],
                             '35_layers_1': [[
                                 'Hero sprite is always on the front layer',
                                 'control_repeat \', \s 150 .+?  looks_(goforwardbackwardlayers|gotofrontback)']],
                             '35_layers_2': [[
                                 'Hero sprite is always on the front layer',
                                 "event_whenkeypressed .+? left \s arrow .+? "
                                 "looks_(goforwardbackwardlayers|gotofrontback)"]],
                             '35_enemy_animated_walk_1': [[
                                 'animated enemy under a green flag, in a forever',
                                 "control_repeat \', \s 150 .+? looks_(switchcostume|nextcostume)"],
                             ],
                             '35_enemy_animated_walk_2': [[
                                 'animated walk for enemy when right arrow pressed',
                                 'looks_(switchcostume|nextcostume)']],
                             '35_enemy_animated_walk_3': [[
                                 'animated walk for hero when right arrow pressed',
                                 'looks_(switchcostume|nextcostume)']],
                             '35_scenery1_1': [[
                                 'scenery 1 moves right when left arrow pressed (with some lag)',
                                 "event_whenkeypressed .+? left \s arrow .+? "
                                 "(motion_movesteps .+? \' [0-9]+ \'|motion_changexby .+? \' [0-9]+ \')"],
                             ],
                             '35_scenery1_2': [[
                                 'scenery 1 moves right when left arrow pressed',
                                 "control_repeat .+? 150 .+? control_if .+? sensing_keypressed .+? "
                                 "sensing_keyoptions .+? left \s arrow .+? "
                                 "(motion_movesteps|changexby)\', \s \'[0-9]+ \'"],
                             ],
                             '35_scenery1_3': [[
                                 'scenery 1 moves right when left arrow pressed (broadcastversion)',
                                 "event_whenbroadcastreceived .+? "
                                 "(motion_movesteps\', \s \' [0-9]+ \'| motion_changexby\', \s \' [0-9]+ \')"],
                             ],
                             '35_scenery1_4': [[
                                 'scenery 1 moves left when right arrow pressed (with some lag)',
                                 "event_whenkeypressed .+? right \s arrow .+? "
                                 "(motion_turn .*? motion_movesteps .+? \' [0-9]+ \'|"
                                 "motion_movesteps .+? \' -[0-9]+ \'|motion_changexby .+? \' -[0-9]+ \')"],
                             ],
                             '35_scenery1_5': [[
                                 'scenery 1 moves left when right arrow pressed',
                                 "control_repeat .+? 150 .+? control_if .+? sensing_keypressed .+? "
                                 "sensing_keyoptions .+? right \s arrow .+? "
                                 "(motion_turn .*? motion_movesteps .+? \' [0-9]+ \'|"
                                 "motion_movesteps .+? \' -[0-9]+ \'|motion_changexby .+? \' -[0-9]+ \')"],
                             ],
                             '35_scenery1_6': [[
                                 'scenery 1 moves left when rightarrow pressed (broadcastversion)',
                                 "event_whenbroadcastreceived .+? "
                                 "(motion_turn .*? motion_movesteps .+? \' [0-9]+ \'|"
                                 "motion_movesteps .+? \' -[0-9]+ \'|motion_changexby .+? \' -[0-9]+ \')"],
                             ],
                             '35_scenery2_1': [[
                                 'scenery 2 moves right when left arrow pressed (with some lag)',
                                 "event_whenkeypressed .+? left \s arrow .+? "
                                 "(motion_movesteps .+? \' [0-9]+ \'|motion_changexby .+? \' [0-9]+ \')"],
                             ],
                             '35_scenery2_2': [[
                                 'scenery 2 moves right when left arrow pressed',
                                 "control_repeat .+? 150 .+? control_if .+? sensing_keypressed .+? "
                                 "sensing_keyoptions .+? left \s arrow .+? "
                                 "(motion_movesteps|changexby)\', \s \'[0-9]+ \'"],
                             ],
                             '35_scenery2_3': [[
                                 'scenery 2 moves right when left arrow pressed (broadcastversion)',
                                 "event_whenbroadcastreceived .+? "
                                 "(motion_movesteps\', \s \' [0-9]+ \'| motion_changexby\', \s \' [0-9]+ \')"],
                             ],
                             '35_scenery2_4': [[
                                 'scenery 2 moves left when right arrow pressed (with some lag)',
                                 "event_whenkeypressed .+? right \s arrow .+? "
                                 "(motion_turn .*? motion_movesteps .+? \' [0-9]+ \'|"
                                 "motion_movesteps .+? \' -[0-9]+ \'|motion_changexby .+? \' -[0-9]+ \')"],
                             ],
                             '35_scenery2_5': [[
                                 'scenery 2 moves left when right arrow pressed',
                                 "control_repeat .+? 150 .+? control_if .+? sensing_keypressed .+? "
                                 "sensing_keyoptions .+? right \s arrow .+? "
                                 "(motion_turn .*? motion_movesteps .+? \' [0-9]+ \'|"
                                 "motion_movesteps .+? \' -[0-9]+ \'|motion_changexby .+? \' -[0-9]+ \')"],
                             ],
                             '35_scenery2_6': [[
                                 'scenery 2 moves left when rightarrow pressed (broadcastversion)',
                                 "event_whenbroadcastreceived .+? "
                                 "(motion_turn .*? motion_movesteps .+? \' [0-9]+ \'|"
                                 "motion_movesteps .+? \' -[0-9]+ \'|motion_changexby .+? \' -[0-9]+ \')"],
                             ],
                             '35_scenery1_rollover_1': [[
                                 'scenery 1 rolls over when going off left side of screen (when right key pressed)',
                                 "event_whenkeypressed .+? right \s arrow .+? "
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \'|motion_goto)'],
                             ],
                             '35_scenery1_rollover_2': [[
                                 'scenery 1 rolls over when going off left side of screen (checking forever)',
                                 "control_repeat .+? 150 .+? "
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \'|motion_goto)'],
                             ],
                             '35_scenery1_rollover_3': [[
                                 'scenery 1 rolls over when going off left side of screen (broadcast version)',
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \'|motion_goto)'],
                             ],
                             '35_scenery1_rollover_4': [[
                                 'scenery 1 rolls over when going off right side of screen (when left key pressed)',
                                 "event_whenkeypressed .+? left \s arrow .+? "
                                 "control_if .+? (operator_gt .+? motion_xposition .+?  ([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx .*?  ([0-9]+)|motion_changexby \' -([0-9]+) \'|'
                                 'motion_movesteps \' -([0-9]+) \'| '
                                 'motion_turn .*?   motion_movesteps \' ([0-9]+) \') | motion_goto )'],
                             ],
                             '35_scenery1_rollover_5': [[
                                 'scenery 1 rolls over when going off right side of screen (checking forever)',
                                 "control_repeat .+? 150 .+? "
                                 "control_if .+? (operator_gt .+? motion_xposition .+?  ([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx .*?  ([0-9]+) |motion_changexby \' -([0-9]+) \'|'
                                 'motion_movesteps \' -([0-9]+) \'| '
                                 'motion_turn .*?   motion_movesteps \' ([0-9]+) \') | motion_goto )'],
                             ],
                             '35_scenery1_rollover_6': [[
                                 'scenery 1 rolls over when going off right side of screen (broadcast version)',
                                 "control_if .+? (operator_gt .+? motion_xposition .+?  ([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx .*? ([0-9]+)|motion_changexby \' -([0-9]+) \'|'
                                 'motion_movesteps \' -([0-9]+) \'| '
                                 'motion_turn .*?   motion_movesteps \' ([0-9]+) \') | motion_goto )'],
                             ],
                             '35_scenery2_rollover_1': [[
                                 'scenery 2 rolls over when going off left side of screen (when right key pressed)',
                                 "event_whenkeypressed .+? right \s arrow .+? "
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \' | motion_goto)'],
                             ],
                             '35_scenery2_rollover_2': [[
                                 'scenery 2 rolls over when going off left side of screen (checking forever)',
                                 "control_repeat .+? 150 .+? "
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \' | motion_goto)'],
                             ],
                             '35_scenery2_rollover_3': [[
                                 'scenery 2 rolls over when going off left side of screen (broadcast version)',
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \' | motion_goto)'],
                             ],
                             '35_scenery2_rollover_4': [[
                                 'scenery 2 rolls over when going off right side of screen (when left key pressed)',
                                 "event_whenkeypressed .+? left \s arrow .+? "
                                 "control_if .+? (operator_gt .+? motion_xposition .+?  ([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx .*? \' -([0-9]+) \'|motion_changexby \' -([0-9]+) \'|'
                                 'motion_movesteps \' -([0-9]+) \'| '
                                 'motion_turn .*?   motion_movesteps \' ([0-9]+) \') | motion_goto)'],
                             ],
                             '35_scenery2_rollover_5': [[
                                 'scenery 2 rolls over when going off right side of screen (checking forever)',
                                 "control_repeat .+? 150 .+? "
                                 "control_if .+? (operator_gt .+? motion_xposition .+?  ([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx .*? \' -([0-9]+) \'|motion_changexby \' -([0-9]+) \'|'
                                 'motion_movesteps \' -([0-9]+) \'| '
                                 'motion_turn .*?   motion_movesteps \' ([0-9]+) \') | motion_goto)'],
                             ],
                             '35_scenery2_rollover_6': [[
                                 'scenery 2 rolls over when going off right side of screen (broadcast version)',
                                 "control_if .+? (operator_gt .+? motion_xposition .+?  ([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx .*? \' -([0-9]+) \'|motion_changexby \' -([0-9]+) \'|'
                                 'motion_movesteps \' -([0-9]+) \'| '
                                 'motion_turn .*?   motion_movesteps \' ([0-9]+) \') | motion_goto)'],
                             ],
                             '35_enemy_move': [[
                                 'enemy moves continuously in x direction towards hero with move or changex by (not '
                                 'glide or goto)',
                                 " control_repeat \', \s 150 .+? (changexby .+? -| motion_move) "],
                             ],
                             '35_enemy_rollover_1': [[
                                 'enemy rolls over when going off left side of screen (when right key pressed)',
                                 "event_whenkeypressed .+? right \s arrow .+? "
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \'| motion_goto)'],
                             ],
                             '35_enemy_rollover_2': [[
                                 'enemy rolls over when going off left side of screen (checking forever)',
                                 "control_repeat .+? 150 .+? "
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \'| motion_goto)'],
                             ],
                             '35_enemy_rollover_3': [[
                                 'enemy rolls over when going off left side of screen (broadcast version)',
                                 "control_if .+? (operator_lt .+? motion_xposition .+?  -([0-9]+?) \'|"
                                 "sensing_touchingobject .+? sensing_touchingobjectmenu .+? _edge_ ) .+?"
                                 '((motion_setx|motion_changexby|motion_movesteps) .+?  \' ([0-9]+) \'| motion_goto)'],
                             ],
                             '35_stop_1': [[
                                 'stop game when hero touches enemy',
                                 'control_repeat .+? 150 .+? control_if .+? sensing_touchingobject .+? '
                                 'sensing_touchingobjectmenu .+? enemy ']],
                             '35_stop_2': [[
                                 'stop game when hero touches enemy',
                                 'control_repeat .+? 150 .+? control_if .+? sensing_touchingobject .+? '
                                 'sensing_touchingobjectmenu .+? hero ']],
                             '42_6': [['When "x" pressed, followed by two questions',
                                       "event_whenkeypressed', \s 'x' .+ sensing_askandwait .+ sensing_askandwait'"
                                       ]
                                      ],
                             '43a_1': [['when "1" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '1' .+  control_repeat"
                                        ],
                                       ['when "1" pressed looks approximately correct (has a set variable)',
                                        "event_whenkeypressed', \s '1' .+  data_setvariableto"
                                        ],
                                       ['when "1" pressed looks approximately correct (has a say)',
                                        "event_whenkeypressed', \s '1' .+  looks_sayforsecs"
                                        ],
                                       ['when "1" pressed looks approximately correct (has a change variable)',
                                        "event_whenkeypressed', \s '1' .+  data_changevariableby"
                                        ],
                                       ],
                             '43a_3': [['when "2" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '2' .+  control_repeat"
                                        ],
                                       ['when "2" pressed looks approximately correct (has a set variable)',
                                        "event_whenkeypressed', \s '2' .+  data_setvariableto"
                                        ],
                                       ['when "2" pressed looks approximately correct (has a say)',
                                        "event_whenkeypressed', \s '2' .+  looks_sayforsecs"
                                        ],
                                       ['when "2" pressed looks approximately correct (has a change variable)',
                                        "event_whenkeypressed', \s '2' .+  data_changevariableby"
                                        ],
                                       ],
                             '43a_5': [['when "3" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '3' .+  control_repeat"
                                        ],
                                       ['when "3" pressed looks approximately correct (has a set variable)',
                                        "event_whenkeypressed', \s '3' .+  data_setvariableto"
                                        ],
                                       ['when "3" pressed looks approximately correct (has a say)',
                                        "event_whenkeypressed', \s '3' .+  looks_sayforsecs"
                                        ],
                                       ['when "3" pressed looks approximately correct (has a change variable)',
                                        "event_whenkeypressed', \s '3' .+  data_changevariableby"
                                        ],
                                       ],
                             '43a_7': [['when "4" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '4' .+  control_repeat"
                                        ],
                                       ['when "4" pressed looks approximately correct (has a set variable)',
                                        "event_whenkeypressed', \s '4' .+  data_setvariableto"
                                        ],
                                       ['when "4" pressed looks approximately correct (has a say)',
                                        "event_whenkeypressed', \s '4' .+  looks_sayforsecs"
                                        ],
                                       ['when "4" pressed looks approximately correct (has a change variable)',
                                        "event_whenkeypressed', \s '4' .+  data_changevariableby"
                                        ],
                                       ],
                             '43b_1': [['when "1" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '1' .+?  control_repeat"
                                        ],
                                       ['when "1" pressed looks approximately correct (has a set variable)',
                                        "event_whenkeypressed', \s '1' .+?  data_setvariableto"
                                        ],
                                       ['when "1" pressed looks approximately correct (has a say)',
                                        "event_whenkeypressed', \s '1' .+?  looks_sayforsecs"
                                        ],
                                       ['when "1" pressed looks approximately correct (has a change variable)',
                                        "event_whenkeypressed', \s '1' .+?  data_changevariableby"
                                        ],
                                       ['when "1" pressed looks approximately correct (has an if block)',
                                        "event_whenkeypressed', \s '1' .+?  control_if"
                                        ],
                                       ['when "1" pressed looks approximately correct (has an operator block checking '
                                        'for length of word)',
                                        "event_whenkeypressed', \s '1' .+?  control_if .+? operator_length"
                                        ],
                                       ],
                             '43b_3': [['when "2" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '2' .+?  control_repeat"
                                        ],
                                       ['when "2" pressed looks approximately correct (has a set variable)',
                                        "event_whenkeypressed', \s '2' .+?  data_setvariableto"
                                        ],
                                       ['when "2" pressed looks approximately correct (has a say)',
                                        "event_whenkeypressed', \s '2' .+?  looks_sayforsecs"
                                        ],
                                       ['when "2" pressed looks approximately correct (has a change variable)',
                                        "event_whenkeypressed', \s '2' .+?  data_changevariableby"
                                        ],
                                       ['when "2" pressed looks approximately correct (has an if block)',
                                        "event_whenkeypressed', \s '2' .+?  control_if"
                                        ],
                                       ['when "2" pressed looks approximately correct (has an operator block checking '
                                        'for letter of word)',
                                        "event_whenkeypressed', \s '2' .+?  control_if .+? operator_letter_of"
                                        ],
                                       ],
                             '43b_5': [['when "3" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '3' .+?  control_repeat"
                                        ],
                                       ['when "3" pressed looks approximately correct (has a set variable)',
                                        "event_whenkeypressed', \s '3' .+?  data_setvariableto"
                                        ],
                                       ['when "3" pressed looks approximately correct (has a say)',
                                        "event_whenkeypressed', \s '3' .+?  looks_sayforsecs"
                                        ],
                                       ['when "3" pressed looks approximately correct (has a change variable)',
                                        "event_whenkeypressed', \s '3' .+?  data_changevariableby"
                                        ],
                                       ['when "3" pressed looks approximately correct (has an if block)',
                                        "event_whenkeypressed', \s '3' .+?  control_if"
                                        ],
                                       ['when "3" pressed looks approximately correct (has an operator block checking '
                                        'for letter of word)',
                                        "event_whenkeypressed', \s '3' .+?  control_if .+? operator_letter_of"
                                        ],
                                       ],
                             '43b_7': [['when "4" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '4' .+?  control_repeat"
                                        ],
                                       ['when "4" pressed looks approximately correct (has a set variable)',
                                        "event_whenkeypressed', \s '4' .+?  data_setvariableto"
                                        ],
                                       ['when "4" pressed looks approximately correct (has a say)',
                                        "event_whenkeypressed', \s '4' .+?  looks_sayforsecs"
                                        ],
                                       ['when "4" pressed looks approximately correct (has a change variable)',
                                        "event_whenkeypressed', \s '4' .+?  data_changevariableby"
                                        ],
                                       ['when "4" pressed looks approximately correct (has an if block)',
                                        "event_whenkeypressed', \s '4' .+?  control_if"
                                        ],
                                       ['when "4" pressed looks approximately correct (has an operator block checking '
                                        'for letter of word)',
                                        "event_whenkeypressed', \s '4' .+?  control_if .+? operator_contains"
                                        ],
                                       ],
                             '44_2': [['when "2" pressed looks approximately correct (loop)',
                                       "event_whenkeypressed', \s '2' .+?  control_repeat"
                                       ],
                                      ['when "2" pressed looks approximately correct (needs TWO set variable).'
                                       '<br>One set for a counter, one set for the initial sum',
                                       "event_whenkeypressed', \s '2' .*?  data_setvariableto .*?  data_setvariableto "
                                       ],
                                      ['when "2" pressed looks approximately correct (needs a say)',
                                       "event_whenkeypressed', \s '2' .+?  looks_sayforsecs"
                                       ],
                                      ['when "2" pressed looks approximately correct (needs TWO change variable)'
                                       '<br>One change for the counter in loop, one to change the sum',
                                       "event_whenkeypressed', \s '2' .+?  data_changevariableby .*? "
                                       "data_changevariableby"
                                       ],
                                      ],
                             '44_4': [['when "3" pressed looks approximately correct (loop)',
                                       "event_whenkeypressed', \s '3' .+?  control_repeat"
                                       ],
                                      ['when "3" pressed looks approximately correct (needs TWO set variable).'
                                       '<br>One set for a counter, one set for the initial sum',
                                       "event_whenkeypressed', \s '3' .*?  data_setvariableto .*?  data_setvariableto "
                                       ],
                                      ['when "3" pressed looks approximately correct (needs a say)',
                                       "event_whenkeypressed', \s '3' .+?  looks_sayforsecs"
                                       ],
                                      ['when "3" pressed looks approximately correct (needs a change variable)'
                                       '<br>One change for the counter in loop',
                                       "event_whenkeypressed', \s '3' .+?  data_changevariableby"
                                       ],
                                      ['when "3" pressed looks approximately correct (needs an if)'
                                       '<br>To check if there is a negative number',
                                       "event_whenkeypressed', \s '3' .+?  control_if"
                                       ],
                                      ],
                             '44_6': [['when "4" pressed looks approximately correct (loop)',
                                       "event_whenkeypressed', \s '4' .+?  control_repeat"
                                       ],
                                      ['when "4" pressed looks approximately correct (needs TWO set variable).'
                                       '<br>One set for a counter, one set for the initial sum',
                                       "event_whenkeypressed', \s '4' .*?  data_setvariableto .*?  data_setvariableto "
                                       ],
                                      ['when "4" pressed looks approximately correct (needs a say)',
                                       "event_whenkeypressed', \s '4' .+?  looks_sayforsecs"
                                       ],
                                      ['when "4" pressed looks approximately correct (needs a change variable)'
                                       '<br>One change for the counter in loop',
                                       "event_whenkeypressed', \s '4' .+?  data_changevariableby"
                                       ],
                                      ['when "4" pressed looks approximately correct (needs an if)'
                                       '<br>To check if there is a negative number',
                                       "event_whenkeypressed', \s '4' .+?  control_if"
                                       ],
                                      ],
                             '44_8': [['when "5" pressed looks approximately correct (loop)',
                                       "event_whenkeypressed', \s '5' .+?  control_repeat"
                                       ],
                                      ['when "5" pressed looks approximately correct (needs set variable).'
                                       '<br>One set for a counter',
                                       "event_whenkeypressed', \s '5' .*?  data_setvariableto "
                                       ],
                                      ['when "5" pressed looks approximately correct (needs a say)',
                                       "event_whenkeypressed', \s '5' .+?  looks_sayforsecs"
                                       ],
                                      ['when "5" pressed looks approximately correct (needs a change variable)'
                                       '<br>One change for the counter in loop',
                                       "event_whenkeypressed', \s '5' .+?  data_changevariableby"
                                       ],
                                      ['when "5" pressed looks approximately correct (needs an if inside the loop)'
                                       '<br>To check if you want to put it in a new list',
                                       "event_whenkeypressed', \s '5' .*? control_repeat .*? control_if"
                                       ],
                                      ['when "5" pressed looks approximately correct (needs to delete items in list)'
                                       '<br>To clear the list at the beginning',
                                       "event_whenkeypressed', \s '5' .+? data_deletealloflist"
                                       ],
                                      ['when "5" pressed looks approximately correct (needs to add items to list)'
                                       '<br>To add item to list',
                                       "event_whenkeypressed', \s '5' .+? data_addtolist"
                                       ],
                                      ],
                             '44_10': [['when "6" pressed looks approximately correct (loop)',
                                        "event_whenkeypressed', \s '6' .+?  control_repeat"
                                        ],
                                       ['when "6" pressed looks approximately correct (needs set variable).'
                                        '<br>One set for a counter',
                                        "event_whenkeypressed', \s '6' .*?  data_setvariableto "
                                        ],
                                       ['when "6" pressed looks approximately correct (needs a say)',
                                        "event_whenkeypressed', \s '6' .+?  looks_sayforsecs"
                                        ],
                                       ['when "6" pressed looks approximately correct (needs a change variable)'
                                        '<br>One change for the counter in loop',
                                        "event_whenkeypressed', \s '6' .+?  data_changevariableby"
                                        ],
                                       ['when "6" pressed looks approximately correct (needs an if inside the loop)'
                                        '<br>To check if you want to put it in a new list',
                                        "event_whenkeypressed', \s '6' .*? control_repeat .*? control_if"
                                        ],
                                       ['when "6" pressed looks approximately correct (needs to delete items in list)'
                                        '<br>To clear the list at the beginning',
                                        "event_whenkeypressed', \s '6' .+? data_deletealloflist"
                                        ],
                                       ['when "6" pressed looks approximately correct (needs to add items to list)'
                                        '<br>To add item to list',
                                        "event_whenkeypressed', \s '6' .+? data_addtolist"
                                        ],
                                       ],
                             }
    events = {'22_press_zero': "'event_whenkeypressed',\s'0'",
              '22_1_1': "'event_whenkeypressed',\s'1'",
              '22_1_2': "'event_whenkeypressed',\s'1'",
              '22_2_1': "'event_whenkeypressed',\s'2'",
              '22_2_2': "'event_whenkeypressed',\s'2'",
              '22_2_3': "'event_whenkeypressed',\s'2'",
              '22_3_1': "'event_whenkeypressed',\s'3'",
              '22_3_2': "'event_whenkeypressed',\s'3'",
              '22_3_3': "'event_whenkeypressed',\s'3'",
              '23name': 'event_whenflagclicked',
              '23triangle': 'event_whenflagclicked',
              '23feel': 'event_whenflagclicked',
              '23a_draw_triangle': 'event_whenflagclicked',
              '23b_color_change_1': 'event_whenflagclicked',
              '23b_costume_change': 'event_whenflagclicked',
              '23b_question_ifelse': 'event_whenflagclicked',
              '23b_two_question': 'event_whenflagclicked',
              '24_green_flag': 'event_whenflagclicked',
              '24_name_variable_to_answer': 'event_whenflagclicked',
              '24_set_random': 'event_whenflagclicked',
              '24_ifelse': 'event_whenflagclicked',
              '26_greenflag_forever': 'event_whenflagclicked',
              '26_test_fall': 'event_whenflagclicked',
              '26_top_1': 'event_whenflagclicked',
              '26_top_2': 'event_whenflagclicked',
              '26_ground_1': 'event_whenflagclicked',
              '26_ground_2': 'event_whenflagclicked',
              '26_ground_3': 'event_whenflagclicked',
              '26_random_x_1': 'event_whenflagclicked',
              '26_random_x_2': 'event_whenflagclicked',
              '26_platform_or_ground_1': 'event_whenflagclicked',
              '26_platform_or_ground_2': 'event_whenflagclicked',
              '26_platform_or_ground_3': 'event_whenflagclicked',
              '35_turn_right_1': 'event_whenflagclicked',
              '35_turn_right_2': "'event_whenkeypressed',\s'right \s arrow'",
              '35_turn_left_1': 'event_whenflagclicked',
              '35_turn_left_2': "'event_whenkeypressed',\s'left \s arrow'",
              '35_animated_walk_1': 'event_whenflagclicked',
              '35_animated_walk_2': "'event_whenkeypressed',\s'right \s arrow'",
              '35_jump_1': 'event_whenflagclicked',
              '35_jump_2': "'event_whenkeypressed',\s'space'",
              '35_stop_1': 'event_whenflagclicked',
              '35_stop_2': 'event_whenflagclicked',
              '35_layers_1': 'event_whenflagclicked',
              '35_layers_2': "'event_whenkeypressed',\s'left \s arrow'",
              '35_enemy_animated_walk_1': 'event_whenflagclicked',
              '35_enemy_animated_walk_2': "'event_whenkeypressed',\s'right \s arrow'",
              '35_enemy_animated_walk_3': "'event_whenbroadcastreceived'",
              '35_enemy_move': 'event_whenflagclicked',
              '35_scenery1_1': "'event_whenkeypressed',\s'left \s arrow'",
              '35_scenery1_2': 'event_whenflagclicked',
              '35_scenery1_3': "'event_whenbroadcastreceived'",
              '35_scenery1_4': "'event_whenkeypressed',\s'right \s arrow'",
              '35_scenery1_5': 'event_whenflagclicked',
              '35_scenery1_6': "'event_whenbroadcastreceived'",
              '35_scenery2_1': "'event_whenkeypressed',\s'left \s arrow'",
              '35_scenery2_2': 'event_whenflagclicked',
              '35_scenery2_3': "'event_whenbroadcastreceived'",
              '35_scenery2_4': "'event_whenkeypressed',\s'right \s arrow'",
              '35_scenery2_5': 'event_whenflagclicked',
              '35_scenery2_6': "'event_whenbroadcastreceived'",
              '35_scenery1_rollover_1': "'event_whenkeypressed',\s'right \s arrow'",
              '35_scenery1_rollover_2': 'event_whenflagclicked',
              '35_scenery1_rollover_3': "'event_whenbroadcastreceived'",
              '35_scenery1_rollover_4': "'event_whenkeypressed',\s'left \s arrow'",
              '35_scenery1_rollover_5': 'event_whenflagclicked',
              '35_scenery1_rollover_6': "'event_whenbroadcastreceived'",
              '35_scenery2_rollover_1': "'event_whenkeypressed',\s'right \s arrow'",
              '35_scenery2_rollover_2': 'event_whenflagclicked',
              '35_scenery2_rollover_3': "'event_whenbroadcastreceived'",
              '35_scenery2_rollover_4': "'event_whenkeypressed',\s'left \s arrow'",
              '35_scenery2_rollover_5': 'event_whenflagclicked',
              '35_scenery2_rollover_6': "'event_whenbroadcastreceived'",
              '35_enemy_moves': 'event_whenflagclicked',
              '35_enemy_rollover_1': "'event_whenkeypressed',\s'right \s arrow'",
              '35_enemy_rollover_2': 'event_whenflagclicked',
              '35_enemy_rollover_3': "'event_whenbroadcastreceived'",
              '42_6': "'event_whenkeypressed',\s'x'",
              '43a_1': "'event_whenkeypressed',\s'1'",
              '43a_3': "'event_whenkeypressed',\s'2'",
              '43a_5': "'event_whenkeypressed',\s'3'",
              '43a_7': "'event_whenkeypressed',\s'4'",
              '43b_1': "'event_whenkeypressed',\s'1'",
              '43b_3': "'event_whenkeypressed',\s'2'",
              '43b_5': "'event_whenkeypressed',\s'3'",
              '43b_7': "'event_whenkeypressed',\s'4'",
              '44_2': "'event_whenkeypressed',\s'2'",
              '44_4': "'event_whenkeypressed',\s'3'",
              '44_6': "'event_whenkeypressed',\s'4'",
              '44_8': "'event_whenkeypressed',\s'5'",
              '44_10': "'event_whenkeypressed',\s'6'",
              }
    help_links = {'22_press_zero': 'https://docs.google.com/presentation/d/105dwt0vptLiKuZLXZcWLrVq6GpGTG-GJsZoelOmP'
                                   'MCE/edit#slide=id.g845c5471f3_0_5',
                  '22_1_1': 'https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiFMZ08NmBFro8LmljYbe6w/'
                            'edit#slide=id.g88c5a09ee6_0_0',
                  '22_1_2': 'https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiFMZ08NmBFro8LmljYbe6w/'
                            'edit#slide=id.g88c5a09ee6_0_0',
                  '22_2_1': 'https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiFMZ08NmBFro8LmljYbe6w/'
                            'edit#slide=id.g88c5a09ee6_0_0',
                  '22_2_2': 'https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiFMZ08NmBFro8LmljYbe6w/'
                            'edit#slide=id.g88c5a09ee6_0_0',
                  '22_2_3': 'https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiFMZ08NmBFro8LmljYbe6w/'
                            'edit#slide=id.g88c5a09ee6_2_0',
                  '22_3_1': 'https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiFMZ08NmBFro8LmljYbe6w/'
                            'edit#slide=id.g88c5a09ee6_0_0',
                  '22_3_2': 'https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiFMZ08NmBFro8LmljYbe6w/'
                            'edit#slide=id.g88c5a09ee6_0_0',
                  '22_3_3': 'https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiFMZ08NmBFro8LmljYbe6w/'
                            'edit#slide=id.g88c5a09ee6_2_0',
                  '23name': 'https://docs.google.com/presentation/d/1fM_9jw-XCvQxCdNCq3GrIGdBns3MzpoK9EzcalRrH_k/'
                            'edit#slide=id.g3f255390c6_0_26',
                  '23triangle': 'https://docs.google.com/presentation/d/1fM_9jw-XCvQxCdNCq3GrIGdBns3MzpoK9EzcalRrH_k/'
                                'edit#slide=id.g3f255390c6_0_26',
                  '23feel': 'https://docs.google.com/presentation/d/1fM_9jw-XCvQxCdNCq3GrIGdBns3MzpoK9EzcalRrH_k/'
                            'edit#slide=id.g3f255390c6_0_26',
                  '23a_draw_triangle': 'https://docs.google.com/presentation/d/1W3bmLtRCv99HlsSGPZmGUvDcBEbi334iwhAGi'
                                       'bJD7aY/edit#slide=id.g3f255390c6_0_11',
                  '23b_color_change_1': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVh'
                                        'DJWf62lFVITA/edit#slide=id.g750298e25a_0_0',
                  '23b_costume_change': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L'
                                        '-9nBzpLwo5sI8E/edit#slide=id.g40e2c193cf_0_9',
                  '23b_question_ifelse': 'https://docs.google.com/presentation/d/1_SFKu28S-0uSnFPMK4Eifm_BFJ-oD'
                                         'CwWXRrWX9lTbwo/edit#slide=id.g76bc15b9c9_0_2',
                  '23b_two_question': 'https://docs.google.com/presentation/d/1_SFKu28S-0uSnFPMK4Eifm_BFJ-oD'
                                      'CwWXRrWX9lTbwo/edit#slide=id.g76bc15b9c9_0_2',
                  '24_green_flag': 'https://docs.google.com/presentation/d/1I2psbQlrb-kbkq_j6V'
                                   'ouSFq_6Lq5qOLLzQxiCEEtAJg/edit#slide=id.g845c5471f3_0_5',
                  '24_name_variable_to_answer': 'https://docs.google.com/presentation/d/1I2psbQlrb-kbkq_j6V'
                                                'ouSFq_6Lq5qOLLzQxiCEEtAJg/edit#slide=id.g845c5471f3_0_5',
                  '24_set_random': 'https://docs.google.com/presentation/d/1I2psbQlrb-kbkq_j6VouSFq_6Lq5qOLLzQxiCE'
                                   'EtAJg/edit#slide=id.g752722b0be_0_0',
                  '24_ifelse': 'https://docs.google.com/presentation/d/1_SFKu28S-0uSnFPMK4Eifm_BFJ-oDCwWXRrWX9lTbwo/'
                               'edit#slide=id.g76bc15b9c9_0_2',
                  '26_greenflag_forever': 'https://docs.google.com/presentation/d/14LRLWqtLAC3SiUAGCWsyXG-QO_VZpimJ'
                                          '0NKcwnMBNQ8/edit#slide=id.g43f5e26e9b_0_2',
                  '26_test_fall': 'https://docs.google.com/presentation/d/14LRLWqtLAC3SiUAGCWsyXG-QO_VZpimJ'
                                  '0NKcwnMBNQ8/edit#slide=id.g43f5e26e9b_0_2',
                  '26_top_1': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                              'edit#slide=id.g8707d29fdb_0_0',
                  '26_top_2': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                              'edit#slide=id.g8707d29fdb_0_0',
                  '26_random_x_1': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVh'
                                   'DJWf62lFVITA/edit#slide=id.g8707d29fdb_0_0',
                  '26_random_x_2': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVh'
                                   'DJWf62lFVITA/edit#slide=id.g8707d29fdb_0_0',
                  '26_ground_1': 'https://docs.google.com/presentation/d/14LRLWqtLAC3SiUAGCWsyXG-QO_VZpimJ'
                                 '0NKcwnMBNQ8/edit#slide=id.g43f5e26e9b_0_8',
                  '26_ground_2': 'https://docs.google.com/presentation/d/14LRLWqtLAC3SiUAGCWsyXG-QO_VZpimJ'
                                 '0NKcwnMBNQ8/edit#slide=id.g43f5e26e9b_0_8',
                  '26_ground_3': 'https://docs.google.com/presentation/d/14LRLWqtLAC3SiUAGCWsyXG-QO_VZpimJ'
                                 '0NKcwnMBNQ8/edit#slide=id.g43f5e26e9b_0_8',
                  '26_platform_or_ground_1': 'https://docs.google.com/presentation/d/14LRLWqtLAC3SiUAGCWsyXG-QO_VZpimJ'
                                             '0NKcwnMBNQ8/edit#slide=id.g43f5e26e9b_0_8',
                  '26_platform_or_ground_2': 'https://docs.google.com/presentation/d/14LRLWqtLAC3SiUAGCWsyXG-QO_VZpimJ'
                                             '0NKcwnMBNQ8/edit#slide=id.g43f5e26e9b_0_8',
                  '26_platform_or_ground_3': 'https://docs.google.com/presentation/d/14LRLWqtLAC3SiUAGCWsyXG-QO_VZpimJ'
                                             '0NKcwnMBNQ8/edit#slide=id.g43f5e26e9b_0_8',
                  '35_turn_right_1': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0'
                                     'Ua7k/edit#slide=id.g43f6e4e8b4_1_2',
                  '35_turn_right_2': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua'
                                     '7k/edit#slide=id.g882c6b2274_0_18',
                  '35_turn_left_1': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0'
                                     'Ua7k/edit#slide=id.g43f6e4e8b4_1_2',
                  '35_turn_left_2': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua'
                                    '7k/edit#slide=id.g882c6b2274_0_18',
                  '35_animated_walk_1': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L-9nBzp'
                                        'Lwo5sI8E/edit#slide=id.g40e2c193cf_0_9',
                  '35_animated_walk_2': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L-9nBzp'
                                        'Lwo5sI8E/edit#slide=id.g40e2c193cf_0_9',
                  '35_animated_walk_3': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L-9nBzp'
                                        'Lwo5sI8E/edit#slide=id.g40e2c193cf_0_9',
                  '35_jump_1': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7k/'
                               'edit#slide=id.g80b4a321f2_0_0',
                  '35_jump_2': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7k/'
                               'edit#slide=id.g80b4a321f2_0_0',
                  '35_layers_1': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                               'edit#slide=id.g883030db0b_0_0',
                  '35_layers_2': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                                 'edit#slide=id.g883030db0b_0_0',
                  '35_enemy_animated_walk_1': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L'
                                              '-9nBzpLwo5sI8E/edit#slide=id.g40e2c193cf_0_9',
                  '35_enemy_animated_walk_2': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L'
                                              '-9nBzpLwo5sI8E/edit#slide=id.g40e2c193cf_0_9',
                  '35_enemy_animated_walk_3': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L'
                                              '-9nBzpLwo5sI8E/edit#slide=id.g40e2c193cf_0_9',
                  '35_scenery1_1': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g885a7762d5_1_13',
                  '35_scenery1_2': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g43f6e4e8b4_1_12',
                  '35_scenery1_3': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g885a7762d5_1_69',
                  '35_scenery1_4': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g885a7762d5_1_13',
                  '35_scenery1_5': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g43f6e4e8b4_1_12',
                  '35_scenery1_6': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g885a7762d5_1_69',
                  '35_scenery2_1': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g885a7762d5_1_13',
                  '35_scenery2_2': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g43f6e4e8b4_1_12',
                  '35_scenery2_3': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g885a7762d5_1_69',
                  '35_scenery2_4': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g885a7762d5_1_13',
                  '35_scenery2_5': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g43f6e4e8b4_1_12',
                  '35_scenery2_6': 'https://docs.google.com/presentation/d/1959t7HXKv4VonDAT1GnHl3IustXWGOTShHPH8k0Ua7'
                                   'k/edit#slide=id.g885a7762d5_1_69',
                  '35_scenery1_rollover_1': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_scenery1_rollover_2': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g43f5e26e9b_0_2',
                  '35_scenery1_rollover_3': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_scenery1_rollover_4': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_scenery1_rollover_5': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQ'
                                            'BtdOf-CJ4vvRjA/edit#slide=id.g43f5e26e9b_0_2',
                  '35_scenery1_rollover_6': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_scenery2_rollover_1': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_scenery2_rollover_2': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQ'
                                            'BtdOf-CJ4vvRjA/edit#slide=id.g43f5e26e9b_0_2',
                  '35_scenery2_rollover_3': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_scenery2_rollover_4': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_scenery2_rollover_5': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQ'
                                            'BtdOf-CJ4vvRjA/edit#slide=id.g43f5e26e9b_0_2',
                  '35_scenery2_rollover_6': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                            '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_enemy_move': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62l'
                                   'FVITA/edit#slide=id.g883030db0b_1_8',
                  '35_enemy_rollover_1': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                         '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_enemy_rollover_2': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQ'
                                         'BtdOf-CJ4vvRjA/edit#slide=id.g43f5e26e9b_0_2',
                  '35_enemy_rollover_3': 'https://docs.google.com/presentation/d/14BoGFXROrP7ht01dwEa45Xf07OjJQBtdOf'
                                         '-CJ4vvRjA/edit#slide=id.g8860556fa9_1_12',
                  '35_stop_1': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                               'edit#slide=id.g883030db0b_1_0',
                  '35_stop_2': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                               'edit#slide=id.g883030db0b_1_0',
                  '42_6': 'https://docs.google.com/presentation/d/1_GvsbbOnGSE6lCdZvMb1Ji7wjfLd5NDSbeYdBVZ9uLQ/'
                          'edit#slide=id.g84893e6519_1_7',
                  '43a_1': 'https://docs.google.com/presentation/d/1xL-_PNmYcnbvdlnu_rh3oNExjYolu6I0ALOCKmfNPpQ/edit#'
                           'slide=id.g8006a4aa44_1_9',
                  '43a_3': 'https://docs.google.com/presentation/d/1xL-_PNmYcnbvdlnu_rh3oNExjYolu6I0ALOCKmfNPpQ/edit#'
                           'slide=id.g8006a4aa44_1_20',
                  '43a_5': 'https://docs.google.com/presentation/d/1xL-_PNmYcnbvdlnu_rh3oNExjYolu6I0ALOCKmfNPpQ/edit#'
                           'slide=id.g8006a4aa44_1_39',
                  '43a_7': 'https://docs.google.com/presentation/d/1xL-_PNmYcnbvdlnu_rh3oNExjYolu6I0ALOCKmfNPpQ/edit#'
                           'slide=id.g8006a4aa44_1_51',
                  '43b_1': 'https://docs.google.com/presentation/d/1JiUTTQ87FZTGpFKOFPbIyC8Ygbd8-dz6dY5Bv6UP00Q/edit#'
                           'slide=id.g84b569ad88_0_13',
                  '43b_3': 'https://docs.google.com/presentation/d/1JiUTTQ87FZTGpFKOFPbIyC8Ygbd8-dz6dY5Bv6UP00Q/edit#'
                           'slide=id.g84b569ad88_0_0',
                  '43b_5': 'https://docs.google.com/presentation/d/1JiUTTQ87FZTGpFKOFPbIyC8Ygbd8-dz6dY5Bv6UP00Q/edit#'
                           'slide=id.g84b569ad88_0_0',
                  '43b_7': 'https://docs.google.com/presentation/d/1JiUTTQ87FZTGpFKOFPbIyC8Ygbd8-dz6dY5Bv6UP00Q/edit#'
                           'slide=id.g84b569ad88_0_13',
                  '44_2': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                          'slide=id.g84f7e90710_0_11',
                  '44_4': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                          'slide=id.g84f7e90710_0_31',
                  '44_6': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                          'slide=id.g84f7e90710_0_31',
                  '44_8': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                          'slide=id.g8031cf97a9_1_0',
                  '44_10': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                           'slide=id.g8031cf97a9_1_0',
                  }
    p_test = {"name": "Testing that there is a " + this_test_description[this_test][0][0] + ". (" + str(p_points) +
                      " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Code has a " + this_test_description[this_test][0][0] + ".<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Code does not find a " + this_test_description[this_test][0][0] + ".<br>",
              'points': 0
              }
    [test_event, script] = one_event(p_scripts, events[this_test])
    if test_event['pass'] is False:
        p_test['fail_message'] += test_event['fail_message']
        return p_test
    else:
        all_passed = True
        for test in this_test_description[this_test]:
            print("test! {} script {}".format(test, script))
            temp_test = match_string(test[1], script)
            if temp_test['pass'] is False:
                p_test['fail_message'] += '<h5 style=\"color:purple;\">There needs to be a(n) ' + \
                                          test[0] + '</h5>'
                all_passed = False
    if all_passed:
        p_test['pass'] = True
        p_test['points'] += p_points
    else:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">See example here: <a href="' + help_links[this_test] +\
                                  '" target="_blank">link to page in presentation</a></h5>'
    return p_test


def find_string_in_custom_block(p_scripts, this_test, p_points):
    """
    Finds a string (multiple strings) in script.  Assumes one sprite.
    Similar to find_block_in_sprite except allows multiple searches and expects a certain event at top.
    More specific testing
    :param p_scripts: scripts from the sprite (dict)
    :param this_test: name of test (string)
    :param p_points: points (int)
    :return: Test dictionary
    """
    this_test_description = {
        'karel_turnright': [['user-defined turnright custom block that turns right',
                             "('control_repeat', \s '3', \s \['turnleft']| 'turnleft', \s 'turnleft', \s 'turnleft')"
                             ],
                            ],
    }
    custom_block = {
        'karel_turnright': "turnright",
    }
    help_links = {
        'karel_turnright': 'https://docs.google.com/presentation/d/1rk0TkaB-tdBf90RimxzPTUVO3_CZouewwGtzn33vxhM/edit#'
                           'slide=id.g77e122c2a8_0_0',
    }
    p_test = {"name": "Testing that there is a " + this_test_description[this_test][0][0] + ". (" + str(p_points) +
                      " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Code has a " + this_test_description[this_test][0][0] + ".<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "Code does not find a " + this_test_description[this_test][0][0] + ".<br>",
              'points': 0
              }
    [test_block, script] = one_custom_block(p_scripts, custom_block[this_test])
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    else:
        all_passed = True
        for test in this_test_description[this_test]:
            temp_test = match_string(test[1], script)
            if temp_test['pass'] is False:
                p_test['fail_message'] += '<h5 style=\"color:purple;\">There needs to be a(n) ' + \
                                          test[0] + '</h5>'
                all_passed = False
    if all_passed:
        p_test['pass'] = True
        p_test['points'] += p_points
    else:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">See example here: <a href="' + help_links[this_test] + \
                                  '" target="_blank">link to page in presentation</a></h5>'
    return p_test


def find_block_in_sprite(p_json, blockname, p_points, *, min_sprites=0, different_ok=False, check_all=False,
                         stage=True):
    """
    Looks for blocks in sprites
    :param p_json:  - json of all code
    :param blockname  - Name of the block we are looking for (string)
    :param p_points:  - points this is worth(int)
    :param min_sprites: - minimum number of sprites to find block in.  0 = find in all. (int)
    :param different_ok - if every is False, then it's OK if what you are looking for is in different scripts (bool)
    :param check_all- Check all scripts for block.  For example, check all scripts for new stage (bool)
    :param stage - include stage in scripts?
    :return: test dictionary
    """
    import re
    block_names = {'green_flag': 'green flag',
                   'broadcast': 'broadcast or broadcast and wait',
                   'broadcast_received': 'when broadcast received',
                   'any_move': 'move, glide, or goto  (under an event block)',
                   'rotate': 'rotate  (under an event block)',
                   'change_costume': 'change costume  (under an event block)',
                   'show_hide': 'show AND hide sprite (under an event block)',
                   'two_backgrounds': 'two background changes (under an event block)',  # this is buggy but OK
                   'karel2a_repeat':  'a repeat, repeating exactly correct times for maximum efficiency in the '
                                      'Coder sprite',
                   'karel2b_repeat': 'a repeat, repeating exactly correct times for maximum efficiency in the '
                                     'Coder sprite',
                   }
    block_json = {'green_flag': "'event_whenflagclicked'",
                  'broadcast': "(event_broadcast|event_broadcastandwait)'",
                  'broadcast_received': "'event_whenbroadcastreceived'",
                  'any_move': "event .*? (motion_move|motion_goto|motion_glide|motion_set|motion_change)",
                  'rotate': 'event .*? motion_turn',
                  'change_costume': 'event .*? looks .*?costume ',
                  'show_hide': 'event .*? (looks_show .*? looks_hide | looks_hide .*? looks_show) ',
                  'two_backgrounds': ': \s \[ \' event .*? (looks_nextbackdrop|looks_switchbackdropto) .*? '
                                     '(looks_nextbackdrop|looks_switchbackdropto)',
                  'karel2a_repeat': "(\['control_repeat', \s '5', \s \[ .*? ]] )",
                  'karel2b_repeat': "(\['control_repeat', \s '4', \s \[ .*? ]] )",
                  }
    block_links = {'green_flag': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                                 'edit#slide=id.g74d477a87c_0_7',
                   'broadcast': 'https://docs.google.com/presentation/d/1NRjar0qBn1Tdi9N71Vdauwcp_4ztY4DnRETtdK55geg/'
                                'edit#slide=id.g7febc2c11f_0_14',
                   'broadcast_received': 'https://docs.google.com/presentation/d/1NRjar0qBn1Tdi9N71Vdauwcp_'
                                         '4ztY4DnRETtdK55geg/edit#slide=id.g7febc2c11f_0_14',
                   'any_move': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L-9nBzpLwo5sI8E/'
                               'edit#slide=id.g74de51b979_0_10',
                   'rotate': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L-9nBzpLwo5sI8E/'
                             'edit#slide=id.g8413959832_1_0',
                   'change_costume': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L-'
                                     '9nBzpLwo5sI8E/edit#slide=id.g40e2c193cf_0_9',
                   'show_hide': 'https://docs.google.com/presentation/d/1-WT5QhXVus75qflQXVd0ZYzWx_a4L-9nBzpLwo5sI8E/'
                                'edit#slide=id.g8413959832_0_11',
                   'two_backgrounds': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62l'
                                      'FVITA/edit#slide=id.g750298e25a_0_0',
                   'karel2a_repeat': 'https://docs.google.com/document/d/18RLvgOiedBK6KvRx6FvEbtpUxu1Nale2g5I'
                                     'MxbB-Iyw/edit#bookmark=id.xoi5p4pd5all',
                   'karel2b_repeat': 'https://docs.google.com/document/d/18RLvgOiedBK6KvRx6FvEbtpUxu1Nale2g5IMxbB-Iyw/'
                                     'edit#bookmark=id.xcweonqyedeb',
                   }
    if min_sprites == 0:
        min_sprites_txt = 'Every'  # Block needs to be in every sprite
        min_sprites = count_sprites(p_json)
    else:
        min_sprites_txt = 'At least ' + str(min_sprites)  # Block must be in minimum of min_sprites sprites
    p_test = {"name": "Checking that " + min_sprites_txt.lower() + " (non-background) sprite has a " +
                      block_names[blockname] +
                      " (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  " + min_sprites_txt +
                              " (non-background) sprite has a " + block_names[blockname] + ".<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> " + min_sprites_txt +
                              " (non-background) sprite does not have a " + block_names[blockname] + ".<br></h5>",
              "points": 0
              }
    found_counter = 0
    if check_all:
        if stage is True:
            all_scripts = arrange_blocks_v2(p_json)
            print('all scripts {}'.format(all_scripts))
            if re.search(block_json[blockname], str(all_scripts), re.X | re.M | re.S):
                p_test['pass_message'] += 'All code for all sprites has a ' + block_names[blockname] + '.<br>'
                found_counter = min_sprites
            else:
                p_test['fail_message'] += '<h5 style=\"color:purple;\"Checked all code of all sprites.' \
                                          'All code does not have a ' + block_names[blockname] + '.<br></h5>'
    else:
        for target in p_json['targets']:  # Loop over sprites
            if found_counter >= min_sprites:
                break
            if target['isStage'] is not True:
                scripts = arrange_blocks_v2(p_json, only_this_sprite=target['name'])
                if different_ok:  # Look at all sprites for a particular string
                    if re.search(block_json[blockname], str(scripts), re.X | re.M | re.S):
                        found_counter += 1
                        p_test['pass_message'] += 'This sprite has a ' + block_names[blockname] +\
                                                  ': ' + target['name'] +\
                                                  '.<br>'
                    else:
                        p_test['fail_message'] += '<h5 style=\"color:purple;\">This sprite has does not have a ' + \
                                                   block_names[blockname] + ': ' + target['name'] + '.<br></h5>'
                else:
                    found_in_sprite = False
                    for key in scripts:
                        script = scripts[key]
                        if re.search(block_json[blockname], str(script), re.X | re.M | re.S):
                            found_counter += 1
                            message = 'This sprite has a ' + block_names[blockname] + ': ' + target['name'] + '.<br>'
                            p_test['pass_message'] += message
                            p_test['fail_message'] += message
                            found_in_sprite = True
                            break
                    message = 'This sprite does not have a ' + block_names[blockname] + ': ' + \
                              target['name'] + '.<br>'
                    if found_in_sprite is False:
                        p_test['fail_message'] += '<h5 style=\"color:purple;\">' + message + '</h5>'
    if found_counter < min_sprites:
        p_test['pass'] = False
        p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                  'See example here: <a href="' + block_links[blockname] +\
                                  '" target="_blank">link to page in presentation</a></h5></br>'
    else:
        p_test['points'] += p_points
    return p_test


def run_script_check_say(p_scripts, this_test, p_points):
    """
    Runs the script, sees what it says.  Assumes one sprite only.  Assumes looking for script under a particular event.
    :param p_scripts: scripts (dict)
    :param this_test - name of test (string)
    :param p_points: points it is worth (int)
    :return: a test dictionary
    """
    import re
    import copy
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2  import brickLayer, do_sprite
    script_test_description = {'23a_name_reply': 'If I reply to the first question with a name, program '
                                                 'replies back with something that includes the name.  For example,'
                                                 '<br>Program asks "what is your name".  <br>You reply "Mr. Murphy".  '
                                                 '<br>Program should reply "Hello Mr. Murphy" with the space '
                                                 'after Hello.<br><br>',
                               '23a_feel_reply': 'If I reply to the third question with how I feel", program '
                                                 'replies back with something that includes that feeling',
                               '24_correct': "If I guess the number correctly, program says " 
                                             "something with person's name and the word 'correct'",
                               '24_wrong': "If I guess the number incorrectly, program says "
                                             "something with person's name and the word 'wrong'",
                               '42_4': "If I press 'i', computer asks me for an ice cream to add to ice_cream_list."
                                       "  Computer adds the ice cream and then says ice_cream_list ",
                               '42_5': "If I press 'w', computer asks me for a wet topping to add to wet_list."
                                       "  Computer adds the wet topping and then says wet_list ",
                               '42_7':  "If I press 'x', computer FIRST asks me for which list (ice_cream_list, "
                                        "dry_list, or wet_list).  Then asks me for which item to delete."
                                       "  Computer deletes the item, then says the list it changed.",
                               '43a_2': "If I press '1', computer will say every song in list, one by one.",
                               '43a_4': "If I press '2', computer will say every other song in list.",
                               '43a_6': "If I press '3', computer will skip the first two and the last two"
                                        "songs in the list, but say the others.",
                               '43a_8': "If I press '4', computer will say every song in the list, starting"
                                        "from the end and going to the beginning.",
                               '43b_2': "If I press '1', computer will say every song in list with more than 10 "
                                        "letters.",
                               '43b_4': "If I press '2', computer will say every song in list starting with 'c'.",
                               '43b_6': "If I press '3', computer will say every song in list ending with 'y'.",
                               '43b_8': "If I press '4', computer will say every song in list containing 'e'.",
                               '44_1': "If I press '1', computer will add the numbers in the list and say"
                                       "the sum at the end ",
                               '44_3': "If I press '2', computer will add the numbers in the list and say"
                                       "the AVERAGE (not sum) at the end",
                               '44_5': "If I press '3', computer will add the check the numbers in the list and "
                                       "at the end say 'True' if there is a negative number, and 'False' if there "
                                       "is not.",
                               '44_7': "If I press '4', computer will add the check the numbers in the list and "
                                       "at the end say the maximum number in the list.",
                               '44_9': "If I press '5', computer will add the check the numbers in the list and "
                                       "at the end say a new list, converting all the number to positive.",
                               '44_11': "If I press '6', computer will add the check the numbers in the list and "
                                        "at the end say a new list, with only even numbers from original list.",
                               }
    events = {'23a_name_reply': 'event_whenflagclicked',
              '23a_feel_reply': 'event_whenflagclicked',
              '24_correct': 'event_whenflagclicked',
              '24_wrong': 'event_whenflagclicked',
              '42_4': "'event_whenkeypressed',\s'i'",
              '42_5': "'event_whenkeypressed',\s'w'",
              '42_7': "'event_whenkeypressed',\s'x'",
              '43a_2': "'event_whenkeypressed',\s'1'",
              '43a_4': "'event_whenkeypressed',\s'2'",
              '43a_6': "'event_whenkeypressed',\s'3'",
              '43a_8': "'event_whenkeypressed',\s'4'",
              '43b_2': "'event_whenkeypressed',\s'1'",
              '43b_4': "'event_whenkeypressed',\s'2'",
              '43b_6': "'event_whenkeypressed',\s'3'",
              '43b_8': "'event_whenkeypressed',\s'4'",
              '44_1': "'event_whenkeypressed',\s'1'",
              '44_3': "'event_whenkeypressed',\s'2'",
              '44_5': "'event_whenkeypressed',\s'3'",
              '44_7': "'event_whenkeypressed',\s'4'",
              '44_9': "'event_whenkeypressed',\s'5'",
              '44_11': "'event_whenkeypressed',\s'6'",
              }
    links = {'23a_name_reply': 'https://docs.google.com/presentation/d/1fM_9jw-XCvQxCdNCq3GrIGdBns3MzpoK9EzcalRrH_k/'
                               'edit#slide=id.g6e44b7432d_0_30',
             '23a_feel_reply': 'https://docs.google.com/presentation/d/1fM_9jw-XCvQxCdNCq3GrIGdBns3MzpoK9EzcalRrH_k/'
                               'edit#slide=id.g6e44b7432d_0_30',
             '24_correct': 'https://docs.google.com/document/d/1uV3lq9ZwAxrRC578r5BXDT6rYLMSnCjXncaVUXiVkKI/'
                           'edit#bookmark=id.bu658u99o3dp',
             '24_wrong': 'https://docs.google.com/document/d/1uV3lq9ZwAxrRC578r5BXDT6rYLMSnCjXncaVUXiVkKI/'
                         'edit#bookmark=id.f4r0po9qam93',
             '42_4': 'https://docs.google.com/presentation/d/1_GvsbbOnGSE6lCdZvMb1Ji7wjfLd5NDSbeYdBVZ9uLQ/edit#'
                     'slide=id.g4608b21e0f_0_197',
             '42_5': 'https://docs.google.com/presentation/d/1_GvsbbOnGSE6lCdZvMb1Ji7wjfLd5NDSbeYdBVZ9uLQ/edit#'
                     'slide=id.g4608b21e0f_0_197',
             '42_7': 'https://docs.google.com/presentation/d/1_GvsbbOnGSE6lCdZvMb1Ji7wjfLd5NDSbeYdBVZ9uLQ/edit#'
                     'slide=id.g84893e6519_1_7',
             '43a_2': 'https://docs.google.com/presentation/d/1xL-_PNmYcnbvdlnu_rh3oNExjYolu6I0ALOCKmfNPpQ/edit#'
                     'slide=id.g8006a4aa44_1_0',
             '43a_4': 'https://docs.google.com/presentation/d/1xL-_PNmYcnbvdlnu_rh3oNExjYolu6I0ALOCKmfNPpQ/edit#'
                      'slide=id.g8006a4aa44_1_20',
             '43a_6': 'https://docs.google.com/presentation/d/1xL-_PNmYcnbvdlnu_rh3oNExjYolu6I0ALOCKmfNPpQ/edit#'
                      'slide=id.g8006a4aa44_1_39',
             '43a_8': 'https://docs.google.com/presentation/d/1xL-_PNmYcnbvdlnu_rh3oNExjYolu6I0ALOCKmfNPpQ/edit#'
                      'slide=id.g8006a4aa44_1_51',
             '43b_2': 'https://docs.google.com/presentation/d/1JiUTTQ87FZTGpFKOFPbIyC8Ygbd8-dz6dY5Bv6UP00Q/edit#'
                      'slide=id.g84b569ad88_0_13',
             '43b_4': 'https://docs.google.com/presentation/d/1JiUTTQ87FZTGpFKOFPbIyC8Ygbd8-dz6dY5Bv6UP00Q/edit#'
                      'slide=id.g84b569ad88_0_0',
             '43b_6': 'https://docs.google.com/presentation/d/1JiUTTQ87FZTGpFKOFPbIyC8Ygbd8-dz6dY5Bv6UP00Q/edit#'
                      'slide=id.g84b569ad88_0_0',
             '43b_8': 'https://docs.google.com/presentation/d/1JiUTTQ87FZTGpFKOFPbIyC8Ygbd8-dz6dY5Bv6UP00Q/edit#'
                      'slide=id.g84b569ad88_0_13',
             '44_1': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                     'slide=id.g84f7e90710_0_4',
             '44_3': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                     'slide=id.g84f7e90710_0_11',
             '44_5': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                     'slide=id.g84f7e90710_0_31',
             '44_7': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                     'slide=id.g84f7e90710_0_31',
             '44_9': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                     'slide=id.g8031cf97a9_1_0',
             '44_11': 'https://docs.google.com/presentation/d/1-9qexvln2vI1QG9dDRDCxmrlVjQcyQL4CpoADq1Jbq8/edit#'
                      'slide=id.g8031cf97a9_1_0',
             }
    runs = {'23a_name_reply': [
        [brickLayer(0, 0, 0, variables={'sensing_answer': ['Mr. Kann', '200', '100', '100', '100', '100', ]}),
         [[1, '\s Mr\. \s Kann', 'Clicked the green flag, answering "Mr. Kann" to the first question.  '
                                 'Expected sprite to say something with "Mr. Kann" '
                                 '(Needs to have a space before the name.)'],
         [2, '\s Mr\. \s Murphy', 'Clicked the green flag, answering "Mr. Kann" to the first question.  '
                                  'Sprite should NOT say something with "Mr. Murphy" ']
          ]
         ],
        [brickLayer(0, 0, 0, variables={'sensing_answer': ['Mr. Murphy', '200', '100', '100', '100', '100', ]}),
         [[1, '\s Mr\. \s Murphy', 'Clicked the green flag, answering "Mr. Murphy" to the first question.  '
                                   'Expected sprite to say something with "Mr. Murphy" '
                                   '(Needs to have a space before the name.)'],
          [2, '\s Mr\. \s Kann', 'Clicked the green flag, answering "Mr. Murphy" to the first question.  '
                                 'Sprite should NOT say something with "Mr. Kann" ']
          ]
         ],
        ],
        '23a_feel_reply': [
            [brickLayer(0, 0, 0, variables={'sensing_answer': ['Mr. Kann', '200', 'great', '100', '100', '100', ]}),
             [[1, '\s feel .*? great', 'Clicked the green flag, answering "Mr. Kann" to first question and '
                                       '"great" to the third question.  '
                                       'Expected sprite to say something with "feel(ing) great" in it. '],
              [2, '\s feel .*? turrible', 'Clicked the green flag, answering "Mr. Kann" to first question and '
                                          'answering "great" to the third question.  '
                                          'Sprite should NOT say something with "turrible".']
              ]
             ],
            [brickLayer(0, 0, 0, variables={'sensing_answer': ['Mr. Kann', '200', 'turrible', '100', '100', '100', ]}),
             [[1, '\s feel .*? turrible', 'Clicked the green flag, answering "Mr. Kann" to first question and '
                                          'answering "turrible" to the third question.  '
                                          'Expected sprite to say something with  "feel(ing) turrible" in it.'],
              [2, '\s feel .*? great', 'Clicked the green flag, answering "Mr. Kann" to first question and '
                                       'answering "turrible" to the third question.   '
                                       'Sprite should NOT say something with "great". ']
              ]
             ],
        ],
        '24_correct': [
            [brickLayer(0, 0, 0, variables={"name": ['Kann'], 'number': [5], 'mock_random': ['5', '5', '5', '5', ],
                                            'sensing_answer': ['Kann', '5', '5', '5', '5', '5', ]}),
             [[1, 'correct', 'Clicked the green flag, answered "Mr. Kann" to first question and guessed correctly '
                             '(i.e. you guessed 5 and the random number was 5).  <br>Sprite should say something with '
                             'the word "correct" in it.'],
              [1, 'Kann', 'Clicked the green flag, answered "Mr. Kann" to first question and guessed correctly '
                          '(i.e. you guessed 5 and the random number was 5).  <br>Sprite should say something with '
                          'the word "Kann" in it.'],
              [2, 'wrong', 'Clicked the green flag, answered "Mr. Kann" to first question and guessed correctly '
                           '(i.e. you guessed 5 and the random number was 5).  <br>Sprite should NOT say something with'
                           ' the word "wrong" in it.'],
              [2, 'Murphy', 'Clicked the green flag, answered "Mr. Kann" to first question and guessed correctly '
                            '(i.e. you guessed 5 and the random number was 5).  <br>Sprite should NOT say '
                            'something with the word "Murphy" in it.'],
              ]
             ],
        ],
        '24_wrong': [
            [brickLayer(0, 0, 0, variables={"name": ['Murphy'], 'number': [5], 'mock_random': ['5', '5', '5', '5', ],
                                            'sensing_answer': ['Murphy', '9', '9', '9', '9', '9', ]}),
             [[1, 'wrong', 'Clicked the green flag, answered "Mr. Murphy" to first question and guessed incorrectly '
                           '(i.e. you guessed 5 and the random number was 9).  <br>Sprite should say something with '
                           'the word "wrong" in it.'],
              [1, 'Murphy', 'Clicked the green flag, answered "Mr. Murphy" to first question and guessed incorrectly '
                            '(i.e. you guessed 5 and the random number was 9).  <br>Sprite should say something with '
                            'the word "Murphy" in it.'],
              [2, 'correct', 'Clicked the green flag, answered "Mr. Murphy" to first question and guessed incorrectly '
                             '(i.e. you guessed 5 and the random number was 9).  '
                             '<br>Sprite should NOT say something with'
                             ' the word "correct" in it.'],
              [2, 'Kann', 'Clicked the green flag, answered "Mr. Murphy" to first question and guessed incorrectly '
                          '(i.e. you guessed 5 and the random number was 9).  <br>Sprite should NOT say '
                          'something with the word "Kann" in it.'],
              ]
             ],
        ],
        '42_4': [
            [brickLayer(0, 0, 0, variables={"ice_cream_list": ['strawberry', 'vanilla', 'chocolate', ],
                                            "dry_list": ['crunches', 'peanuts', 'coconut'],
                                            "wet_list": ['chocolate', 'caramel', 'cream', ],
                                            'sensing_answer': ['tea', ]
                                            }),
             [[1, 'strawberry .*? vanilla .*? chocolate .*? tea',
               'Pressed "i". Then answered "tea".  Sprite says ice_cream_list, which should be exactly this:'
               '"strawberry vanilla chocolate tea"<br>'],
              [2, 'mint',
               'Pressed "i". Then answered "tea".  Sprite says ice_cream_list, which should NOT have:'
               '"mint"<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"ice_cream_list": ['mint', ''],
                                            "dry_list": ['crunches', 'peanuts', 'coconut'],
                                            "wet_list": ['chocolate', 'caramel', 'cream', ],
                                            'sensing_answer': ['poop', ]
                                            }),
             [[1, 'mint .*? poop',
               'Pressed "i". Then answered "poop".  Sprite says ice_cream_list, which should be exactly this:'
               '"mint poop"<br>'],
              [2, 'strawberry',
               'Pressed "i". Then answered "poop".  Sprite says ice_cream_list, which should NOT have:'
               '"strawberry" in it<br>'],
              ],
             ],
        ],
        '42_5': [
            [brickLayer(0, 0, 0, variables={"ice_cream_list": ['strawberry', 'vanilla', 'chocolate', ],
                                            "dry_list": ['crunches', 'peanuts', 'coconut'],
                                            "wet_list": ['chocolate', 'caramel', 'cream', ],
                                            'sensing_answer': ['hotsauce', ]
                                            }),
             [[1, 'chocolate .*? caramel .*? cream .*? hotsauce',
               'Pressed "w". Then answered "hotsauce".  Sprite says wet_list, which should be exactly this:'
               '"chocolate caramel cream hotsauce"<br>'],
              [2, 'poop',
               'Pressed "w". Then answered "poop".  Sprite says wet_list, which should NOT have:'
               '"poop"<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"ice_cream_list": ['strawberry', 'vanilla', 'chocolate', ],
                                            "dry_list": ['crunches', 'peanuts', 'coconut'],
                                            "wet_list": ['kiwisauce'],
                                            'sensing_answer': ['poop', ]
                                            }),
             [[1, 'kiwisauce .*? poop',
               'Pressed "w". Then answered "poop".  Sprite says wetlist, which should be exactly this:'
               '"kiwisauce poop"<br>'],
              [2, 'caramel',
               'Pressed "w". Then answered "poop".  Sprite says ice_cream_list, which should NOT have:'
               '"caramel" in it<br>'],
              ],
             ],
        ],
        '42_7': [
            [brickLayer(0, 0, 0, variables={"ice_cream_list": ['chocolate', 'vanilla'],
                                            "dry_list": ['crunches', 'peanuts', 'coconut'],
                                            "wet_list": ['chocolate', 'caramel', 'cream', ],
                                            'sensing_answer': ['wet_list', '2', '2', '2', '2']
                                            }),
             [[1, 'chocolate .*? .*? cream .*?',
               'Pressed "x". Then answered "wet_list".  Then answered 2.  List before deletion was this:'
               "['chocolate', 'caramel', 'cream'].<br> List after deletion is supposed to be this:"
               "['chocolate', 'cream']"],
              [2, 'poop',
               'Pressed "x". Then answered "wet_list".  Then answered 2.  List before deletion was this:'
               "['chocolate', 'caramel', 'cream'].<br> List after deletion should NOT include this:"
               "poop"],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"ice_cream_list": ['chocolate', 'vanilla'],
                                            "dry_list": ['crunches', 'peanuts', 'coconut'],
                                            "wet_list": ['poop', 'sauce'],
                                            'sensing_answer': ['wet_list', '2', '2', '2', '2']
                                            }),
             [[1, 'poop',
               'Pressed "x". Then answered "wet_list".  Then answered 2.  List before deletion was this:'
               "['poop', 'sauce'].<br> List after deletion is supposed to be this:"
               "['poop']"],
              [2, 'chocolate',
               'Pressed "x". Then answered "wet_list".  Then answered 2.  List before deletion was this:'
               "['chocolate', 'caramel', 'cream'].<br> List after deletion should NOT include this:"
               "chocolate"],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"ice_cream_list": ['chocolate', 'vanilla'],
                                            "wet_list": ['chocolate', 'caramel', 'cream', ],
                                            "dry_list": ['crunch', 'gummies', 'coconut'],
                                            'sensing_answer': ['dry_list', '3', '3', '3', '3', ]
                                            }),
             [[1, 'crunch .*? gummies',
               'Pressed "x". Then answered "dry_list".  Then answered 3.  List before deletion was this:'
               " ['crunch', 'gummies', 'coconut'].<br> List after deletion is supposed to be this:"
               " ['crunch', 'gummies',]"],
              [2, 'driedbooger',
               'Pressed "w". Then answered "dry_list".  Sprite says ice_cream_list, which should NOT have:'
               '"driedbooger" in it<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"ice_cream_list": ['chocolate', 'vanilla'],
                                            "wet_list": ['chocolate', 'caramel', 'cream', ],
                                            "dry_list": ['coconut', 'driedbooger', 'flakes'],
                                            'sensing_answer': ['dry_list', '1', '1', '1', '1', '1']
                                            }),
             [[1, 'driedbooger .*? flakes',
               'Pressed "x". Then answered "dry_list".  Then answered 1.  List before deletion was this:'
               "['coconut', 'driedbooger', 'crunch'].<br> List after deletion is supposed to be this:"
               "['driedbooger', 'flakes']"],
              [2, 'crunch',
               'Pressed "x". Then answered "dry_list".  Then answered 1.  List before deletion was this:'
               "['coconut', 'driedbooger', 'flakes'].<br> List after deletion should NOT include this:"
               "crunch"],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"wet_list": ['chocolate', 'caramel', 'cream', ],
                                            "dry_list": ['crunch', 'gummies', 'coconut'],
                                            "ice_cream_list": ['strawberry', 'chocolate', 'vanilla'],
                                            'sensing_answer': ['ice_cream_list', '1', '1', '1', '1', '1']
                                            }),
             [[1, 'chocolate .*? vanilla',
               'Pressed "x". Then answered "ice_cream_list".  Then answered 1.  List before deletion was this:'
               "['strawberry', 'chocolate', 'vanilla'].<br> List after deletion is supposed to be this:"
               "['chocolate', 'vanilla']"],
              [2, 'peach',
               'Pressed "x". Then answered "ice_cream_list".  Then answered 1.  List before deletion was this:'
               "['strawberry', 'chocolate', 'vanilla'].<br> List after deletion should NOT include this:"
               "crunch"],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"wet_list": ['chocolate', 'caramel', 'cream', ],
                                            "dry_list": ['crunch', 'gummies', 'coconut'],
                                            "ice_cream_list": ['mint', 'peach', ],
                                            'sensing_answer': ['ice_cream_list', '1', '1', '1', '1', '1']
                                            }),
             [[1, 'peach',
               'Pressed "x". Then answered "ice_cream_list".  Then answered 1.  List before deletion was this:'
               "['mint', 'peach'].<br> List after deletion is supposed to be this:"
               "['peach']"],
              [2, 'strawberry',
               'Pressed "x". Then answered "ice_cream_list".  Then answered 1.  List before deletion was this:'
               "['mint', 'peach'].<br> List after deletion should NOT include this:"
               "mint"],
              ],
             ],
        ],
        '43a_2': [
            [brickLayer(0, 0, 0, variables={"songs": ['Brahms op 118 no 1', 'Brahms op 118 no 2', 'Brahms op 118 no 3',
                                                      'Brahms op 118 no 4', 'Brahms op 118 no 5',
                                                      'Brahms op 118 no 6', ]
                                            }),
             [[1, 'Brahms \s op \s 118 \s no \s 1 \s Brahms \s op \s 118 \s no \s 2 \s'
                  'Brahms \s op \s 118 \s no \s 3 \s Brahms \s op \s 118 \s no \s 4 \s'
                  'Brahms \s op \s 118 \s no \s 5 \s Brahms \s op \s 118 \s no \s 6 \s',
               'Pressed "1". Song list is  Brahms op 118 no 1, Brahms op 118 no 2 ... Brahms op 118 no 6.'
               '<br>Sprite should say every song in the list."<br>'],
              [2, 'club',
               'Pressed "1". Song list is  Brahms op 118 no 1, Brahms op 118 no 2 ... Brahms op 118 no 6.'
               '<br>Sprite should say NOT say "in da club".<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['in da club', ]
                                            }),
             [[1, 'club',
               'Pressed "1". Song list is 1 song: "in da club".'
               '<br>Sprite should say ONLY in da club."<br>'],
              [2, 'one \s more \s time',
               'Pressed "1". Song list is 1 song: "in da club".'
               '<br>Sprite should say NOT say baby one more time."<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['Baby one more time', 'Oops I did it again', 'Lucky', ]
                                            }),
             [[1, 'Baby \s one \s more \s time \s Oops \s I \s did \s it \s again \s Lucky',
               "Pressed '1'. Song list is 3 songs : ['Baby one more time', 'Oops I did it again', 'Lucky', ]."
               '<br>Sprite should say Baby one more time Oops I did it again Lucky.<br>'],
              [2, 'rahms',
               "Pressed '1'. Song list is 3 songs : ['Baby one more time', 'Oops I did it again', 'Lucky', ]."
               '<br>Sprite should say NOT Brahms."<br>'],
              ],
             ],
        ],
        '43a_4': [
            [brickLayer(0, 0, 0, variables={"songs": ['Brahms op 118 no 1', 'Brahms op 118 no 2', 'Brahms op 118 no 3',
                                                      'Brahms op 118 no 4', 'Brahms op 118 no 5',
                                                      'Brahms op 118 no 6', ]
                                            }),
             [[1, 'Brahms \s op \s 118 \s no \s 1 \s Brahms \s op \s 118 \s no \s 3 \s '
                  'Brahms \s op \s 118 \s no \s 5 \s',
               'Pressed "2". Song list is  Brahms op 118 no 1, Brahms op 118 no 2 ... Brahms op 118 no 6.'
               '<br>Sprite should say every other song in the list : '
               'Brahms op 118 no 1, Brahms op 118 no 3 Brahms op 118 no 5.<br>'],
              [2, 'club',
               'Pressed "2". Song list is Brahms op 118 no 1, Brahms op 118 no 2 ... Brahms op 118 no 6.'
               '<br>Sprite should say NOT say "in da club".<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['in da club', ]
                                            }),
             [[1, 'club',
               'Pressed "2". Song list is 1 song: "in da club".'
               '<br>Sprite should say ONLY in da club."<br>'],
              [2, 'one \s more \s time',
               'Pressed "2". Song list is 1 song: "in da club".'
               '<br>Sprite should say NOT say baby one more time."<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['Baby one more time', 'Oops I did it again', 'Lucky',
                                                      'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes', 'My prerogative']
                                            }),
             [[1, 'Baby \s one \s more \s time \s Lucky \s Stronger\s Sometimes',
               "Pressed '2'. Song list is 8 songs : ['Baby one more time', 'Oops I did it again', 'Lucky',"
               "'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]."
               '<br>Sprite should say this: Baby one more time  Lucky Stronger Sometimes.<br><br>'
               'If are you reading this message, you may have hard-coded the code to work with '
               'a playlist of exactly 6 items instead of using length_of_list.<br>'],
              [2, 'rahms',
               "Pressed '2'. Song list is 8 songs.]."
               '<br>Sprite should say NOT Brahms."<br>'],
              ],
             ],
        ],
        '43a_6': [
            [brickLayer(0, 0, 0, variables={"songs": ['Brahms op 118 no 1', 'Brahms op 118 no 2', 'Brahms op 118 no 3',
                                                      'Brahms op 118 no 4', 'Brahms op 118 no 5',
                                                      'Brahms op 118 no 6', ]
                                            }),
             [[1, 'Brahms \s op \s 118 \s no \s 3 \s Brahms \s op \s 118 \s no \s 4 \s ',
               'Pressed "3". Song list is  Brahms op 118 no 1, Brahms op 118 no 2 ... Brahms op 118 no 6.'
               '<br>Sprite should say  all songs except first two and last two : '
               'Brahms op 118 no 3, Brahms op 118 no 4.<br>'],
              [2, 'club',
               'Pressed "3". Song list is Brahms op 118 no 1, Brahms op 118 no 2 ... Brahms op 118 no 6.'
               '<br>Sprite should say NOT say "in da club".<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['in da club', ]
                                            }),
             [[1, '',
               'Pressed "3". Song list is 1 song: "in da club".'
               '<br>Sprite should say not say anything (if under 4, skip)."<br>'],
              [2, 'one \s more \s time',
               'Pressed "3". Song list is 1 song: "in da club".'
               '<br>Sprite should say NOT say baby one more time."<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['Baby one more time', 'Oops I did it again', 'Lucky',
                                                      'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes', 'My prerogative']
                                            }),
             [[1, 'Lucky \s Crazy \s Stronger \s Slave \s 4 \s U ',
               "Pressed '3'. Song list is 8 songs : ['Baby one more time', 'Oops I did it again', 'Lucky',"
               "'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]."
               '<br>Sprite should say this:Lucky Crazy Stronger Slave 4 U.<br><br>'
               'If are you reading this message, you may have hard-coded the code to work  '
               'with a list of exactly 6 instead of using length_of_list.<br>'],
              [2, 'rahms',
               "Pressed '3'. Song list is 8 songs: ['Baby one more time', 'Oops I did it again', 'Lucky',"
               "'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]."
               '<br>Sprite should NOT say Brahms."<br>'],
              [2, 'prerogative',
               "Pressed '3'. Song list is 8 songs. ['Baby one more time', 'Oops I did it again', 'Lucky',"
               "'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]."
               '<br>Sprite should NOT say my prerogative."<br>'],
              ],
             ],
        ],
        '43a_8': [
            [brickLayer(0, 0, 0, variables={"songs": ['Brahms op 118 no 1', 'Brahms op 118 no 2', 'Brahms op 118 no 3',
                                                      'Brahms op 118 no 4', 'Brahms op 118 no 5',
                                                      'Brahms op 118 no 6', ]
                                            }),
             [[1, 'Brahms \s op \s 118 \s no \s 6 \s Brahms \s op \s 118 \s no \s 5 \s'
                  'Brahms \s op \s 118 \s no \s 4 \s Brahms \s op \s 118 \s no \s 3 \s'
                  'Brahms \s op \s 118 \s no \s 2 \s Brahms \s op \s 118 \s no \s 1 \s',
               'Pressed "4". Song list is  Brahms op 118 no 1, Brahms op 118 no 2 ... Brahms op 118 no 6.'
               '<br>Sprite should say  all songs in reverse order : '
               'Brahms op 118 no 6 Brahms op 118 no 5 Brahms op 118 no 4 Brahms op 118 no 3'
               'Brahms op 118 no 2 Brahms op 118 no 1.<br>'],
              [2, 'club',
               'Pressed "4". Song list is Brahms op 118 no 1, Brahms op 118 no 2 ... Brahms op 118 no 6.'
               '<br>Sprite should say NOT say "in da club".<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['in da club', ]
                                            }),
             [[1, '',
               'Pressed "4". Song list is 1 song: "in da club".'
               '<br>Sprite should say not say anything (if under 4, skip)."<br>'],
              [2, 'one \s more \s time',
               'Pressed "4". Song list is 1 song: "in da club".'
               '<br>Sprite should say NOT say baby one more time."<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['Baby one more time', 'Oops I did it again', 'Lucky',
                                                      'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes', 'My prerogative']
                                            }),
             [[1, 'My \s prerogative \s Sometimes \s Slave \s 4 \s U \s Stronger \s Crazy \s Lucky \s '
                  'Oops \s I \s did \s it \s again \s Baby \s one \s more \s time ',
               "Pressed '4'. Song list is 8 songs : ['Baby one more time', 'Oops I did it again', 'Lucky',"
               "'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]."
               '<br>Sprite should say this: My prerogative Sometimes Slave 4 U Stronger Crazy Lucky '
               'Oops I did it again Baby one more time.<br><br>'
               'If are you reading this message, you may have hard-coded the code to work with '
               'exactly 6 items in the list instead of using length_of_list.<br>'],
              [2, 'rahms',
               "Pressed '4'. Song list is 8 songs: ['Baby one more time', 'Oops I did it again', 'Lucky',"
               "'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]."
               '<br>Sprite should NOT say Brahms."<br>'],
              ],
             ],
        ],
        '43b_2': [
            [brickLayer(0, 0, 0, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                      'She Wolf', 'Runaway', 'Jesus Walks',
                                                      'Blood on the Leaves',
                                                      "Cant tell me nothing", ]
                                            }),
             [[1, 'Whenever \s wherever \s Jesus \s Walks \s Blood \s on \s the \s Leaves \s'
                  'Cant \s tell \s me \s nothing',
               "<br>Sprite should say Whenever wherever Jesus Walks Blood on the Leaves Cant tell me nothing"
               ".<br>"],
              [2, 'club',
               "Pressed '1'. Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
               "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]",
               "<br>Sprite should say NOT say  'in da club'.<br>", ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['in da club', ]
                                            }),
             [[1, '^',
               'Pressed "1". Song list is 1 song: "in da club (10 letters)".'
               '<br>Sprite should say nothing (needs to be MORE than 10 letters)."<br>'],
              [2, 'one \s more \s time',
               'Pressed "1". Song list is 1 song: "in da club".'
               '<br>Sprite should say NOT say baby one more time."<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['Baby one more time', 'Oops I did it again', 'Lucky',
                                                      'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes', 'My prerogative']
                                            }),
             [[1, 'Baby \s one \s more \s time \s Oops \s I \s did \s it \s again \s My \s prerogative',
               "Pressed '1'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should say Baby one more time Oops I did it again My prerogative.<br>'],
              [2, 'whenever',
               "Pressed '1'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should say NOT whenever."<br>'],
              ],
             ],
        ],
        '43b_4': [
            [brickLayer(0, 0, 0, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                      'She Wolf', 'Runaway', 'Jesus Walks',
                                                      'Blood on the Leaves',
                                                      "Cant tell me nothing", ]
                                            }),
             [[1, 'Chantaje \s Cant \s tell \s me \s nothing',
               "<br>Pressed '2'.   Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
               "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]"
               "<br>Sprite should say Chantaje Cant tell me nothing"
               ".<br>"],
              [2, 'club',
               "Pressed '2'. Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
               "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]",
               "<br>Sprite should say NOT say  'in da club'.<br>", ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['in da club', ]
                                            }),
             [[1, '^',
               'Pressed "2". Song list is 1 song: "in da club (10 letters)".'
               '<br>Sprite should say nothing."<br>'],
              [2, 'one \s more \s time',
               'Pressed "2". Song list is 1 song: "in da club".'
               '<br>Sprite should say NOT say baby one more time."<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['Baby one more time', 'Oops I did it again', 'Lucky',
                                                      'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes', 'My prerogative']
                                            }),
             [[1, 'Crazy \s',
               "Pressed '2'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should say Crazy .<br>'],
              [2, 'Chantaje',
               "Pressed '2'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should say NOT Chantaje."<br>'],
              [2, 'Lucky',
               "Pressed '2'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should NOT say Lucky."<br>'],

              ],
             ],
        ],
        '43b_6': [
            [brickLayer(0, 0, 0, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                      'She Wolf', 'Runaway', 'Jesus Walks',
                                                      'Blood on the Leaves',
                                                      "Cant tell me nothing", ]
                                            }),
             [[1, 'Runaway',
               "<br>Pressed '3'.   Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
               "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]"
               "<br>Sprite should say Chantaje Cant tell me nothing"
               ".<br>"],
              [2, 'club',
               "Pressed '3'. Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
               "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]",
               "<br>Sprite should say NOT say  'in da club'.<br>", ],
              ],
             [2, 'Wolf',
              "Pressed '3'. Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
              "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]",
              "<br>Sprite should say NOT say  'She Wolf'.<br>", ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['in da club', ]
                                            }),
             [[1, '^',
               'Pressed "3". Song list is 1 song: "in da club ".'
               '<br>Sprite should say nothing."<br>'],
              [2, 'one \s more \s time',
               'Pressed "3". Song list is 1 song: "in da club".'
               '<br>Sprite should say NOT say baby one more time."<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['Baby one more time', 'Oops I did it again', 'Lucky',
                                                      'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes', 'My prerogative']
                                            }),
             [[1, 'Lucky \s Crazy',
               "Pressed '3'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should say Lucky Crazy .<br>'],
              [2, 'Chantaje',
               "Pressed '3'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should say NOT Chantaje."<br>'],
              [2, 'Stronger',
               "Pressed '3'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should NOT say Stronger."<br>'],

              ],
             ],
        ],
        '43b_8': [
            [brickLayer(0, 0, 0, variables={"songs": ['Chantaje', 'Whenever wherever',
                                                      'She Wolf', 'Runaway', 'Jesus Walks',
                                                      'Blood on the Leaves',
                                                      "Cant tell me nothing", ]
                                            }),
             [[1, 'Chantaje \s Whenever \s wherever \s She \s Wolf \s Jesus \s Walks \s Blood \s on \s the \s Leaves \s'
                  'Cant \s tell \s me \s nothing',
               "<br>Pressed '4'.   Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
               "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]"
               "<br>Sprite should say Chantaje Whenever wherever She Wolf Jesus Walks Blood on the Leaves "
               "Cant tell me nothing"
               ".<br>"],
              [2, 'club',
               "Pressed '4'. Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
               "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]",
               "<br>Sprite should say NOT say  'in da club'.<br>", ],
              ],
             [2, 'Runaway',
              "Pressed '4'. Test song list is 7 songs by Shakira ['Chantaje', 'Whenever wherever',"
              "'She Wolf', 'Runaway', 'Jesus Walks', 'Blood on the Leaves', 'Cant tell me nothing', ]",
              "<br>Sprite should say NOT say  'Runaway'.<br>", ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['in da club', ]
                                            }),
             [[1, '^',
               'Pressed "4". Song list is 1 song: "in da club ".'
               '<br>Sprite should say nothing."<br>'],
              [2, 'one \s more \s time',
               'Pressed "4". Song list is 1 song: "in da club".'
               '<br>Sprite should say NOT say baby one more time."<br>'],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"songs": ['Baby one more time', 'Oops I did it again', 'Lucky',
                                                      'Crazy', 'Stronger', 'Slave 4 U', 'Sometimes', 'My prerogative']
                                            }),
             [[1, 'Baby \s one \s more \s time \s Stronger \s Slave \s 4 \s U \s Sometimes \s My \s prerogative',
               "Pressed '4'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should say Baby one more time Stronger Slave 4 U Sometimes My prerogative .<br>'],
              [2, 'Chantaje',
               "Pressed '4'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should say NOT Chantaje."<br>'],
              [2, 'Lucky',
               "Pressed '4'. Song list is 8 Britney songs songs ['Baby one more time', 'Oops I did it again', "
               "'Lucky','Crazy', 'Stronger', 'Slave 4 U', 'Sometimes','My prerogative' ]"
               '<br>Sprite should NOT say Lucky."<br>'],
              ],
             ],
        ],
        '44_1': [
            [brickLayer(0, 0, 0, variables={"numbers": [5, 2, -4, 0, ]}),
             [[1, '3',
               "Pressed '1'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].  Sum should be 3"],
              [2, '5',
               "Pressed '1'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].  Sum should be 3, not 555.<br>",
               ],
              [2, '9',
               "Pressed '1'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].  Sum should be 3, not 999.<br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [999]}),
             [[1, '999',
               "Pressed '1'.  Numbers list is [999].  Sum should be 999"],
              [2, '3',
               "Pressed '1'.  Numbers list is [999].  Sum should be 999, not 3.<br>",
               ],
              [2, '5',
               "Pressed '1'.  Numbers list is [999].  Sum should be 999, not 555.<br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]}),
             [[1, '555',
               "Pressed '1'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].  Sum should be 555"],
              [2, '3',
               "Pressed '1'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].  Sum should be 555, not 3.<br>",
               ],
              [2, '9',
               "Pressed '1'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].  Sum should be 555, "
               "not 999.<br>",
               ],
              ],
             ],
        ],
        '44_3': [
            [brickLayer(0, 0, 0, variables={"numbers": [5, 2, -4, 0, ]}),
             [[1, '0\.75',
               "Pressed '2'.  Numbers list is [5, 2, -4, 0, ].  Average should be 0.75"],
              [2, '4',
               "Pressed '2'.  Numbers list is [5, 2, -4, 0, ].  Average should be 0.75, "
               "not 50.45.<br>",
               ],
              [2, '9',
               "Pressed '2'.  Numbers list is [5, 2, -4, 0, ].  Average should be 0.75, "
               "not 999.<br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [999]}),
             [[1, '999',
               "Pressed '2'.  Numbers list is [999].  Average should be 999"],
              [2, '5',
               "Pressed '2'.  Numbers list is [999].  Average should be 999, not 50.45.<br>",
               ],
              [2, '7',
               "Pressed '2'.  Numbers list is [999].  Average should be 999, not 0.75.<br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]}),
             [[1, '50\.45',
               "Pressed '2'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].  Average should be 50.45"],
              [2, '7',
               "Pressed '2'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].   Average should be 50.45, "
               "not 0.75.<br>",
               ],
              [2, '9',
               "Pressed '2'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].   Average should be 50.45,"
               "not 999.<br>",
               ],
              ],
             ],
        ],
        '44_5': [
            [brickLayer(0, 0, 0, variables={"numbers": [5, 2, -4, 0, ]}),
             [[1, '(True|true)',
               "Pressed '3'.  Numbers list is [5, 2, -4, 0, ]]. Should say 'True'."],
              [2, '(False|false)',
               "Pressed '3'.  Numbers list is [5, 2, -4, 0, ]].  Should say 'True', not 'False' ",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [999]}),
             [[1, '(False|false)',
               "Pressed '3'.  Numbers list is [999].  Should say 'False'"],
              [2, '5',
               "Pressed '3'.  Numbers list is [999].  Should say 'False' not 'True.<br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555, ]}),
             [[1, '(True|true)',
               "Pressed '3'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555].  Should say 'True"],
              [2, '7',
               "Pressed '3'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 555]. Should say 'True' not 'False, ",
               ],
              ],
             ],
        ],
        '44_7': [
            [brickLayer(0, 0, 0, variables={"numbers": [5, 2, -4, 0, ]}),
             [[1, '5',
               "Pressed '4'.  Numbers list is [5, 2, -4, 0, ]. Maximum should be 5 and sprite should say this."],
              [2, '9',
               "Pressed '4'.  Numbers list is [5, 2, -4, 0, ]. Maximum is NOT 9, sprite should not say a 9  , "
               "not 50.45.<br>",
               ],
              [2, '6',
               "Pressed '4'.  Numbers list is [5, 2, -4, 0, ].  Maximum is NOT 6, sprite should not say a 6, "
               "not 999.<br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [999]}),
             [[1, '999',
               "Pressed '4'.  Numbers list is [999].  Maximum should be 999 and sprite should say this."],
              [2, '5',
               "Pressed '4'.  Numbers list is [999]. Maximum is NOT 5, sprite should not say a 5 .<br>",
               ],
              [2, '6',
               "Pressed '4'.  Numbers list is [999].   Maximum is NOT 6, sprite should not say a 6, .<br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666, ]}),
             [[1, '666',
               "Pressed '4'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666].  Maximum is 666 "
               "and sprite should say this"],
              [2, '5',
               "Pressed '4'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666].  Maximum is NOT 5 and sprite "
               "should not say a 5, ",
               ],
              [2, '9',
               "Pressed '4'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666].   Maximum is NOT 9 and "
               "sprite should not say 9.<br>",
               ],
              ],
             ],
        ],
        '44_9': [
            [brickLayer(0, 0, 0, variables={"numbers": [5, 2, -4, 0, ]}),
             [[1, "\['5', \s '2', \s '4', \s '0']",
               "Pressed '5'.  Numbers list is [5, 2, -4, 0, ]. New list should be [5, 2, 4, 0] "
               " and sprite should say this."],
              [2, "\['999']",
               "Pressed '5'.  Numbers list is [5, 2, -4, 0, ].  New list should be [5, 2, 4, 0], NOT [999]<br>",
               ],
              [2, "\['1', \s '2', \s '3', \s '4', \s '5', \s '1', \s '2', \s '3', \s '4', \s '5',  \s '666'] ",
               "Pressed '5'.  Numbers list is [5, 2, -4, 0, ].  New list should be [5, 2, 4, 0], NOT "
               "[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 666] <br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [999]}),
             [[1, '999',
               "Pressed '5'.  Numbers list is [999].  New list should be [999] and sprite should say this."],
              [2, '5',
               "Pressed '5'.  Numbers list is [999].  New list should be [999], NOT  [5, 2, 4, 0] .<br>",
               ],
              [2, '6',
               "Pressed '5'.  Numbers list is [999].  New list should be [999], NOT  "
               "[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 666].<br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666, ]}),
             [[1, "\['1', \s '2', \s '3', \s '4', \s '5', \s '1', \s '2', \s '3', \s '4', \s '5',  \s '666']",
               "Pressed '5'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666]. New list should be"
               " [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 666] and sprite should  say this"],
              [2, "999",
               "Pressed '5'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666].  New list should be"
               " [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 666] and NOT [999]",
               ],
              [2, "\['5', \s '2', \s '4', \s '0']",
               "Pressed '5'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666].  New list should be"
               " [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 666] and NOT [5, 2, 4, 0]",
               ],
              ],
             ],
        ],
        '44_11': [
            [brickLayer(0, 0, 0, variables={"numbers": [5, 2, -4, 0, ]}),
             [[1, "\['2', \s '-4', \s '0']",
               "Pressed '6'.  Numbers list is [5, 2, -4, 0, ]. New list should be [2, -4, 0] "
               " and sprite should say this."],
              [2, "\[]",
               "Pressed '6'.  Numbers list is [5, 2, -4, 0, ].   New list should be [2, -4, 0], NOT []<br>",
               ],
              [2, "\['2', \s '4', \s '2', \s '4', \s '666'] ",
               "Pressed '6'.  Numbers list is [5, 2, -4, 0, ].  New list should be [2, -4, 0] , NOT "
               "[2, 4, -2, -4, 666] <br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [999]}),
             [[1, '\[]',
               "Pressed '6'.  Numbers list is [999].  New list should be [] and sprite should say this."],
              [2, "\['2', \s '-4', \s '0']",
               "Pressed '6'.  Numbers list is [999].  New list should be [], NOT [2, -4, 0].<br>",
               ],
              [2,  "\['2', \s '4', \s '2', \s '4', \s '666'] ",
               "Pressed '6'.  Numbers list is [999].  New list should be [], NOT [2, 4, -2, -4, 666] <br>",
               ],
              ],
             ],
            [brickLayer(0, 0, 0, variables={"numbers": [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666, ]}),
             [[1, "\['2', \s '4', \s '-2', \s '-4', \s '666'] ",
               "Pressed '6'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666]. New list should be"
               "[2, 4, 2, 4, 666] and sprite should  say this"],
              [2, "999",
               "Pressed '6'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666].  New list should be"
               " [2, 4, -2, -4, 666] and NOT []",
               ],
              [2, "\['5', \s '2', \s '4', \s '0']",
               "Pressed '6'.  Numbers list is [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 666].  New list should be"
               " [2, 4, -2, -4, 666] and NOT [2, -4, 0]",
               ],
              ],
             ],
        ],
    }
    p_test = {"name": "Testing that " + script_test_description[this_test].lower() + '(' + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>" + script_test_description[this_test],
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>  This test does NOT pass successfully: " +
                              script_test_description[this_test],
              "points": 0
              }
    [test_event, script] = one_event(p_scripts, events[this_test])
    if test_event['pass'] is False:
        p_test['fail_message'] += test_event['fail_message']
        return p_test
    else:
        passed = True

    # dictionary of links to pages
    # dicationary.  key = testname, value: list[ [ sprite.  [1/0, jpass conditions (list), error message ]   ] .
        sprites = runs[this_test]
        for sprite_info in sprites:
            tests = sprite_info[1]
            for test in tests:
                sprite = copy.deepcopy(sprite_info[0])
                search_flag = test[0]
                search_string = test[1]
                error_string = test[2]
                test_run = do_sprite(sprite, script, True)
                if test_run is False:
                    p_test['fail_message'] += "<h5 style=\"color:purple;\"> Run crashed try again<br>" \
                                              "sprite said this:<br>" + sprite.say_history + " </h5>"
                    return p_test
                else:
                    pass_individual = True
                    print("search this {}".format(search_string))
                    print("sprite said this: {}".format(sprite.say_history))
                    if search_flag == 1:
                        if not re.search(search_string, str(sprite.say_history), re.X | re.M | re.S):
                            passed = False
                            pass_individual = False
                    elif search_flag == 2:
                        if re.search(search_string, str(sprite.say_history), re.X | re.M | re.S):
                            passed = False
                            pass_individual = False
                    if pass_individual is False:
                        p_test['fail_message'] += '<h5 style=\"color:purple;\">' + error_string + \
                                                  "<br>Sprite said this for entire script: " + \
                                                  str(sprite.say_history) + "<br></h5>"
    if passed:
        p_test['points'] += p_points
        p_test['pass'] = True
    else:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                  '<br>See link for example: <a href="' + links[this_test] + \
                                  '" target="_blank">link to page in presentation or lab</a></h5>'
    return p_test


def one_event(p_scripts, event, p_points=0):
    """
    Finds the number of sprites that are NOT background
    :param p_scripts:  - all scratch scripts (list of dictionaries)
    :param event:  - regex of event I'm looking for (str) example: event_whenflagclicked
    :param p_points:  - points this is worth (int)
    :return: a dictionary with test info as well as the script itself
    """
    import re
    event_dict = {"event_whenflagclicked": 'green flag',
                  "'event_whenkeypressed',\s'd'": "When d pressed",
                  "'event_whenkeypressed',\s'i'": "When i pressed",
                  "'event_whenkeypressed',\s'w'": "When w pressed",
                  "'event_whenkeypressed',\s'x'": "When x pressed",
                  "'event_whenkeypressed',\s'0'": "When 0 pressed",
                  "'event_whenkeypressed',\s'1'": "When 1 pressed",
                  "'event_whenkeypressed',\s'2'": "When 2 pressed",
                  "'event_whenkeypressed',\s'3'": "When 3 pressed",
                  "'event_whenkeypressed',\s'4'": "When 4 pressed",
                  "'event_whenkeypressed',\s'5'": "When 5 pressed",
                  "'event_whenkeypressed',\s'6'": "When 6 pressed",
                  "'event_whenkeypressed',\s'right \s arrow'": "When right arrow pressed",
                  "'event_whenkeypressed',\s'left \s arrow'": "When left arrow pressed",
                  "'event_whenkeypressed',\s'space'": "When space pressed",
                  "'event_whenbroadcastreceived',\s'~ready'": "When I receive \"~ready\" ",
                  "'event_whenbroadcastreceived'": "When broadcast received (any broadcast) ",
                  }
    p_test = {"name": "Checking there is only one event of " + str(event) + " (" + str(p_points) + " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Scripts have only one event of " + str(event) + " .<br>",
              "points": 0
              }
    count = 0
    if event == "'event_whenbroadcastreceived'":
        final_script = ''
    else:
        final_script = {}
    for key in p_scripts:
        script = p_scripts[key]
        found = re.search(event, str(script), re.X | re.M | re.S)
        if found:
            count += 1
            if event == "'event_whenbroadcastreceived'":
                final_script += str(script)
            else:
                final_script = script

    if count != 1 and event != "'event_whenbroadcastreceived'":
        p_test['pass'] = False
        p_test['fail_message'] = "<h5 style=\"color:purple;\">You are supposed to have exactly one of '" + \
                                 event_dict[event] + "'.  <br>Autograder found: " + str(count) + \
                                 "<br>If you have too many, please merge code into one and recheck.<br>" \
                                 '<br>See link for reason why you only want one sprite:' \
                                 ' <a href="https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m' \
                                 '8QGkVhDJWf62lFVITA/edit#slide=id.g896bf80e15_0_3">link</a></h5>'
    return [p_test, final_script]


def one_custom_block(p_scripts, custom_block, p_points=0):
    """
    Verifies a particular custom_block only shows up once
    :param p_scripts:  - all scratch scripts (list of dictionaries)
    :param custom_block:  - name of custom_block  I'm looking for (str) example: draw_triangle
    :param p_points:  - points this is worth (int)
    :return: dictionary containing custom block
    """
    import re
    p_test = {"name": "Checking there is only one custom block of " + str(custom_block) + " (" + str(p_points) +
                      " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Scripts have only one custom_block of " + str(custom_block) + " .<br>",
              "points": 0
              }
    count = 0
    final_block = {}
    for key in p_scripts:
        script = p_scripts[key]
        search_this = "^" + custom_block + "($|\s)"
        found = re.search(search_this, key, re.X | re.M | re.S)
        if found:
            count += 1
            final_block = {key: script}
    if count != 1:
        p_test['pass'] = False
        p_test['fail_message'] = "<h5 style=\"color:purple;\">" \
                                 "You need exactly one custom block named <i>exactly</i> '" + \
                                 custom_block + "'.  <br>Autograder found: " + str(count) + \
                                 "<br>If you have too many, please merge code into one and recheck.<br> </h5>"
    return [p_test, final_block]


def find_sprite_name(p_json, p_name):
    """
    Finds the number of sprites that are NOT background
    :param p_json:  - json of all code
    :param p_name: name you are looking for
    :return: all matches, as a list of integers
    """
    for target in p_json['targets']:
        if target['name'] == p_name:
            return True
    return False


# delete after 1.9 hecked
def count_stage_changes(p_json):
    """
    Finds the number of times backdrop changes happen (does not work for repeats)
    :param p_json:  - json of all code
    :return: all matches, as a list of integers
    """
    import re
    changes = 0
    matches = 0
    for target in p_json['targets']:
        if target['isStage'] is True:
            matches = len(re.findall(r'(looks_nextbackdrop|looks_switchbackdropto)', str(p_json), re.X | re.M | re.S))
        else:
            matches = len(re.findall(r'(looks_nextbackdrop|looks_switchbackdropto)', str(p_json), re.X | re.M | re.S))
        if matches:
            changes += matches
    return matches


def unique_coordinates(p_coordinates):
    """
    Gets unique coordintes from list of coordinates
    :param p_coordinates: something like [ [0,0], [150, 0], [0,0]
    :return: something like [ [0,0], [150,0]
    """
    temp_dict = {}
    off = False
    for coordinate in p_coordinates:
        if coordinate == 'penup':
            off = True
        elif coordinate == 'pendown':
            off = False
        elif off is False:
            coord_tuple = tuple(coordinate)
            if coord_tuple not in temp_dict:
                temp_dict[coord_tuple] = 1
    return_coordinates = [list(key) for key, val in temp_dict.items()]
    print("RETURN COOREDS " + str(return_coordinates))
    return return_coordinates


def distance(p1, p2):
    """
    Given 2 points p1 and p2, calculate distance
    :param p1: list like [0,0]
    :param p2: list like [0,150]
    :return: distance
    """
    import math
    print("before crash " + str(p1) + " " + str(p2))
    d = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return d


def is_equilateral_triangle(p_coordinates):
    """
    tests to see if 3 points is equilateral triangle.  Basically a = b = c.
    Also that there are 3 points
    :param p_coordinates:
    :return: True is yes, F if no
    """
    if len(p_coordinates) != 3:
        return False
    d12 = distance(p_coordinates[0], p_coordinates[1])
    d23 = distance(p_coordinates[1], p_coordinates[2])
    d13 = distance(p_coordinates[0], p_coordinates[2])
    tol = 0.02 * d12
    if abs(d12 - d23) < tol and abs(d12 - d13) < tol and abs(d23 - d13) < tol:
        return True
    else:
        return False


def is_square(p_coordinates):
    """
    tests to see if 4 points is square.  See algorithm:
    https://softwareengineering.stackexchange.com/questions/176938/how-to-check-if-4-points-form-a-square
    :param p_coordinates:
    :return: True is yes, F if no
    """

    if len(p_coordinates) != 4:
        return False
    d12 = distance(p_coordinates[0], p_coordinates[1])
    d13 = distance(p_coordinates[0], p_coordinates[2])
    d14 = distance(p_coordinates[0], p_coordinates[3])
    d23 = distance(p_coordinates[1], p_coordinates[2])
    d24 = distance(p_coordinates[1], p_coordinates[3])
    d34 = distance(p_coordinates[2], p_coordinates[3])
    tol = 0.02 * d12
    if abs(d12 - d13) < tol:   # distance to 4 is the long one
        if abs(d14 - d23) < tol:
            return True
        else:
            return False
    elif abs(d12 - d14) < tol:  # distance to 3 is the long one
        if abs(d13 - d24) < tol:
            return True
        else:
            return False
    elif abs(d13 - d14) < tol:  # distance to 2 is the long one
        if abs(d12 - d34) < tol:
            return True
        else:
            return False


def midpoint(p1, p2):
    """
        Given 2 points p1 and p2, calculate distance
        :param p1: list like [0,0]
        :param p2: list like [0,150]
        :return: midpoint (list like [0,75]
        """
    p_midpoint = [(p1[0] + p2[0]) / 2.0, (p1[1] + p2[1])]
    return p_midpoint


def is_parallelogram(p_coordinates):
    """
    tests to see if 4 points is square.  See algorithm:
    https://www.geeksforgeeks.org/check-whether-four-points-make-parallelogram/
    :param p_coordinates:
    :return: True is yes, F if no
    """

    if len(p_coordinates) != 4:
        return False

    midpoint12 = midpoint(p_coordinates[0], p_coordinates[1])
    midpoint13 = midpoint(p_coordinates[0], p_coordinates[2])
    midpoint14 = midpoint(p_coordinates[0], p_coordinates[3])
    midpoint23 = midpoint(p_coordinates[1], p_coordinates[2])
    midpoint24 = midpoint(p_coordinates[1], p_coordinates[3])
    midpoint34 = midpoint(p_coordinates[2], p_coordinates[3])

    midpoints = [midpoint12,  midpoint13, midpoint14, midpoint23, midpoint24, midpoint34]

    tol = 0.1
    match = 0
    for i, midpoint1 in enumerate(midpoints):
        for j, midpoint2 in enumerate(midpoints):
            if i == j:
                continue
            if distance(midpoint1, midpoint2) < tol:
                match += 1
    if match == 2:
        return True
    else:
        return False


def is_pentagon(p_coordinates):
    """
    tests to see if 4 points is square.  See algorithm:
    https://www.geeksforgeeks.org/check-whether-four-points-make-parallelogram/
    :param p_coordinates:
    :return: True is yes, F if no
    """
    if len(p_coordinates) != 5:
        return False
    d12 = distance(p_coordinates[0], p_coordinates[1])

    tol = 0.03 * d12
    matches = {}
    for i, point1 in enumerate(p_coordinates):
        for j, point2 in enumerate(p_coordinates):
            if j <= i:
                continue
            distance_p1_p2 = distance(point1, point2)
            key = round(distance_p1_p2, 2)
            found = False
            for key2 in matches.keys():
                if abs(float(key) - float(key2)) < tol:
                    matches[key2] += 1
                    found = True
                    break
            if found is False:
                matches[key] = 1
    for key in matches:
        if matches[key] != 5:
            return False
    return True


def custom_block_exists(p_name, p_num_parameters, p_scripts, points=0):
    """
    Tests to see if procedure with X name and certain variables exists
    :param p_name: names that I'm looking for with args.  Like make_triangle %s
    :param p_num_parameters: number of input parameters that the custom block has (int)
    :param p_scripts: dictionary of scripts
    :param points: number of points this test is worth
    :return: True or false
    """
    import re
    p_test = {"name": "Checking that there is a custom block called " + str(p_name) + " with " +
                      str(p_num_parameters) + " input parameters (" + str(points) + " points).<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "There is a custom block called " + str(p_name) + " with " + str(p_num_parameters) +
                              " input parameters.",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              '<h5 style=\"color:purple;\">' 
                              "There is not a custom block called " + str(p_name) + " with " +
                              str(p_num_parameters) + " input parameters.</h5>",
              "points": 0
              }
    search_string = p_name
    for _ in range(p_num_parameters):
        search_string += "\s VARIABLE_ .*? "
    search_string = '^' + search_string
    for key in p_scripts.keys():
        if re.search(search_string, key, re.X | re.M | re.S):
            p_test['pass'] = True
            p_test['points'] += points
            return p_test
    return p_test


def extract_custom_custom_block(p_name, p_num_parameters, p_scripts):
    """
    Tests to see if procedure with X name and certain variables exists
    :param p_name: names that I'm looking for with args.  Like make_triangle %s
    :param p_num_parameters: number of input parameters that the custom block has (int)
    :param p_scripts: dictionary of scripts
    :return: dictionary of custom block
    """
    import re
    custom_block_test = custom_block_exists(p_name, p_num_parameters, p_scripts)
    if custom_block_test['pass']:
        search_string = p_name
        for _ in range(p_num_parameters):
            search_string += "\s VARIABLE_ .*? "
        search_string = '^' + search_string
        for key in p_scripts.keys():
            if re.search(search_string, key, re.X | re.M | re.S):
                return p_scripts[key]
    else:
        return {}


def extract_procedure_name(p_name, p_scripts):
    """
    Tests to see if procedure with X name and certain variables exists
    :param p_name: names that I'm looking for with args.  Like make_triangle %s
    :param p_scripts: dictionary of scripts
    :return: True or false
    """
    import re
    for key in p_scripts.keys():
        match = '^' + p_name + ' '
        if re.search(match, key, re.X | re.M | re.S):
            return key
    return ''


def free_points(p_points):
    """
    Gives free points
    :param p_points: Number of points this test is worth
    :return: test dictionary
    """
    p_test = {"name": "Free points "
                      "(" + str(p_points) + " points)",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>"
                              "Free points. <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>"
                              "This will always pass.  <br>",
              'points': 0
              }
    p_test['points'] += p_points
    return p_test


def variable_check_no_space(p_monitors):
    import re
    test_spaces = {"name": "Testing that Scratch variables have no spaces",
                   "pass": True,
                   "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Scratch variables appear to have no spaces",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                   "Looks like there is at least one space in your variables "
                                   " Rename your variable and and resubmit.<br>"
                                   "File name should be like this: <br> <br>",
                   'points': 0,
                   }
    for monitor in p_monitors:
        if monitor['opcode'] == 'data_variable':
            variable = monitor['params']['VARIABLE']
            if re.search(r'\s', variable):
                test_spaces['pass'] = False
                test_spaces['fail_message'] += 'This variable has a space in it: ' + str(variable) + "<br>"
    return test_spaces


def variable_check_list_different_name_than_regular(p_monitors):
    p_test = {"name": "Testing that Scratch list variables have different names than regular variables. ",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> Scratch list variables have different names "
                              "than regular variables",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Looks like there is at least one list variable with the same name"
                              "as a regular variable "
                              " Rename your variables and and resubmit.<br>",
              'points': 0,
              }
    regular_variable_names = []
    list_variables_names = []
    for monitor in p_monitors:
        if 'LIST' in monitor['params']:
            list_variables_names.append(monitor['params']['LIST'])
        elif 'VARIABLE' in monitor['params']:
            regular_variable_names.append(monitor['params']['VARIABLE'])
    for variable in regular_variable_names:
        if variable in list_variables_names:
            p_test['pass'] = False
            p_test['fail_message'] += "<h5 style=\"color:purple;\">" \
                                      "You have both a list and a regular variables with this name:" + str(variable) + \
                                      '<br>Please rename one or both of them.<br>' \
                                      'See link for good naming conventions:<a href="https://docs.google.com/' \
                                      'presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/' \
                                      'edit#slide=id.g77373e6d39_0_0" target="_blank">link</a>'

    return p_test


def check_straggler_variable_no_space(p_scripts):
    import re
    test_spaces = {"name": "Testing that straggler Scratch variables have no spaces",
                   "pass": True,
                   "pass_message": "<h5 style=\"color:green;\">Pass!</h5>Scratch variables appear to have no spaces",
                   "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                   "Looks like there is at least one space in a variable in a block somewhere.  <br> "
                                   "This error can happen if you rename a variable - scratch does not automatically"
                                   " go through and rename your variables everywhere. <br>You have to take out the old "
                                   "variable and put in the new variable.  <br> <br>",
                   'points': 0,
                   }
    for key in p_scripts:
        script = p_scripts[key]
        match = re.findall(r"\'VARIABLE_ (.*?)  \'", str(script), re.X | re.M | re.S)
        if match:
            for capture in match:
                variable = capture
                if re.search(r"\s", variable, re.X | re.M | re.S):
                    test_spaces['pass'] = False
                    test_spaces['fail_message'] += "<h5 style=\"color:purple;\">" \
                                                   "This variable has a space in it: " + str(capture) +\
                                                   "</h5>  Debugging information: <br>" \
                                                   "Bad script is this:" + str(script)
    return test_spaces


def set_variable_in_block(p_script, p_variable):
    """
    verifies you aren't setting a variable in a script where you don't want
    :param p_script: that script
    :param p_variable: variable you arelooking for
    :return: a test dictionary
    """
    import re
    p_test = {"name": "Testing that this script has a 'set " + str(p_variable) + " to xxx",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5> This script has a 'set " +
                              str(p_variable) + " to xxx' ",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> This script has does not have a 'set  " +
                              str(p_variable) +
                              " to xxx'. <br> This variable name is special for this problem and should not be used."
                              "<br> Sometimes you are reading this error because you are doing something like set "
                              "(singular) variable = list.<br><br>",
              'points': 0,
              }
    findthis = r"\[\'data_setvariableto', \s \'" + str(p_variable) + "\', .+? ]"
    match = re.search(findthis, str(p_script), re.X | re.M | re.S)
    if match:
        p_test['pass'] = True
    return p_test


def run_custom_block_check_say(testname, p_scripts, p_points):
    """
    Runs the custom block, sees what it says.  Assumes one sprite only.
    :param testname - name of test (string)
    :param p_scripts: scripts (dict)
    :param p_points: points it is worth (int)
    :return: a test dictionary
    """
    import re
    import copy
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2  import brickLayer, do_sprite
    test_info = {
        '32_1': {'name': 'happy_birthday',
                 'block_params': 1,
                 'description': "Checking that happy_birthday with one input paramter 'name works. <br>",
                 'help_link': 'https://docs.google.com/presentation/d/14BGDnhzYyNK6ON0ouAyyo3Q-T7VpJO2FLC0iD_0p53U/'
                              'edit#slide=id.g85a5e95574_0_0',
                 'run_info': [
                     [1,
                      brickLayer(0, 0, 0, pendown=False, variables={"name": 'McGlathery'}),
                      [[1, '(McGlathery|Mcglathery|mcglathery)',
                        'Ran happy_birthday with argument "McGlathery".  Expected sprite to say McGlathery, Mcglathery,'
                        'or mcglathery, but sprite does not say it.'],
                       [1, '(birthday|Birthday|BIRTHDAY)',
                        'Ran happy_birthday with argument "McGlathery".  Expected sprite to say birthday,'
                        ' but sprite does not say it.'],
                       [2, 'ordan',
                        'Ran happy_birthday with argument "McGlathery".  Sprite should NOT say Jordan but it does.'
                        ],
                       ]
                      ],
                     [1,
                      brickLayer(0, 0, 0, pendown=False, variables={"name": 'Michael Jordan'}),
                      [[1, '(Jordan|jordan)',
                        'Ran happy_birthday with argument "Michael Jordan".  Expected sprite to say Jordan.'],
                       [1, '(birthday|Birthday|BIRTHDAY)',
                        'Ran happy_birthday with argument "Michael Jordan".  Expected sprite to say birthday,'
                        ' but sprite does not say it.'],
                       [2, 'athery',
                        'Ran happy_birthday with argument "Michael Jjrdan".  Sprite should NOT say McGlathery, but'
                        'it does'
                        ],
                       ]
                      ]
                 ]
                 },
        '34_1': {'name': 'day_of_week',
                 'block_params': 1,
                 'description': "Checking that day_of_week with one input parameter 'day' works. <br>",
                 'help_link': 'https://docs.google.com/presentation/d/1hub7R1qTCGTqgKRP_gzZ-j9dJ3st7HM4_hmeBJlxkds/'
                              'edit#slide=id.g739f674ef6_2_27',
                 'run_info': [
                     [1,
                      brickLayer(0, 0, 0, pendown=False, variables={"day": '1'}),
                      [[1, '(sunday|Sunday)',
                        'Ran day_of_week with argument "1".  Expected sprite to say Sunday,'
                        'but sprite does not say it.'],
                       [2, '(friday|Friday)',
                        'Ran day_of_week with argument "1".  Expected sprite to say Sunday.<br>'
                        'Sprite should NOT say "Friday" but it does.'
                        ],
                       ]
                      ],
                     [1,
                      brickLayer(0, 0, 0, pendown=False, variables={"day": '6'}),
                      [[1, '(friday|Friday)',
                        'Ran day_of_week with argument "6".  Expected sprite to say Friday,'
                        'but sprite does not say it.'],
                       [2, '(sunday|Sunday)',
                        'Ran day_of_week with argument "6".  Expected sprite to say Friday.<br>'
                        'Sprite should NOT say "Sunday" but it does.'
                        ],
                       ]
                      ],
                 ]
                 },
        '34_2': {'name': 'min',
                 'block_params': 2,
                 'description': "Checking that min with two input parameters 'number1' and 'number2' works. <br>",
                 'help_link': 'https://docs.google.com/presentation/d/1hub7R1qTCGTqgKRP_gzZ-j9dJ3st7HM4_hmeBJlxkds/'
                              'edit#slide=id.g739f674ef6_2_27',
                 'run_info': [
                     [1,
                      brickLayer(0, 0, 0, pendown=False, variables={"number1": 5, "number2": 8}),
                      [[1, '5',
                        'Ran min with arguments "5" and "8".  Expected sprite to say 5,'
                        'but sprite does not say it.'],
                       [2, '8',
                        'Ran min with arguments "5" and "8".  Expected sprite to say 5,'
                        'Sprite should NOT say "8" but it does.'
                        ],
                       ]
                      ],
                     [1,
                      brickLayer(0, 0, 0, pendown=False, variables={"number1": 555, "number2": -8}),
                      [[1, '-8',
                        'Ran min with arguments "555" and "-8".  Expected sprite to say -8,'
                        'but sprite does not say it.'],
                       [2, '5',
                        'Ran min with arguments "555" and "-8".  Expected sprite to say -8.<br>'
                        'Sprite should NOT say anything with "5" in it, but it does.'
                        ],
                       ]
                      ],
                     [1,
                      brickLayer(0, 0, 0, pendown=False, variables={"number1": 9, "number2": 9}),
                      [[1, '9',
                        'Ran min with arguments "9" and "9".  Expected sprite to say 9,'
                        'but sprite does not say it.'],
                       ]
                      ]
                 ]
                 },
        '34_3': {'name': 'distance',
                 'block_params': 2,
                 'description': "Checking that min with two input parameters 'x2' and 'y2' works. <br>",
                 'help_link': 'https://docs.google.com/document/d/1B-ul2dJZcHLAQJEsAQRv-P2oDS-pO070EVjYevAB4nE/edit#'
                              'bookmark=id.1cuoovnkpnvu',
                 'run_info': [
                     [1,
                      brickLayer(0, 0, 0, pendown=False, variables={"x2": 3, "y2": 4}),
                      [[1, '5',
                        'Ran distance with arguments "3" and "4".  Expected sprite to say 5,'
                        'but sprite does not say it.'],
                       [2, '10',
                        'Ran distance  with arguments "5" and "8".  Expected sprite to say 5,'
                        'Sprite should NOT say "10" but it does.'
                        ],
                       ]
                      ],
                     [1,
                      brickLayer(10, 10, 0, pendown=False, variables={"x2": 16, "y2": 18}),
                      [[1, '10',
                        'Ran min with arguments "16" and "18" and x1=10 y1=10.  Expected sprite to say 10,'
                        'but sprite does not say it.'],
                       [2, '5',
                        'Ran min with arguments "16" and "18" and x1=10 y1=10.  Expected sprite to say 10.<br>'
                        'Sprite should NOT say anything with "5" in it, but it does.'
                        ],
                       ]
                      ],
                 ]
                 },

        '42_1': {'name': 'smash_in',
                 'block_params': 0,
                 'description': "Checking that smash_in works. <br>"
                                "ice_cream_list = [ 'strawberry', 'vanilla', 'chocolate']<br>"
                                "dry_list = ['coconut', 'gummies', 'sprinkles']<br>"
                                "If I run this custom block 100 times, it should give every possible "
                                "combination of smash_in.<br>",
                 'help_link': 'https://docs.google.com/document/d/1E0ji1aLrLEWMeBryNT4_s59f'
                              'YE4JXq0Q74b9rxGRx44/edit#bookmark=id.vwmbm3xtl6m2',
                 'run_info': [
                     [30,
                      brickLayer(0, 0, 0, variables={
                          'wet_list': ['cream', 'fudge', ],
                          "ice_cream_list": ['strawberry', 'vanilla', 'chocolate', ],
                          'dry_list': ['coconut', 'gummies', 'sprinkles', ]
                      }
                                 ),
                      [[1, 'strawberry', 'Ran smash_in 100 times.  Expected sprite to say strawberry (ice cream) '
                                         'at least once, but sprite does not say it.'],
                       [1, 'vanilla', 'Ran smash_in 100 times.  Expected sprite to say vanilla (ice cream) '
                                      'at least once, but sprite does not say it.'],
                       [1, 'chocolate', 'Ran smash_in 100 times.  Expected sprite to say chocolate (ice cream) '
                                        'at least once, but sprite does not say it.'],
                       [1, 'coconut', 'Ran smash_in 100 times.  Expected sprite to say coconut (dry topping) '
                                      'at least once, but sprite does not say it.'],
                       [1, 'gummies', 'Ran smash_in 100 times.  Expected sprite to say gummies (dry topping) '
                                      'at least once, but sprite does not say it.'],
                       [1, 'sprinkles', 'Ran smash_in 100 times.  Expected sprite to say sprinkls (dry topping) '
                                        'at least once, but sprite does not say it.'],
                       ]
                      ],
                     [1,
                      brickLayer(0, 0, 0, variables={
                          "ice_cream_list": ['dairy-free sorbet', ],
                          'dry_list': ['poop pellets', ]
                      }
                                 ),
                      [[2, 'strawberry', 'Ran smash_in once with ice_cream_list = ["dairy-free sorbet"] and dry_list = '
                                         '["poop pellets"].'
                                         '  Expected that strawberry should NOT appear in what sprite '
                                         'says, but it does.'],
                       [1, 'sorbet', 'Ran smash_in once with ice_cream_list = ["dairy-free sorbet"] and dry_list = '
                                     '["poop pellets"].'
                                     'Expected that sorbet should appear in what sprite says.'],
                       ],
                      ]
                 ]
                 },
        '42_2': {'name': 'smash_in',
                 'block_params': 0,
                 'description': "Checking that smash_in works with correct spacing. <br>"
                                "ice_cream_list = [ 'mint']<br>"
                                "dry_list = ['peanuts',]<br>"
                                "If I run this custom block, it should give 'strawberry peanuts' with a space in "
                                "between the two items<br>",
                 'help_link': 'https://docs.google.com/presentation/d/1IU3JXnclUJUgxMDorXXrDn42m8QGkVhDJWf62lFVITA/'
                              'edit#slide=id.g848c669080_0_5',
                 'run_info': [
                     [1,
                      brickLayer(0, 0, 0, variables={
                          'wet_list': ['cream', 'fudge', ],
                          "ice_cream_list": ['mint', ],
                          'dry_list': ['peanuts', ]
                      }
                                 ),
                      [[1, 'mint \s+ peanuts', 'Ran smash_in.  Expected sprite to say mint peanuts'],
                       ]
                      ],
                 ]
                 },
        '42_3': {'name': 'sundae',
                 'block_params': 0,
                 'description': "Checking that sundae works. <br>"
                                "ice_cream_list = [ 'strawberry', 'vanilla', 'chocolate']<br>"
                                "wet_list = ['fudge', 'caramel', 'whipped cream']<br>"
                                "If I run this custom block 100 times, it should give every possible "
                                "combination of sundae.<br>",
                 'help_link': 'https://docs.google.com/document/d/1E0ji1aLrLEWMeBryNT4_s59f'
                              'YE4JXq0Q74b9rxGRx44/edit#bookmark=id.vwmbm3xtl6m2',
                 'run_info': [
                     [30,
                      brickLayer(0, 0, 0, variables={
                          'dry_list': ['peanuts', 'crunches'],
                          "ice_cream_list": ['strawberry', 'vanilla', 'chocolate', ],
                          'wet_list': ['fudge', 'caramel', 'whipped cream', ]
                      }
                                 ),
                      [[1, 'strawberry', 'Ran sundae 100 times.  Expected sprite to say strawberry (ice cream) '
                                         'at least once, but sprite does not say it.'],
                       [1, 'vanilla', 'Ran sundae 100 times.  Expected sprite to say vanilla (ice cream) '
                                      'at least once, but sprite does not say it.'],
                       [1, 'chocolate', 'Ran sundae 100 times.  Expected sprite to say chocolate (ice cream) '
                                        'at least once, but sprite does not say it.'],
                       [1, 'fudge', 'Ran sundae 100 times.  Expected sprite to say fudge (wet topping) '
                                    'at least once, but sprite does not say it.'],
                       [1, 'caramel', 'Ran sundae 100 times.  Expected sprite to say caramel (wet topping) '
                                      'at least once, but sprite does not say it.'],
                       [1, 'whipped \s cream',
                        'Ran sundae 100 times.  Expected sprite to say whipped cream (dry topping) '
                        'at least once, but sprite does not say it.'],
                       ]
                      ],
                     [1,
                      brickLayer(0, 0, 0, variables={
                          'dry_list': ['peanuts', ],
                          "ice_cream_list": ['sorbet', ],
                          'wet_list': ['poop', ]
                      }
                                 ),
                      [[2, 'strawberry', 'Ran sundae once with ice_cream_list = ["sorbet"] and wet_list = ["poop"].'
                                         '  Expected that strawberry should NOT appear in what sprite '
                                         'says, but it does.'],
                       [1, 'sorbet \s+ poop', 'Ran sundae once with ice_cream_list = ["sorbet"] and wet_list = '
                                              '["poop"]. Expected that sprite says "sorbet poop".'],
                       ],
                      ],
                 ]
                 },
    }

    p_test = {"name": "Testing that " + test_info[testname]['name'].lower() + ' works (' + str(p_points) + " points)",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass. <h5>" + test_info[testname]['description'],
              "fail_message": "<h5 style=\"color:red;\">Fail. </h5>  This test does NOT pass successfully: " +
                              test_info[testname]['description'],
              "points": 0
              }
    test_block = custom_block_exists(test_info[testname]['name'], test_info[testname]['block_params'], p_scripts)
    if test_block['pass'] is False:
        p_test['fail_message'] += test_block['fail_message']
        return p_test
    else:
        passed = True
        custom_block = extract_custom_custom_block(test_info[testname]['name'], test_info[testname]['block_params'],
                                                   p_scripts)

    # dictionary of links to pages
    # dicationary.  key = testname, value: list[ [ sprite.  [1/0, jpass conditions (list), error message ]   ] .
        sprites = test_info[testname]['run_info']
        for sprite_info in sprites:
            tests = sprite_info[2]
            times = sprite_info[0]
            for test in tests:
                sprite = copy.deepcopy(sprite_info[1])
                search_flag = test[0]
                search_string = test[1]
                error_string = test[2]
                print("CUstom block " + str(custom_block))
                for _ in range(times):
                    test_run = do_sprite(sprite, custom_block, True)
                    sprite.say_history += "<br>"
                    if test_run is False:
                        p_test['fail_message'] += "<h5 style=\"color:purple;\"> Run crashed try again </h5>"
                        return p_test
                pass_individual = True
                if search_flag == 1:
                    if not re.search(search_string, str(sprite.say_history), re.X | re.M | re.S):
                        passed = False
                        pass_individual = False
                elif search_flag == 2:
                    if re.search(search_string, str(sprite.say_history), re.X | re.M | re.S):
                        passed = False
                        pass_individual = False
                if pass_individual is False:
                    p_test['fail_message'] += '<h5 style=\"color:purple;\">' + error_string + \
                                              "<br>Sprite said this for all runs of custom block: <br>" + \
                                              str(sprite.say_history) + "</h5>"
    if passed:
        p_test['points'] += p_points
        p_test['pass'] = True
    else:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                                  '<br>See link for example: <a href="' + test_info[testname]['help_link'] + \
                                  '" target="_blank">link to page in presentation or lab</a></h5>'
    return p_test

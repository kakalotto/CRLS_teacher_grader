import math


class brickLayer(object):
    def __init__(self, x, y, direction, *, pendown=True, draw_targets={}, variables={}, check_targets=True):
        self.x = x
        self.y = y
        self.direction = math.radians(direction)
        self.draw_targets = draw_targets
        self.pendown = pendown
        self.move_history = [[self.x, self.y]]
        self.variables = variables
        self.say_history = ''
        self.error = ''
        self.check_targets = check_targets
        self.num_errors = 0

    def move(self, amount):
        orig_x = self.x
        orig_y = self.y
        amount = int(amount)
        self.y += round(math.cos(self.direction) * amount)
        self.x += round(math.sin(self.direction) * amount)
        # print("end move selfx {} selfy {} hist {}".format(self.x, self.y, self.move_history))
        if self.pendown is True:
            self.move_history.append([self.x, self.y])
        if self.pendown is True and self.check_targets:
            print("chek targets is on.  Checking {} ".format(((orig_x, orig_y), (self.x, self.y))))
            if ((orig_x, orig_y), (self.x, self.y)) in self.draw_targets.keys():
                print("is there, same order")
                self.draw_targets[((orig_x, orig_y), (self.x, self.y))] = 0
                return True
            elif ((self.x, self.y), (orig_x, orig_y)) in self.draw_targets.keys():
                print('is there, reversed')
                self.draw_targets[((self.x, self.y), (orig_x, orig_y))] = 0
                return True
            else:
                print("not there")
                return True

    def turn(self, amount):
        self.direction += amount
        # print("end turn selfx {} selfy {} hist {}".format(self.x, self.y, self.move_history))


def eval_boolean(p_boolean, p_sprite):
    """
    evaluates p_boolean given from scratch json, after simplifying
    :param p_boolean: the statement to evaluate
    :param p_sprite: sprite object(we will use the sprite variables)
    :return: True or False
    """
    import re

    print("aaa inside eval_boolean.  p_boolean {}".format(p_boolean))

    p_boolean = re.sub(",", '', p_boolean)
    p_boolean = re.sub('=', '==', p_boolean)
    p_boolean = sub_variables(p_boolean, p_sprite)
    print("aaa inside eval, after variable subs {}".format(p_boolean))
    words = p_boolean.split()
    p_boolean = ''
    print("aaa inside words {}".format(words))
    # got a blank?
    if len(words) == 2:
        if words[0] == '==' or words[0] == '>' or words[0] == '<':
            words.insert(0, "' '")
        else:
            words.append("' '")
    print("aaa inside wordsafter space check {}".format(words))

    for word in words:
        if word != '==' and word != '>' and word != '<':
            if re.search(r"[^a-zA-Z]", word):
                p_boolean += " " + word + " "  # numbers only
            else:
                p_boolean += "'" + word + "' "
        else:
            p_boolean += ' ' + word + ' '  # pass through ==, >, or <
    print("aaa inside   eval boolean{}".format(p_boolean))
    ret_val = eval(p_boolean)
    print(ret_val)
    return ret_val


def sub_variables(p_words, p_sprite):
    """
    Sub in variables to expressions
    :param p_words: words (such as VARIABLES_x is this)
    :param p_sprite: contains p_sprite.variables, which is the dictionary conversion of variables to values
    :return:
    """
    import re
    print("WORDS!!! " + str(p_words))
    p_words = str(p_words)
    p_words = re.sub("'", '', p_words)
    p_words = re.sub(r"\[", '', p_words)
    p_words = re.sub("]", '', p_words)
    pre_sub = p_words
    # print('aaa in sub_variables, before subbing {}'.format(p_words))
    print("sub variables lokoing here {}".format(p_sprite.variables))
    if re.search("VARIABLE_", p_words):
        for key in sorted(p_sprite.variables, key=len, reverse=True):
            #print("aaa key for subbing vars {}".format(key))
            match_string = r'VARIABLE_' + key
            match = re.search(match_string, p_words, re.X | re.M | re.S)
            if match:
                p_words = re.sub(match_string, str(p_sprite.variables[key]), p_words)
            # p_words = re.sub(sub_this, str(p_sprite.variables[variable_name]), p_words)
            words = p_words
            # print("aaa words after first sub {}".format(p_words))
    if re.search("sensing_answer", p_words):
        print('ccc sensing answer p_words{}'.format)
        if 'sensing_answer' not in p_sprite.variables.keys():
            return '0'
            raise Exception("Code has a sensing answer, but test does not. <br>"
                            "Students: Remove the question if you do'nt need it and do it a different way.<br>"
                            "Teacher: Create a sensing_answer variable in the sprite object.<br>")
        sensing_answers = True
        while sensing_answers:
            match_string = 'sensing_answer'
            print("ccc ensing answers match_string {}  p_words {}".format(match_string, p_words))
            match = re.search(match_string, p_words, re.X | re.M | re.S)
            if match:
                if 'current_answer' in p_sprite.variables:
                    answer = p_sprite.variables['current_answer']
                else:
                    answer = '1000000'
                p_words = re.sub(match_string, answer, p_words, 1)
            else:
                sensing_answers = False
    # print("aaa after all variable substitutios  pre: {} post: {}".format(pre_sub, p_words))
    return p_words


def do_sprite(p_sprite, moves, success):
    """
    This function does the sprite movements
    :param p_sprite: The sprite object
    :param moves: moves sprite will try (list, looks like scripts in main code)
    :param success: What it returns  If false then exit right away
    :return: True/False depending on if crash or maximum fly exceeded.
    """
    import re
    import random
    if success is False:
        print("ccc exiting, success if false")
        return False
    # print("aaa beginning of do sprite.  here are all  moves {} \n".format(moves))
    for i, move in enumerate(moves):
        # print("next move is this {}\n".format(move))
        if isinstance(move, list):
            ret_val = do_sprite(p_sprite, moves[i], success)
            if ret_val is False:
                success = False
                break
        else:
            # print("ggg move  to execute is this {}".format(move))
            if move == 'event_whenkeypressed':
                break
            if move == 'motion_movesteps':
                amount = sub_variables(str(moves[i+1]), p_sprite)

                ret_val = True
                try:
                    int(amount)
                    ret_value = p_sprite.move(amount)
                except ValueError:
                    p_sprite.say_history += "<br>Tried to move this amount and failed: " + \
                                            str(amount) + \
                                            "<br>  Lab 2.3a: Be sure your second question is how much you want" \
                                            " to move.<br>"
                    success = False
                if ret_val is False:
                    p_sprite.say_history += "Return value is false in move"
                    success = False
                break
            elif move == 'motion_turnleft':
                degrees = sub_variables(str(moves[i+1]), p_sprite)
                degrees = float(degrees)
                degrees = -math.radians(degrees)
                p_sprite.turn(degrees)
                break
            elif move == 'motion_turnright':
                degrees = sub_variables(str(moves[i+1]), p_sprite)
                degrees = float(degrees)
                degrees = math.radians(degrees)
                p_sprite.turn(degrees)
                break
            elif move == 'motion_pointindirection':
                direction = moves[i+1]
                # note this fails for anthing other than number
                p_sprite.direction = math.radians(float(direction))
                break
            elif move == 'motion_yposition':
                print("Y position1111 {}".format(p_sprite.y))
                return p_sprite.y
            elif move == 'motion_xposition':
                print("X position1111 'yesss {}".format(p_sprite.x))
                return p_sprite.x
            elif move == 'motion_changeyby':
                dy = int(moves[i + 1])
                if p_sprite.pendown is True:
                    orig_x = p_sprite.x
                    orig_y = p_sprite.y
                p_sprite.y += dy
                p_sprite.move_history.append([p_sprite.x, p_sprite.y])
                if p_sprite.pendown is True:
                    if ((orig_x, orig_y), (p_sprite.x, p_sprite.y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((orig_x, orig_y), (p_sprite.x, p_sprite.y))] = 0
                        return True
                    elif ((p_sprite.x, p_sprite.y), (orig_x, orig_y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((p_sprite.x, p_sprite.y), (orig_x, orig_y))] = 0
                        return True
                    else:
                        return False
                break
            elif move == 'motion_changexby':
                print("changexby")
                dx = int(moves[i + 1])
                if p_sprite.pendown is True:
                    orig_x = p_sprite.x
                    orig_y = p_sprite.y
                p_sprite.x += dx
                p_sprite.move_history.append([p_sprite.x, p_sprite.y])
                if p_sprite.pendown is True:
                    if ((orig_x, orig_y), (p_sprite.x, p_sprite.y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((orig_x, orig_y), (p_sprite.x, p_sprite.y))] = 0
                        return True
                    elif ((p_sprite.x, p_sprite.y), (orig_x, orig_y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((p_sprite.x, p_sprite.y), (orig_x, orig_y))] = 0
                        return True
                    else:
                        return False
                break
            elif move == 'motion_setx':
                x = int(moves[i + 1])
                if p_sprite.pendown is True:
                    orig_x = p_sprite.x
                    orig_y = p_sprite.y
                p_sprite.x = x
                p_sprite.move_history.append([p_sprite.x, p_sprite.y])

                if p_sprite.pendown is True:
                    if ((orig_x, orig_y), (p_sprite.x, p_sprite.y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((orig_x, orig_y), (p_sprite.x, p_sprite.y))] = 0
                        return True
                    elif ((p_sprite.x, p_sprite.y), (orig_x, orig_y)) in p_sprite.draw_targets.keys():
                        p_sprite.draw_targets[((p_sprite.x, p_sprite.y), (orig_x, orig_y))] = 0
                        return True
                    else:
                        return False
                break
            elif move == 'motion_gotoxy':
                if isinstance(moves[i + 1], list):
                    x = int(do_sprite(p_sprite, moves[i + 1], success))
                else:
                    x = int(moves[i + 1])
                if isinstance(moves[i + 2], list):
                    y = int(do_sprite(p_sprite, moves[i + 2], success))
                else:
                    y = int(moves[i + 2])

                p_sprite.x = x
                p_sprite.y = y
                p_sprite.move_history.append([p_sprite.x, p_sprite.y])

                break
            elif move == 'data_setvariableto':
                # print("ccc beginning of set variable to.   variable: {} value: {}".format(moves[i+1], moves[i+2]))
                key = moves[i + 1]
                value = moves[i + 2]
                if isinstance(value, list):
                    if str(value) == "['sensing_answer']":
                        value = p_sprite.variables['current_answer']
                    else:
                        value = do_sprite(p_sprite, value, success)
                value = str(value)
                value = sub_variables(value, p_sprite)

                if re.search(r'VARIABLE_', value, re.X | re.M | re.S):
                    value_no_variable = value.replace('VARIABLE_', '')
                    p_sprite.say_history += "<br><br>WARNING WARNING! You set the variable " + str(key) + \
                                            " to the variable " + str(value_no_variable) +\
                                            " before you set the value for " + str(value_no_variable) +\
                                            "<br> This will probably cause some bug or autograder failure later" \
                                            ".<br><br>"
                p_sprite.variables[key] = value

                # print('ccc variables after data_setvariableto after data set {}  '.format(p_sprite.variables))

                break
            elif move == 'data_changevariableby':
                variable_plus_variable = moves[1]
                print("aaa change variable.  variable {} changeby {}".format(moves[1], moves[2]))
                delta_value = moves[2]
                if isinstance(moves[2], list):
                    ret_val = do_sprite(p_sprite, moves[2], success)
                    delta_value = ret_val
                else:
                    delta_value = moves[2]
                print("aaa change delta {}".format(delta_value))
                delta_value = sub_variables(delta_value, p_sprite)
                if re.search(r'Error: Index out of range', str(delta_value)):
                    p_sprite.say_history = "BROKEN.  Tried to access an Index out of range.<br>" \
                                           "You are trying to access a list item that doesn't exist" \
                                           "<br>For example  trying to access a 5th item when there are " \
                                           "only 4 items in the list.<br>"
                    delta_value = 0
                elif re.search("\. \d", str(delta_value), re.X | re.M | re.S):
                    delta_value = float(delta_value)
                else:
                    delta_value = int(delta_value)
                variable = re.sub('VARIABLE_', '', variable_plus_variable)
                if variable in p_sprite.variables.keys():
                    print("vava " + str(p_sprite.variables[variable]))
                    if re.search(r"\d \. \d", str(p_sprite.variables[variable]), re.X | re.M | re.S):
                        p_sprite.variables[variable] = float(p_sprite.variables[variable])
                        p_sprite.variables[variable] += delta_value
                    elif re.search(r"^\d+", str(p_sprite.variables[variable]), re.X | re.M | re.S):
                        p_sprite.variables[variable] = int(p_sprite.variables[variable])
                        p_sprite.variables[variable] += delta_value
                    else:
                        p_sprite.error += "Bug in changing " + str(variable) + " by " + str(delta_value) + \
                                          ". Setting variable to " + str(delta_value) + " and continuing. <br>"
                        p_sprite.variables[variable] = delta_value
                else:
                    p_sprite.say_history += "Tried to edit variable " + str(variable) + \
                                            " but that variable does not exist.<br>" \
                                            " Did you remember to create the variable?<br>" \
                                            "Did you remember to set <variable> to <value> at the beginning?<br>"
                    return False
                print("changevariable by worked? {}".format(p_sprite.variables))
                break
            elif move == 'data_lengthoflist':
                list_name = moves[i + 1]
                if list_name in p_sprite.variables:
                    list_length = len(p_sprite.variables[list_name])
                else:
                    p_sprite.say_history += '<br>Tried to get length of this list in your code: ' + str(list_name) + \
                                            '<br>But this list is not expected to be in this script or custom block.' \
                                            '<br>Picked a length of 1 so as not to crash.<br>' \
                                            'Did you name your list wrong or are you using the wrong list? <br>' \
                                            'Please check the instructions.<br>' \
                                            'For example, if you name your variable "ice_creams" and the instructions '\
                                            'wants "ice_cream_list", you will get this error.<br> '
                    return 1
                return list_length
            elif move == 'data_itemoflist':
                index = moves[i + 1]
                list_name = moves[i + 2]
                # print("fff returning this for index {} list name {}".format(index, list_name))
                if isinstance(index, list):
                    index = do_sprite(p_sprite, index, success)
                index = sub_variables(str(index), p_sprite)
                # print("asdfasdf list name " + str(list_name))
                if list_name not in p_sprite.variables:
                    p_sprite.say_history += "<br>Found a bad variable/listname: " + str(list_name) + \
                                            ".  This variable or list name is in your script somewhere " \
                                            "and it should not be there.   <br>Check your pull downs to be sure" \
                                            " you did not accidentally select the wrong variable or list name." \
                                            "<br><br>"
                    return False
                list_length = len(p_sprite.variables[list_name])
                # print("iiu index {}".format(index))
                try:
                    temp = int(index)
                except ValueError:
                    p_sprite.say_history += "<br>Found an index of a list to be a non-integer number." \
                                            "List is this: " + str(list_name) + \
                                            "<br> and index is this: " + str(index) + "<br><br>"
                    return False
                index = int(index)
                if index - 1 < 0:
                    if p_sprite.num_errors < 5:
                        p_sprite.num_errors += 1
                        return "Error: Index is too low "\
                               "  Did you try to 'say' 0th item of list or something like that?<br> "
                    else:
                        return False
                try:
                    item = p_sprite.variables[list_name][index - 1]
                except IndexError:
                    return "Error: Index out of range.  " \
                           "You are trying to access the {} item in a list, " \
                           "but list only has {} items. <br>".format(index, list_length)
                return item
            elif move == 'data_deletealloflist':
                list_name = moves[i + 1]
                print("jjj data_deletealloflist")
                p_sprite.variables[list_name] = []

                break
            elif move == 'data_addtolist':
                item = moves[i + 1]
                list_name = moves[i + 2]
                if list_name not in p_sprite.variables:
                    p_sprite.say_history += 'Tried to access ' + \
                                            str(list_name) + ' of the sprite, but it does not exist in the list ' \
                                                             'of expected lists or variable names. <br>Did you name ' \
                                                             'your list wrong or are you using the wrong list? <br>' \
                                                             'Please check the instructions.<br>' \
                                                             'For example, if you name your variable "ice_creams"' \
                                                             ' and the instructions want "ice_cream_list", ' \
                                                             'you will get this error.<br> '
                    return False
                print("fff data_addtolist thisthis for item {} list name {}".format(item, list_name))
                if isinstance(item, list):
                    item = do_sprite(p_sprite, item, success)

                item = sub_variables(str(item), p_sprite)
                p_sprite.variables[list_name].append(item)

                break
            elif move == 'data_deleteoflist':
                item = moves[i + 1]
                list_name = moves[i + 2]
                print("fff data_deleteoflist item {} list name {}".format(item, list_name))
                if isinstance(item, list):
                    item = do_sprite(p_sprite, item, success)
                try:
                    item = int(sub_variables(str(item), p_sprite))
                except ValueError:
                    p_sprite.say_history += '<br>Tried to delete an invalid list entry.  Tried to delete this item: ' + \
                                            str(item) + " of this list " + list_name +\
                                            ".  If this says you tried to delete 'sensing_answer' that means you did " \
                                            "not ask a question when you were supposed to."

                    return False
                if list_name not in p_sprite.variables:
                    p_sprite.say_history += 'Tried to access ' + \
                                            str(list_name) +  \
                                            ' of the sprite, but it does not exist in the list ' \
                                                             'of expected lists or variable names. <br>Did you name ' \
                                                             'your list wrong or are you using the wrong list? <br>' \
                                                             'Please check the instructions.<br>' \
                                                             'For example, if you name your variable "ice_creams"' \
                                                             ' and the instructions want "ice_cream_list", ' \
                                                             'you will get this error.<br> '
                    return False
                try:
                    p_sprite.variables[list_name].pop(item - 1)
                except IndexError:
                    p_sprite.say_history += 'Tried to delete item ' + str(item) + ' from the list ' + str(list_name) + \
                                            ' but there is nothing there!<br>  For this test run, list ' + \
                                            str(list_name) + " is " + str(p_sprite.variables[list_name])

                break
            if move == 'operator_random':
                if 'mock_random' in p_sprite.variables:
                    this_random = p_sprite.variables['mock_random'].pop()
                    return this_random
                else:
                    print("These are the randoms!. {} {}".format(moves[1], moves[2]))
                    if isinstance(moves[2], list) is False:
                        try:
                            temp = int(moves[1])
                        except ValueError:
                            p_sprite.say_history += "Something wrong with random number generation. Random number " \
                                                    "bounds are the following {} and {}".format(moves[1], moves[2])
                            return 1
                        try:
                            temp = int(moves[2])
                        except ValueError:
                            p_sprite.say_history += "Something wrong with random number generation. Random number " \
                                                    "bounds are the following {} and {}".format(moves[1], moves[2])
                            return 1
                        if abs(float(moves[1]) - round(float(moves[1]))) < .001 and \
                                abs(float(moves[2]) - round(float(moves[2]))) < .001:
                            rand_number = random.randint(int(moves[1]), int(moves[2]))
                        else:
                            rand_number = random.uniform(float(moves[1]), float(moves[2]))
                        print("returning this  rand num {}".format(rand_number))
                    else:
                        upper_bound = do_sprite(p_sprite, moves[2], success)
                        try:
                            temp = int(moves[1])
                        except ValueError:
                            p_sprite.say_history += "Something wrong with random number generation. Random number " \
                                                    "bounds are the following {} and {}".format(moves[1], moves[2])
                            return 1
                        try:
                            temp = int(upper_bound)
                        except ValueError:
                            p_sprite.say_history += "Something wrong with random number generation. Random number " \
                                                    "bounds are the following {} and {}".format(moves[1], moves[2])
                            return 1
                        if abs(float(moves[1]) - round(float(moves[1]))) < .001 and \
                                abs(float(upper_bound) - round(float(upper_bound))) < .001:
                            print("rocky {} {}".format(moves[1], upper_bound))
                            rand_number = random.randint(int(moves[1]), int(upper_bound))
                        else:
                            rand_number = random.uniform(float(moves[1]), float(upper_bound))
                        # print("returning this  for randnumber {}".format(rand_number))
                    return rand_number
            if move == 'operator_mathop':
                programmed = ['sqrt', 'abs']
                operation = moves[i+1]
                if operation not in programmed:
                    p_sprite.say_history += "You tried a math operation that hasn't been programmed yet.<br>" \
                                            "Tried: " + str(operation)
                    return 0
                if isinstance(moves[i + 2], list):
                    mathop_arg = do_sprite(p_sprite, moves[i + 2], success)
                else:
                    mathop_arg = moves[i + 2]
                mathop_arg = sub_variables(str(mathop_arg), p_sprite)
                try:
                    test1 = float(mathop_arg)
                    test2 = int(mathop_arg)
                    if abs(test1 - test2) < 0.001:
                        temp = test2
                    else:
                        temp = test1
                except ValueError:
                    p_sprite.say_history += "Tried to convert mathop argument to float and ints but failed.<br> " \
                                            "Argument is {} Number is: {}".format(operation, mathop_arg)
                    return 0
                if operation == 'sqrt':
                    return temp ** 0.5
                elif operation == 'abs':
                    return abs(temp)

            elif move == 'operator_subtract':
                print("subtract! fmoves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                try:
                    temp = float(num1)
                except ValueError:
                    p_sprite.say_history += "First number of subtraction can't be converted to int. " \
                                             " Number is: {} <br>Returning a 0 instead.".format(num1)
                    return 0
                try:
                    temp = float(num2)
                except ValueError:
                    p_sprite.say_history += "Second number of subtraction can't be converted to int. " \
                                            " Number is: {} <br>Returning a 0 instead.".format(num2)
                    return 0
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(float(num1))
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(float(num2))
                else:
                    num2 = float(num2)
                evaluated = num1 - num2
                print("jjj ran operator_subtract and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_equals':
                print("operator_equals moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("operator_equals pre sub num1 {} num2 {}".format(num1, num2))
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                print("operator_equals post sub num1 {} num2 {}".format(num1, num2))
                
                evaluated = num1 == num2
                print("jjj ran operator_equals and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_contains':
                print("operator_contains moves {}".format(moves))
                if isinstance(moves[1], list):
                    char1 = do_sprite(p_sprite, moves[1], success)
                else:
                    char1 = moves[1]
                if isinstance(moves[2], list):
                    string1 = do_sprite(p_sprite, moves[2], success)
                else:
                    string1 = moves[2]
                print("operator_contains pre sub char1 {} string1 {}".format(char1, string1))
                char1 = sub_variables(str(char1), p_sprite)
                string1 = sub_variables(str(string1), p_sprite)
                print("operator_contains  post sub char1 {} string1 {}".format(char1, string1))
                evaluated = char1 in string1
                print("jjj ran operator_contains and got this {}".format(evaluated))
                return evaluated

            elif move == 'operator_gt':
                print("operator_gt moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                print("operator_gt post sub num1 {} num2 {}".format(num1, num2))

                try:
                    temp = float(num1)
                except ValueError:
                    p_sprite.say_history += "YOU HAVE A CODE BUG!!!!<br>" \
                                            "First number of gt can't be converted to float.  Number is: " + str(num1)
                    num1 = 0
                    # raise Exception("First number of gt can't be converted to float.  Number is: {}"
                    #                 .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    p_sprite.say_history += "YOU HAVE A CCODE BUG!!!! <br>" \
                                            "second number of gt can't be converted to float.  Number is: " + str(num2)
                    num2 = 0
                    # raise Exception("Second number of gt can't be converted to float.  Number is: {}"
                    #                 .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(float(num1))
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(float(num2))
                else:
                    num2 = float(num2)
                evaluated = num1 > num2
                print("jjj ran operator_gt and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_lt':
                print("operator_lt moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("operator_lt pre sub num1 {} num2 {}".format(num1, num2))
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                print("operator_lt post sub num1 {} num2 {}".format(num1, num2))

                try:
                    temp = float(num1)
                except ValueError:
                    num1 = 999999999999999999
                try:
                    temp = float(num2)
                except ValueError:
                    num2 = 99999999999

                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 < num2
                print("jjj ran operator_lt and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_and':
                print("operator_and moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("operator_and pre sub num1 {} num2 {}".format(num1, num2))
                if not isinstance(num1, bool):
                    num1 = sub_variables(str(num1), p_sprite)

                if not isinstance(num2, bool):
                    num2 = sub_variables(str(num2), p_sprite)
                print("operator_and post sub num1 {} num2 {}".format(num1, num2))


                evaluated = num1 and num2
                print("jjj ran operator_and and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_or':
                print("operator_or moves {}".format(moves))
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("operator_or pre sub num1 {} num2 {} {} {}".format(num1, num2, type(num1), type(num2)))
                if not isinstance(num1, bool):
                    num1 = sub_variables(str(num1), p_sprite)
                if not isinstance(num2, bool):
                    num2 = sub_variables(str(num2), p_sprite)
                print("operator_or post sub num1 {} num2 {} {} {}".format(num1, num2, type(num1), type(num2)))
                evaluated = num1 or num2
                # evaluated = bool(evaluated)

                print("jjj ran operator_or and got this {} {}".format(evaluated, type(evaluated)))
                return evaluated
            elif move == 'operator_mod':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)
                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of mod can't be converted to float.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of mod can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                print("aaa mod numbers are this num1 {} num2 {}".format(num1, num2))
                evaluated = num1 % num2
                print("jjj ran operator_mod and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_divide':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("aaa num1 {} num2 {}".format(num1, num2))
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)

                print("this is what I got num1 {} num2 {}".format(num1, num2))
                try:
                    temp = float(num1)
                except ValueError:
                    p_sprite.say_history += "First number of divide can't be converted to int.  Number is: " + str(num1)
                    return False
                try:
                    temp = float(num2)
                except ValueError:
                    p_sprite.say_history += "Second number of divide can't be converted to int.  Number is: " + str(num2)
                    return False
                    # raise Exception("Second number of divide can't be converted to int.  Number is: {}"
                    #                 .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                if num2 == 0:
                    evaluated = 9999999
                else:
                    evaluated = num1 / num2
                print("jjj ran operator_divide and got this {}".format(evaluated))
                return evaluated
            elif move == 'operator_multiply':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)

                try:
                    temp = float(num1)
                except ValueError:
                    p_sprite.say_history += "First number of subtraction can't be converted to int.  Number is: " +\
                                            str(num1)
                    num1 = 99999
#                    raise Exception("First number of subtraction can't be converted to int.  Number is: {}"
#                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    num2 = 99999999
                    p_sprite.say_history += "Second number of subtraction can't be converted to int.  Number is: " + \
                                            str(num2)


#                    raise Exception("Second number of subtraction can't be converted to int.  Number is: {}"
#                                    .format(num2))
                tol = 0.01
                print("LETS GO {} {} ".format(num1, num2))
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 * num2
                print("jjj ran operator_multiply and got this {}".format(evaluated))
                return evaluated

            elif move == 'operator_length':
                if isinstance(moves[1], list):
                    operator_string = do_sprite(p_sprite, moves[1], success)
                else:
                    operator_string = moves[1]
                operator_string = sub_variables(str(operator_string), p_sprite )
                print("iii operator_length l string is {} length is {}".format(operator_string, len(operator_string)))
                return len(operator_string)
            elif move == 'operator_letter_of':
                print("tried operator letter of")
                if isinstance(moves[1], list):
                    number = do_sprite(p_sprite, moves[1], success)
                else:
                    number = moves[1]
                print("aaa number {}".format(number))
                number = str(number)
                number = sub_variables(number, p_sprite)
                try:
                    number = int(number)
                except ValueError:
                    p_sprite.say_history += \
                        "Your number for operator_letter_of isn't an integer?  Got this: {}".format(moves[1])
                    p_sprite.say_history += "If this has VARIABLE_ in it, check to see you are setting the variable" \
                                            "in this script and that it isn't from outside the script.<br>"
                    number = 999999
#                    raise Exception("Your number for operator_letter_of isn't an integer?  Got this: {}".
#                                    format(moves[1]))
                if isinstance(moves[2], list):
                    operator_string = do_sprite(p_sprite, moves[2], success)
                else:
                    operator_string = moves[2]
                operator_string = sub_variables(str(operator_string), p_sprite)
                if number - 1 < 0 or number > len(operator_string):
                    p_sprite.say_history += "Tried to get letter more or less than word. N" \
                                            "umber is: {} word is : {} <br>".format(number, operator_string)
                    return 'broken list usage review say history<br>'
                return operator_string[number - 1].lower()
            elif move == 'operator_add':
                if isinstance(moves[1], list):
                    num1 = do_sprite(p_sprite, moves[1], success)
                else:
                    num1 = moves[1]
                if isinstance(moves[2], list):
                    num2 = do_sprite(p_sprite, moves[2], success)
                else:
                    num2 = moves[2]
                print("Trying to add num1 {}  num2 {}".format(num1, num2))
                num1 = sub_variables(str(num1), p_sprite)
                num2 = sub_variables(str(num2), p_sprite)

                try:
                    temp = float(num1)
                except ValueError:
                    raise Exception("First number of addition can't be converted to int.  Number is: {}"
                                    .format(num1))
                try:
                    temp = float(num2)
                except ValueError:
                    raise Exception("Second number of addition can't be converted to int.  Number is: {}"
                                    .format(num2))
                tol = 0.01
                if abs(round(float(num1)) - float(num1)) < tol:
                    num1 = float(num1)
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if abs(round(float(num2)) - float(num2)) < tol:
                    num2 = float(num2)
                    num2 = int(num2)
                else:
                    num2 = float(num2)
                evaluated = num1 + num2
                print("result of add operator is this: {}".format(evaluated))
                return evaluated
            elif move == 'pen_penUp':
                print('pen up')
                p_sprite.move_history.append('penup')
                p_sprite.pendown = False
            elif move == 'pen_penDown':
                print('pen down')
                p_sprite.move_history.append('pendown')

                p_sprite.pendown = True
            elif move == 'looks_sayforsecs':
                print("looks_say. beginning entire list " + str(moves))
                # print("looks say i is this {}".format(i))
                say_this = moves[i+1]

                # print("what is saying?  Type?  {}".format(type(moves[i+1])))
                if isinstance(say_this, list):
                    ret_val = do_sprite(p_sprite, say_this, success)
                    # print('ggg say this {}'.format(ret_val))
                    words_pre_sub = ret_val
                else:
                    words_pre_sub = str(moves[i+1])
                # print("looks_say.  beginning efore subbing words" + str(words_pre_sub))
                words = words_pre_sub
                if isinstance(words_pre_sub, str):
                    words_pre_sub = re.sub("'", '', words_pre_sub)
                    words_pre_sub = re.sub(r"\[", '', words_pre_sub)
                    words_pre_sub = re.sub("]", '', words_pre_sub)
                    # print('aaa presub words {}'.format(words_pre_sub))
                    if re.search("VARIABLE_", words_pre_sub) :
                        for key in sorted(p_sprite.variables, key=len, reverse=True):
                            # print("aaa key for subbing vars {}".format(key))
                            match_string = r'VARIABLE_' + key
                            match = re.search(match_string, words_pre_sub, re.X | re.M | re.S)
                            if match:
                                words_pre_sub = re.sub(match_string, str(p_sprite.variables[key]), words_pre_sub)
                            # words_pre_sub = re.sub(sub_this, str(p_sprite.variables[variable_name]), words_pre_sub)
                            words = words_pre_sub
                    else:
                        words = words_pre_sub
                p_sprite.say_history += str(words) + "\n"
                print("in do_sprite, sprite is saying this {}".format(p_sprite.say_history))
                break
            elif move == 'sensing_answer':
                return 'sensing_answer'
            elif move == 'sensing_askandwait':
                if 'sensing_answer' in p_sprite.variables:
                    try:
                        p_sprite.variables['current_answer'] = p_sprite.variables['sensing_answer'].pop(0)
                        print("ooo sensing answer.  current answer is this {}".
                              format(p_sprite.variables['current_answer']))
                    except IndexError:
                        p_sprite.variables['current_answer'] = 'Tried asking too many questions.  <br>' \
                                                               'Program expected you to ask questions, ' \
                                                               'but you asked too many.<br>.'
                else:
                    p_sprite.variables['current_answer'] = '<br>You asked a question in this script/custom block ' \
                                                           'but program does not a question to be here.<br>'
            elif move == 'join':
                string1 = moves[i+1]
                if isinstance(string1, list):
                    ret_val1 = do_sprite(p_sprite, string1, success)
                    string1 = ret_val1
                elif string1 == 'sensing_answer':
                    if 'current_answer' in p_sprite.variables:
                        string1 = p_sprite.variables['current_answer']
                    else:
                        string1 = ' Program is not expecting you to put in an answer to a question.' \
                                  'Do not ask a question here or use "answer".<br>' \
                                  '  If you are inside a custom block you ' \
                                  'should be using the input parameters'
                string2 = moves[i+2]
                if isinstance(string2, list):
                    ret_val2 = do_sprite(p_sprite, string2, success)
                    string2 = ret_val2
                elif string2 == 'sensing_answer':
                    string2 = p_sprite.variables['current_answer']

#                print("uuu join string1 {} string2 {}".format(string1, string2))
                if string1 is True:
                    string1 = 'string1 is True somehow.  Check your code.  Are you asking too many questions?'
                if string2 is True:
                    string2 = 'string2 is True somehow.  Check your code.  Are you asking too many questions?'
                return string1 + string2
            elif move == 'control_error':
                p_sprite.error += moves[i + 1]
                return False
            elif move == 'control_if_else':
                print("ooo found a control if_else moves{}  i{}".format(moves, i))
                operator = moves[i + 1]
                operator_result = do_sprite(p_sprite, operator, success)
                print("aaa in control_if_else, result of operator {} and type {} ".format(operator_result,
                                                                                   type(operator_result)))
                print("two sets of moves moves2 {} moves 3 {}".format(moves[2], moves[3]))

                if operator_result:
                    print("aaa operator_result is true")
                    ret_val = do_sprite(p_sprite, moves[2], success)
                else:
                    print("aaa operator_result is false aaa{}aaa".format(operator_result))

                    ret_val = do_sprite(p_sprite, moves[3], success)
                break
            elif move == 'control_if':
                print("ooo control_if moves{}  i{}".format(moves, i))
                operator = moves[i + 1]
                operator_result = do_sprite(p_sprite, operator, success)
                print("aaa in control_if, result of operator {} ".format(operator_result))
                if operator_result:
                    ret_val = do_sprite(p_sprite, moves[2], success)
                break
            elif move == 'control_repeat':
                if isinstance(moves[i+1], list):
                    times = do_sprite(p_sprite, moves[i+1], success)
                else:
                    times = int(moves[i + 1])
                if isinstance(times, float):
                    p_sprite.say_history += "Tried to do a repeat with a float number of times.  " \
                                            "Can only repeat integers."
                    success = False
                    break

                for _ in range(times):
                    ret_val = do_sprite(p_sprite, moves[2], success)
                    if ret_val is False:
                        success = False
                        break
                break
            elif move == 'control_repeat_until':
                operator = moves[i + 1]
                print("ffff in repeat until operator {}".format(operator))
                operator_result = do_sprite(p_sprite, operator, success)

                wu_counter = 1
                while operator_result is False:
                    print("repeat until move is this {}".format(moves[2]))
                    print("variables are this {}".format(p_sprite.variables))
                    # print("ppp what is say hist {}".format(p_sprite.say_history))

                    ret_val = do_sprite(p_sprite, moves[2], success)
                    print("finished a loop variables {}".format(p_sprite.variables))
                    # print("ppp what is say hist  {}".format(p_sprite.say_history))
                    operator_result = do_sprite(p_sprite, operator, success)
                    #true_false = eval_boolean(new_condition, p_sprite)
                    print("ppp wu counter {}".format(wu_counter))
                    wu_counter += 1
                    if wu_counter > 50:
                        break
                break
            elif re.search('VARIABLE_', move):
                return move
            elif move == '=':
                return move
            else:
                print("WARNING WARNING! this move did not get done {}".format(move))
    return success


def create_drawing(p_filename):
    """
    Runs the filename to create the debugging drawing
    :param p_filename: python filename to run (str)
    :return: none
    """
    import delegator
    cmd = 'python3 ' + p_filename
    print("CMD " + str(cmd))
    c = delegator.run(cmd)


def finalize_picture(p_basename, p_suffix, p_list, p_sprite):
    filename = '/tmp/' + p_basename + '-' + str(p_suffix) + '.py'
    print("FILANEM " + str(filename))
    fh = open(filename, 'w')
    initial_txt = init_turtle(p_list)
    fh.write(initial_txt)
    final_txt = draw_me(p_basename, p_sprite.move_history, p_suffix)
    fh.write(final_txt)
    fh.close()
    create_drawing(filename)


def expected_arrows(p_list):
    p_arrow_list = []
    for direction in p_list:
        x1 = direction[0][0]
        y1 = direction[0][1]
        x2 = direction[1][0]
        y2 = direction[1][1]
        dx = x2 - x1
        dy = y2 - y1
        p_arrow_list.append([x1, y1, dx, dy])
    return p_arrow_list


def actual_arrows(p_list):
    p_arrow_list = []
    pendown = True
    print("STARTING")
    print(p_list)
    for index, direction in enumerate(p_list):
        print("current dir " + str(direction))
        if direction == 'penup':
            pendown = False
            continue
        elif direction == 'pendown':
            pendown = True
            continue
        if pendown is False:
            continue
        next = index + 1
        try:
            print("next" + str(p_list[next]))
            if p_list[next] == 'penup' or p_list[next] == 'pendown':
                continue
            x1 = direction[0] + 1
            y1 = direction[1] + 1
            x2 = p_list[next][0] + 1
            y2 = p_list[next][1] + 1
            dx = x2 - x1
            dy = y2 - y1
            p_arrow_list.append([x1, y1, dx, dy])
        except IndexError:
            print('indexerror')
            return p_arrow_list
    return p_arrow_list


def get_static_dir():
    import sys
    import socket
    if sys.platform == 'darwin':
        static_dir = '/Users/dimmyfinster/PycharmProjects/CRLS_APCSP_autograder/app/static/'  # Eric's home computer
    else:
        if len(socket.gethostname()) > 25:
            static_dir = '/app/app/static/'  # assume heroku here
        else:
            static_dir = '/home/ewu/CRLS_APCSP_autograder/app/static/'
    return static_dir


def press_one(p_scripts, p_points):

    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use("Agg")
    import time
    from app.scratch_labs.scratch import find_string_in_script, one_event

    p_test = {"name": "Checking that there is a script that has 'when 1 key is pressed' and that this "
                      "script draws a single brick, assuming 0 is pressed first "
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Script that has 'when 1 key is pressed' draws a single brick"
                              " (assuming 0 is pressed first).<br>"
                              "Script also has a repeat with the correct number of times.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Script that has 'when 1 key is pressed does NOT draw a single brick"
                              " (assuming 0 is pressed first)<br>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br><br>",
              "points": 0
              }

    [test_press_one, script] = one_event(p_scripts,  "'event_whenkeypressed',\s'1'")
    if test_press_one['pass'] is False:
        p_test['fail_message'] += test_press_one['fail_message']
        return p_test
    test_22_1_1 = find_string_in_script(p_scripts, '22_1_1', 0)
    if test_22_1_1['pass'] is False:
        p_test['fail_message'] += test_22_1_1['fail_message']
        return p_test
    t_list = (
        ((-160, -180), (-120, -180)), ((-120, -180), (-120, -160)), ((-120, -160), (-160, -160)), ((-160, -160),
                                                                                                   (-160, -180))
    )
    target_dict = {}
    for target in t_list:
        if target not in target_dict.keys():
            target_dict[target] = 1
    sprite = brickLayer(-160, -180, 90, draw_targets=target_dict)
    success = do_sprite(sprite, script, True)
    if success is False or 1 in target_dict.values():
        # matplotlib.pyplot.ylabel('y')
        # matplotlib.pyplot.xlabel('x')
        # matplotlib.pyplot.title('Results of pressing one \n(green = expected, red = what your code draws)')
        # arrow_list = expected_arrows(t_list)
        # for arrow in arrow_list:
        #     matplotlib.pyplot.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=5,
        #                             head_width=5, color='green')
        # arrow_list = actual_arrows(sprite.move_history)
        # for arrow in arrow_list:
        #     matplotlib.pyplot.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=5,
        #                             head_width=5, color='red')
        # matplotlib.pyplot.xlim(-200, 200)
        # matplotlib.pyplot.ylim(-200, 200)
        # timestr = time.strftime("%Y%m%d-%H%M%S")
        # filename = 'press_one-' + str(timestr) + '.png'
        # static_dir = get_static_dir()
        # matplotlib.pyplot.savefig(static_dir + filename)
        # p_test['fail_message'] += 'You probably drew the brick in the wrong position.  Look at the image below... <br>' \
        #                           'your bricks should be where the green bricks are.   However, currently you are ' \
        #                           'drawing where the red bricks are: <br>'
        # p_test['download'] = '/static/' + filename
        plt.ylabel('y')
        plt.xlabel('x')
        plt.title('Results of pressing one \n(green = expected, red = what your code draws)')
        arrow_list = expected_arrows(t_list)
        for arrow in arrow_list:
            plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=5,
                                    head_width=5, color='green')
        arrow_list = actual_arrows(sprite.move_history)
        for arrow in arrow_list:
            plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=5,
                                    head_width=5, color='red')
        plt.xlim(-200, 200)
        plt.ylim(-200, 200)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = 'press_one-' + str(timestr) + '.png'
        static_dir = get_static_dir()
        plt.savefig(static_dir + filename)
        p_test['fail_message'] += 'You probably drew the brick in the wrong position.  Look at the image below... <br>' \
                                  'your bricks should be where the green bricks are.   However, currently you are ' \
                                  'drawing where the red bricks are: <br>'
        p_test['download'] = '/static/' + filename
    else:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def press_two(p_scripts, p_points):
    import time
    import matplotlib
    import matplotlib.pyplot as plt

    matplotlib.use("Agg")
    from app.scratch_labs.scratch import one_event, find_string_in_script

    p_test = {"name": "Checking that there is a script that has 'when 2 key is pressed' and that this "
                      "script draws a two bricks, assuming 0 is pressed first "
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Script that has 'when 2 key is pressed' draws two bricks"
                              " (assuming 0 is pressed first).<br>"
                              "Script also has a repeat with the correct number of times.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Script that has 'when 2 key is pressed does NOT draw two bricks"
                              " (assuming 0 is pressed first)<br>"
                              "<h5 style=\"color:purple;\">If this failed, you should be sure copy "
                              " your code from 'press 1' and add to it.</h5>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br><br>",
              "points": 0
              }
    [test_press_two, script] = one_event(p_scripts,  "'event_whenkeypressed',\s'2'")
    test_22_2_1 = find_string_in_script(p_scripts, '22_2_1', 0)
    if test_press_two['pass'] is False:
        p_test['fail_message'] += test_press_two['fail_message']
        return p_test
    if test_22_2_1['pass'] is False:
        p_test['fail_message'] += test_22_2_1['fail_message']
        return p_test
    test_22_2_3 = find_string_in_script(p_scripts, '22_2_3', 0)
    if test_22_2_3['pass'] is False:
        p_test['fail_message'] += test_22_2_3['fail_message']

    target_list = (
        ((-160, -180), (-120, -180)), ((-120, -180), (-120, -160)), ((-120, -160), (-160, -160)), ((-160, -160),
                                                                                                   (-160, -180)),
        ((-120, -180), (-80, -180)), ((-80, -180), (-80, -160)), ((-80, -160), (-120, -160)), ((-120, -160),
                                                                                               (-120, -180)))
    target_dict = {}
    for target in target_list:
        if target not in target_dict.keys():
            target_dict[target] = 1

    sprite = brickLayer(-160, -180, 90, draw_targets=target_dict)
    success = do_sprite(sprite, script, True)
    if success is False or 1 in sprite.draw_targets.values():
        plt.ylabel('y')
        plt.xlabel('x')
        plt.title('Results of pressing two \n(green = expected, red = what your code draws)')
        arrow_list = expected_arrows(target_list)
        for arrow in arrow_list:
            plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=5,
                                    head_width=5, color='green')
        arrow_list = actual_arrows(sprite.move_history)
        for arrow in arrow_list:
            plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=5,
                                    head_width=5, color='red')
        plt.xlim(-200, 200)
        plt.ylim(-200, 200)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = 'press_two-' + str(timestr) + '.png'
        static_dir = get_static_dir()
        plt.savefig(static_dir + filename)
        p_test['fail_message'] += 'You probably drew the brick in the wrong position.  Look at the image below... <br>' \
                                  'your bricks should be where the green bricks are.   However, currently you are ' \
                                  'drawing where the red bricks are: <br>'
        p_test['download'] = '/static/' + filename
    else:
        p_test['pass'] = True
        p_test['points'] += p_points

    if test_22_2_3['pass'] is False:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">Your picture drew the right shape, but not ' \
                                  'efficiently.  Be sure to check out this link. ' \
                                  '<a href="https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiF' \
                                  'MZ08NmBFro8LmljYbe6w/edit#slide=id.g88c5a09ee6_2_16">link</a></h5>'
    return p_test


def press_three(p_scripts, p_points):
    import time
    import matplotlib
    import matplotlib.pyplot as plt

    matplotlib.use("Agg")
    from app.scratch_labs.scratch import find_string_in_script, one_event

    p_test = {"name": "Checking that there is a script that has 'when 3 key is pressed' and that this "
                      "script draws 8 bricks, assuming 0 is pressed first "
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Script that has 'when 3 key is pressed' draws 8 bricks"
                              " (assuming 0 is pressed first).<br>"
                              "Script also has a repeat with the correct number of times.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Script that has 'when 3 key is pressed does NOT draw 8 bricks"
                              " (assuming 0 is pressed first)<br>"
                              "<h5 style=\"color:purple;\">If this failed, you should be sure copy "
                              " your code from 'press 1' and add to it.</h5>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br><br>",
              "points": 0
              }
    [test_press_three, script] = one_event(p_scripts,  "'event_whenkeypressed',\s'3'")
    if test_press_three['pass'] is False:
        p_test['fail_message'] += test_press_three['fail_message']
        return p_test
    test_22_3_1 = find_string_in_script(p_scripts, '22_3_1', 0)
    if test_22_3_1['pass'] is False:
        p_test['fail_message'] += test_22_3_1['fail_message']
        return p_test
    test_22_3_3 = find_string_in_script(p_scripts, '22_3_3', 0)
    if test_22_3_3['pass'] is False:
        p_test['fail_message'] += test_22_3_3['fail_message']
    target_list = (
        ((-160, -180), (-120, -180)), ((-120, -180), (-120, -160)), ((-120, -160), (-160, -160)), ((-160, -160),
                                                                                                   (-160, -180)),
        ((-120, -180), (-80, -180)), ((-80, -180), (-80, -160)), ((-80, -160), (-120, -160)), ((-120, -160),
                                                                                               (-120, -180)),
        ((-80, -180), (-40, -180)), ((-40, -180), (-40, -160)), ((-40, -160), (-80, -160)), ((-80, -160),
                                                                                             (-80, -180)),
        ((-40, -180), (0, -180)), ((0, -180), (0, -160)), ((0, -160), (-40, -160)), ((-40, -160),
                                                                                     (-40, -180)),
        ((0, -180), (40, -180)), ((40, -180), (40, -160)), ((40, -160), (0, -160)), ((0, -160), (0, -180)),
        ((40, -180), (80, -180)), ((80, -180), (80, -160)), ((80, -160), (40, -160)), ((40, -160), (40, -180)),
        ((80, -180), (120, -180)), ((120, -180), (120, -160)), ((120, -160), (80, -160)), ((80, -160), (80, -180)),
        ((120, -180), (160, -180)), ((160, -180), (160, -160)), ((160, -160), (120, -160)), ((120, -160), (120, -180)))
    target_dict = {}
    for target in target_list:
        if target not in target_dict.keys():
            target_dict[target] = 1
    sprite = brickLayer(-160, -180, 90, draw_targets=target_dict)
    success = do_sprite(sprite, script, True)
    if success is False or 1 in sprite.draw_targets.values():
        plt.ylabel('y')
        plt.xlabel('x')
        plt.title('Results of pressing three \n(green = expected, red = what your code draws)')
        arrow_list = expected_arrows(target_list)
        for arrow in arrow_list:
            plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=5,
                                    head_width=5, color='green')
        arrow_list = actual_arrows(sprite.move_history)
        for arrow in arrow_list:
            plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=5,
                                    head_width=5, color='red')
        plt.xlim(-200, 200)
        plt.ylim(-200, 200)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = 'press_three-' + str(timestr) + '.png'
        static_dir = get_static_dir()
        plt.savefig(static_dir + filename)
        p_test['fail_message'] += 'You probably drew the brick in the wrong position.  Look at the image below... <br>' \
                                  'your bricks should be where the green bricks are.   However, currently you are ' \
                                  'drawing where the red bricks are: <br>'
        p_test['download'] = '/static/' + filename
    else:
        p_test['pass'] = True
        p_test['points'] += p_points

    if success and 1 not in sprite.draw_targets.values() and test_22_3_3['pass'] is False:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">Your picture drew the right shape, but not ' \
                                  'efficiently.  Be sure to check out this link. ' \
                                  '<a href="https://docs.google.com/presentation/d/1HnORWjzEZq8k7bGGRU49GiF' \
                                  'MZ08NmBFro8LmljYbe6w/edit#slide=id.g88c5a09ee6_2_16">link</a></h5>'
    return p_test


def press_four(p_scripts, p_points):
    import time
    import matplotlib
    import matplotlib.pyplot as plt

    matplotlib.use("Agg")
    from app.scratch_labs.scratch import find_string_in_script, one_event

    p_test = {"name": "Checking that there is a script that has 'when 4 key is pressed' and that this "
                      "script draws an entire brick road, assuming 0 is pressed first "
                      "(" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "Script that has 'when 4 key is pressed' draws a road of bricks"
                              " (assuming 0 is pressed first).<br>"
                              "Script also has a repeat with the correct number of times.<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Script that has 'when 4 key is pressed does NOT draw an entire road of bricks"
                              " (assuming 0 is pressed first)<br>"
                              "Checker assumes you pressed 0 first, so you start in bottom left corner.<br><br>",
              "points": 0
              }
    [test_press_four, script] = one_event(p_scripts, "'event_whenkeypressed',\s'4'")
    if test_press_four['pass'] is False:
        p_test['fail_message'] += test_press_four['fail_message']
        return p_test
    t_list = (((-160, -180), (-120, -180)), ((-120, -180), (-120, -160)), ((-120, -160), (-160, -160)),
              ((-160, -160), (-160, -180)), ((-120, -180), (-80, -180)), ((-80, -180), (-80, -160)),
              ((-80, -160), (-120, -160)), ((-120, -160), (-120, -180)), ((-80, -180), (-40, -180)),
              ((-40, -180), (-40, -160)), ((-40, -160), (-80, -160)), ((-80, -160), (-80, -180)),
              ((-40, -180), (0, -180)), ((0, -180), (0, -160)), ((0, -160), (-40, -160)),
              ((-40, -160), (-40, -180)), ((0, -180), (40, -180)), ((40, -180), (40, -160)),
              ((40, -160), (0, -160)), ((0, -160), (0, -180)), ((40, -180), (80, -180)),
              ((80, -180), (80, -160)), ((80, -160), (40, -160)), ((40, -160), (40, -180)),
              ((80, -180), (120, -180)), ((120, -180), (120, -160)), ((120, -160), (80, -160)),
              ((80, -160), (80, -180)), ((120, -180), (160, -180)), ((160, -180), (160, -160)),
              ((160, -160), (120, -160)), ((120, -160), (120, -180)), ((-140, -160), (-100, -160)),
              ((-100, -160), (-100, -140)), ((-100, -140), (-140, -140)), ((-140, -140), (-140, -160)),
              ((-100, -160), (-60, -160)), ((-60, -160), (-60, -140)), ((-60, -140), (-100, -140)),
              ((-100, -140), (-100, -160)), ((-60, -160), (-20, -160)), ((-20, -160), (-20, -140)),
              ((-20, -140), (-60, -140)), ((-60, -140), (-60, -160)), ((-20, -160), (20, -160)),
              ((20, -160), (20, -140)), ((20, -140), (-20, -140)), ((-20, -140), (-20, -160)),
              ((20, -160), (60, -160)), ((60, -160), (60, -140)), ((60, -140), (20, -140)),
              ((20, -140), (20, -160)), ((60, -160), (100, -160)), ((100, -160), (100, -140)),
              ((100, -140), (60, -140)), ((60, -140), (60, -160)), ((100, -160), (140, -160)),
              ((140, -160), (140, -140)), ((140, -140), (100, -140)), ((100, -140), (100, -160)),
              ((140, -160), (180, -160)), ((180, -160), (180, -140)), ((180, -140), (140, -140)),
              ((140, -140), (140, -160)), ((-160, -140), (-120, -140)), ((-120, -140), (-120, -120)),
              ((-120, -120), (-160, -120)), ((-160, -120), (-160, -140)), ((-120, -140), (-80, -140)),
              ((-80, -140), (-80, -120)), ((-80, -120), (-120, -120)), ((-120, -120), (-120, -140)),
              ((-80, -140), (-40, -140)), ((-40, -140), (-40, -120)), ((-40, -120), (-80, -120)),
              ((-80, -120), (-80, -140)), ((-40, -140), (0, -140)), ((0, -140), (0, -120)),
              ((0, -120), (-40, -120)), ((-40, -120), (-40, -140)), ((0, -140), (40, -140)),
              ((40, -140), (40, -120)), ((40, -120), (0, -120)), ((0, -120), (0, -140)),
              ((40, -140), (80, -140)), ((80, -140), (80, -120)), ((80, -120), (40, -120)),
              ((40, -120), (40, -140)), ((80, -140), (120, -140)), ((120, -140), (120, -120)),
              ((120, -120), (80, -120)), ((80, -120), (80, -140)), ((120, -140), (160, -140)),
              ((160, -140), (160, -120)), ((160, -120), (120, -120)), ((120, -120), (120, -140)),
              ((-140, -120), (-100, -120)), ((-100, -120), (-100, -100)), ((-100, -100), (-140, -100)),
              ((-140, -100), (-140, -120)), ((-100, -120), (-60, -120)), ((-60, -120), (-60, -100)),
              ((-60, -100), (-100, -100)), ((-100, -100), (-100, -120)), ((-60, -120), (-20, -120)),
              ((-20, -120), (-20, -100)), ((-20, -100), (-60, -100)), ((-60, -100), (-60, -120)),
              ((-20, -120), (20, -120)), ((20, -120), (20, -100)), ((20, -100), (-20, -100)),
              ((-20, -100), (-20, -120)), ((20, -120), (60, -120)), ((60, -120), (60, -100)),
              ((60, -100), (20, -100)), ((20, -100), (20, -120)), ((60, -120), (100, -120)),
              ((100, -120), (100, -100)), ((100, -100), (60, -100)), ((60, -100), (60, -120)),
              ((100, -120), (140, -120)), ((140, -120), (140, -100)), ((140, -100), (100, -100)),
              ((100, -100), (100, -120)), ((140, -120), (180, -120)), ((180, -120), (180, -100)),
              ((180, -100), (140, -100)), ((140, -100), (140, -120)), ((-160, -100), (-120, -100)),
              ((-120, -100), (-120, -80)), ((-120, -80), (-160, -80)), ((-160, -80), (-160, -100)),
              ((-120, -100), (-80, -100)), ((-80, -100), (-80, -80)), ((-80, -80), (-120, -80)),
              ((-120, -80), (-120, -100)), ((-80, -100), (-40, -100)), ((-40, -100), (-40, -80)),
              ((-40, -80), (-80, -80)), ((-80, -80), (-80, -100)), ((-40, -100), (0, -100)),
              ((0, -100), (0, -80)), ((0, -80), (-40, -80)), ((-40, -80), (-40, -100)),
              ((0, -100), (40, -100)), ((40, -100), (40, -80)), ((40, -80), (0, -80)), ((0, -80), (0, -100)),
              ((40, -100), (80, -100)), ((80, -100), (80, -80)), ((80, -80), (40, -80)), ((40, -80), (40, -100)),
              ((80, -100), (120, -100)), ((120, -100), (120, -80)), ((120, -80), (80, -80)), ((80, -80), (80, -100)),
              ((120, -100), (160, -100)), ((160, -100), (160, -80)), ((160, -80), (120, -80)),
              ((120, -80), (120, -100)), ((-140, -80), (-100, -80)), ((-100, -80), (-100, -60)),
              ((-100, -60), (-140, -60)), ((-140, -60), (-140, -80)), ((-100, -80), (-60, -80)),
              ((-60, -80), (-60, -60)), ((-60, -60), (-100, -60)), ((-100, -60), (-100, -80)),
              ((-60, -80), (-20, -80)), ((-20, -80), (-20, -60)), ((-20, -60), (-60, -60)), ((-60, -60), (-60, -80)),
              ((-20, -80), (20, -80)), ((20, -80), (20, -60)), ((20, -60), (-20, -60)), ((-20, -60), (-20, -80)),
              ((20, -80), (60, -80)), ((60, -80), (60, -60)), ((60, -60), (20, -60)), ((20, -60), (20, -80)),
              ((60, -80), (100, -80)), ((100, -80), (100, -60)), ((100, -60), (60, -60)), ((60, -60), (60, -80)),
              ((100, -80), (140, -80)), ((140, -80), (140, -60)), ((140, -60), (100, -60)), ((100, -60), (100, -80)),
              ((140, -80), (180, -80)), ((180, -80), (180, -60)), ((180, -60), (140, -60)), ((140, -60), (140, -80)),
              ((-160, -60), (-120, -60)), ((-120, -60), (-120, -40)), ((-120, -40), (-160, -40)),
              ((-160, -40), (-160, -60)), ((-120, -60), (-80, -60)), ((-80, -60), (-80, -40)),
              ((-80, -40), (-120, -40)), ((-120, -40), (-120, -60)), ((-80, -60), (-40, -60)),
              ((-40, -60), (-40, -40)), ((-40, -40), (-80, -40)), ((-80, -40), (-80, -60)),
              ((-40, -60), (0, -60)), ((0, -60), (0, -40)), ((0, -40), (-40, -40)), ((-40, -40), (-40, -60)),
              ((0, -60), (40, -60)), ((40, -60), (40, -40)), ((40, -40), (0, -40)), ((0, -40), (0, -60)),
              ((40, -60), (80, -60)), ((80, -60), (80, -40)), ((80, -40), (40, -40)), ((40, -40), (40, -60)),
              ((80, -60), (120, -60)), ((120, -60), (120, -40)), ((120, -40), (80, -40)), ((80, -40), (80, -60)),
              ((120, -60), (160, -60)), ((160, -60), (160, -40)), ((160, -40), (120, -40)), ((120, -40), (120, -60)),
              ((-140, -40), (-100, -40)), ((-100, -40), (-100, -20)), ((-100, -20), (-140, -20)),
              ((-140, -20), (-140, -40)), ((-100, -40), (-60, -40)), ((-60, -40), (-60, -20)),
              ((-60, -20), (-100, -20)), ((-100, -20), (-100, -40)), ((-60, -40), (-20, -40)),
              ((-20, -40), (-20, -20)), ((-20, -20), (-60, -20)), ((-60, -20), (-60, -40)),
              ((-20, -40), (20, -40)), ((20, -40), (20, -20)), ((20, -20), (-20, -20)), ((-20, -20), (-20, -40)),
              ((20, -40), (60, -40)), ((60, -40), (60, -20)), ((60, -20), (20, -20)),
              ((20, -20), (20, -40)), ((60, -40), (100, -40)), ((100, -40), (100, -20)),
              ((100, -20), (60, -20)), ((60, -20), (60, -40)), ((100, -40), (140, -40)),
              ((140, -40), (140, -20)), ((140, -20), (100, -20)), ((100, -20), (100, -40)),
              ((140, -40), (180, -40)), ((180, -40), (180, -20)), ((180, -20), (140, -20)),
              ((140, -20), (140, -40)), ((-160, -20), (-120, -20)), ((-120, -20), (-120, 0)),
              ((-120, 0), (-160, 0)), ((-160, 0), (-160, -20)), ((-120, -20), (-80, -20)),
              ((-80, -20), (-80, 0)), ((-80, 0), (-120, 0)), ((-120, 0), (-120, -20)),
              ((-80, -20), (-40, -20)), ((-40, -20), (-40, 0)), ((-40, 0), (-80, 0)),
              ((-80, 0), (-80, -20)), ((-40, -20), (0, -20)), ((0, -20), (0, 0)), ((0, 0), (-40, 0)),
              ((-40, 0), (-40, -20)), ((0, -20), (40, -20)), ((40, -20), (40, 0)), ((40, 0), (0, 0)),
              ((0, 0), (0, -20)), ((40, -20), (80, -20)), ((80, -20), (80, 0)), ((80, 0), (40, 0)),
              ((40, 0), (40, -20)), ((80, -20), (120, -20)), ((120, -20), (120, 0)), ((120, 0), (80, 0)),
              ((80, 0), (80, -20)), ((120, -20), (160, -20)), ((160, -20), (160, 0)), ((160, 0), (120, 0)),
              ((120, 0), (120, -20)), ((-140, 0), (-100, 0)), ((-100, 0), (-100, 20)), ((-100, 20), (-140, 20)),
              ((-140, 20), (-140, 0)), ((-100, 0), (-60, 0)), ((-60, 0), (-60, 20)), ((-60, 20), (-100, 20)),
              ((-100, 20), (-100, 0)), ((-60, 0), (-20, 0)), ((-20, 0), (-20, 20)), ((-20, 20), (-60, 20)),
              ((-60, 20), (-60, 0)), ((-20, 0), (20, 0)), ((20, 0), (20, 20)), ((20, 20), (-20, 20)),
              ((-20, 20), (-20, 0)), ((20, 0), (60, 0)), ((60, 0), (60, 20)), ((60, 20), (20, 20)),
              ((20, 20), (20, 0)), ((60, 0), (100, 0)), ((100, 0), (100, 20)), ((100, 20), (60, 20)),
              ((60, 20), (60, 0)), ((100, 0), (140, 0)), ((140, 0), (140, 20)), ((140, 20), (100, 20)),
              ((100, 20), (100, 0)), ((140, 0), (180, 0)), ((180, 0), (180, 20)), ((180, 20), (140, 20)),
              ((140, 20), (140, 0)), ((-160, 20), (-120, 20)), ((-120, 20), (-120, 40)), ((-120, 40), (-160, 40)),
              ((-160, 40), (-160, 20)), ((-120, 20), (-80, 20)), ((-80, 20), (-80, 40)), ((-80, 40), (-120, 40)),
              ((-120, 40), (-120, 20)), ((-80, 20), (-40, 20)), ((-40, 20), (-40, 40)), ((-40, 40), (-80, 40)),
              ((-80, 40), (-80, 20)), ((-40, 20), (0, 20)), ((0, 20), (0, 40)), ((0, 40), (-40, 40)),
              ((-40, 40), (-40, 20)), ((0, 20), (40, 20)), ((40, 20), (40, 40)), ((40, 40), (0, 40)),
              ((0, 40), (0, 20)), ((40, 20), (80, 20)), ((80, 20), (80, 40)), ((80, 40), (40, 40)),
              ((40, 40), (40, 20)), ((80, 20), (120, 20)), ((120, 20), (120, 40)), ((120, 40), (80, 40)),
              ((80, 40), (80, 20)), ((120, 20), (160, 20)), ((160, 20), (160, 40)), ((160, 40), (120, 40)),
              ((120, 40), (120, 20)), ((-140, 40), (-100, 40)), ((-100, 40), (-100, 60)), ((-100, 60), (-140, 60)),
              ((-140, 60), (-140, 40)), ((-100, 40), (-60, 40)), ((-60, 40), (-60, 60)), ((-60, 60), (-100, 60)),
              ((-100, 60), (-100, 40)), ((-60, 40), (-20, 40)), ((-20, 40), (-20, 60)), ((-20, 60), (-60, 60)),
              ((-60, 60), (-60, 40)), ((-20, 40), (20, 40)), ((20, 40), (20, 60)), ((20, 60), (-20, 60)),
              ((-20, 60), (-20, 40)), ((20, 40), (60, 40)), ((60, 40), (60, 60)), ((60, 60), (20, 60)),
              ((20, 60), (20, 40)), ((60, 40), (100, 40)), ((100, 40), (100, 60)), ((100, 60), (60, 60)),
              ((60, 60), (60, 40)), ((100, 40), (140, 40)), ((140, 40), (140, 60)), ((140, 60), (100, 60)),
              ((100, 60), (100, 40)), ((140, 40), (180, 40)), ((180, 40), (180, 60)), ((180, 60), (140, 60)),
              ((140, 60), (140, 40)), ((-160, 60), (-120, 60)), ((-120, 60), (-120, 80)), ((-120, 80), (-160, 80)),
              ((-160, 80), (-160, 60)), ((-120, 60), (-80, 60)), ((-80, 60), (-80, 80)), ((-80, 80), (-120, 80)),
              ((-120, 80), (-120, 60)), ((-80, 60), (-40, 60)), ((-40, 60), (-40, 80)), ((-40, 80), (-80, 80)),
              ((-80, 80), (-80, 60)), ((-40, 60), (0, 60)), ((0, 60), (0, 80)), ((0, 80), (-40, 80)),
              ((-40, 80), (-40, 60)), ((0, 60), (40, 60)), ((40, 60), (40, 80)), ((40, 80), (0, 80)),
              ((0, 80), (0, 60)), ((40, 60), (80, 60)), ((80, 60), (80, 80)), ((80, 80), (40, 80)),
              ((40, 80), (40, 60)), ((80, 60), (120, 60)), ((120, 60), (120, 80)), ((120, 80), (80, 80)),
              ((80, 80), (80, 60)), ((120, 60), (160, 60)), ((160, 60), (160, 80)), ((160, 80), (120, 80)),
              ((120, 80), (120, 60)), ((-140, 80), (-100, 80)), ((-100, 80), (-100, 100)), ((-100, 100), (-140, 100)),
              ((-140, 100), (-140, 80)), ((-100, 80), (-60, 80)), ((-60, 80), (-60, 100)), ((-60, 100), (-100, 100)),
              ((-100, 100), (-100, 80)), ((-60, 80), (-20, 80)), ((-20, 80), (-20, 100)), ((-20, 100), (-60, 100)),
              ((-60, 100), (-60, 80)), ((-20, 80), (20, 80)), ((20, 80), (20, 100)), ((20, 100), (-20, 100)),
              ((-20, 100), (-20, 80)), ((20, 80), (60, 80)), ((60, 80), (60, 100)), ((60, 100), (20, 100)),
              ((20, 100), (20, 80)), ((60, 80), (100, 80)), ((100, 80), (100, 100)), ((100, 100), (60, 100)),
              ((60, 100), (60, 80)), ((100, 80), (140, 80)), ((140, 80), (140, 100)), ((140, 100), (100, 100)),
              ((100, 100), (100, 80)), ((140, 80), (180, 80)), ((180, 80), (180, 100)), ((180, 100), (140, 100)),
              ((140, 100), (140, 80)), ((-160, 100), (-120, 100)), ((-120, 100), (-120, 120)),
              ((-120, 120), (-160, 120)), ((-160, 120), (-160, 100)), ((-120, 100), (-80, 100)),
              ((-80, 100), (-80, 120)), ((-80, 120), (-120, 120)), ((-120, 120), (-120, 100)),
              ((-80, 100), (-40, 100)), ((-40, 100), (-40, 120)), ((-40, 120), (-80, 120)),
              ((-80, 120), (-80, 100)), ((-40, 100), (0, 100)), ((0, 100), (0, 120)),
              ((0, 120), (-40, 120)), ((-40, 120), (-40, 100)), ((0, 100), (40, 100)), ((40, 100), (40, 120)),
              ((40, 120), (0, 120)), ((0, 120), (0, 100)), ((40, 100), (80, 100)), ((80, 100), (80, 120)),
              ((80, 120), (40, 120)), ((40, 120), (40, 100)), ((80, 100), (120, 100)), ((120, 100), (120, 120)),
              ((120, 120), (80, 120)), ((80, 120), (80, 100)), ((120, 100), (160, 100)), ((160, 100), (160, 120)),
              ((160, 120), (120, 120)), ((120, 120), (120, 100)), ((-140, 120), (-100, 120)),
              ((-100, 120), (-100, 140)), ((-100, 140), (-140, 140)), ((-140, 140), (-140, 120)),
              ((-100, 120), (-60, 120)), ((-60, 120), (-60, 140)), ((-60, 140), (-100, 140)),
              ((-100, 140), (-100, 120)), ((-60, 120), (-20, 120)), ((-20, 120), (-20, 140)),
              ((-20, 140), (-60, 140)), ((-60, 140), (-60, 120)), ((-20, 120), (20, 120)), ((20, 120), (20, 140)),
              ((20, 140), (-20, 140)), ((-20, 140), (-20, 120)), ((20, 120), (60, 120)), ((60, 120), (60, 140)),
              ((60, 140), (20, 140)), ((20, 140), (20, 120)), ((60, 120), (100, 120)), ((100, 120), (100, 140)),
              ((100, 140), (60, 140)), ((60, 140), (60, 120)), ((100, 120), (140, 120)), ((140, 120), (140, 140)),
              ((140, 140), (100, 140)), ((100, 140), (100, 120)), ((140, 120), (180, 120)), ((180, 120), (180, 140)),
              ((180, 140), (140, 140)), ((140, 140), (140, 120)), ((-160, 140), (-120, 140)),
              ((-120, 140), (-120, 160)), ((-120, 160), (-160, 160)), ((-160, 160), (-160, 140)),
              ((-120, 140), (-80, 140)), ((-80, 140), (-80, 160)), ((-80, 160), (-120, 160)),
              ((-120, 160), (-120, 140)), ((-80, 140), (-40, 140)), ((-40, 140), (-40, 160)),
              ((-40, 160), (-80, 160)), ((-80, 160), (-80, 140)), ((-40, 140), (0, 140)),
              ((0, 140), (0, 160)), ((0, 160), (-40, 160)), ((-40, 160), (-40, 140)), ((0, 140), (40, 140)),
              ((40, 140), (40, 160)), ((40, 160), (0, 160)), ((0, 160), (0, 140)), ((40, 140), (80, 140)),
              ((80, 140), (80, 160)), ((80, 160), (40, 160)), ((40, 160), (40, 140)), ((80, 140), (120, 140)),
              ((120, 140), (120, 160)), ((120, 160), (80, 160)), ((80, 160), (80, 140)), ((120, 140), (160, 140)),
              ((160, 140), (160, 160)), ((160, 160), (120, 160)), ((120, 160), (120, 140)), ((-140, 160), (-100, 160)),
              ((-100, 160), (-100, 180)), ((-100, 180), (-140, 180)), ((-140, 180), (-140, 160)),
              ((-100, 160), (-60, 160)), ((-60, 160), (-60, 180)), ((-60, 180), (-100, 180)),
              ((-100, 180), (-100, 160)), ((-60, 160), (-20, 160)), ((-20, 160), (-20, 180)),
              ((-20, 180), (-60, 180)), ((-60, 180), (-60, 160)), ((-20, 160), (20, 160)), ((20, 160), (20, 180)),
              ((20, 180), (-20, 180)), ((-20, 180), (-20, 160)), ((20, 160), (60, 160)), ((60, 160), (60, 180)),
              ((60, 180), (20, 180)), ((20, 180), (20, 160)), ((60, 160), (100, 160)), ((100, 160), (100, 180)),
              ((100, 180), (60, 180)), ((60, 180), (60, 160)), ((100, 160), (140, 160)), ((140, 160), (140, 180)),
              ((140, 180), (100, 180)), ((100, 180), (100, 160)), ((140, 160), (180, 160)), ((180, 160), (180, 180)),
              ((180, 180), (140, 180)), ((140, 180), (140, 160)))
    target_dict = {}
    for target in t_list:
        if target not in target_dict.keys():
            target_dict[target] = 1
    sprite = brickLayer(-160, -180, 90, draw_targets=target_dict)
    success = do_sprite(sprite, script, True)
    if success is False or 1 in sprite.draw_targets.values():
        plt.ylabel('y')
        plt.xlabel('x')
        plt.title('Results of pressing four \n(green = expected, red = what your code draws)')
        arrow_list = expected_arrows(t_list)
        for arrow in arrow_list:
            plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=3,
                                    head_width=3, color='green')
        arrow_list = actual_arrows(sprite.move_history)
        print("All arrows" + str(arrow_list))
        for arrow in arrow_list:
            print("arrow " + str(arrow))
            plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], length_includes_head=True, head_length=3,
                                    head_width=3, color='red')
        plt.xlim(-200, 200)
        plt.ylim(-200, 200)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = 'press_four-' + str(timestr) + '.png'
        static_dir = get_static_dir()
        plt.savefig(static_dir + filename)
        p_test['fail_message'] += 'You probably drew the brick in the wrong position.  Look at the image below... <br>' \
                                  'your bricks should be where the green bricks are.   However, currently you are ' \
                                  'drawing where the red bricks are: <br>'
        p_test['download'] = '/static/' + filename
    else:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test

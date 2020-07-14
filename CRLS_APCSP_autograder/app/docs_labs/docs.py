def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement.
    swiped directly from https://developers.google.com/docs/api/samples/extract-text?refresh=1
    then modified slightly for our needs
        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = element.get('textRun')
    inlineobject = element.get('inlineObjectElement')
    if inlineobject:
        return "AAA INLINEOBJECT"
    if not text_run:
        return ' '
    return text_run.get('content')


def read_strucutural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.
       swiped directly from https://developers.google.com/docs/api/samples/extract-text?refresh=1
       then modified slightly for our needs
        Args:
            elements: a list of Structural Elements.
    """
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)

        elif 'table' in value:
            # The text in table cells are in nested Structural Elements and tables may be
            # nested.
            # text += 'start_answer\n'
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += "start_answer \n tabledata " + read_strucutural_elements(cell.get('content'))
#                     text += read_strucutural_elements(cell.get('content'))
                    text += 'end_answer\n'

        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_strucutural_elements(toc.get('content'))
    return text


def get_google_drive_id(p_link):
    """
    Took this from CRLS_google_classroom_autopopulator.  Should just link it through git but maybe later
    :param p_link: link to the file
    :return:
    """
    import re

    print("aaa p_link {}".format(p_link))
    # Figure out which format it is
    classroom = re.search(r'classroom', p_link)
    if classroom:
        return 'classroom'
    format1 = re.search(r'\?id=', p_link)
    format2 = re.search(r'/d/', p_link)

    # Extract google_id from the link
    google_id = ''
    if format1:
        google_id = re.sub(r'^.+\?id=', '', p_link)
    if format2:
        google_id = re.sub(r'.+/d/', '', p_link)
        google_id = re.sub(r'/.+$', '', google_id)

    print("aaa g_id {}".format(google_id))

    return google_id


def get_text(document_id):
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    Swiped directly from https://developers.google.com/docs/api/samples/extract-text?refresh=1
    then modified slightly for our needs
    """
    import pickle
    import os.path
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

    # https://docs.google.com/document/d/1LZfjuWRdWNRA0vysLC1J8LYnp49cL5UWk2rGrd34lPc/edit#heading=h.gg00kbxzvzqj

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service_document = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service_document.documents().get(documentId=document_id).execute()

    #print('The title of the document is: {}'.format(document.get('title')))

    doc = service_document.documents().get(documentId=document_id).execute()
    doc_content = doc.get('body').get('content')

    p_doctext = read_strucutural_elements(doc_content)
    return p_doctext


def get_question_string(question, fulltext):
    import re

    fulltext = fulltext.lower()
    match = str(question) + '. .*? start_answer (.*?) end_answer'
    question_text_obj = re.search(match, fulltext, re.X | re.M | re.S)
    if question_text_obj:
        return_val = re.sub('tabledata', '', question_text_obj.group(1))
        return_val = re.sub('\A\s*', '', return_val)
        return return_val

    else:
        return ''


def run_question_string(p_string):
    import delegator
    import time

    timestr = time.strftime("%Y%m%d-%H%M%S")
    p_filename = '/tmp/question_string' + str(timestr) + '.py'
    fh = open(p_filename, 'w')
    fh.write(p_string)
    fh.close()
    cmd = 'python3 ' + p_filename
    c = delegator.run(cmd)
    if c.err:
        return c.err
    elif c.out:
        return c.out
    else:
        return 'Running ' + cmd + ' did not return an input or an output'


def return_answer_run(question, fulltext):
    question_string = get_question_string(question, fulltext)
    answer_run = run_question_string(question_string)
    return question + '. ' + ' start_answer' + str(answer_run) + ' end_answer'


def check_answer(question, label, fulltext, query, *, points=0):
    """

    :param question: question number e.g. 3a (str)
    :param label: how to label the queston e.g. 'what is a BIOS' (str)
    :param fulltext: Full text of the google doc (from get_text)
    :param query: dictionary of questions I'm looking for (dict)
    :param min_matches: if given answers in list, the minimum number of matches needed to score
    :param points: number of points this is worth (int)
    :return: a test dictionary
    """
    import re

    # min_words
    # screenshot
    # answers
    # min_answers
    # help_link

    p_test = {"name": "Checking that " + str(question) + ". " + str(label) + " is correct (" + str(points) +
                      " points)<br>",
              "pass": True,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  " + str(question) + ". " +
                              str(label) + " appears correct!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> " + str(label) + " does not appear correct.<br>",
              "points": 0,
              "match": '',
              }
    fulltext = fulltext.lower()
    fulltext = re.sub('tabledata', '', fulltext)
    match = str(question) + '\. .*? start_answer (.*?) end_answer'
    question_text_obj = re.search(match, fulltext, re.X | re. M | re.S)
    question_text = ''
    if question_text_obj:
        question_text = question_text_obj.group(1)
        p_test['match'] = question_text
    else:
        p_test['fail_message'] += '<h5 style=\"color:purple;\">Did not find match for text.  Either autograder ' \
                                  'is broken or question is blank. Or you deleted the box the answer goes in.</h5>'
        p_test['pass'] = False
    print("MATCH " + str(match))
    print("QUESTION TEXT " + str(question_text))

    if 'min_words' not in query.keys() and 'screenshot' not in query.keys() and 'answers' not in query.keys():
        p_test['fail_message'] += "<h5 style=\"color:purple;\">Autograder programming bug for this question</h5>  " + \
                                  str(label) + " There are no tests for min words, screenshot, or answers."
        return p_test


    if 'min_words' in query.keys() and question_text:
        if query['min_words']:
            min_words = query['min_words']
            if isinstance(query['min_words'], int) is False:
                p_test['fail_message'] += "<h5 style=\"color:purple;\">Autograder programming bug for this question" \
                                          "</h5>  " + str(label) + " min_words needs to be an integer"
            else:
                result = re.findall(r'[a-zA-Z0-9]+ [\s+ | \. | : | \? | ! | \n]',
                                    str(question_text), re.X | re.M | re.S)
                words = len(result)
                print("result" + str(result))
                print("question texxt" + str(question_text))
                print("words" + str(words))
                if words < min_words:
                    p_test['fail_message'] += "<h5 style=\"color:purple;\"> Failed minimum word count test.<br>" \
                                              "Found this many words: " + str(words) + \
                                              "<br> Require this many words: " + str(min_words) + "<br>"
                    p_test['pass'] = False

                else:
                    p_test['pass_message'] += "Found: Minimum number of words required (" + str(min_words) +\
                                              ").<br>Your answer had this many words (" + str(words) + \
                                              ").<br>  Correctness of your answer will be checked later manually."
                    p_test['points'] += points
    if 'screenshot' in query.keys() and question_text:
        print("Looking screenshot!")
        if query['screenshot']:
            result = re.search('aaa \s inlineobject', str(question_text), re.X | re.M | re.S)
            print(question_text)
            if result:
                p_test['points'] += points
            else:
                p_test['pass'] = False
    passed = 0
    if 'answers' in query.keys() and question_text:
        if isinstance(query['answers'], str):
            print("yes")
            answer = query['answers']
            print(answer)
            print(question_text)
            result = re.search(answer, str(question_text), re.X | re.M | re.S)
            if result:
                p_test['points'] += points
            else:
                p_test['pass'] = False
        elif isinstance(query['answers'], list):
            if 'min_matches' in query.keys():
                expected = query['min_matches']
            else:
                expected = 1
            for item in query['answers']:
                result = re.search(str(item), str(question_text), re.X | re.M | re.S)
                p_test['pass'] = False
                if result:
                    passed += 1

                    item = re.sub('<', '&lt;', item)
                    item = re.sub('>', '&gt;', item)
                    p_test['fail_message'] += "Matched this regex expression in the answer " + str(item) + "<br>"
                    p_test['pass_message'] += "Matched this regex expression in the answer " + str(item) + "<br>"
            if passed >= expected:
                p_test['points'] += points
                p_test['pass'] = True
            else:
                p_test['fail_message'] += "<h5 style=\"color:purple;\"><br>"\
                                          "Needed this many matches: " + str(expected) + \
                                          "<br>Found this many matches: " +  str(passed) + "<br></h5>"
    # question_text = re.sub('\n', '<br>', question_text)
    question_text = re.sub('<', '&lt;', question_text)
    question_text = re.sub('>', '&gt;', question_text)
    p_test['fail_message'] += 'Your answer was this:<br>' + str(question_text)  + "<br>"

    print("WTF " + question_text)
    print("WTF 2 " + str(question_text))
    if 'help_link' in query.keys():
        p_test['fail_message'] += 'See this link for help answering this question: <a href="' +\
                                  query['help_link'] + '" target="_blank">link</a>'

    return p_test


def exact_answer(p_label, p_answers, p_text, *, points=0, required=1):
    """
    checks that the answer is exactly correct.
    :param p_label: the label of the problem (i.e. 3a, 3b.) (str)
    :param p_answers: The text you are searching for REGEX.  LIST, in case multiple correct answers. (list)
    :param p_text: The text you are searching (str)
    :param points: how many this is worth
    :param required: how many of the answers in list you are required to have
    :return: test dictionary
    """
    import re
    p_test = {"name": "Checking that " + str(p_label) + " is exactly correct (" + str(points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  " +
                              str(p_label) + " appears correct!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> " +
                              str(p_label) + " does not appear correct.  Try again.<br>"
                                             "Answers must be spelled correctly (no typos), "
                                             "but capitalization does not matter.<br>",
              "points": 0,
              }
    passed = 0
    for answer in p_answers:
        answer = answer.lower()
        p_text = p_text.lower()
        if re.search(answer, p_text, re.X | re.M | re.S):
            # print("MATCHED THIS!!!!! " + str(answer))
            passed += 1
    if passed >= required:
        p_test['pass'] = True
        p_test['points'] += points
    elif passed >= 1 and required >= 2:  # passed, but not enough
        p_test['fail_message'] += "Needed this many matches " + str(required) + "<br>Found this many matches " + \
                                  str(passed) + "<br>"
    return p_test


def keyword_and_length(p_label, p_answers, p_text, *, search_string='', min_matches=1, min_length=5, points=0):
    """
    checks that the answer has x number of required keywords and a minimum word length.
    :param p_label: the label of the problem (i.e. 3a, 3b.) (str)
    :param p_answers: The words you are searching for.  LIST of allowed answers. (list)
    :param p_text: The text you are searching (str)
    :param search_string: regex for what you want to capture.  Basically search only this.
    :param min_matches: how many words of the keywords you need to match
    :param min_length: minimum length of answer
    :param points: how many this is worth
    :return:
    """
    import re
    p_test = {"name": "Checking that " + str(p_label) + " is has at least " + str(min_matches) + " words that we are "
                      "looking for, with a minimum word length of " + str(min_length) + " (" + str(points) +
                      " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  " +
                              str(p_label) + " appears to pass the test or checkoff!<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> " +
                              str(p_label) + " does not appear correct.  Try again.<br>"
                                             "keywords must be spelled correctly (no typos), "
                                             "but capitalization does not matter.<br><br>",
              "points": 0,
              "match": ''
              }
    found_matches = 0
    pass_len = False
    pass_match = False

    final_search_string = ''
    p_text = p_text.lower()
    if search_string:
        search_obj = re.search(search_string, p_text, re.X | re.M | re.S)
        if search_obj:
            final_search_string = search_obj.group(1)
    else:
        final_search_string = search_string
    final_search_string = final_search_string.lower()
    p_test['match'] += final_search_string
    # print("final search string is this" + final_search_string + "search is this" + search_string)
    for answer in p_answers:
        answer = answer.lower()
        if re.search(answer, final_search_string, re.X | re.M | re.S):
            found_matches += 1
    if found_matches < min_matches:
        p_test['fail_message'] += "Found this many words we were looking for: " + str(found_matches) + "<br>" \
                                  "Require this many matches: " + str(min_matches) + "<br>" \
                                  "Looked in this string: <br>" + \
                                  final_search_string + "<br><br>"
    else:
        pass_match = True
    p_text_list = final_search_string.split()
    if len(p_text_list) < min_length:
        p_test['fail_message'] += 'Found answer was this many words ' + str(len(p_text_list) + 1) + "<br>" \
                                  'Require this length: ' + str(min_length) + "<br>Looked in this string: <br>" + \
                                  final_search_string + "<br><br>"
    else:
        pass_len = True
    if pass_len and pass_match:
        p_test['pass'] = True
        p_test['points'] += points
    return p_test

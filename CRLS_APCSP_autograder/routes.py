from flask import render_template, url_for, request, redirect, flash
from app import app
from app.forms import UploadForm, UploadScratchForm, UploadDocLinkForm, UploadIT2DocLinkForm
from werkzeug.utils import secure_filename
import os


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please select a file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('This type of file not allowed.  Only files ending in .py. In particular, Google doc and text files '
                  'are not allowed.  You have to turn in a Python file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(file.filename + ' uploaded')
            if request.form['lab'] in ['1.040', '1.060', '2.020', '2.021', '2.032a', '2.032b', '2.040', '2.051a',
                                       '2.051b',
                                       '3.011', '3.020', '3.026', '4.011', '4.012', '4.021', '4.022', '4.023', '4.025',
                                       '4.026',
                                       '4.031', '4.036', '4.037', '6.011', '6.021', '6.022', '6.031', '6.032',
                                       '6.041', '6.042',
                                       '7.021', '7.031',
                                       '7.034', '7.036']:
                return redirect(url_for('feedback_' + request.form['lab'].replace(".", ""), filename=filename))

    form = UploadForm()
    user = {'username': 'CRLS Scholar!!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/scratch', methods=['GET', 'POST'])
def scratch():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please select a file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('This type of file not allowed.  Only files ending in .sb3.  '
                  'In particular, Google doc and text files are not allowed.'
                  'You have to turn in a Scratch 3 file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(file.filename + ' uploaded')
            if request.form['lab'] in []:
                return redirect(url_for('scratch_feedback_' + request.form['lab'].replace(".", ""), filename=filename))
            elif request.form['lab'] in ['1.3', '1.5', '1.x', '1.9', '2.2', '2.3a', '2.3b', '2.4', '2.6', '3.2', '3.4',
                                         '3.5', '4.2', '4.3a', '4.3b', '4.4',
                                         'karel1', 'karel2a', 'karel2b', 'karel3a', 'karel3b', 'karel3c', 'karel3d']:
                return redirect(url_for('scratch_feedback_new', lab=request.form['lab'], filename=filename))
    form = UploadScratchForm()
    user = {'username': 'CRLS Scratch Scholar!!'}
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/docs', methods=['GET', 'POST'])
def docs():
    from app.docs_labs.docs import get_google_drive_id
    user = {'username': 'CRLS Intro to CS-IT1/ APCSP Scholar!!'}

    if request.method == 'POST':
        form = UploadDocLinkForm()
        link = get_google_drive_id(form.link.data)
        if link == 'classroom':
            score_info = {'finished_scoring': False}
            tests = [{"name": "Google doc file isn't a classroom file", "pass": False,
                      "fail_message": "The link you put in the autograder should not have the string"
                                      " 'classroom' in it.<br>"
                                      "<h5 style=\"color:purple;\">In Google classroom, try to open up the Google doc."
                                      "by  click on 'open in new window' in the upper right.<br>"
                                      "Then use that link.</h5>"}]
            return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)
        else:
            if request.form['lab'] in ['binary_practice_v4', 'binary_practice_v5',
                                       'hex_minilab', 'hex_minilab_v2', 'HW01', 'HW02', 'HW03', 'HW04', 'HW05', 'HW06',
                                       'HW07', 'HW08', 'HW09', 'HW10', 'HW11', 'HW12', 'HW13', 'HW14', 'HW16', 'HW17',
                                       'HW18', 'HW19a',
                                       'HW20', 'HW21',
                                       'privacy_policies',
                                       'research_yourself']:
                return redirect(url_for('docs_feedback_level_1', lab=request.form['lab'].lower(), link=link))
            else:
                return redirect(url_for('docs_feedback_' + request.form['lab'].replace(".", ""), link=link))
    form = UploadDocLinkForm()
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/it2_docs', methods=['GET', 'POST'])
def it2_docs():
    from app.docs_labs.docs import get_google_drive_id
    user = {'username': 'Cybersecurity/IT2 Scholar!!'}

    if request.method == 'POST':
        form = UploadIT2DocLinkForm()
        link = get_google_drive_id(form.link.data)
        if link == 'classroom':
            score_info = {'finished_scoring': False}
            tests = [{"name": "Google doc file isn't a classroom file", "pass": False,
                      "fail_message": "The link you put in the autograder should not have the string"
                                      " 'classroom' in it.<br>"
                                      "<h5 style=\"color:purple;\">In Google classroom, try to open up the Google doc."
                                      "by  click on 'open in new window' in the upper right.<br>"
                                      "Then use that link.</h5>"}]
            return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)
        else:
            if request.form['lab'] in ['binary_practice_v4', 'binary_practice_v5',
                                       'hex_minilab', 'hex_minilab_v2', 'privacy_policies', 'research_yourself']:
                return redirect(url_for('docs_feedback_level_1', lab=request.form['lab'], link=link))
            else:
                return redirect(url_for('docs_feedback_' + request.form['lab'].replace(".", ""), link=link))
    form = UploadIT2DocLinkForm()
    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/scratch/scratch_feedback_new')
def scratch_feedback_new():
    import app.scratch_labs.routes_scratch as routes_scratch

    lab = request.args['lab']
    filename = '/tmp/' + request.args['filename']
    lab_underscore = lab.replace('.', '_')
    method_to_call = getattr(routes_scratch, 'route_scratch_' + str(lab_underscore))
    [user, tests, score_info] = method_to_call(filename)
    return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/scratch/doc_feedback_level_1')
def docs_feedback_level_1():
    import app.docs_labs.routes_docs_level_1 as routes_docs_level_1

    lab = request.args['lab']
    lab_underscore = lab.replace('.', '_')
    link = request.args['link']
    method_to_call = getattr(routes_docs_level_1, 'route_docs_' + str(lab_underscore))
    [user, tests, score_info] = method_to_call(link)
    return render_template('feedback.html', user=user, tests=tests, score_info=score_info)


def sum_score(p_tests, p_score_info):
    """
    Calculates the score for a particular assignment
    :param p_tests: list of tests (list of dictionaries)
    :param p_score_info: dictionary containing info about score (dict)
    :return: p_score_info, updated.
    """

    p_sum = 0
    for test in p_tests:
        if test['pass']:
            p_sum += test['points']
    p_score_info['score'] = p_sum
    p_score_info['finished_scoring'] = True
    return p_score_info


def initialize_scoring(username='dummy', score_max=0, score_manual=15):
    """
    Initializes each series of tests for a particular assignment
    :param username: username CRLS Python scholar, CRLS Scratch scholar etc...  (string)
    :param score_max: maximum score for this lab (int)
    :param score_manual: manually scored points for this lab (int)
    :return: list of 3 items, user dictionary, blank list of tests, score_info dictionary
    """
    p_user = {'username': username}
    p_tests = []
    p_score_info = {'score': 0, 'max_score': score_max, 'manually_scored': score_manual, 'finished_scoring': False}
    return [p_user, p_tests, p_score_info]


def get_scripts_wrapper(p_filename, no_backgrounds=False, *, karel=False):
    from app.scratch_labs.scratch import unzip_sb3, read_json_file, arrange_blocks_v2
    unzip_sb3(p_filename)
    p_json_data = read_json_file()
    if karel is True:
        p_scripts = arrange_blocks_v2(p_json_data, no_background=False, only_this_sprite='Coder')
    else:
        p_scripts = arrange_blocks_v2(p_json_data, no_background=no_backgrounds)
    return [p_json_data, p_scripts]


@app.route('/docs/applications_and_updates')
def docs_feedback_applications_and_updates():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 7, 'manually_scored': 93, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    # answer = {'label': 'Screenshot Chrome running', 'start':'1a', 'searchstring': 'screenshot', 'link': ''}
    test1a = exact_answer('1a. Screenshot Chrome running',
                          [r'1a\. .+? tabledata \s aaa \s inlineobject .+? 1b\.'], text, points=1)
    test1b = exact_answer('1b. Screenshot Chrome uninstalled',
                          [r'1b\. .+? tabledata \s aaa \s inlineobject .+? verify'], text, points=1)
    test2a = exact_answer('2a. Screenshot Windows activation status',
                          [r'2a\. .+? tabledata \s aaa \s inlineobject .+? software'], text, points=1)
    test3a = exact_answer('3a. Screenshot updates running',
                          [r'3a\. .+? tabledata \s aaa \s inlineobject .+? 3b\.'], text, points=1)
    test3b = keyword_and_length('3b. Why auto updates?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c\.', min_length=10, points=1)
    test3c = keyword_and_length('3c. Why no auto updates?', [r'[a-zA-Z]+'], text,
                                search_string=r'3c\. .+? tabledata (.+?) 3d\.', min_length=10, points=1)
    test3d = keyword_and_length('3d. How test an updates?', [r'[a-zA-Z]+'], text,
                                search_string=r'3d\. .+? tabledata (.+?) $', min_length=10, points=1)

    tests.extend([test1a, test1b, test2a, test3a, test3b, test3c, test3d])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/big_data_sleuth_card')
def docs_feedback_big_data_sleuth_card():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 9, 'manually_scored': 16, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('1a. source?', [r'1a .+? tabledata \s* .+? archive.+? 2a\.',
                                          r'1a .+? tabledata \s* .+? measure .+? 2a\.',
                                          r'1a .+? tabledata \s* .+? wind .+? 2a\.',
                                          r'1a .+? tabledata \s* .+? earth .+? 2a\.',
                                          r'1a .+? tabledata \s* .+? twitter .+? 2a\.',
                                          r'1a .+? tabledata \s* .+? alternative.+? 2a\.',
                                          r'1a .+? tabledata \s* .+? locator .+? 2a\.'], text, points=5)
    test2a = keyword_and_length('2a. Website useful for?', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+?) tabledata .+? tabledata  .+? 3a\.',
                                min_length=10, points=1)
    test3a = keyword_and_length('3a. Visualization useful?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) tabledata .+? tabledata  .+? 4a\.',
                                min_length=10, points=1)
    test4a = keyword_and_length('4a. Where data coming from?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) tabledata .+? tabledata  .+? 5a\.',
                                min_length=10, points=1)
    test5a = keyword_and_length('5a. Is this big data??', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) tabledata .+? check', min_length=10, points=1)

    tests.extend([test1a, test2a, test3a, test4a, test5a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/big_data_worksheet')
def docs_feedback_big_data_worksheet():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 12, 'manually_scored': 23, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    test1a = exact_answer('1a. 5 years?', [r'1a .+? tabledata \s* 5\.7 .+? 1b\.'], text, points=5)
    test1b = exact_answer('1b. 15 years?', [r'1b .+? tabledata \s* 190 .+? 1c\.'], text, points=1)
    test1c = keyword_and_length('1c. Show work', [r'[a-zA-Z]+'], text,
                                search_string=r'1c\. .+? tabledata (.+?) 1d\.', min_length=7, points=1)
    test1d = keyword_and_length('1d. Moores law', [r'[a-zA-Z]+'], text,
                                search_string=r'1d\. .+? tabledata (.+?) code', min_length=10, points=1)
    test2a = keyword_and_length('2a. 3 sources of data', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+?) 3a\.', min_length=7, points=1)
    test3a = keyword_and_length('3a. 3Vs', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 4a\.', min_length=10, points=1)
    test4a = keyword_and_length('4a. Big data good?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 4b\.', min_length=10, points=1)
    test4b = keyword_and_length('4b. Big data bad', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) heck', min_length=10, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test2a, test3a, test4a, test4b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/black_and_white_pixelation')
def docs_feedback_black_and_white_pixelation():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 45, 'manually_scored': 35, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Bits for A?', [r'1a\. .*? tabledata .*? 0 \s* 0 \s* 0 \s* 0 \s*     0\s* 0\s*1 \s* 1\s*  '
                                              '\s* 0 \s* 0\s*0\s*0  \s* 0\s*1 \s*0\s*1\s*  '
                                              '1\s*0\s*1 \s*'
                                              '0\s*1\s*0 \s*'
                                              '0\s*0\s*0\s*'
                                              '0\s*1\s*0 \s*'
                                              '0\s*1\s*0 .*? 2a\.'], text, points=20)
    test2a = exact_answer('2a. Screenshot of your image', [r'2a\. .*? tabledata .*? aaa \s* inlineobject .*? 2b\.'], text, points=1)
    test2b = exact_answer('2b. Bits of your image', [r'2b\. .*? tabledata .*? [0-9]+ .*? 3a\.'], text, points=5)
    test3a = exact_answer('3a. Maximum dimensions of this widget', [r'3a\. .*? tabledata .*? 255 .*? 255 .*? 3b\.'], text, points=5)
    test3b = keyword_and_length('3b. Explain 3a', [r'[a-z]+'], text,
                                search_string=r'3b\. .*? tabledata (.+?) 3c\.', min_length=7, points=1)
    test3c = exact_answer('3c. Total bits in largest image?', [r'3c\. .*? tabledata .*? 65 .*? 041 .*? 3d\.'], text, points=5)
    test3d = keyword_and_length('3d. Explain 3c', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'3d\. .*? tabledata (.+?) 3e\.', min_length=7, points=1)
    test3e = exact_answer('3e. Bits for smallest image', [r'3e\. .*? tabledata .*? (1(\s\n)|17) .*? 3f\.'], text, points=5)
    test3f = keyword_and_length('3f. Explain 3e.', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'3f\. .*? tabledata (.+?) 4\. \s what', min_length=7, points=1)
    test4a = keyword_and_length('4a. What if we did not include width and height', [r'[a-z]+'], text,
                                search_string=r'4\. \s what  .*? tabledata (.+?) check \s your \s work', min_length=10, points=1)
    tests.extend([test1a, test2a, test2b, test3a, test3b, test3c, test3d, test3e, test3f, test4a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/bytes_and_file_sizes_v3')
def docs_feedback_bytes_and_file_sizes_v3():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 27, 'manually_scored': 23, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. KB', [r'1a\. .*? tabledata .*? 1 [\s,]* 000  .*?  1b\. ',
                                     r'1a\. .*? tabledata .*? 1e3  .*?  1b\. ',],text, points=2)
    test1b = exact_answer('1b. MB', [r'1b\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000  .*?  1c\. ',
                                     r'1b\. .*? tabledata .*? 1e6  .*?  1c\. ',],text, points=2)
    test1c = exact_answer('1c. GB', [r'1c\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000 [\s,]* 000 .*?  1d\. ',
                                     r'1c\. .*? tabledata .*? 1e9  .*?  1d\. ',],text, points=2)
    test1d = exact_answer('1d. TB', [r'1d\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 .*?  1e\. ',
                                     r'1d\. .*? tabledata .*? 1e12  .*?  1e\. ',],text, points=2)
    test1e = exact_answer('1e. PB', [r'1e\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 .*?  1f\. ',
                                     r'1e\. .*? tabledata .*? 1e15  .*?  1f\. ',],text, points=2)
    test1f = exact_answer('1f. EB', [r'1f\. .*? tabledata .*? 1 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000 [\s,]* 000.*?  in \s the \s real ',
                                     r'1f\. .*? tabledata .*? 1e18  .*?  in \s the \s real ',],text, points=2)
    test2a = keyword_and_length('2a. jpg size dimensions', [r'[0-9]'], text, search_string=r'2a\. .*? tabledata (.+?) 2b\.', min_length=1, points=0.5)
    test2c = keyword_and_length('2c. animated gif size dimensions', [r'[0-9]'], text, search_string=r'2c\. .*? tabledata (.+?) 2d\.',
                                min_length=1, points=0.5)
    test2e = keyword_and_length('2e. PDF size #', [r'[0-9]'], text,
                                search_string=r'2e\. .*? tabledata (.+?) 2f\.', min_length=1, points=0.5)
    test2g = keyword_and_length('2g. audio size #', [r'[0-9]'], text,
                                search_string=r'2g\. .*? tabledata (.+?) 2h\.', min_length=1, points=0.5)
    test2i = keyword_and_length('2i. video size #', [r'[0-9]'], text,
                            search_string=r'2i\. .*? tabledata (.+?) 2j\.', min_length=1, points=0.5)
    test2b = keyword_and_length('2b. jpg size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2b\. .*? tabledata (.+?) 2c\.', min_length=1, points=0.5)
    test2d = keyword_and_length('2d. animated gif file size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2d\. .*? tabledata (.+?) 2e\.', min_length=1, points=0.5)
    test2f = keyword_and_length('2f. PDF file size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2f\. .*? tabledata (.+?) 2g\.', min_length=1, points=0.5)
    test2h = keyword_and_length('2h. audio file size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2h\. .*? tabledata (.+?) 2i\.', min_length=1, points=0.5)
    test2j = keyword_and_length('2j. video file size (requires units)', [r'[0-9] .*? B'], text,
                                search_string=r'2j\. .*? tabledata (.+?) test \s your \s', min_length=1, points=0.5)
    test3a = exact_answer('3a. Fits on drive?', [r'3a\. .+? tabledata .*? yes .*? 3b\.'], text, points=1)
    test3b = keyword_and_length('3b. Show work for 3a', [r'[0-9]'], text,
                                search_string=r'3b\. .*? tabledata (.+?) 4a\.', min_length=1, points=1)
    test4a = exact_answer('4a. How much space?', [r'4a\. .*? tabledata .*?  52\.5 .+? 4b\. '],
                           text, points=1)
    test4b = keyword_and_length('4b. Show work for 4a', [r'[0-9]'], text,
                                search_string=r'4b\. .*? tabledata (.+?) 5a\.', min_length=1, points=1)
    test5a = exact_answer('5a. Enough?', [r'5a\. .*? tabledata .*?  not .+? 5b\. '],
                          text, points=1)
    test5b = keyword_and_length('5b. Show work for 5a', [r'[0-9]'], text,
                                search_string=r'5b\. .*? tabledata (.+?) 6a\.', min_length=1, points=1)
    test6a = exact_answer('6a. shakespeare or video??', [r'6a\. .*? tabledata .*?  video .*? 6b\. '],
                           text, points=1)
    test6b = keyword_and_length('6b. Show work for 6a', [r'[0-9]'], text,
                                search_string=r'6b\. .*? tabledata (.+?) 7a\.', min_length=1, points=1)
    test7a = exact_answer('7a. Ohio facetube??', [r'7a\. .*? tabledata .*? 324 .*? 7b\. '],
                           text, points=1)
    test7b = keyword_and_length('7b. Show work for 7a', [r'[0-9]'], text,
                                search_string=r'7b\. .*? tabledata (.+?) question \s ', min_length=1, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test1e, test1f, test2a, test2b, test2c, test2d, test2e, test2f,
                  test2g, test2h, test2i, test2j, test3a, test3b, test4a, test4b, test5a, test5b, test6a, test6b,
                  test7a, test7b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/cybersecurity_and_crime')
def docs_feedback_cybersecurity_and_crime():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 5, 'manually_scored':20, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = keyword_and_length('1a. 3 examples of cybercrime', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=10, points=1)
    test2a = keyword_and_length('2a. What is a virus', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 3a\.', min_length=7, points=1)
    test3a = keyword_and_length('3a. What is DDOS?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 4a\.', min_length=10, points=1)
    test4a = keyword_and_length('4a. What is phishing?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 5a\.', min_length=10, points=1)
    test5a = keyword_and_length('5a. Pick one, write about how to defend against it?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) $', min_length=10, points=1)
    tests.extend([test1a, test2a, test3a, test4a, test5a,])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/databases_1')
def docs_feedback_databases_1():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 12, 'manually_scored': 78, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test2a = exact_answer('2a. screenshot connection', [r'2a\. .+? tabledata \s aaa \s inlineobject .+? 3a\.'],
                           text, points=1)
    test3a = exact_answer('3a. screenshot DB+table', [r'3a\. .+? tabledata \s aaa \s inlineobject .+? 4a\.'],
                           text, points=1)
    test4a = exact_answer('4a. screenshot table+columns', [r'4a\. .+? tabledata \s aaa \s inlineobject .+? 4b\.'],
                          text, points=1)
    test4b = exact_answer('4b. screenshot primary key', [r'4b\. .+? tabledata \s aaa \s inlineobject .+? 5a\.'],
                          text, points=1)
    test5a = keyword_and_length('5a. What is primary key', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+) 5b\.', min_length=7, points=1)
    test5b = exact_answer('5b. jersey or name? ', [r'5b\. .+? tabledata .+? jersey .+? 5c\.'],
                          text, points=5)
    test5c = keyword_and_length('5c. Why', [r'[a-zA-Z]+'], text,
                                search_string=r'5c\. .+? tabledata (.+) 6\.', min_length=7, points=1)
    test6a = exact_answer('6a. screenshot data', [r'6a\. .+? tabledata \s aaa \s inlineobject .+? $.'],
                          text, points=1)
    tests.extend([test2a, test3a, test4a, test4b, test5a, test5b, test5c, test6a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/databases_2_002')
def docs_feedback_databases_2002():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 59, 'manually_scored': 41, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test3a = exact_answer('3a. screenshot', [r'3a\. .+? tabledata \s* aaa \s* inlineobject .+? create'], text, points=1)
    test4a = exact_answer('4a. screenshot', [r'4a\. .+? tabledata \s* aaa \s* inlineobject .+? 4b\.'], text, points=1)
    test4b = exact_answer('4b. code', [r'4b\. .+? tabledata \s* insert \s* into .+? deleting'], text, points=5)
    test5a = exact_answer('5a. screenshot', [r'5a\. .+? tabledata \s* aaa \s* inlineobject .+? 5b\.'], text, points=1)
    test5b = exact_answer('5b. code', [r'5b\. .+? tabledata \s* delete \s* from .+? updating'], text, points=5)
    test6a = exact_answer('6a. screenshot', [r'6a\. .+? tabledata \s* aaa \s* inlineobject .+? 6b\.'], text, points=1)
    test6b = exact_answer('6b. code', [r'6b\. .+? tabledata \s* update .+? country .+? set .+? running'], text, points=5)
    test7a = exact_answer('7a. sql query select all',
                          [r'7a\. .+? tabledata \s* select \s* \* \s* from \s* country .+? 7b\.'],
                          text, points=10)
    test7b = exact_answer('7b. sql query select city, M names',
                          [r'7b\. .+? tabledata \s* select .+?  from .+? city .+? where .+? name .+? like \s*'
                           r' .+? m%  .+? 7c\.'],
                          text, points=10)
    test7c = exact_answer('7c. sql query surface area',
                          [r'7c\. .+? tabledata \s* select .+? from .+? country .+? where .+? surfacearea .+? > '
                           r'\s* 50 ,* 000 \s*'
                           r' .+?  7d\.'],
                          text, points=10)
    test7d = exact_answer('7d. life expectancy > 70',
                          [r'7d\. .+? tabledata \s* select \s* count .+? from .+? country .+? where \s* '
                           r'lifeexpectancy \s* > '
                           r'\s* 70 \s*'
                           r' .+?  $'],
                          text, points=10)

    tests.extend([test3a, test4a, test4b, test5a, test5b, test6a, test6b, test7a, test7b, test7c, test7d])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/databases_3_002')
def docs_feedback_databases_3002():
    from app.docs_labs.docs import get_text, exact_answer

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 50, 'manually_scored': 0, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test3a = exact_answer('3a. Christmas island',
                          [r'3a\. .+? tabledata \s* update .+? country .+? set .+? name .*?  = '
                           r'\s* .+? holiday \s island .+? '
                           r'where .+? name .*? = .*? christmas \s island .+? 3b\.',
                           r'3a\. .+? tabledata \s* update .+? country .+? set .+? name .*? \s* = \s* .*? holiday \s island .+? where .+? code .*?  = .*? cxr .+? 3b\.',
                           ], text, points=10)
    test3b = exact_answer('3b. population > 5M', [r'3b\. .+? tabledata \s* select .+? from .+? world .+?'
                                                  r'country .+? where .+? population .+? > \s* 5,*000,*000 '
                                                  r'.+? 3c\.',
                                                  r'3b\. .+? tabledata \s* select \s* .+? \s* from \s* `*country`* \s* where \s* `*population`* \s* > \s* 5,*000,*000 \s* .+? 3c\.  '],
                          text, points=10)
    test3c = exact_answer('3c. Beginning w/York', [r'3c\. .+? tabledata \s* select \s* .+? \s* from .+? `* city .+? '
                                                   r'where .+? name .+? like .+? york% .+? 3d\.',], text, points=5)
    test3d = exact_answer('3d. Ending w/York',    [r'3d\. .+? tabledata \s* select \s* .+? \s* from .+? `* city .+? '
                                                   r'where .+? name .+? like .+? %york .+? 3e\.'], text, points=5)
    test3e = exact_answer('3e. Avg. Asia population', [r'3e\. .+? tabledata \s* select  \s* avg  \(population\) \s* '
                                                         r'from \s* `*country`* \s* where .+? continent .+? asia .+? '
                                                         r'3f\.'], text, points=10)
    test3f = exact_answer('3f. unville', [r'3f\. .+? tabledata \s*  insert \s* into .+? city .+? unville .+? $'],
                          text, points=10)
    

    tests.extend([test3a, test3b, test3c, test3d, test3e, test3f])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/encoding_color_images')
def docs_feedback_encoding_color_images():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 25, 'manually_scored': 25, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Two other colors?', [r'1a\. .*? tabledata .*? \s* 011 \s* .*?  2a\.',
                                                    r'1a\. .*? tabledata .*? \s* 110 \s* .*?  2a\.'], text, points=5, required=2)
    test2a = exact_answer('2a. 4 other colors?', [r'2a\. .*? tabledata .*? [01][01][01][01][01][01] \s* [01][01][01][01][01][01] \s*'
                                                  '[01][01][01][01][01][01] \s* [01][01][01][01][01][01]  .*?  3a\.'], text, points=5)
    test3a = exact_answer('3a. Fill out 16 colors', [r'3a\. .+? tabledata \s* \d .+? questions'], text, points=1)
    test4a = exact_answer('4a. Arrange numbers', [r'4a\. .*? tabledata .*?  0000 \s* 0010 .*? \n  0000 \s* 0010 .*? \n'
                                                  r' .*? 0000 \s*0011 .*? \n .*?'
                                          '010 \s* 010 .*? \n .*? 101 \s* 010 .*?'], text, points=5)
    test4b = keyword_and_length('4b. Explain arrangement', [r'[a-z]+'], text,
                                search_string=r'4b\. .*? tabledata (.+?) 5a\.', min_length=7, points=1)
    test5a = exact_answer('5a. How many times more colors?', [r'5a\. .*? tabledata .*? 64 .*? 5b\.'], text, points=5)
    test5b = keyword_and_length('Explain 5a', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'5b\. .*? tabledata (.+?)  6a\.', min_length=3, points=1)
    test6a = keyword_and_length('6a. Change 6 bits/pixel to 12?', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'6a\. .*? tabledata (.+?)  7a\.', min_length=7, points=1)
    test7a = keyword_and_length('7a. Need a color more green than #79B', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'7a\. .*? tabledata (.+?)  check \s your \s work', min_length=10,
                                points=1)
    tests.extend([test1a, test2a, test3a, test4a, test4b, test5a, test5b, test6a, test7a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_1a')
def docs_feedback_encryption_1a():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 17, 'manually_scored': 33, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('1a. How many combos for random substitution?',
                          [r'1a\. .*? tabledata .*? 26! .*?  1b\.',
                           r'1a\. .*? tabledata .*? 26 \s* fac .*? 1b\.',
                           r'1a\. .*? tabledata .*? 26 \s* x \s* 25 \s* x \s* 24 .*? 1b\.'], text, points=5,
                          required=1)

    test1b = keyword_and_length('1b. Explain 1a.', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'1b. .*? tabledata (.+?) 2a\.', min_length=1, points=1)
    test2a = keyword_and_length('2a. How much easier to crack Caesar QUALITATIVELY', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .*? tabledata (.+?) 2b\.', min_length=10, points=1)
    test2b = exact_answer('2b. How much easier to crack Caesar QUANTITATIVELY',
                          [r'2b\. .*? tabledata .*? 1 \. 6 .*? 25 .*? 2c\.'], text, points=5,)
    test2c = keyword_and_length('2c. Show work for 2b.', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .*? tabledata (.+?) 3a\.', min_length=3, points=1)
    test3a = keyword_and_length('3a. Hard to crack random?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .*? tabledata (.+?) 3b\.', min_length=10, points=1)
    test3b = keyword_and_length('3a. Shorter or longer to crack Random and WHY?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .*? tabledata (.+?) 4a\.', min_length=10, points=1)
    test4a = keyword_and_length('4a. Algorithm to crack Caesar?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .*? tabledata (.+?) 4b\.', min_length=8, points=1)
    test4b = keyword_and_length('4b. Algorithm to crack random?', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .*? tabledata (.+?) utograder', min_length=8, points=1)
    tests.extend([test1a, test1b, test2a, test2b, test2c, test3a, test3b, test4a, test4b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_1b')
def docs_feedback_encryption_1b():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 17, 'manually_scored': 33, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('1a. How many combos for random substitution?',
                          [r'1a\. .*? tabledata .*? 24! .*?  1b\.',
                           r'1a\. .*? tabledata .*? 24 \s* fac .*? 1b\.',
                           r'1a\. .*? tabledata .*? 24 \s* x \s* 23 \s* x \s* 22 .*? 1b\.',
                           r'1a\. .*? tabledata .*? 6\.2 .*? 23 .*? 1b\.'], text, points=5,
                          required=1)

    test1b = keyword_and_length('1b. Explain 1a.', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'1b. .*? tabledata (.+?) 2a\.', min_length=1, points=1)
    test2a = keyword_and_length('2a. How much easier to crack Caesar QUALITATIVELY', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .*? tabledata (.+?) 2b\.', min_length=10, points=1)
    test2b = exact_answer('2b. How much easier to crack Caesar QUANTITATIVELY',
                          [r'2b\. .*? tabledata .*? 2 \. 6 .*? 22 .*? 2c\.',
                           r'2b\. .*? tabledata .*? 2 \. 7 .*? 22 .*? 2c\.'], text, points=5, required=1)
    test2c = keyword_and_length('2c. Show work for 2b.', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .*? tabledata (.+?) 3a\.', min_length=3, points=1)
    test3a = keyword_and_length('3a. Hard to crack random?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .*? tabledata (.+?) 3b\.', min_length=10, points=1)
    test3b = keyword_and_length('3a. Shorter or longer to crack Random and WHY?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .*? tabledata (.+?) 4a\.', min_length=10, points=1)
    test4a = keyword_and_length('4a. Algorithm to crack Caesar?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .*? tabledata (.+?) 4b\.', min_length=8, points=1)
    test4b = keyword_and_length('4b. Algorithm to crack random?', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .*? tabledata (.+?) utograder', min_length=8, points=1)
    tests.extend([test1a, test1b, test2a, test2b, test2c, test3a, test3b, test4a, test4b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_2')
def docs_feedback_encryption_2():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 24, 'manually_scored': 26, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = keyword_and_length('question 1a', [r'[^\s]+'], text,
                                search_string=r'1a. .+? tabledata .+? tabledata (.+) tabledata .+? 1b', min_length=1,
                                points=3)
    test1b = keyword_and_length('question 1b', [r'[^\s]+'], text,
                                search_string=r'1b. .+? tabledata .+? tabledata (.+) tabledata .+? 1c', min_length=1,
                                points=3)
    test1c = keyword_and_length('question 1c', [r'[^\s]+'], text,
                                search_string=r'1c. .+? tabledata .+? tabledata (.+) tabledata .+? 1d', min_length=1,
                                points=3)
    test1d = keyword_and_length('question 1d', [r'[^\s]+'], text,
                                search_string=r'1d. .+? tabledata .+? tabledata (.+) tabledata .+? 1e', min_length=1,
                                points=3)
    test1e = keyword_and_length('question 1e', [r'[^\s]+'], text,
                                search_string=r'1e. .+? tabledata .+? tabledata (.+) hought', min_length=1,
                                points=3)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 2b', min_length=10, points=1)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .+? tabledata (.+) 3a', min_length=10, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 4a', min_length=10, points=1)
    test4a = keyword_and_length('question 4a', [r'no'], text,
                                search_string=r'4a. .+? tabledata (.+?) 4b', min_length=1, points=5)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]+'], text,
                                search_string=r'4b. .+? tabledata (.+?) utograder', min_length=7, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test1e, test2a, test2b, test3a, test4a, test4b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_3')
def docs_feedback_encryption_3():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 13, 'manually_scored': 37, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = keyword_and_length('question 1a', [r'[a-zA-Z]+'], text,
                                search_string=r'1a. .+? tabledata (.+) 2a.', min_length=10,
                                points=1)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a. .+? tabledata (.+) 3a.', min_length=10,
                                points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .+? tabledata (.+) 4a', min_length=7, points=1)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=7, points=1)
    test4b = keyword_and_length('question 4b', [r'\s*secur'], text,
                                search_string=r'4b. .+? tabledata (.+) 5', min_length=1, points=5)
    test5a = keyword_and_length('question 5a', [r'[a-zA-Z]+'], text,
                                search_string=r'5a. .+? tabledata (.+) 6a', min_length=8, points=1)
    test6a = keyword_and_length('question 6a', [r'[a-zA-Z]+'], text,
                                search_string=r'6a. .+? tabledata (.+?) 6b', min_length=7, points=1)
    test6b = keyword_and_length('question 6b', [r'[a-zA-Z]+'], text,
                                search_string=r'6b. .+? tabledata (.+?) 6c', min_length=7, points=1)
    test6c = keyword_and_length('question 6c', [r'[a-zA-Z]+'], text,
                                search_string=r'6c. .+? tabledata (.+?) $', min_length=7, points=1)

    tests.extend([test1a, test2a, test3a, test4a, test4b, test5a, test6a, test6b, test6c])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_4a')
def docs_feedback_encryption_4a():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 20, 'manually_scored': 30, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('1a. 8 char lowercase time?', [r'1a\. .+? tabledata .*? 5 \s* s .+? 2a\.', ], text, points=10)
    test2a = exact_answer('1a. 8 char any char time?', [r'2a\. .+? tabledata .*? 2 \s* d .+? 2b\.', ], text, points=5)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .*? tabledata (.+?) 3a', min_length=10, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .*? tabledata (.+?) 3b', min_length=2, points=1)
    test3b = keyword_and_length('question 3b', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .*? tabledata (.+?) 4a', min_length=8, points=1)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .*? tabledata (.+?) 5a', min_length=1, points=1)
    test5a = keyword_and_length('question 5a', [r'[a-zA-Z]+'], text,
                                search_string=r'5a. .*? tabledata (.+?) the \s autograder', min_length=10, points=1)
    tests.extend([test1a, test2a, test2b, test3a, test3b, test4a, test5a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_encryption_4b')
def docs_feedback_encryption_4b():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 20, 'manually_scored': 30, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('1a. 9 char lowercase time?', [r'1a\. .+? tabledata .*? 2 \s* m .+? 2a\.', ], text, points=10)
    test2a = exact_answer('2a. 9 char any char time?', [r'2a\. .+? tabledata .*? 7 \s* m .+? 2b\.', ], text, points=5)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b. .*? tabledata (.+?) 3a', min_length=10, points=1)
    test3a = keyword_and_length('question 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3a. .*? tabledata (.+?) 3b', min_length=2, points=1)
    test3b = keyword_and_length('question 3b', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .*? tabledata (.+?) 4a', min_length=8, points=1)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .*? tabledata (.+?) 5a', min_length=1, points=1)
    test5a = keyword_and_length('question 5a', [r'[a-zA-Z]+'], text,
                                search_string=r'5a. .*? tabledata (.+?) the \s autograder', min_length=10, points=1)
    tests.extend([test1a, test2a, test2b, test3a, test3b, test4a, test5a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_bios')
def docs_feedback_hardware_bios():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 16, 'manually_scored': 54, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. BIOS version?', [r'1a\. .+? tabledata .*? A0 .+? 1b',], text, points=5)
    test1b = exact_answer('1b. BIOS year?', [r'1b\. .+? tabledata .*? 2 .+? 1c',], text, points=5)
    test1c = exact_answer('1c. How often?', [r'1c\. .+? tabledata .*? only .+? 1d',], text, points=5)
    test1d = keyword_and_length('1d. Explain how often?', [r'[a-ZA-Z]'], text,
                                 search_string=r'1c. .+? tabledata (.+) oot', min_length=7, points=1)
    tests.extend([test1a, test1b, test1c, test1d,])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_cpus')
def docs_feedback_hardware_cpus():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 22, 'manually_scored': 78, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Computer core?', [r'process', r'comput', r'calcul', r'brain'], text,
                                search_string=r'1a. .+? tabledata (.+) 1b.', min_length=7, points=1)
    test1b = keyword_and_length('1b. CPU cache?', [r'memory'], text,
                                search_string=r'1b. .+? tabledata (.+) 1c.', min_length=7, points=1)
    test1c = keyword_and_length('1c. Why cache good?', [r'perform', r'speed', r'process'], text,
                                search_string=r'1c. .+? tabledata (.+) buying', min_length=9, points=1)
    test2a = exact_answer('2a. model of computer?', [r'2a\. .+? tabledata .*? ell .+? 2b',
                                                     r'2a\. .+? tabledata .*? [0-9] .+? 2b'], text, points=1,
                          required=2)
    test2b = exact_answer('2b. model of chip?', [r'2b\. .+? tabledata .*? (amd|intel) .+? 2c',
                                                 r'2b\. .+? tabledata .*? [0-9] .+? 2c'], text, points=1, required=2)
    test2c = exact_answer('2b. Cache L1, L2, L3?', [r'2c\. .+? tabledata .*? L1 .+? through',
                                                    r'2c\. .+? tabledata .*? L2 .+? through',
                                                    r'2c\. .+? tabledata .*? L3 .+? through',
                                                    r'2c\. .+? tabledata .*? M .+? through',
                                                    r'2c\. .+? tabledata .*? K .+? through', ],
                          text, points=1, required=5)
    test3a = exact_answer('3a. Type of CPU', [r'3a\. .+? tabledata .*? (intel|amd) .*?  3b\.',
                                              r'3a\. .+? tabledata .*?  i7 .*?  3b\.', ], text, points=8, required=2)
    test3b = exact_answer('3b. How many cores?', [r'3b\. .+? tabledata .*? 4 .*? installation',
                                                  ], text, points=7)
    test4a = keyword_and_length('4a. Heat sink?', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .+? tabledata (.+) emove', min_length=10, points=1)

    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test3a, test3b, test4a])
    # test1c, test2a, test2b, test3a, test3b, test4a, test4b, test4c])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_displays')
def docs_feedback_hardware_displays():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 29, 'manually_scored': 71, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Resolution of monitors?', [r'1a\. .+? tabledata .*? 1920 \s* x \s* 1080 .*?  1b\.',
                                                          r'1a\. .+? tabledata .*? 1440 \s* x \s* 900 .*?  1b\.',],
                          text, points=5)
    test1b = exact_answer('1b. Type of video card?',
                          [r'1b\. .+? tabledata .*? AMD \s Radeon  .*? Graphics  .*?  1c\.',
                           r'1b\. .+? tabledata .*? 1200 \s* x \s* 1020 .*?  1c\.', ],
                          text, points=5)
    test1c = exact_answer('1c. Monitor type?', [r'1c\. .+? tabledata .*? [gG]eneric .*?  ideo.',],
                          text, points=5)
    test2a = exact_answer('2a. Driver name, provider, version?',
                          [r'2a\. .+? tabledata .*? AMD \s Radeon \s HD  \s 8570 \s Graphics  .*?  2b\.',
                           r'2a\. .+? tabledata .*? Advanced \s Micro \s Devices .*?  2b\.',
                           r'2a\. .+? tabledata .*? [0-9][0-9]\.[0-9][0-9][0-9] .*?  2b\.',
                           r'2a\. .+? tabledata .*? ATI \s Technologies \s  .*?  2b\.',
                           r'2a\. .+? tabledata .*? ATI \s Radeon \s HD   .*?  2b\.'
                           ],
                          text, points=5, required=3)
    test2b = exact_answer('2b. Driver date version?',
                          [r'2b\. .+? tabledata .*? [0-9][0-9]\.[0-9][0-9][0-9] .*? isplay',
                           r'2b\. .+? tabledata .*? 20[0-9][0-9] .*? isplay'],
                          text, points=5)
    test3a = exact_answer('3a. VGA pic?', [r'3a\. .+? tabledata .*? aaa \s inlineobject .*? 3b\.'],
                          text, points=1, )
    test3b = exact_answer('3b. DVI pic?', [r'3b\. .+? tabledata .*? aaa \s inlineobject .*? 3c\.'],
                          text, points=1, )
    test3c = exact_answer('3c. Displayport pic?', [r'3c\. .+? tabledata .*? aaa \s inlineobject .*? 3d\.'],
                          text, points=1, )
    test3d = keyword_and_length('3d. Why DVI/Display over VGA?', [r'[a-zA-Z]+'], text,
                                search_string=r'3d. .+? tabledata (.+?) rouble', min_length=7, points=1)

    tests.extend(
        [test1a, test1b, test1c, test2a, test2b, test3a, test3b, test3c, test3d,  ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_esd_formfactors_cards')
def docs_feedback_hardware_esd_formfactors_cards():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 29, 'manually_scored': 71, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s* .+? electr .+ static .* discharg .+ 1b'], text, points=5)
    test1b = keyword_and_length('question 1b', [r'[a-zA-Z]+'], text,
                                search_string=r'1b. .+? tabledata (.+) 1c.', min_length=7, points=1)
    test1c1 = exact_answer('question 1c-1', [r'1c. .+? tabledata .+ touch .+ side .+ 2.'], text, points=4)
    test1c2 = exact_answer('question 1c-2', [r'1c. .+? tabledata .+ (wrist|strap|brac) .+ 2.'], text, points=3)
    test1c3 = exact_answer('question 1c-3', [r'1c. .+? tabledata .+ (mat|rug) .+ 2.'], text, points=3)
    test2a = exact_answer('question 2a', [r'2a. .+? tabledata .+ small .+ form .+ factor .+ 2b.',
                                          r'2a. .+? tabledata .+ micro .+ 2b.',
                                          r'2a. .+? tabledata .+ tower.+ 2b.',
                                          r'2a. .+? tabledata .+ rack.+ 2b.'], text, points=3, required=2)
    test2b = exact_answer('question 2b', [r'2b. .+? tabledata .+ [a-zA-Z] .+ pci'], text, points=1)
    test3a = exact_answer('question 3a', [r'3a. .+? tabledata .+ inlineobject .+ 3b'], text, points=1)
    test3b = exact_answer('question 3b', [r'3b. .+? tabledata .+ [a-zA-Z] .+ pci'], text, points=1)
    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]+'], text,
                                search_string=r'4a. .+? tabledata (.+) 4b', min_length=7, points=1)
    test4b = exact_answer('question 4b', [r'4b. .+? tabledata .+ (1|16) .+ 4c'], text, points=5)
    test4c = keyword_and_length('question 4c', [r'[a-zA-Z]+'], text,
                                search_string=r'4c. .+? tabledata (.+) how', min_length=15, points=1)
    tests.extend([test1a, test1b, test1c1, test1c2, test1c3, test2a, test2b, test3a, test3b, test4a, test4b, test4c])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_memory')
def docs_feedback_hardware_memory():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 22, 'manually_scored': 78, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1c = exact_answer('1c. How much memory?', [r'1c\. .+? tabledata \s* (8|16|32) .*? g .+? 1d\.'], text, points=5)
    test1d = exact_answer('1d. ECC?', [r'1d\. .+? tabledata \s* n .+? 1e\.'], text, points=5)
    test1e = exact_answer('1e. Full memory test. How long??', [r'1d\. .+? tabledata .+? [0-9] .+? 1f\.'],
                          text, points=1)
    test1f = exact_answer('1f. Memory speed and type', [r'1f\. .+? tabledata .+? [0-9] .+? 1g\.',
                                                        r'1f\. .+? tabledata .+? ddr .+? 1g\.'],
                          text, required=2, points=1)
    test1g = exact_answer('1g. Full memory test 192G. How long??', [r'1g\. .+? tabledata \s* [0-9] .+? memory'],
                          text, points=1)
    test2b = exact_answer('2b. removed. Teacher marks?', [r'2b\. .+? tabledata .+? [a-z] .+? 2c\.'], text, points=1)
    test2c = exact_answer('2c. replaced. Teacher marks?', [r'2c\. .+? tabledata .+? [a-z] .+? how'], text, points=1)
    test3a = exact_answer('3a. screenshot memory', [r'3a\. .+? tabledata \s aaa \s inlineobject .+? picking'],
                          text, points=1)
    test4a = exact_answer('4a. Memory speed and type', [r'4a\. .+? tabledata .+? [0-9] .+? 4b\.',
                                                        r'4a\. .+? tabledata .+? ddr .+? 4b\.',
                                                        r'4a\. .+? tabledata .+? ecc .+? 4b\.'],
                          text, required=3, points=1)
    test4b = exact_answer('4b. Max memory desktop?', [r'4b\. .+? tabledata \s* [0-9] .*? g .+? pick'], text, points=1)
    test5a = exact_answer('5a. Memory speed and type', [r'5a\. .+? tabledata .+? [0-9] .+? 5b\.',
                                                        r'5a\. .+? tabledata .+? ddr .+? 5b\.',
                                                        r'5a\. .+? tabledata .+? ecc .+? 5b\.'],
                          text, required=3, points=1)
    test5b = exact_answer('5b. Max memory server?', [r'5b\. .+? tabledata \s* [0-9] .*? g .+? comparison'],
                          text, points=1)

    test6a = keyword_and_length('6a. Compare server/desktop memory', [r'[a-zA-Z]+'], text,
                                search_string=r'6a\. .+? tabledata (.+?) laptop', min_length=15, points=1)
    test7a = keyword_and_length('7a. sodimm', [r'[a-zA-Z]+'], text,
                                search_string=r'7a\. .+? tabledata (.+) check', min_length=7, points=1)
    tests.extend([test1c, test1d, test1e, test1f, test1g, test2b, test2c, test3a, test4a, test4b, test5a, test5b,
                  test6a, test7a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_motherboards')
def docs_feedback_hardware_motherboards():
    from app.docs_labs.docs import get_text, exact_answer

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 20, 'manually_scored': 80, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)

    test1a = exact_answer('1a. Chipset?', [r'1a\. .+? tabledata .*? G45 .*?   1b\.',
                                           r'1a\. .+? tabledata .*? Q45 .*?   1b\.', ], text, points=5)
    test1b = exact_answer('1b. Memory to chipset?', [r'1b\. .+? tabledata .*? 17 \s* GB .*? s .*?   1c\.', ], text,
                          points=5)
    test1c = exact_answer('1c. CPU to chipset?', [r'1c\. .+? tabledata .*? 10 .+? GB .*? s .*?   1d\.', ], text,
                          points=5)
    test1d = exact_answer('1d. CPU to chipset or RAM to chipset?',
                          [r'1d\. .+? tabledata .*? CPU .*?  ell', ], text,
                          points=5)
    tests.extend(
        [test1a, test1b, test1c, test1d, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_power')
def docs_feedback_hardware_power():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 28, 'manually_scored': 72, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Power/server?', [r'1a\. .+? tabledata .*? 360 \s* [wW] .*?   1b\.', ], text, points=5)
    test1b = keyword_and_length('1b. Show work for 1a.', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) 1c\.', min_length=2, points=1)
    test1c = exact_answer('1c. 3A/server, how many?', [r'1c\. .+? tabledata .*? 6 .*? 1d\.'], text, points=5)
    test1d = keyword_and_length('1d. Show work for 1c.', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'1d\. .+? tabledata (.+?) 1e\.', min_length=2, points=1)
    test1e = exact_answer('1e. 3A/server with 30% fluctuations, how many?',
                          [r'1e\. .+? tabledata .*? 5 .*? 1f\.'], text, points=5)
    test1f = keyword_and_length('1f. Show work for 1e.', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'1f\. .+? tabledata (.+?) 1g\.', min_length=2, points=1)
    test1g = exact_answer('1g. 1000 KW power, 3A/server, how many?',
                          [r'1g\. .+? tabledata .*? 2136 .*? 1h\.'], text, points=5)
    test1h = keyword_and_length('1h. Show work for 1g.', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'1h\. .+? tabledata (.+?) ower.', min_length=2, points=1)
    test2a = exact_answer('2a. CPU power?', [r'2a\. .+? tabledata .*? aaa \s inlineobject .*? 2b\.'],text, points=1,)
    test2b = exact_answer('2b. slimsata power?', [r'2b\. .+? tabledata .*? aaa \s inlineobject .*? 2c\.'],
                          text, points=1,)
    test2c = exact_answer('2c. motherboard power?', [r'2c\. .+? tabledata .*? aaa \s inlineobject .*? 2d\.'],
                          text, points=1, )
    test2d = exact_answer('2d. SATA power?', [r'2d\. .+? tabledata .*? aaa \s inlineobject .*? stalling'],
                          text, points=1, )
    test3a = exact_answer('3a. Power supply watts?', [r'3a\. .+? tabledata .*? 235 \s* [wW] .*? 3b\.'],
                          text, points=5, )

    tests.extend(
        [test1a, test1b, test1c, test1d, test1e, test1f, test1g, test1h, test2a, test2b, test2c, test2d, test3a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_RAID')
def docs_feedback_hardware_RAID():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 46, 'manually_scored': 54, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. RAID0 (include units)', [r'1a\. .+? tabledata .*? 10 \s* TB .*? 1b\.'], text, points=5)
    test1b = exact_answer('1b. RAID1 (include units)', [r'1b\. .+? tabledata .*? 1 \s* TB .*? 1c\.'], text, points=5)
    test1c = exact_answer('1c. RAID5 (include units)', [r'1c\. .+? tabledata .*? 9 \s* TB .*? 1d\.'], text, points=5)
    test1d = exact_answer('1d. RAID10 (include units)', [r'1d\. .+? tabledata .*? 5 \s* TB .*? 1e\.'], text, points=5)
    test1e = exact_answer('1e. RAID6 (include units)', [r'1e\. .+? tabledata .*? 8 \s* TB .*? 1f\.'], text, points=5)
    test1f = exact_answer('1f. RAID60 (include units)', [r'1f\. .+? tabledata .*? 6 \s* TB .*? understanding'], text, points=5)
    test2a = exact_answer('2a. checkoff', [r'2a\. .+? tabledata .*? [a-zA-Z] .*? hich'], text, points=1)
    test3a = exact_answer('3a. fast RAID?', [r'3a\. .+? tabledata .*? [^156]0 .*? 3b\.'], text, points=2, )
    test3b = keyword_and_length('3b. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+?) 3c\.', min_length=5, points=1)
    test3c = exact_answer('3c. safe RAID?', [r'3c\. .+? tabledata .*? 10 .*? 3d\.'],
                          text, points=2, )
    test3d = keyword_and_length('3d. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3d. .+? tabledata (.+?) 3e\.', min_length=5, points=1)
    test3e = exact_answer('3e. fast and safe RAID?', [r'3e\. .+? tabledata .*? 10 .*? 3f\.'], text, points=2, )
    test3f = keyword_and_length('3f. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3f. .+? tabledata (.+?) 3g\.', min_length=5, points=1)
    test3g = exact_answer('3g. large and safe RAID?', [r'3g\. .+? tabledata .*? 5[^0] .*? 3h\.',
                                                       r'3g\. .+? tabledata .*? 6[^0] .*? 3h\.'], text, points=2, )
    test3h = keyword_and_length('3h. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3h. .+? tabledata (.+?) 3i\.', min_length=5, points=1)
    test3i = exact_answer('3i. 48 drive RAID?', [r'3i\. .+? tabledata .*? 50 .*? 3j\.',
                                                 r'3i\. .+? tabledata .*? 60 .*? 3j\.'], text, points=2, )
    test3j = keyword_and_length('3j. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3j. .+? tabledata (.+?) hands', min_length=7, points=1)
    tests.extend(
        [test1a, test1b, test1c, test1d, test1e, test1f, test2a, test3a, test3b, test3c, test3d, test3e, test3f,
         test3g, test3h, test3i, test3j])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hardware_storage')
def docs_feedback_hardware_storage():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 22, 'manually_scored': 78, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Capacity range of SATA?', [r'1a\. .+? tabledata .*? [0-9]+ .*? g .+? 1b\.',
                                                          r'1a\. .+? tabledata .*? aaa \s inlineobject .*? 1b\.', ], \
                          text, points=1, required=2)
    test1b = exact_answer('1b. Cost/TB  of SATA?', [r'1b\. .+? tabledata .*? [0-9]+ .*? g .+? ssd'], text, points=1)
    test2a = exact_answer('2a. Capacity range of SSD?', [r'2a\. .+? tabledata .*? [0-9]+ .*? g .*? 2b\.',
                                                         r'2a\. .+? tabledata .*? aaa \s inlineobject .*? 2b\.'],
                          text, points=1, required=2)
    test2b = exact_answer('2b. cost/TB of SSD?', [r'2b\. .+? tabledata .*? [0-9]+ .*? g .+? speed'], text, points=1)
    test3a = exact_answer('3a. SSD reads?', [r'3a\. .+? tabledata .*? [0-9]+ .*?  3b\.',
                                             r'3a\. .+? tabledata .*? s .*?  3b\.', ], text, points=1, required=2)
    test3b = exact_answer('3b. SSD writes?', [r'3b\. .+? tabledata .*? [0-9]+ .*? 3c\.',
                                              r'3b\. .+? tabledata .*? s .*?  3c\.',], text, points=1, required=2)
    test3c = exact_answer('3c. SATA reads?', [r'3c\. .+? tabledata .*? [0-9]+ .*? 3d\.',
                                              r'3c\. .+? tabledata .*? s .*? 3d\.'], text, points=1, required=2)
    test3d = exact_answer('3d. SATA writes?', [r'3d\. .+? tabledata .*? [0-9]+ .*? putting.',
                                               r'3d\. .+? tabledata .*? s .*? .+? putting.'], text, points=1, required=2)
    test4a = keyword_and_length('4a. Table', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+) 4b', min_length=15, points=1)
    test4b = keyword_and_length('4b. Explain', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+) hardware', min_length=15, points=1)
    test5a = exact_answer('5a. screenshot SATA cable', [r'5a\. .+? tabledata .* aaa \s inlineobject .+? 5b\.'],
                          text, points=1)
    test5b = exact_answer('5b. screenshot power cable', [r'5b\. .+? tabledata .* aaa \s inlineobject .+? 5c\.'],
                          text, points=1)
    test5c = exact_answer('5c. Teacher checkoff rubric', [r'5c\. .+? tabledata .+? wu .+? 5d\.'],
                          text, points=5)
    test5d = exact_answer('5d. Teacher checkoff rubric', [r'5d\. .+? tabledata .+? wu .+? $'],
                          text, points=5)
    
    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test3c, test3d, test4a, test4b, test5a, test5b, test5c, test5d,])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hexadecimal_numbers_v3')
def docs_feedback_hexadecimal_numbers_v3():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 33, 'manually_scored': 0, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. A  ', [r'1a\. .*? tabledata .*? 1010 .*? 2a\.'], text, points=3)
    test2a = exact_answer('2a. 2E ', [r'2a\. .*? tabledata .*? 0* 10 \s* 1110 .*? 3a\.'], text, points=3)
    test3a = exact_answer('3a. D6 ', [r'3a\. .*? tabledata .*? 1101 \s* 0110 .*?  4a\.'], text, points=3)
    test4a = exact_answer('4a. DD1', [r'4a\. .*? tabledata .*? 1101 \s* 1101 .*? 5a\.'], text,
                          points=3)
    test5a = exact_answer('5a. DEF9', [r'5a\. .*? tabledata .*? 1101 \s* 1110 \s* 1111 \s* 1001 .*? example'],
                          text, points=3)
    test6a = exact_answer('6a. 0100', [r'6a\. .*? tabledata .*? 4 .*? 7a\.'], text, points=3)
    test7a = exact_answer('7a. 1111', [r'7a\. .*? tabledata .*? f .*? 8a\.'], text, points=3)
    test8a = exact_answer('8a. 0111 1001', [r'8a\. .*? tabledata .*? 7 \s* 9 .*? 9a\.'], text, points=3)
    test9a = exact_answer('9a. 1110 0111', [r'9a\. .*? tabledata .*?  e \s* 7 .*? 10a\.'], text, points=3)
    test10a = exact_answer('10a. 010101011111', [r'10a\. .*? tabledata .*? 5 \s* 5 \s* f .*?  11a\.'], text,
                           points=3)
    test11a = exact_answer('11a. 101101111110', [r'11a\. .*? tabledata .*? b \s* 7 \s* e .*? check \s your \s work'], text, points=3)
    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a, test7a, test8a, test9a, test10a, test11a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/hexadecimal_numbers_v4')
def docs_feedback_hexadecimal_numbers_v4():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 33, 'manually_scored': 0, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. B  ', [r'1a\. .*? tabledata .*? 1011 .*? 2a\.'], text, points=3)
    test2a = exact_answer('2a. 3E ', [r'2a\. .*? tabledata .*? 11  \s* 1110 .*? 3a\.'], text, points=3)
    test3a = exact_answer('3a. D6 ', [r'3a\. .*? tabledata .*? 1101 \s* 0110 .*?  4a\.'], text, points=3)
    test4a = exact_answer('4a. CC1', [r'4a\. .*? tabledata .*? 1100 \s* 1100 \s* 0001 .*? 5a\.'], text, points=3)
    test5a = exact_answer('5a. ABC9', [r'5a\. .*? tabledata .*? 1010 \s* 1011 \s* 1100 \s* 1001 \s* .*? example'], text, points=3)
    test6a = exact_answer('6a. 0010', [r'6a\. .*? tabledata .*? 2 .*? 7a\.'], text, points=3)
    test7a = exact_answer('7a. 1110', [r'7a\. .*? tabledata .*? e .*? 8a\.'], text, points=3)
    test8a = exact_answer('8a. 0111 1010', [r'8a\. .*? tabledata .*? 7 \s* a .*? 9a\.'], text, points=3)
    test9a = exact_answer('9a. 1110 0111', [r'9a\. .*? tabledata .*?  e \s* 7 .*? 10a\.'], text, points=3)
    test10a = exact_answer('10a. 010101011110', [r'10a\. .*? tabledata .*? 5 \s* 5 \s* e .*?  11a\.'], text,
                           points=3)
    test11a = exact_answer('11a. 101101111111', [r'11a\. .*? tabledata .*? b \s* 7 \s* f .*? check \s your \s work'], text, points=3)
    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a, test7a, test8a, test9a, test10a, test11a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/infosec_logical_security')
def docs_feedback_infosec_logical_security():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 28, 'manually_scored': 72, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Example of logical security at CRLS', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) brute', min_length=10, points=1)
    test2a = exact_answer('2a. 4 digits.  Combos?', [r'2a\. .+? tabledata .+? 10 [,.\s]* 000 .+? 2b\.'], text, points=5)
    test2b = keyword_and_length('2b. Show work', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'2b\. .+? tabledata (.+?) 2c\.', min_length=5, points=1)
    test2c = exact_answer('2c. 1000/s.  Time??', [r'2c\. .+? tabledata .+? 10 \s* s .+? 2d\.'], text, points=5)
    test2d = keyword_and_length('2d. Show work', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'2d\. .+? tabledata (.+?) 2e\.', min_length=5, points=1)
    test2e = exact_answer('2e. 1 lockout /10 passwords.  Time??', [r'2e\. .+? tabledata .+? 1 [,\s]* 000 [mM]* .+? 2f\.'],
                          text, points=5)
    test2f = keyword_and_length('2f. Show work', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'2f\. .+? tabledata (.+?) password', min_length=5, points=1)
    test3a = exact_answer('question 3a. screenshot password policies',
                          [r'3a\. .+? tabledata \s aaa \s inlineobject .+? 3b\.'], text, points=1)
    test3b = keyword_and_length('3b. 1 day not 0?', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c\.', min_length=5, points=1)
    test3c = keyword_and_length('3c. test ?', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'3c\. .+? tabledata (.+?) lockout', min_length=5, points=1)
    test4a = exact_answer('4a. screenshot lockout policies',
                          [r'4a\. .+? tabledata \s aaa \s inlineobject .+? 4b\.'], text, points=1)
    test4b = keyword_and_length('4b. Lockout, why?', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) 4c\.', min_length=5, points=1)
    test4c = keyword_and_length('4c.test', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'4c\. .+? tabledata (.+?) changing', min_length=5, points=1)
    test5a = exact_answer('5a. screenshot admin name change',
                          [r'5a\. .+? tabledata \s aaa \s inlineobject .+? 5b\.'], text, points=1)
    test5b = keyword_and_length('5b. Test?', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) 5c\.', min_length=5, points=1)
    test5c = keyword_and_length('5c. Why?', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'5c\. .+? tabledata (.+?) autograder', min_length=9, points=1)
    tests.extend([test1a, test2a, test2b, test2c, test2d, test2e, test2f, test3a, test3b, test3c, test4a, test4b,
                  test4c, test5a, test5b, test5c])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/multimedia')
def docs_feedback_multimedia():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 6, 'manually_scored': 94, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. 3 electronic interactive media tools', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 2a\.', min_length=12, points=1)
    test2a = exact_answer('2a. graphic',
                          [r'2a\. .+? tabledata \s aaa \s inlineobject .+? 3a\.'], text, points=1)
    test3a = exact_answer('3a. PDF', [r'3a\. .+? tabledata .+? done .+? 4a\.'], text, points=1)
    test4a = keyword_and_length('4a. image, audio, video, 6 total', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 5a\.', min_length=12, points=1)
    test5a = exact_answer('5a. PDF', [r'5a\. .+? tabledata .+? done .+? 6a\.'], text, points=1)
    test6a = exact_answer('6a. sound', [r'5a\. .+? tabledata .+? done .+? $'], text, points=1)

    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/infosec_disk_encryption')
def docs_feedback_infosec_disk_encryption():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 21, 'manually_scored':79, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    test1a = exact_answer('1a. Screenshot proof of seeing files on stolen drive',
                          [r'1a\. .+? tabledata \s aaa \s inlineobject .+? 1b\.'], text, points=1)
    test1b = keyword_and_length('1b. What happens, stolen drive?', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) do \s this \s with', min_length=10, points=1)
    test2a = exact_answer('2a. Screenshot proof of seeing files on unencrypted flash drive',
                          [r'2a\. .+? tabledata \s aaa \s inlineobject .+? 2b\.'], text, points=1)
    test2b = exact_answer('2b. Screenshot proof of seeing files on encrypted flash drive',
                          [r'2b\. .+? tabledata \s aaa \s inlineobject .+? 2c\.'], text, points=1)
    test2c = keyword_and_length('2c. What happens, wrong encryption password?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) give \s the \s encrypted', min_length=10, points=1)
    test3a = exact_answer('3a. How long to finish (answer_a, answer_b, answer_c, or answer_d)',
                          [r'3a\. .*? answer_b .*? 3b\.'], text, points=1)
    test3b = keyword_and_length('3b. Show work (how long)', [r'[0-9]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c', min_length=7, points=1)
    test3c = exact_answer('3c. How fast to finish  (answer_a, answer_b, answer_c, or answer_d)',
                          [r'3c\. .*? answer_b .*? 3d\.'], text, points=5)
    test3d = keyword_and_length('3d. Show work (how long)', [r'[0-9]+'], text,
                                search_string=r'3d\. .+? tabledata (.+?) 3e', min_length=7, points=1)
    test3e = exact_answer('3e. How fast to finish (answer_a, answer_b, answer_c, or answer_d)',
                          [r'3e\. .*? answer_c .*? 3f\.'], text, points=5)
    test3f = keyword_and_length('3f. Show work (how long)', [r'[0-9]+'], text,
                                search_string=r'3f\. .+? tabledata (.+?) 3g', min_length=7, points=1)
    test3g = keyword_and_length('3g. Why DBAN', [r'[0-9]+'], text,
                                search_string=r'3g\. .+? tabledata (.+?) 3h', min_length=7, points=1)
    test3h = keyword_and_length('3h. How different from physical shredding', [r'[0-9]+'], text,
                                search_string=r'3h\. .+? tabledata (.+?) check \s your \s work', min_length=7, points=1)

    tests.extend([test1a, test1b, test2a, test2b, test2c, test3a, test3b, test3c, test3d, test3e, test3f, test3g, test3h])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/infosec_physical_security')
def docs_feedback_infosec_physical_security():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 8, 'manually_scored': 92, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. What is defense in depth', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=7, points=1)
    test1b = keyword_and_length('1b. What is defense in depth at CRLS', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) 1c\.', min_length=7, points=1)
    test1c = keyword_and_length('1c. What is least privilege', [r'[a-zA-Z]+'], text,
                                search_string=r'1c\. .+? tabledata (.+?) 1d\.', min_length=7, points=1)
    test1d = keyword_and_length('1d. What is least privilege at CRLS', [r'[a-zA-Z]+'], text,
                                search_string=r'1d\. .+? tabledata (.+?) 1e\.', min_length=7, points=1)
    test1e = keyword_and_length('1e. What is separation of duties at CRLS', [r'[a-zA-Z]+'], text,
                                search_string=r'1e\. .+? tabledata (.+?) hysical', min_length=7, points=1)
    test2a = keyword_and_length('2a. Physical security @ CRLS in detail', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+?) 2b\.', min_length=12, points=1)
    test2b = keyword_and_length('2b. neutralize', [r'[a-zA-Z] + '], text,
                                search_string=r'2b\. .+? tabledata (.+?) 2c\.', min_length=10, points=1)
    test2c = keyword_and_length('2c. Write about tradeoffs', [r'[a-zA-Z] + '], text,
                                search_string=r'2c\. .+? tabledata (.+?) autograder', min_length=12, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test1e, test2a, test2b, test2c])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/internet_2_v2')
def docs_feedback_internet_2_v2():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 32, 'manually_scored': 44, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. packets guaranteed?', [r'1a\. .+? tabledata \s* no \s*  1b\.'], text, points=5)
    test1b = exact_answer('1b. protocol name?', [r'1b\. .+? tabledata \s* tcp \s*  1c\.'], text, points=5)
    test1c = keyword_and_length('1c. explain', [r'[a-zA-Z]+'], text,
                                search_string=r'1c\. .+? tabledata (.+) scalin', min_length=10, points=1)
    test2a = keyword_and_length('2a. DNS again', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 2b\.', min_length=7, points=1)
    test2b = keyword_and_length('2b. IP again', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+) 2c\.', min_length=7, points=1)
    test2c = keyword_and_length('2c. Hierarchy in DNS/IP and scaling', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+) 2d\.', min_length=10, points=1)
    test2d = keyword_and_length('2d. Fault-tolerant routing and scaling', [r'[a-zA-Z]+'], text,
                                search_string=r'2d\. .+? tabledata (.+) 2e\.', min_length=10, points=1)
    test2e = keyword_and_length('2e. Protocols and scaling', [r'[a-zA-Z]+'], text,
                                search_string=r'2e\. .+? tabledata (.+) 2f\.', min_length=10, points=1)
    test2f = keyword_and_length('2f. Protocols and scaling', [r'[a-zA-Z]+'], text,
                                search_string=r'2f\. .+? tabledata (.+?) latency', min_length=7, points=1)
    test3a = keyword_and_length('3a. Bandwidth vs. Latency', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) internet', min_length=10, points=1)
    test4a = keyword_and_length('4a. Cookie', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+)  4b\.', min_length=10, points=1)
    test4b = keyword_and_length('4b. Cookie good?', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+)  4c\.', min_length=10, points=1)
    test4c = keyword_and_length('4c. Cookie good?', [r'[a-zA-Z]+'], text,
                                search_string=r'4c\. .+? tabledata (.+?)  internet', min_length=10, points=1)
    test5a = keyword_and_length('5a. What going on?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+)  5b\.', min_length=10, points=1)
    test5b = exact_answer('5b. Min number?', [r'5b\. .+? tabledata .*? 2 .*?  5c\.'], text, points=5)
    test5c = exact_answer('5b. Max number??', [r'5c\. .+? tabledata .*? 8 .*?  $'], text, points=5)

    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test2d, test2e, test2f, test3a, test4a, test4b,
                  test4c, test5a, test5b, test5c, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_ip_addressing_dns')
def docs_feedback_ip_addressing_dns():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 22, 'manually_scored': 28, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    print(text)
    test1 = keyword_and_length('question 1a', [r'(standard|rule)'], text,
                               search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=5,
                               points=5)
    test2a = keyword_and_length('question 2a', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 2b\.', min_length=1,
                                points=1)
    test2b = keyword_and_length('question 2b', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+) 3a\.', min_length=5, points=1)
    test3a = keyword_and_length('question 3a', [r'32'], text,
                                search_string=r'3a\. .+? tabledata (.+) 3b\.', min_length=1, points=5)
    test3b = keyword_and_length('question 3b', [r'4\s*billion', '2 .+32', '4[\s,]*294[\s,]*967[\s,]*296',
                                                r'4 [\s,]* 000 [\s,]* 000 [\s,]* 000'], text,
                                search_string=r'3b\. .+? tabledata (.+) 4a\.', min_length=1, points=5)

    test4a = keyword_and_length('question 4a', [r'[a-zA-Z]'], text,
                                search_string=r'4a\. .+? tabledata (.+) 4b\.', min_length=7, points=1)
    test4b = keyword_and_length('question 4b', [r'[a-zA-Z]'], text,
                                search_string=r'4b\. .+? tabledata (.+) 5a\.', min_length=7, points=1)
    test5 = keyword_and_length('question 5', [r'[a-zA-Z]+'], text,
                               search_string=r'5a\. .+? tabledata (.+) 6a\.', min_length=6, points=1)
    test6 = keyword_and_length('question 6', [r'[a-zA-Z]+'], text,
                               search_string=r'6a\. .+? tabledata (.+) 7a\.', min_length=10, points=1)
    test7 = keyword_and_length('question 7', [r'[a-zA-Z]+'], text,
                               search_string=r'7a\. .+? tabledata (.+?) check \s your \s work', min_length=5, points=1)
    tests.extend([test1, test2a, test2b, test3a, test3b, test4a, test4b, test5, test6, test7, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/level1_internet_2')
def docs_feedback_level1_internet_2():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 47, 'manually_scored': 13, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. What is an IP address', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=5, points=1)
    test1b = exact_answer('1b. IP address of your machine?', [r'1b\. .+? tabledata .+? 172\.25\.233  .+? 1c\.'], text, points=5)
    test1c = exact_answer('1c. DNS servers of your machine?', [r'1c\. .+? tabledata .+? 172\.25\.234\.7 .+?  1d\.',
                                                               r'1c\. .+? tabledata .+? 172\.25\.234\.8 .+? 1d\.'],
                          text, points=5)
    test1d = exact_answer('1d. Router (gateway) of your machine?',
                          [r'1d\. .+? tabledata .+? 172\.25\.233\.1  .+? 1e\.'],
                          text, points=5)
    test1e = exact_answer('1e. DHCP server of your machine?', [r'1e\. .+? tabledata .+? 172\.25\.234\.7  .+? etwork'],
                          text, points=5)
    test2a = exact_answer('2a. Ping a partner.', [r'2a\. .+? tabledata .+? 172\.25\.233 .+? 2b\.',
                                                  r'2a\. .+? tabledata .+? [pP]inging .+? 2b\.',
                                                  r'2a\. .+? tabledata .+? [rR]eply .+? 2b\.'],
                          text, points=5, required=3)
    test2b = exact_answer('2b. Ping Amazon Japan.', [r'2b\. .+? tabledata .+? amazon\.co\.jp .+? 2c\.',
                                                     r'2b\. .+? tabledata .+? [pP]inging .+? 2c\.',
                                                     r'2b\. .+? tabledata .+? [rR]eply .+? 2c\.'],
                          text, points=5, required=2)
    test2c = exact_answer('2c. Ping nonexistent or down machine.',
                          [r'2c\. .+? tabledata .+? [pP]inging .+? nslookup',
                           r'2c\. .+? tabledata .+? timed \s out .+? nslookup',],
                          text, points=5, required=2)
    test3a = exact_answer('3a. nslookup.',
                          [r'3a\. .+? tabledata .+? [sS]erver .+? 3b\.',
                           r'3a\. .+? tabledata .+? [nN]ame .+? 3b\.', ],
                          text, points=5, required=2)
    test3b = keyword_and_length('3b. What does nslookup mean', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) tracert', min_length=5, points=1)
    test4a = exact_answer('4a. tracert',
                          [r'4a\. .+? tabledata .+? [hH]ops .+? 4b\.',
                           r'4a\. .+? tabledata .+? ms .+? 4b\.',
                           r'4a\. .+? tabledata .+? [tT]racing .+? 4b\.',
                           ],
                          text, points=5, required=3)

    test4b = keyword_and_length('4b. Explain tracert ', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) work', min_length=10, points=1)

    tests.extend([test1a, test1b, test1c, test1d, test1e, test2a, test2b, test2c, test3a, test3b, test4a, test4b,])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/lossless_compression')
def docs_feedback_lossless_compression():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 13, 'manually_scored': 32, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. song name', [r'\s1a\. .+? tabledata \s [a-zA-Z\.0-9] .+? 2a\.'], text, points=5)
    test2a = keyword_and_length('2a. Copy+paste compressed song', [r'[a-zA-Z]'], text,
                                search_string=r'2a\. .*? tabledata (.+?) 3a\.', min_length=1, points=1)
    test3a = keyword_and_length('3a. Copy+paste dictionary', [r'[a-zA-Z]'], text,
                                search_string=r'3a\. .*? tabledata (.+?) 4a\.', min_length=1, points=1)
    test4a = keyword_and_length('4a. Copy+paste stats', [r'[a-zA-Z]'], text,
                                search_string=r'4a\. .*? tabledata (.+?) 5a\.', min_length=20, points=1)
    test5a = keyword_and_length('5a. What made compression hard', [r'[a-zA-Z]'], text,
                                search_string=r'5a\. .*? tabledata (.+?) 6a\.', min_length=10, points=1)
    test6a = keyword_and_length('6a. Describe thinking process', [r'[a-zA-Z]'], text,
                                search_string=r'6a\. .*? tabledata (.+?) 7a\.', min_length=10, points=1)
    test7a = keyword_and_length('7a. Possible to write instructions always better than heuristic?', [r'[a-zA-Z]'], text,
                                search_string=r'7a\. .*? tabledata (.+?) 8a\.', min_length=10, points=1)
    test8a = keyword_and_length('8a. Possible to know most compressed?', [r'[a-zA-Z]'], text,
                                search_string=r'8a\. .*? tabledata (.+?) 9a\.', min_length=8, points=1)
    test9a = keyword_and_length('9a. Can your friend read compressed? Dictionary?', [r'[a-zA-Z]'], text,
                                search_string=r'9a\. .*? tabledata (.+?) check \s your \s work', min_length=10, points=1)
    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a, test7a, test8a, test9a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/lossy_compression')
def docs_feedback_lossy_compression():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 26, 'manually_scored': 19, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a what is happening', [r'[a-zA-Z]'], text,
                                search_string=r'1a\. .*? tabledata (.+?) 2a\.', min_length=10, points=1)
    test2a = exact_answer('2a counts?', [r'2a\. .*? tabledata .*? (y|yes) .*? 2b\.'], text, points=5)
    test2b = keyword_and_length('2b. Why or why not?', [r'[a-zA-Z]'], text,
                                search_string=r'2b\. .*? tabledata (.+?) 3a\.', min_length=10, points=1)
    test3a = keyword_and_length('3a Lossy refers to?', [r'[a-zA-Z]'], text,
                                search_string=r'3a\. .*? tabledata (.*?) identify \s 3', min_length=7, points=1)
    test4a1 = exact_answer('4a-1', [r'\s4a-1\. .+? tabledata \s (audio|video|image) .+? 4b-1\.'], text, points=2)
    test4a2 = exact_answer('4a-2', [r'\s4a-2\. .+? tabledata \s (audio|video|image) .+? 4b-2\.'], text, points=2)
    test4a3 = exact_answer('4a-3', [r'\s4a-3\. .+? tabledata \s (audio|video|image) .+? 4b-3\.'], text, points=2)
    test4b1 = exact_answer('4b-1', [r'\s4b-1\. .+? tabledata \s [\.a-zA-Z] .+? 4c-1\.'], text, points=2)
    test4b2 = exact_answer('4b-2', [r'\s4b-2\. .+? tabledata \s [\.a-zA-Z] .+? 4c-2\.'], text, points=2)
    test4b3 = exact_answer('4b-3', [r'\s4b-3\. .+? tabledata \s [\.a-zA-Z] .+? 4c-3\.'], text, points=2)
    test4c1 = exact_answer('4c-1', [r'\s4c-1\. .+? tabledata \s (uncompressed|lossy|lossless) .+? 4a-2\.'], text, points=2)
    test4c2 = exact_answer('4c-2', [r'\s4c-2\. .+? tabledata \s (uncompressed|lossy|lossless) .+? 4a-3\.'], text, points=2)
    test4c3 = exact_answer('4c-3', [r'\s4c-3\. .+? tabledata \s (uncompressed|lossy|lossless) .+? $'], text, points=2)
    tests.extend([test1a, test2a, test2b, test3a, test4a1, test4b1, test4c1, test4a2, test4b2, test4c2, test4a3, test4b3,
                  test4c3, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/network_protocols_nmap')
def docs_feedback_network_protocols_nmap():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 77, 'manually_scored': 23, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print('TEXT IS THIS ' + text)
    test1a = exact_answer('1a. SSH protocol', [r'1a\. .+? tabledata \s* tcp \s*  tabledata \s* 1b\.'], text, points=2)
    test1b = exact_answer('1b. SSH port', [r'1b\. .+? tabledata \s* 22\s*  tabledata .+? 2a'], text, points=2)
    test2a = exact_answer('2a. http protocol', [r'2a\. .+? tabledata \s* tcp \s*  tabledata \s* 2b\.'], text, points=2)
    test2b = exact_answer('2b. http port', [r'2b\. .+? tabledata \s* 80\s*  tabledata .+? 3a'], text, points=2)
    test3a = exact_answer('3a. https protocol', [r'3a\. .+? tabledata \s* tcp \s*  tabledata \s* 3b\.'], text, points=2)
    test3b = exact_answer('3b. https port', [r'3b\. .+? tabledata \s* 443 \s*  tabledata .+? 4a'], text, points=2)
    test4a = exact_answer('4a. ping protocol', [r'4a\. .+? tabledata \s* icmp \s*  tabledata \s* 4b\.'], text, points=2)
    test4b = exact_answer('4b. ping port', [r'4b\. .+? tabledata \s* none \s*  tabledata .+? 5a\.'], text, points=2)
    test5a = exact_answer('5a. DNS protocol', [r'5a\. .+? tabledata \s* (both\s*|tcp\/udp) \s*  tabledata \s* 5b\.'], text, points=2)
    test5b = exact_answer('5b. DNS port', [r'5b\. .+? tabledata \s* 53 \s*  tabledata .+? 6a\.'], text, points=2)
    test6a = exact_answer('6a. DHCP protocol', [r'6a\. .+? tabledata \s* udp\s*  tabledata \s* 6b\.'], text, points=2)
    test6b = exact_answer('6b. DHCP port', [r'6b\. .+? tabledata .+? 68 .+? tabledata .+? 7a\. ',
                                            r'6b\. .+? tabledata .+? 67 .+? tabledata .+? 7a\.'], text, points=2,
                          required=2)
    test7a = exact_answer('7a. remote desktop protocol',
                          [r'7a\. .+? tabledata \s* (both\s*|tcp\/udp) \s*  tabledata \s* 7b\.'], text, points=2)
    test7b = exact_answer('7b. remote desktop port', [r'7b\. .+? tabledata \s* 3389 \s*  tabledata \s* '], text,
                          points=2)
    test8a = exact_answer('8a. Screenshot Nmap is running',
                          [r'8a\. .+? tabledata \s* aaa \s* inlineobject .+?  scan \s an \s internal'], text, points=1)
    test9a = exact_answer('9a. CPSD scan',
                          [r'9a\. .+? tabledata .*? starting \s nmap .*? 9b\.',
                           r'9a\. .+? tabledata .*? host \s is \s up .*? 9b\.',
                           r'9a\. .+? tabledata .*? nmap \s done.*? 9b\.'], text, points=5, required=3)
    test9b = exact_answer('9b. CPSD scan, ports',
                          [r'9b\. .+? tabledata .*? [0-9]+.*? 9c\.',
                           ], text, points=5)
    test9c = exact_answer('9c. TCP/UDP?',
                          [r'9c\. .+? tabledata  .+? tcp .+? 9d\.'], text, points=10)
    test9d = keyword_and_length('9d. Describe services', [r'[a-zA-Z]+'], text,
                                search_string=r'9d\. .+? tabledata (.+?)  use \s nmap', min_length=7,
                                points=1)
    test10a = exact_answer('10a. OS detection scan of 1311a Windows computer',
                           [r'10a\. .+? tabledata .*? starting \s nmap .*? 10b\.',
                            r'10a\. .+? tabledata .*? host \s is \s up .*? 10b\.',
                            r'10a\. .+? tabledata .*? nmap \s done .*? 10b\.',
                            r'10a\. .+? tabledata .*? os \s detection .*? 10b\.',
                            r'10a\. .+? tabledata .*? cpe:/o:microsoft .*? 10b\.'
                            ], text, points=10, required=5)
    test10b = exact_answer('10b. OS detection scan of 1311b Mac computer',
                           [r'10b\. .+? tabledata .*? starting \s nmap .*? 11a\.',
                            r'10b\. .+? tabledata .*? host \s is \s up .*? 11a\.',
                            r'10b\. .+? tabledata .*? os \s detection .*? 11a\.',
                            r'10b\. .+? tabledata .*? no \s exact \s os \s matches .*? 11a\.',
                            r'10b\. .+? tabledata .*? apple .*? 11a\.'
                            ], text, points=10, required=4)
    test11a = exact_answer('11a. UDP scan of public DNS server',
                           [r'11a\. .+? tabledata .*? starting \s nmap .*? use \s nmap',
                            r'11a\. .+? tabledata .*? host \s is \s up .*? use \s nmap',
                            r'11a\. .+? tabledata .*? nmap \s done .*? use \s nmap',
                            r'11a\. .+? tabledata .*? 53/udp .*? use \s nmap'
                            ], text, points=10, required=4)
    test12a = exact_answer('12a. Public machine scan scan',
                          [r'12a\. .+? tabledata .*? starting \s nmap .*? 12b\.',
                           r'12a\. .+? tabledata .*? host \s is \s up .*? 12b\.',
                           r'12a\. .+? tabledata .*? nmap \s done.*? 12b\.'], text, points=5, required=3)
    test12b = keyword_and_length('12b. Public machine, ports, TCP/UDP, and what they do', [r'[0-9]+', r'(udp|tcp)',
                                                                                           r'[a-zA-Z]+'], text,
                                 search_string=r'12b\. .+? tabledata (.+?) autograder', min_length=10, points=1,
                                 min_matches=3)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test5b, test6a, test6b,
                  test7a, test7b, test8a, test9a, test9b, test9c, test9d, test10a, test10b, test11a, test12a, test12b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/network_protocols_nmap_APCSP')
def docs_feedback_network_protocols_nmap_APCSP():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 66, 'manually_scored': 22, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print('TEXT IS THIS ' + text)
    test1a = exact_answer('1a. SSH protocol', [r'1a\. .+? tabledata \s* tcp \s*  tabledata \s* 1b\.'], text, points=2)
    test1b = exact_answer('1b. SSH port', [r'1b\. .+? tabledata \s* 22\s*  tabledata .+? 2a'], text, points=2)
    test2a = exact_answer('2a. http protocol', [r'2a\. .+? tabledata \s* tcp \s*  tabledata \s* 2b\.'], text, points=2)
    test2b = exact_answer('2b. http port', [r'2b\. .+? tabledata \s* 80\s*  tabledata .+? 3a'], text, points=2)
    test3a = exact_answer('3a. https protocol', [r'3a\. .+? tabledata \s* tcp \s*  tabledata \s* 3b\.'], text, points=2)
    test3b = exact_answer('3b. https port', [r'3b\. .+? tabledata \s* 443 \s*  tabledata .+? 4a'], text, points=2)
    test4a = exact_answer('4a. ping protocol', [r'4a\. .+? tabledata \s* icmp \s*  tabledata \s* 4b\.'], text, points=2)
    test4b = exact_answer('4b. ping port', [r'4b\. .+? tabledata \s* none \s*  tabledata .+? 5a\.'], text, points=2)
    test5a = exact_answer('5a. DNS protocol', [r'5a\. .+? tabledata \s* (both\s*|tcp\/udp) \s*  tabledata \s* 5b\.'], text, points=2)
    test5b = exact_answer('5b. DNS port', [r'5b\. .+? tabledata \s* 53 \s*  tabledata .+? 6a\.'], text, points=2)
    test6a = exact_answer('6a. DHCP protocol', [r'6a\. .+? tabledata \s* udp\s*  tabledata \s* 6b\.'], text, points=2)
    test6b = exact_answer('6b. DHCP port', [r'6b\. .+? tabledata .+? 68 .+? tabledata .+? 7a\. ',
                                            r'6b\. .+? tabledata .+? 67 .+? tabledata .+? 7a\.'], text, points=2,
                          required=2)
    test7a = exact_answer('7a. remote desktop protocol',
                          [r'7a\. .+? tabledata \s* (both\s*|tcp\/udp) \s*  tabledata \s* 7b\.'], text, points=2)
    test7b = exact_answer('7b. remote desktop port', [r'7b\. .+? tabledata \s* 3389 \s*  tabledata \s* '], text,
                          points=2)
    test9a = exact_answer('9a. CPSD scan',
                          [r'9a\. .+? tabledata .*? starting \s nmap .*? 9b\.',
                           r'9a\. .+? tabledata .*? host \s is \s up .*? 9b\.',
                           r'9a\. .+? tabledata .*? nmap \s done.*? 9b\.'], text, points=5, required=3)
    test9b = exact_answer('9b. CPSD scan, ports',
                          [r'9b\. .+? tabledata .*? [0-9]+ .*? 9c\.',
                           ], text, points=1)
    test9c = exact_answer('9c. TCP/UDP?',
                          [r'9c\. .+? tabledata  .+? tcp .+? 9d\.'], text, points=5)
    test9d = keyword_and_length('9d. Describe services', [r'[a-zA-Z]+'], text,
                                search_string=r'9d\. .+? tabledata (.+?)  use \s nmap', min_length=7,
                                points=1)
    test10a = exact_answer('10a. OS detection scan of 1311a Windows computer',
                           [r'10a\. .+? tabledata .*? starting \s nmap .*? 10b\.',
                            r'10a\. .+? tabledata .*? host \s is \s up .*? 10b\.',
                            r'10a\. .+? tabledata .*? nmap \s done .*? 10b\.',
                            r'10a\. .+? tabledata .*? os \s detection .*? 10b\.',
                            r'10a\. .+? tabledata .*? cpe:/o:microsoft .*? 10b\.'
                            ], text, points=10, required=10)
    test11a = exact_answer('11a. UDP scan of public DNS server',
                           [r'11a\. .+? tabledata .*? starting \s nmap .*? use \s nmap',
                            r'11a\. .+? tabledata .*? host \s is \s up .*? use \s nmap',
                            r'11a\. .+? tabledata .*? nmap \s done .*? use \s nmap',
                            r'11a\. .+? tabledata .*? 53/udp .*? use \s nmap'
                            ], text, points=10, required=10)
    test12a = exact_answer('12a. Public machine scan scan',
                          [r'12a\. .+? tabledata .*? starting \s nmap .*? 12b\.',
                           r'12a\. .+? tabledata .*? host \s is \s up .*? 12b\.',
                           r'12a\. .+? tabledata .*? nmap \s done.*? 12b\.'], text, points=5, required=3)
    test12b = keyword_and_length('12b. Public machine, ports, TCP/UDP, and what they do', [r'[0-9]+', r'(udp|tcp)',
                                                                                           r'[a-zA-Z]+'], text,
                                 search_string=r'12b\. .+? tabledata (.+?) autograder', min_length=10, points=1,
                                 min_matches=3)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test5b, test6a, test6b,
                  test7a, test7b, test9a, test9b, test9c, test9d, test10a, test11a, test12a, test12b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/password_crack')
def docs_feedback_password_crack():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 7, 'manually_scored': 93, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test2a = exact_answer('2a. screenshot new users', [r'2a\. .+? tabledata \s aaa \s inlineobject .+? 3\.'],
                          text, points=1)
    test6a = exact_answer('6a. screenshot brute force', [r'6a\. .+? tabledata \s aaa \s inlineobject .+? 6b\.'],
                          text, points=1)
    test6b = exact_answer('6b. screenshot precomputation', [r'6b\. .+? tabledata \s aaa \s inlineobject .+? 7a\.'],
                          text, points=1)
    test7a = keyword_and_length('7a. Interpret your results', [r'[a-zA-Z]+'], text,
                                search_string=r'7a\. .+? tabledata (.+) 8\.', min_length=15, points=1)
    test8a = keyword_and_length('8a. precomputation drawback', [r'[a-zA-Z]+'], text,
                                search_string=r'8a\. .+? tabledata (.+) 8b\.', min_length=15, points=1)
    test8b = keyword_and_length('8b. max length and why', [r'[a-zA-Z]+'], text,
                                search_string=r'8b\. .+? tabledata (.+) 9a\.', min_length=10, points=1)
    test9a = keyword_and_length('9a. max length and why', [r'[a-z]+'], text,
                                search_string=r'9a\. .+? tabledata (.+) $', min_length=10, points=1)
    tests.extend([test2a, test6a, test6b, test7a, test8a, test8b, test9a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/passwords_passwords_revisited')
def docs_feedback_passwords_passwords_revisited():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34, 'manually_scored': 66, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Offline vs. online? ?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a. .+? tabledata (.+?) 1b\.', min_length=7, points=1)
    test1b = exact_answer('1b. offline slower why?', [r'1b\. .+? tabledata .*? network.*? 1c\.',
                                                      r'1b\. .+? tabledata .*? internet .*? 1c\.',
                                                      r'1b\. .+? tabledata .*? lock .*? 1c\.',
                                                      r'1b\. .+? tabledata .*? firewall .*? 1c\.'], text, points=5,
                          required=2)
    test1c = exact_answer('1c. Steal HD?', [r'1c\. .+? tabledata .*? offline .*? 1d\.'], text, points=1)
    test1d = keyword_and_length('1d. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'1d\. .+? tabledata (.+?) 1e\.', min_length=5, points=1)
    test1e = exact_answer('1e. How secure is my pword?', [r'1e\. .+? tabledata .*? offline .*? 1f\.'], text, points=1)
    test1f = keyword_and_length('1f. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'1f\. .+? tabledata (.+?) 1g\.', min_length=5, points=1)
    test1g = exact_answer('1g. movie scene?', [r'1g\. .+? tabledata .*? online .*? 1h\.'], text, points=1)
    test1h = keyword_and_length('1h. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'1h\. .+? tabledata (.+?) demonstra', min_length=5, points=1)
    test2a = exact_answer('2a. paste MD5 hash', [r'2a\. .+? tabledata .{32,35} 2b\.'], text, points=3)
    test2b = exact_answer('2b. paste MD5 hash 3x', [r'2b\. .+? tabledata .{96,102} 2c\.'], text, points=2)
    test2c = keyword_and_length('2c. Why hashes in common?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) questions', min_length=7, points=1)
    test3a = keyword_and_length('3a. What is hash and what it contains ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=7, points=1)
    test3b = keyword_and_length('3b. How users authenticated ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c\.', min_length=10, points=1)
    test3c = keyword_and_length('3c. Why hash needed ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3c\. .+? tabledata (.+?) 3d\.', min_length=7, points=1)
    test3d = exact_answer('3d. Speed ranking?', [r'3d\. .+? tabledata .*?  WPA .*?  SHA -* 256 .*?'
                                                 r' SHA -* 1 .*?'
                                                 r' MD5 .*?  NTLM .*? 3e\.'], text, points=5, )
    test3e = keyword_and_length('3e. Why ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3e\. .+? tabledata (.+?) cracking', min_length=7, points=1)
    test4a = keyword_and_length('4a. Brute force cracking?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 4b\.', min_length=7, points=1)
    test4b = keyword_and_length('4b. Dictionary cracking?', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) 4c\.', min_length=7, points=1)
    test4c = keyword_and_length('4c. Precopmutation cracking?', [r'[a-zA-Z]+'], text,
                                search_string=r'4c\. .+? tabledata (.+?) 4d\.', min_length=7, points=1)
    test4d = keyword_and_length('4d. Why rainbow tables?', [r'[a-zA-Z]+'], text,
                                search_string=r'4d\. .+? tabledata (.+?) alts', min_length=7, points=1)
    test5a = keyword_and_length('5a. What is password salt?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) 5b\.', min_length=7, points=1)
    test5b = keyword_and_length('5b. Salt vs Brute force?', [r'[a-zA-Z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) 5c\.', min_length=7, points=1)
    test5c = keyword_and_length('5c. Salt vs precomputation?', [r'[a-zA-Z]+'], text,
                                search_string=r'5c\. .+? tabledata (.+?) kiddies', min_length=7, points=1)

    tests.extend(
        [test1a, test1b, test1c, test1d, test1e, test1f, test1g, test1h, test2a, test2b, test2c, test3a,
         test3b, test3c, test3d, test3e, test4a, test4b, test4c, test4d, test5a, test5b, test5c, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/passwords_offline_crack_1')
def docs_feedback_passwords_offline_crack_1():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 74, 'manually_scored': 26, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)

    test1a = exact_answer('1a. Screenshot of accounts',
                          [r'1a\. .+? tabledata \s* aaa \s* inlineobject .+?  2a\.'], text, points=1)
    test2a = exact_answer('2a. Copy+paste hash file dump', [r'2a\. .+? tabledata .*?  NO \s PASSWORD .*? 2b\.',
                                                            r'2a\. .+? tabledata .*? ADMINISTRATOR .*? 2b\.',
                                                            r'2a\. .+? tabledata .*? 500 .*? 2b\.',
                                                            r'2a\. .+? tabledata .*? :.+?:.+?:.+?:.+?:.+?: .*? 2b\.', ]
                          , text, points=10, required=4)
    test2b = exact_answer('2b. Dump hash file as non-admin?', [r'2b\. .+? tabledata .+? (no|No|NO) .+? 2c\.'],
                          text, points=5)
    test2c = keyword_and_length('2c. Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) 3a\.', min_length=7, points=1)
    test3a = exact_answer('3a. Copy+paste word list file?', [r'3a\. .+? tabledata .+? q \n w \n e \n r \n t \n y \n'
                                                             r'u \n i \n o \n p .+? 4a\.'],
                          text, points=20)
    test4a = exact_answer('4a. Copy+paste crack password',
                          [r'4a\. .+? tabledata .*? Loaded \s [0-9]+ \s password \s hashes .*? 5a\.',
                           r'4a\. .+? tabledata .*? Proceeding \s with \s wordlist .*? 5a\.',
                           r'4a\. .+? tabledata .*? Proceeding \s with \s incremental.*? 5a\.',
                           r'4a\. .+? tabledata .*? [a-zA-Z]+ \s* \(.+?\)  .*? 5a\.', ]
                          , text, points=35, required=2)
    test5a = keyword_and_length('5a.How long does this take??', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) 5b\.', min_length=4, points=1)
    test5b = keyword_and_length('5b. Explain offline vs. online?', [r'[a-zA-Z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) gnore.', min_length=10, points=1)
    tests.extend(
        [test1a, test2a, test2b, test2c, test3a, test4a, test5a, test5b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/passwords_offline_crack_2')
def docs_feedback_passwords_offline_crack_2():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 33, 'manually_scored': 67, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)

    test1a = exact_answer('1a. Checkoff',
                          [r'1a\. .+? tabledata .+? .+?  notes'], text, points=1)
    test1ab = exact_answer('1a. Stratfor password file cracked',
                           [r'1a\. .+? tabledata (.+? \s+ \(user[0-9]+\)){9,} .+? notes', ], text)
    test2a = keyword_and_length('2a. Describe what you are seeing in Stratfor crack.', [r'password', r'(begin|first)'],
                                text,
                                search_string=r'2a\. .+? tabledata (.+?) 2b\.', min_length=15, points=1, min_matches=2)
    test2b = keyword_and_length('2b. Friend password stolen.  Advice??', [r'(advice|advise)', 'because'], text,
                                search_string=r'2b\. .+? tabledata (.+?) odern', min_length=10, points=1, min_matches=2)
    test3a = keyword_and_length('3a. Article?', [r'[0-9a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) ashcat \s is \s basically \s', min_length=50,
                                points=1)

    tests.extend(
        [test1a, test1ab, test1ab, test2a, test2b, test3a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/passwords_password_hijack')
def docs_feedback_passwords_password_hijack():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    score_info = {'score': 0, 'max_score': 74, 'manually_scored': 26, 'finished_scoring': True}
    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    link = request.args['link']
    text = get_text(link)

    test1a = exact_answer('1a. Screenshot hijack',
                          [r'1a\. .+? tabledata \s* aaa \s* inlineobject .+?  reventing \s this'], text, points=1)
    test2a = exact_answer('2a. Windows 2k16 settings to lock?', [r'2a\. .+? tabledata .{32,35} 2b\.'], text, points=3)
    test2b = exact_answer('2b. Screenshot windows 2k16 locks',
                          [r'2b\. .+? tabledata \s* aaa \s* inlineobject .+?  2c\.'], text, points=1)
    test2c = keyword_and_length('2c. Windows 7 settings to lock?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) questions', min_length=7, points=1)
    test2d = exact_answer('2d. Screenshot windows 7 lock settings',
                          [r'2d\. .+? tabledata .+? screen \s* saver .+? ot \s saving',
                           r'2d\. .+? tabledata .+? personalization .+? ot \s saving'
                           r'2d\. .+? tabledata .+? on \s* resume .+? ot \s saving'], text, points=1,
                          required=2)
    test3a = exact_answer('3a. Chrome settings do not save pwords',
                          [r'3a\. .+? tabledata .+? offer \s* to \s* save \s* passwords .+?  3b\.'], text, points=10)
    test3b = exact_answer('3b. Screenshot no chrome passwords saved',
                          [r'2d\. .+? tabledata \s* aaa \s* inlineobject .+?  $'], text, points=1)
    tests.extend(
        [test1a, test2a, test2b, test2c, test2d,  test3a, test3b,])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)

    
@app.route('/docs/passwords_snooping_passwords')
def docs_feedback_passwords_snooping_passwords():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS IT2 Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 55, 'manually_scored': 45, 'finished_scoring': True}
    link = request.args['link']
    text = get_text(link)

    print(text)

    test1a = exact_answer('1a. Screenshot of Nmap',
                          [r'1a\. .+? tabledata \s* aaa \s* inlineobject .+?  iew'], text, points=1)
    test2a = exact_answer('2a. Copy+paste ping of website in cmd', [r'2a\. .+? tabledata .*? inging  .*? 2b\.',
                                                             r'2a\. .+? tabledata .*? bytes .*? 2b\.',
                                                             r'2a\. .+? tabledata .*? time .*? 2b\.',
                                                             r'2a\. .+? tabledata .*? round \s* trip .*? 2b\.', ]
                          , text, points=10, required=4)
    test2b = exact_answer('2b. Copy+paste ping of website in wireshark',
                          [r'2b\. .+? tabledata .*? ping  .*? 2c\.',
                           r'2b\. .+? tabledata .*? Echo .*? 2c\.',
                           r'2b\. .+? tabledata .*? src .*? 2c\.',
                           r'2b\. .+? tabledata .*? dst .*? 2c\.', ]
                          , text, points=10, required=4)
    test2c = keyword_and_length('2c. Explain what you see?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) iew \s passwords', min_length=7, points=1)
    test3a = exact_answer('3a. Copy+paste password  in wireshark',
                          [r'3a\. .+? tabledata .*? username  .*? trying',
                           r'3a\. .+? tabledata .*? password .*? trying',
                           r'3a\. .+? tabledata .*? email_id .*? trying',
                           r'3a\. .+? tabledata .*? user_pwd .*? trying',
                           r'3a\. .+? tabledata .*? hypertext .*? trying']
                          , text, points=30, required=3)
    test4a = exact_answer('4a. Screenshot of Nmap',
                          [r'4a\. .+? tabledata \s* aaa \s* inlineobject .+?  4b'], text, points=1)
    test4b = keyword_and_length('4b. Explain why you can not see passwords?', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) wrap-up', min_length=1, points=1)

    test5a = keyword_and_length('5a. Explain what you did in this lab?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) autograder', min_length=15, points=1)
    tests.extend(
        [test1a, test2a, test2b, test2c, test3a, test4a, test4b, test5a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/privacy_labs_anonymity_and_privacy')
def docs_feedback_privacy_labs_anonymity_and_privacy():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    link = request.args['link']
    text = get_text(link)

    score_info = {'score': 0, 'max_score': 28, 'manually_scored': 72, 'finished_scoring': True}

    test1a = exact_answer('1a. Troll ppl online?',
                          [r'1a\. .+? tabledata .*? anonymity .*? 1b\.'], text, points=5)
    test1b = exact_answer('1b. Keep password secre?',
                          [r'1b\. .+? tabledata .*? privacy .*? 1c\.'], text, points=5)
    test1c = exact_answer('1c. Arrest info lost?',
                          [r'1c\. .+? tabledata .*? privacy .*? 1d\.'], text, points=5)
    test1d = exact_answer('1d. MAC address forging',
                          [r'1d\. .+? tabledata .*? anonymity .*? privacy \s \(revisited '], text, points=5)
    test2a = keyword_and_length('2a. Google somebody?', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+?) 2b\.', min_length=20, points=1)
    test2b = keyword_and_length('2b. What to worry against doxxer?', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+?) social \s media', min_length=10, points=1)
    test3a = keyword_and_length('3a. Pros and cons, fake FB name?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=7, points=1)
    test3b = keyword_and_length('3b. What do you do?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) who \s has \s your', min_length=7, points=1)
    test4a = keyword_and_length('4a. Who has your back?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) social \s media \s privacy \s settings', min_length=15, points=1)
    test5a = keyword_and_length('5a. Your settings?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) 5b.', min_length=7, points=1)
    test5b = keyword_and_length('5b. Recommended settings?', [r'[a-zA-Z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) 5c.', min_length=7, points=1)
    test5c = keyword_and_length('5c. Changes to settings?', [r'[a-zA-Z]+'], text,
                                search_string=r'5c\. .+? tabledata (.+?) check \s your \s work \s with.', min_length=5, points=1)

    
    tests.extend([test1a, test1b, test1c, test1d, test2a, test2b, test3a, test3b, test4a, test5a, test5b, test5c])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/privacy_labs_proxies')
def docs_feedback_privacy_labs_proxies():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    link = request.args['link']
    text = get_text(link)

    score_info = {'score': 0, 'max_score': 8, 'manually_scored': 92, 'finished_scoring': True}
    test1a = keyword_and_length('1a. What is a proxy?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=10, points=1)
    test1b = keyword_and_length('1b. Convince head of company?', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) proxies\,', min_length=10, points=1)
    test2a = exact_answer('2a. Screenshot proxy usage',
                          [r'2a\. .+? tabledata \s aaa \s inlineobject .+? 2b\.'], text, points=1)
    test2b = keyword_and_length('2b. How does it compare?', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+?) 2c\.', min_length=10, points=1)
    test2c = keyword_and_length('2c. Advise classmates?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) research', min_length=10, points=1)

    test3a = keyword_and_length('3a. Research?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) check \s that \s you', min_length=40, points=1)

    tests.extend([test1a, test1b, test2a, test2b, test2c, test3a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/privacy_labs_tor_1')
def docs_feedback_privacy_labs_tor_1():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 6, 'manually_scored': 94, 'finished_scoring': True}


    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Screenshot Tor running',
                          [r'1a\. .+? tabledata \s* aaa \s inlineobject .+? 1b\.'], text, points=1)
    test1b = exact_answer('1b. Screenshot Tor circuit',
                          [r'1b\. .+? tabledata \s* aaa \s inlineobject .+? 1c\.'], text, points=1)
    test1c = exact_answer('1c. Test network settings',
                          [r'1c\. .+? tabledata \s* aaa \s inlineobject .+? tor,\s usability'], text, points=1)
    test2a = keyword_and_length('2a. Usability', [r'.+'], text,
                                search_string=r'2a\. .+? tabledata (.+?) tor, \s bridges', min_length=25, points=1)
    test3a = exact_answer('3a. Screenshot Tor bridges',
                          [r'3a\. .+? tabledata \s* aaa \s inlineobject .+? tor,\s basics'], text, points=1)
    test4a = keyword_and_length('4a. Describe how Tor works', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 4b\.', min_length=20, points=1)
    test4b = keyword_and_length('4b. Describe Tor encryption', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) 4c\.', min_length=20, points=1)
    test4c = keyword_and_length('4c. Why use Tor?', [r'[a-zA-Z]+'], text,
                                search_string=r'4c\. .+? tabledata (.+?) check \s that \s you', min_length=20, points=1)

    tests.extend([test1a, test1b, test1c, test2a, test3a, test4a, test4b, test4c])

    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/privacy_labs_vpn_1')
def docs_feedback_privacy_labs_vpn_1():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 55, 'manually_scored': 45, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. CRLS to VPN',
                          [r'1a\. .+? tabledata .*? encrypted .*? 1b\.'], text, points=5)
    test1b = exact_answer('1b. VPN to youtube',
                          [r'1b\. .+? tabledata .*? un .*? 1c\.'], text, points=5)
    test1c = exact_answer('1c. youtube to VPN',
                          [r'1c\. .+? tabledata .*? un .*? 1d\.'], text, points=5)
    test1d = exact_answer('1d. VPN to CRLS',
                          [r'1d\. .+? tabledata .*? encrypted .*? 1e\.'], text, points=5)
    test1e = keyword_and_length('1e. VPN like proxy?', [r'.+'], text,
                                search_string=r'1e\. .*? tabledata (.+?) 1f\.', min_length=10, points=1)
    test1f = keyword_and_length('1f. VPN different from proxy?', [r'.+'], text,
                                search_string=r'1f\. .*? tabledata (.+?) 1g\.', min_length=10, points=1)
    test1g = keyword_and_length('1g. Download stuff while connected to VPN?', [r'.+'], text,
                                search_string=r'1g\. .*? tabledata (.+?) vpns \s to \s beat.', min_length=10, points=1)
    test2a = keyword_and_length('2a. What is protocol', [r'(standard|rule)'], text,
                                search_string=r'2a\. .*? tabledata (.+?) 2b\.', min_length=5,
                                points=5)
    test2b = exact_answer('2b. L2TP-IPSEC port 1',
                          [r'2b\. .+? tabledata .*? 500 .*? 2c\.'], text, points=2)
    test2c = exact_answer('2c. L2TP-IPSEC UDP/TCP 1',
                          [r'2c\. .+? tabledata .*? udp .*? 2d\.'], text, points=2)
    test2d = exact_answer('2d. L2TP-IPSEC inbound/outbound 1',
                          [r'2d\. .+? tabledata .*? outbound .*? 2e\.'], text, points=2)
    test2e = exact_answer('2e. L2TP-IPSEC port 2',
                          [r'2e\. .+? tabledata .*? 1701 .*? 2f\.'], text, points=2)
    test2f = exact_answer('2f. L2TP-IPSEC UDP/TCP 2',
                          [r'2f\. .+? tabledata .*? udp .*? 2g\.'], text, points=2)
    test2g = exact_answer('2g. L2TP-IPSEC inbound/outbound 2',
                          [r'2g\. .+? tabledata .*? outbound .*? 2h\.'], text, points=2)
    test2h = exact_answer('2h. L2TP-IPSEC port 3',
                          [r'2h\. .+? tabledata .*? 4500 .*? 2i\.'], text, points=2)
    test2i = exact_answer('2i. L2TP-IPSEC UDP/TCP 3',
                          [r'2i\. .+? tabledata .*? udp .*? 2j\.'], text, points=2)
    test2j = exact_answer('2j. L2TP-IPSEC inbound/outbound 3',
                          [r'2j\. .+? tabledata .*? outbound .*? 2k\.'], text, points=2)
    test2k = exact_answer('2k. OpenVPN port 1',
                          [r'2k\. .+? tabledata .*? 1194 .*? 2l\.'], text, points=2)
    test2l = exact_answer('2l. OpenVPN UDP/TCP 1',
                          [r'2l\. .+? tabledata .*? tcp .*? 2m\.'], text, points=2)
    test2m = exact_answer('2m. OpenVPN inbound/outbound 1',
                          [r'2m\. .+? tabledata .*? outbound .*? crls'], text, points=2)

    test3a = keyword_and_length('3a. Drawbacks of free VPNs', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=100, points=1)
    test3b = keyword_and_length('3b. Pick a free VPN', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) check \s your \s work', min_length=100,
                                points=1)
    tests.extend([test1a, test1b, test1c, test1d, test1e, test1f, test1g, test2a, test2b, test2c, test2d,
                  test2e, test2f, test2g, test2h, test2i, test2j, test2k, test2l, test2m, test3a, test3a, test3b, ])

    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/privacy_labs_wireshark_proxies_vpns_tor')
def docs_feedback_privacy_labs_wireshark_proxies_vpns_tor():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 31, 'manually_scored': 104, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Screenshot of wireshark',
                          [r'1a\. .+? tabledata \s* aaa \s* inlineobject .+?  1b\.'], text, points=5)
    test1b = keyword_and_length('1b. IP address of site you visited?', [r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'], text,
                                search_string=r'1b\. .*? tabledata (.+?) 1c\.', min_length=1, points=1)
    test1c = keyword_and_length('1c. Destination IP address of site?', [r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'], text,
                                search_string=r'1c\. .*? tabledata (.+?) 1d\.', min_length=1, points=1)
    test1d = keyword_and_length('1d. Hostname of site you visited?', [r'.+'], text,
                                search_string=r'1d\. .*? tabledata (.+?) 1e\.', min_length=1, points=1)
    test1e = keyword_and_length('1e. Put it all together', [r'.+'], text,
                                search_string=r'1e\. .*? tabledata (.+?) cpsd \s actually \s uses', min_length=12, points=1)   
    test2a = keyword_and_length('2a. What is a VPN', [r'.+'], text,
                                search_string=r'2a\. .*? tabledata (.+?) 2b\.', min_length=7, points=1)   
    test2b = exact_answer('2b. What is public IP, VPN off',
                          [r'2b\. .+? tabledata .*? 204\.167\.[0-9]+\.[0-9]+ .*? 2c\.'], text, points=2)
    test2c = exact_answer('2c. Screenshot of scan',
                          [r'2c\. .+? tabledata \s* aaa \s* inlineobject .+?  2d\.'], text, points=5)    
    test2d = keyword_and_length('2d. IP address you visited?', [r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'], text,
                                search_string=r'2d\. .*? tabledata (.+?) 2e\.', min_length=1, points=1)
    test2e = keyword_and_length('2e. Destination IP address in wireshark?', [r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'], text,
                                search_string=r'2e\. .*? tabledata (.+?) 2f\.', min_length=1, points=1)
    test2f = keyword_and_length('2f. Public IP with VPN on?', [r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'], text,
                                search_string=r'2f\. .*? tabledata (.+?) 2g\.', min_length=1, points=1)
    test2g = keyword_and_length('2g. Put it all together', [r'.+'], text,
                                search_string=r'2g\. .*? tabledata (.+?) wireshark \s \+ ', min_length=12, points=1)   
    test3a = keyword_and_length('3a. What is Tor', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=5, points=1)
    test3b = exact_answer('3b. Screenshot of scan',
                          [r'3b\. .+? tabledata \s* aaa \s* inlineobject .+?  3c\.'], text, points=5)    
    test3c = keyword_and_length('3c. IP address you visited?', [r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'], text,
                                search_string=r'3c\. .*? tabledata (.+?) 3d\.', min_length=1, points=1)
    test3d = keyword_and_length('3d. Destination IP address in wireshark?', [r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'], text,
                                search_string=r'3d\. .*? tabledata (.+?) 3e\.', min_length=2, points=1)
    test3e = keyword_and_length('3e. Public IP with Tor on?', [r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'], text,
                                search_string=r'3e\. .*? tabledata (.+?) 3f\.', min_length=1, points=1)
    test3f = keyword_and_length('3f. Put it all together', [r'.+'], text,
                                search_string=r'3f\. .*? tabledata (.+?) check \s that \s you \s answered ', min_length=12, points=1)   
    tests.extend([test1a, test1b, test1c, test1d, test1e, test2a, test2b, test2c, test2d,
                  test2e, test2f, test2g, test3a, test3b, test3c, test3d, test3e, test3f])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_1020')
def docs_feedback_python_1020():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 39, 'manually_scored': 10, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('question 1 expected', [r'1a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 1b\.'],
                          text, points=0.5)
    test1b = exact_answer('question 1 actual', [r'1b\. .*? tabledata \s 9 .*? tabledata \s 1c\.'],
                          text, points=0.5)
    test1c = exact_answer('question 1 difference',
                          [r'1c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 2a\.'],
                          text, points=0.5)
    test2a = exact_answer('question 2 expected', [r'2a\. .*? tabledata .*? [\.a-zA-Z0-9] .*? tabledata \s 2b\.'],
                          text, points=0.5)
    test2b = exact_answer('question 2 actual', [r'2b\. .*? tabledata .*? 0*\.6+ .*? tabledata \s 2c\.'],
                          text, points=0.5)
    test2c = exact_answer('question 2 difference',
                          [r'2c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 3a\.'],
                          text, points=0.5)
    test3a = exact_answer('question 3 expected', [r'3a\. .*? tabledata \s [\.a-zA-Z0-9] .*? tabledata \s 3b\.'],
                          text, points=0.5)
    test3b = exact_answer('question 3 actual', [r'3b\. .*? tabledata \s 3\.0 .*? tabledata \s 3c\.'],
                          text, points=0.5)
    test3c = exact_answer('question 3 difference',
                          [r'3c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 4a\.'],
                          text, points=0.5)
    test4a = exact_answer('question 4 expected', [r'4a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 4b\.'],
                          text, points=0.5)
    test4b = exact_answer('question 4 actual', [r'4b\. .*? tabledata \s 50 .*? tabledata \s 4c\.'],
                          text, points=0.5)
    test4c = exact_answer('question 4 difference',
                          [r'4c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 5a\.'],
                          text, points=0.5)
    test5a = exact_answer('question 5 expected', [r'5a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 5b\.'],
                          text, points=0.5)
    test5b = exact_answer('question 5 actual', [r'5b\. .*? tabledata \s 2\.0 .*? tabledata \s 5c\.'],
                          text, points=0.5)
    test5c = exact_answer('question 5 difference',
                          [r'5c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 6a\.'],
                          text, points=0.5)
    test6a = exact_answer('question 6 expected', [r'6a\. .*? tabledata .*? [a-zA-Z0-9] .*? tabledata \s 6b\.'],
                          text, points=0.5)
    test6b = exact_answer('question 6 actual', [r'6b\. .*? tabledata .*? 1\.0 .*? tabledata \s 6c\.'],
                          text, points=0.5)
    test6c = exact_answer('question 6 difference',
                          [r'6c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? section'],
                          text, points=0.5)
    test7a = exact_answer('question 7 expected', [r'7a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 7b\.'],
                          text, points=0.5)
    test7b = exact_answer('question 7 actual', [r'7b\. .*? tabledata \s error .*? tabledata \s 7c\.'],
                          text, points=0.5)
    test7c = exact_answer('question 7 difference',
                          [r'7c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 8a\.'],
                          text, points=0.5)
    test8a = exact_answer('question 8 expected', [r'8a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 8b\.'],
                          text, points=0.5)
    test8b = exact_answer('question 8 actual', [r'8b\. .*? tabledata \s a .*? tabledata \s 8c\.'],
                          text, points=0.5)
    test8c = exact_answer('question 8 difference',
                          [r'8c\. .*? tabledata \s [a-zA-Z0-9] .*? section'],
                          text, points=0.5)
    test9a = exact_answer('question 9 expected', [r'9a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 9b\.'],
                          text, points=0.5)
    test9b = exact_answer('question 9 actual', [r'9b\. .*? tabledata \s a \s* \+ \s* b .*? tabledata \s 9c\.'],
                          text, points=0.5)
    test9c = exact_answer('question 9 difference',
                          [r'9c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 10a\.'],
                          text, points=0.5)
    test10a = exact_answer('question 10 expected', [r'10a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 10b\.'],
                          text, points=0.5)
    test10b = exact_answer('question 10 actual', [r'10b\. .*? tabledata \s ab .*? tabledata \s 10c\.'],
                          text, points=0.5)
    test10c = exact_answer('question 10 difference', [r'10c\. .*? tabledata \s [a-zA-Z0-9] .*? section'],
                          text, points=0.5)
    test11a = exact_answer('question 11 expected', [r'11a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 11b\.'],
                           text, points=0.5)
    test11b = exact_answer('question 11 actual', [r'11b\. .*? tabledata \s error .*? tabledata \s 11c\.'],
                           text, points=0.5)
    test11c = exact_answer('question 11 difference',
                           [r'11c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 12a\.'],
                           text, points=0.5)
    test12a = exact_answer('question 12 expected', [r'12a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 12b\.'],
                           text, points=0.5)
    test12b = exact_answer('question 12 actual', [r'12b\. .*? tabledata \s aa .*? tabledata \s 12c\.'],
                           text, points=0.5)
    test12c = exact_answer('question 12 difference',
                           [r'12c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s .*? part'],
                           text, points=0.5)
    test13a = exact_answer('question 13 expected datatype',
                           [r'13a\. .*? tabledata .*? (integer|float|string|error) .*? tabledata \s 13b\.'],
                           text, points=0.5)
    test14a = exact_answer('question 14 expected datatype',
                           [r'14a\. .*? tabledata .*? (integer|float|string|error) .*? tabledata \s 14b\.'],
                           text, points=0.5)
    test15a = exact_answer('question 15 expected datatype',
                           [r'15a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 15b\.'],
                           text, points=0.5)
    test16a = exact_answer('question 16 expected datatype',
                           [r'16a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 16b\.'],
                           text, points=0.5)
    test17a = exact_answer('question 17 expected datatype',
                           [r'17a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 17b\.'],
                           text, points=0.5)
    test18a = exact_answer('question 18 expected datatype',
                           [r'18a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 18b\.'],
                           text, points=0.5)
    test19a = exact_answer('question 19 expected datatype',
                           [r'19a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 19b\.'],
                           text, points=0.5)
    test20a = exact_answer('question 20 expected datatype',
                           [r'20a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 20b\.'],
                           text, points=0.5)
    test21a = exact_answer('question 21 expected datatype',
                           [r'21a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 21b\.'],
                           text, points=0.5)
    test22a = exact_answer('question 22 expected datatype',
                           [r'22a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 22b\.'],
                           text, points=0.5)
    test23a = exact_answer('question 23 expected datatype',
                           [r'23a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 23b\.'],
                           text, points=0.5)
    test24a = exact_answer('question 24 expected datatype',
                           [r'24a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 24b\.'],
                           text, points=0.5)
    test25a = exact_answer('question 25 expected datatype',
                           [r'25a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 25b\.'],
                           text, points=0.5)
    test26a = exact_answer('question 26 expected datatype',
                           [r'26a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 26b\.'],
                           text, points=0.5)
    test13b = exact_answer('question 13 expected', [r'13b\. .*? tabledata .*? [a-zA-Z0-9] .+ tabledata \s 13c\.'],
                           text, points=0.5)
    test14b = exact_answer('question 14 expected', [r'14b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 14c\.'],
                           text, points=0.5)
    test15b = exact_answer('question 15 expected', [r'15b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 15c\.'],
                           text, points=0.5)
    test16b = exact_answer('question 16 expected', [r'16b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 16c\.'],
                           text, points=0.5)
    test17b = exact_answer('question 17 expected', [r'17b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 17c\.'],
                           text, points=0.5)
    test18b = exact_answer('question 18 expected', [r'18b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 18c\.'],
                           text, points=0.5)
    test19b = exact_answer('question 19 expected', [r'19b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 19c\.'],
                           text, points=0.5)
    test20b = exact_answer('question 20 expected', [r'20b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 20c\.'],
                           text, points=0.5)
    test21b = exact_answer('question 21 expected', [r'21b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 21c\.'],
                           text, points=0.5)
    test22b = exact_answer('question 22 expected', [r'22b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 22c\.'],
                           text, points=0.5)
    test23b = exact_answer('question 23 expected', [r'23b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 23c\.'],
                           text, points=0.5)
    test24b = exact_answer('question 24 expected', [r'24b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 24c\.'],
                           text, points=0.5)
    test25b = exact_answer('question 25 expected', [r'25b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 25c\.'],
                           text, points=0.5)
    test26b = exact_answer('question 26 expected', [r'26b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 26c\.'],
                           text, points=0.5)
    test13c = exact_answer('question 13 actual',
                           [r'13c\. .*? tabledata .*?  5\.0 .*? tabledata \s 14a\.'],
                           text, points=0.5)
    test14c = exact_answer('question 14 actual',
                           [r'14c\. .*? tabledata \s  0 .*? tabledata \s 15a\.'],
                           text, points=0.5)
    test15c = exact_answer('question 15 actual',
                           [r'15c\. .*? tabledata \s  8 .*? tabledata \s 16a\.'],
                           text, points=0.5)
    test16c = exact_answer('question 16 actual',
                           [r'16c\. .*? tabledata \s  21 .*? tabledata \s 17a\.'],
                           text, points=0.5)
    test17c = exact_answer('question 17 actual',
                           [r'17c\. .*? tabledata \s  17 .*? tabledata \s 18a\.'],
                           text, points=0.5)
    test18c = exact_answer('question 18 actual',
                           [r'18c\. .*? tabledata \s  ab123 .*? tabledata \s 19a\.'],
                           text, points=0.5)
    test19c = exact_answer('question 19 actual',
                           [r'19c\. .*? tabledata .*?  error .*? tabledata \s 20a\.'],
                           text, points=0.5)
    test20c = exact_answer('question 20 actual',
                           [r'20c\. .*? tabledata \s  abcd .*? tabledata \s 21a\.'],
                           text, points=0.5)
    test21c = exact_answer('question 21 actual',
                           [r'21c\. .*? tabledata \s  abcabc .*? tabledata \s 22a\.'],
                           text, points=0.5)
    test22c = exact_answer('question 22 actual',
                           [r'22c\. .*? tabledata \s 11222 .*? tabledata \s 23a\.'],
                           text, points=0.5)
    test23c = exact_answer('question 23 actual',
                           [r'23c\. .*? tabledata \s error .*? tabledata \s 24a\.'],
                           text, points=0.5)
    test24c = exact_answer('question 24 actual',
                           [r'24c\. .*? tabledata \s error .*? tabledata \s 25a\.'],
                           text, points=0.5)
    test25c = exact_answer('question 25 actual',
                           [r'25c\. .*? tabledata \s error .*? tabledata \s 26a\.'],
                           text, points=0.5)
    test26c = exact_answer('question 26 actual',
                           [r'26c\. .*? tabledata \s error .*? $'],
                           text, points=0.5)
    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test3a, test3b, test3c, test4a, test4b, test4c,
                  test5a, test5b, test5c, test6a, test6b, test6c, test7a, test7b, test7c, test8a, test8b, test8c,
                  test9a, test9b, test9c, test10a, test10b, test10c, test11a, test11b, test11c,
                  test12a, test12b, test12c, test13a, test13b, test13c, test14a, test14b, test14c, test15a, test15b,
                  test15c, test16a, test16b, test16c, test17a, test17b, test17c, test18a, test18b, test18c, test19a,
                  test19b, test19c, test20a, test20b, test20c, test21a, test21b, test21c, test22a, test22b, test22c,
                  test23a, test23b, test23c, test24a, test24b, test24c, test25a,
                  test25b, test25c, test26a, test26b, test26c, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_1030')
def docs_feedback_python_1030():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 29.5, 'manually_scored': 8, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('question 1a expected',
                         [r'1a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 1b\.\n'],
                         text, points=0.5)
    test2a = exact_answer('question 2a expected',
                         [r'2a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 2b\.\n'],
                         text, points=0.5)
    test3a = exact_answer('question 3a expected',
                         [r'3a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 3b\.\n'],
                         text, points=0.5)
    test4a = exact_answer('question 4a expected',
                         [r'4a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 4b\.\n'],
                         text, points=0.5)
    test5a = exact_answer('question 5a expected',
                         [r'5a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 5b\.\n'],
                         text, points=0.5)
    test1b = exact_answer('question 1b actual', [r'1b\. \n+ tabledata \s  1 .+? tabledata \s 1c\.\n'],
                          text, points=0.5)
    test2b = exact_answer('question 2b actual', [r'2b\. \n+ tabledata \s  1 .+? tabledata \s 2c\.\n'],
                          text, points=0.5)
    test3b = exact_answer('question 3b actual', [r'3b\. \n+ tabledata \s  3 .+? tabledata \s 3c\.\n'],
                          text, points=0.5)
    test4b = exact_answer('question 4b actual', [r'4b\. \n+ tabledata \s  12 .+? tabledata \s 4c\.\n'],
                          text, points=0.5)
    test5b = exact_answer('question 5b actual',
                          [r'5b\. \n+ tabledata \s  this \s is \s a \s sentence\. .+? tabledata \s 5c\.\n'],
                          text, points=0.5)
    test1c = exact_answer('question 1c different', [r'1c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 2a\.\n'],
                          text, points=0.5)
    test2c = exact_answer('question 2c different', [r'2c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 3a\.\n'],
                          text, points=0.5)
    test3c = exact_answer('question 3c different', [r'3c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 4a\.\n'],
                          text, points=0.5)
    test4c = exact_answer('question 4c different', [r'4c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 5a\.\n'],
                          text, points=0.5)
    test5c = exact_answer('question 5c different', [r'5c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? part'],
                          text, points=0.5)
    test6a = exact_answer('question 6a', [r'6a\. .+? \n+ tabledata \s dogs \s are \s really \s cool .+? 6b\.'],
                          text, points=5)
    test7a = exact_answer('question 7a', [r'7a\. .+? \n+ tabledata \s error .+? 7b\.'],
                          text, points=5)
    test6b = keyword_and_length('question 6b', [r'[a-zA-Z]+'], text,
                                search_string=r'6b\. .+? tabledata (.+?) type', min_length=4, points=1)
    test7b = keyword_and_length('question 7b', [r'[a-zA-Z]+'], text,
                                search_string=r'7b\. .+? tabledata (.+?) [wW]rite', min_length=5, points=1)
    test8a = exact_answer('question 8a', [r'8\. .+? tabledata .+? number \s* = \s* 100 .+? create\sa\svariable'],
                          text, points=2.5)
    test8b = exact_answer('question 8b', [r'8\. .+? tabledata .+? print \s* \(number\) .+? create\sa\svariable'],
                          text, points=2.5)
    test8c = exact_answer('question 8c', [r'8\. .+? tabledata .+? number2 .+? 100 .+? create\sa\svariable'],
                          text, points=2.5)
    test8d = exact_answer('question 8d', [r'8\. .+? tabledata .+? print \s* \(number2\) .+? create\sa\svariable'],
                          text, points=2.5)

    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test3a, test3b, test3c, test4a, test4b, test4c,
                  test5a, test5b, test5c, test6a, test6b, test7a, test7b, test8a, test8b, test8c, test8d])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_2020')
def docs_feedback_python_2020():
    from app.docs_labs.docs import get_text, exact_answer

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 14, 'manually_scored': 0, 'finished_scoring': True}
    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('1a expected', [r'1a\. .+? tabledata \s* [0-9a-zA-Z] .+? 1b\.'], text, points=1)
    test1b = exact_answer('1b expected', [r'1b\. .+? tabledata \s* 1\.0 \s* tabledata .+? 2a\.'], text, points=1)
    test2a = exact_answer('2a expected', [r'2a\. .+? tabledata \s* [0-9a-zA-Z] .+? 2b\.'], text, points=1)
    test2b = exact_answer('2b expected', [r'2b\. .+? tabledata \s* error \s* tabledata .+? 3a\.'], text, points=1)
    test3a = exact_answer('3a expected', [r'3a\. .+? tabledata \s* [0-9a-zA-Z] .+? 3b\.'], text, points=1)
    test3b = exact_answer('3b expected', [r'2b\. .+? tabledata \s* 2 \s* tabledata .+? 4a\.'], text, points=1)
    test4a = exact_answer('4a expected', [r'4a\. .+? tabledata \s* [0-9a-zA-Z] .+? 4b\.'], text, points=1)
    test4b = exact_answer('4b expected', [r'4b\. .+? tabledata \s* error \s* tabledata .+? 5a\.'], text, points=1)
    test5a = exact_answer('5a expected', [r'5a\. .+? tabledata \s* [0-9a-zA-Z] .+? 5b\.'], text, points=1)
    test5b = exact_answer('5b expected', [r'5b\. .+? tabledata \s* 1 \s* tabledata .+? 6a\.'], text, points=1)
    test6a = exact_answer('6a expected', [r'6a\. .+? tabledata \s* [0-9a-zA-Z] .+? 6b\.'], text, points=1)
    test6b = exact_answer('6b expected', [r'6b\. .+? tabledata \s* 1\.0 \s* tabledata .+? 7a\.'], text, points=1)
    test7a = exact_answer('7a expected', [r'7a\. .+? tabledata \s* [0-9a-zA-Z] .+? 7b\.'], text, points=1)
    test7b = exact_answer('7b expected', [r'7b\. .+? tabledata \s* 1\.0 \s* .+? $'], text, points=1)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test5b, test6a, test6b,
                  test7a, test7b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_2021')
def docs_feedback_python_2021():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Python Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 14, 'manually_scored': 0, 'finished_scoring': True}
    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('1a expected', [r'1a\. .+? tabledata \s* [0-9a-zA-Z] .+? 1b\.'], text, points=1)
    test1b = exact_answer('1b expected', [r'1b\. .+? tabledata \s* 1\.0 \s* tabledata .+? 2a\.'], text, points=1)
    test2a = exact_answer('2a expected', [r'2a\. .+? tabledata \s* [0-9a-zA-Z] .+? 2b\.'], text, points=1)
    test2b = exact_answer('2b expected', [r'2b\. .+? tabledata \s* error \s* tabledata .+? 3a\.'], text, points=1)
    test3a = exact_answer('3a expected', [r'3a\. .+? tabledata \s* [0-9a-zA-Z] .+? 3b\.'], text, points=1)
    test3b = exact_answer('3b expected', [r'2b\. .+? tabledata \s* 2 \s* tabledata .+? 4a\.'], text, points=1)
    test4a = exact_answer('4a expected', [r'4a\. .+? tabledata \s* [0-9a-zA-Z] .+? 4b\.'], text, points=1)
    test4b = exact_answer('4b expected', [r'4b\. .+? tabledata \s* error \s* tabledata .+? 5a\.'], text, points=1)
    test5a = exact_answer('5a expected', [r'5a\. .+? tabledata \s* [0-9a-zA-Z] .+? 5b\.'], text, points=1)
    test5b = exact_answer('5b expected', [r'5b\. .+? tabledata \s* 1 \s* tabledata .+? 6a\.'], text, points=1)
    test6a = exact_answer('6a expected', [r'6a\. .+? tabledata \s* [0-9a-zA-Z] .+? 6b\.'], text, points=1)
    test6b = exact_answer('6b expected', [r'6b\. .+? tabledata \s* 1\.0 \s* tabledata .+? 7a\.'], text, points=1)
    test7a = exact_answer('7a expected', [r'7a\. .+? tabledata \s* [0-9a-zA-Z] .+? 7b\.'], text, points=1)
    test7b = exact_answer('7b expected', [r'7b\. .+? tabledata \s* 1\.0 \s* .+? $'], text, points=1)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test5b, test6a, test6b,
                  test7a, test7b, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_2032')
def docs_feedback_python_2032():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 12, 'manually_scored': 0, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a ', [r'1a\. .+? tabledata \s* (true|false) .+? 1b\.'], text, points=0.5)
    test1b = exact_answer('1b ', [r'1b\. .+? tabledata \s* true \s* tabledata .+? 2a\.'], text, points=0.5)
    test2a = exact_answer('2a ', [r'2a\. .+? tabledata \s* (true|false) .+? 2b\.'], text, points=0.5)
    test2b = exact_answer('1b ', [r'2b\. .+? tabledata \s* false \s* tabledata .+? 3a\.'], text, points=0.5)
    test3a = exact_answer('3a ', [r'3a\. .+? tabledata \s* (true|false) .+? 3b\.'], text, points=0.5)
    test3b = exact_answer('3b ', [r'3b\. .+? tabledata \s* true \s* tabledata .+? 4a\.'], text, points=0.5)
    test4a = exact_answer('4a ', [r'4a\. .+? tabledata \s* (true|false) .+? 4b\.'], text, points=0.5)
    test4b = exact_answer('4b ', [r'4b\. .+? tabledata \s* false \s* .+? check'], text, points=0.5)
    test5a = exact_answer('5a ', [r'5a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test6a = exact_answer('6a ', [r'6a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test7a = exact_answer('7a ', [r'7a\. .+? tabledata \s* true \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test8a = exact_answer('8a ', [r'8a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test9a = exact_answer('9a ', [r'9a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test10a = exact_answer('10a ', [r'10a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test11a = exact_answer('11a ', [r'11a\. .+? tabledata \s* false \s* .+? tabledata .+? 6a\.'], text, points=0.5)
    test12a = exact_answer('12a ', [r'12a\. .+? tabledata \s* false \s* .+?  program'], text, points=0.5)
    test13a = exact_answer('13a ', [r'13a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 13b\.'], text, points=0.1)
    test14a = exact_answer('14a ', [r'14a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 14b\.'], text, points=0.1)
    test15a = exact_answer('15a ', [r'15a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 15b\.'], text, points=0.1)
    test16a = exact_answer('16a ', [r'16a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 16b\.'], text, points=0.1)
    test17a = exact_answer('17a ', [r'17a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 17b\.'], text, points=0.1)
    test18a = exact_answer('18a ', [r'18a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 18b\.'], text, points=0.1)
    test19a = exact_answer('19a ', [r'19a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 19b\.'], text, points=0.1)
    test20a = exact_answer('20a ', [r'20a\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 20b\.'], text, points=0.1)
    test13b = exact_answer('13b ', [r'13b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 13c\.'], text, points=0.1)
    test14b = exact_answer('14b ', [r'14b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 14c\.'], text, points=0.1)
    test15b = exact_answer('15b ', [r'15b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 15c\.'], text, points=0.1)
    test16b = exact_answer('16b ', [r'16b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 16c\.'], text, points=0.1)
    test17b = exact_answer('17b ', [r'17b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 17c\.'], text, points=0.1)
    test18b = exact_answer('18b ', [r'18b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 18c\.'], text, points=0.1)
    test19b = exact_answer('19b ', [r'19b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 19c\.'], text, points=0.1)
    test20b = exact_answer('20b ', [r'20b\. .+? tabledata \s* [0-9]+ \s* .+? tabledata .+? 20c\.'], text, points=0.1)
    test13c = exact_answer('13c ', [r'13c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 14a\.'], text, points=0.3)
    test14c = exact_answer('14c ', [r'14c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 15a\.'], text, points=0.3)
    test15c = exact_answer('15c ', [r'15c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 16a\.'], text,
                           points=0.3)
    test16c = exact_answer('16c ', [r'16c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 17a\.'], text,
                           points=0.3)
    test17c = exact_answer('17c ', [r'17c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 18a\.'], text,
                           points=0.3)
    test18c = exact_answer('18c ', [r'18c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 19a\.'], text,
                           points=0.3)
    test19c = exact_answer('19c ', [r'19c\. .+? tabledata \s* (true|false) \s* .+? tabledata .+? 20a\.'], text,
                           points=0.3)
    test20c = exact_answer('20c ', [r'20c\. .+? tabledata \s* (true|false) \s* .+? $'], text,
                           points=0.3)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test6a, test7a, test8a,
                  test9a, test10a, test11a, test12a, test13a, test13b, test13c, test14a, test14b, test14c, test15a,
                  test15b, test15c, test16a, test16b, test16c, test17a, test17b, test17c, test18a, test18b, test18c,
                  test19a, test19b, test19c, test20a, test20b,test20c])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_2040')
def docs_feedback_python_2040():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 8, 'manually_scored': 0, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a ', [r'1a\. .+? tabledata \s* pretty \s good \s grade .+? tabledata .+? 2a\.'], text, points=2)
    test2a = exact_answer('2a ', [r'2a\. .+? tabledata \s*  .+? tabledata .+? 3a\.'], text, points=3)
    test3a = exact_answer('3a ', [r'3a\. .+? tabledata \s* .+? Chec'], text, points=3)

    tests.extend([test1a, test2a, test3a])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/python_2050')
def docs_feedback_python_2050():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 8, 'manually_scored': 0, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a ', [r'1a\. .+? tabledata \s* [a-zA-Z] .+? tabledata .+? 1b\.'], text, points=1)
    test2a = exact_answer('2a ', [r'2a\. .+? tabledata \s* [a-zA-Z] .+? tabledata .+? 2b\.'], text, points=1)
    test3a = exact_answer('3a ', [r'3a\. .+? tabledata \s* [a-zA-Z] .+? tabledata .+? 3b\.'], text, points=1)
    test4a = exact_answer('4a ', [r'4a\. .+? tabledata .+? [a-zA-Z] .+? tabledata .+? 4b\.'], text, points=1)
    test1b = exact_answer('1b ', [r'1b\. .+? tabledata \s* a \s* d \s* .+? tabledata .+? 2a\.'], text, points=1)
    test2b = exact_answer('2b ', [r'2b\. .+? tabledata \s* c .+? tabledata .+? 3a\.'], text, points=1)
    test3b = exact_answer('3b ', [r'3b\. .+? tabledata \s* e .+? tabledata .+? 4a\.'], text, points=1)
    test4b = exact_answer('4b ', [r'4b\. .+? tabledata .+? a .+? b.+? c .+? haha .+? e .+? check'], text, points=1)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_routers_and_redundancy')
def docs_feedback_routers_and_redundancy():
    from app.docs_labs.docs import get_text, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 11, 'manually_scored': 39, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)
    test1 = keyword_and_length('question 1', [r'[a-zA-Z]+'], text,
                               search_string=r'1. .+? tabledata (.+) 2.', min_length=1,
                               points=1)
    test2 = keyword_and_length('question 2', [r'[a-zA-Z]+'], text,
                               search_string=r'2. .+? tabledata (.+) 3.', min_length=5,
                               points=1)
    test3 = keyword_and_length('question 3', [r'[a-zA-Z]+'], text,
                               search_string=r'3. .+? tabledata (.+) 4.', min_length=1,
                               points=1)
    test4 = keyword_and_length('question 4', [r'[a-zA-Z]+'], text,
                               search_string=r'4\. .+? tabledata (.+?) ind', min_length=10,
                               points=1)
    test5 = keyword_and_length('question 5', [r'[a-zA-Z]+'], text,
                               search_string=r'5. .+? tabledata (.+) 6.', min_length=1,
                               points=1)
    test6 = keyword_and_length('question 6', [r'[a-zA-Z]+'], text,
                               search_string=r'6. .+? tabledata (.+) 7.', min_length=7,
                               points=1)
    test7 = keyword_and_length('question 7', [r'[a-zA-Z]+'], text,
                               search_string=r'7. .+? tabledata (.+) 8.', min_length=1,
                               points=1)
    test8 = keyword_and_length('question 8', [r'[a-zA-Z]+'], text,
                               search_string=r'8. .+? tabledata (.+) 9.', min_length=5,
                               points=1)
    test9 = keyword_and_length('question 9', [r'[a-zA-Z]+'], text,
                               search_string=r'9. .+? tabledata (.+) 10a.', min_length=5,
                               points=1)
    test10a = keyword_and_length('question 10a', [r'[a-zA-Z]+'], text,
                                 search_string=r'10a. .+? tabledata (.+) 10b.', min_length=5,
                                 points=1)
    test10b = keyword_and_length('question 10b', [r'[a-zA-Z]+'], text,
                                 search_string=r'10b. .+? tabledata (.+) $', min_length=10,
                                 points=1)

    tests.extend([test1, test2, test3, test4, test5, test6, test7, test8, test9, test10a, test10b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_scratch_25_alternate')
def docs_feedback_scratch_25_alternate():
    from app.docs_labs.docs import get_text, exact_answer

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 12, 'manually_scored': 0, 'finished_scoring': True}

    print(request.args)
    link = request.args['link']
    text = get_text(link)
    print(text)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 1b'], text, points=1)
    test1b = exact_answer('question 1b', [r'1b .+? tabledata \s*  (false|False|f|F) \s* tabledata \s 1c'], text, points=1)
    test1c = exact_answer('question 1c', [r'1c .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 1d'], text, points=1)
    test1d = exact_answer('question 1d', [r'1d .+? tabledata \s*  (true|True|t|T) \s* Fill '], text, points=1)
    test2a = exact_answer('question 2a', [r'2a .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 2b'], text, points=1)
    test2b = exact_answer('question 2b', [r'2b .+? tabledata \s*  (false|False|f|F) \s* tabledata \s 2c'], text, points=1)
    test2c = exact_answer('question 2c', [r'2c .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 2d'], text, points=1)
    test2d = exact_answer('question 2d', [r'2d .+? tabledata \s*  (false|False|f|F) \s* Fill '], text, points=1)
    test3a = exact_answer('question 2a', [r'3a .+? tabledata \s*  (false|False|f|F) \s* tabledata \s 3b'], text, points=1)
    test3b = exact_answer('question 2b', [r'3b .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 3c'], text, points=1)
    test3c = exact_answer('question 2c', [r'3c .+? tabledata \s*  (true|True|t|T) \s* tabledata \s 3d'], text, points=1)
    test3d = exact_answer('question 2d', [r'3d .+? tabledata \s*  (true|True|t|T) \s*  '], text, points=1)

    tests.extend([test1a, test1b, test1c, test1d, test2a, test2b, test2c, test2d, test3a, test3b, test3c, test3d])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/docs_feedback_scratch_12')
def docs_feedback_scratch_12():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scratch Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 38, 'manually_scored': 12, 'finished_scoring': True}

    print(request.args)
    link = request.args['link']
    text = get_text(link)
    print(text)
    test1b2 = exact_answer('question 1 b2', [r'b\.aaa \s inlineobject\ntabledata?\s*looks?'], text, points=1)
    test1b3 = keyword_and_length('question 1 b3', ['say', 'seconds', 'time', 'text', 'bubble', 'speak',], text,
                                 search_string=r'b\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1c2 = exact_answer('question 1 c2', [r'c\.aaa \s inlineobject\ntabledata?\s*sound?'], text, points=1)
    test1c3 = keyword_and_length('question 1 c3', ['play', 'sound', 'meow', 'noise'], text,
                                 search_string=r'c\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1d2 = exact_answer('question 1 d2', [r'd\.aaa \s inlineobject\ntabledata?\s*looks?'], text, points=1)
    test1d3 = keyword_and_length('question 1 d3', ['costume', 'switch', 'look', 'appear'], text,
                                 search_string=r'd\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1e2 = exact_answer('question 1 e2', [r'e\.aaa \s inlineobject\ntabledata?\s*motion?'], text, points=1)
    test1e3 = keyword_and_length('question 1 e3', ['move', 'glide', 'location', 'smooth', 'slow', 'position', 'slide'], text,
                                 search_string=r'e\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1f2 = exact_answer('question 1 f2', [r'f\.aaa \s inlineobject\ntabledata?\s*looks?'], text, points=1)
    test1f3 = keyword_and_length('question 1 f3', ['size', 'change', 'size',], text,
                                 search_string=r'f\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1g2 = exact_answer('question 1 g2', [r'g\.aaa \s inlineobject\ntabledata?\s*control?'], text, points=1)
    test1g3 = keyword_and_length('question 1 g3', ['repeat', 'control', ], text,
                                 search_string=r'g\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1h2 = exact_answer('question 1 h2', [r'h\.aaa \s inlineobject\ntabledata?\s*looks?'], text, points=1)
    test1h3 = keyword_and_length('question 1 h3', ['color', 'sprite', 'change', ], text,
                                 search_string=r'h\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1i2 = exact_answer('question 1 i2', [r'i\.aaa \s inlineobject\ntabledata?\s*motion?'], text, points=1)
    test1i3 = keyword_and_length('question 1 i3', ['move', 'go', 'location', 'position','appear', 'teleport',  ], text,
                                 search_string=r'i\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1j2 = exact_answer('question 1 j2', [r'j\.aaa \s inlineobject\n.+?tabledata?\s*pen?'], text, points=1)
    test1j3 = keyword_and_length('question 1 j3', ['pen', 'change', 'size', ], text,
                                 search_string=r'j\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata\sk', points=1)
    test1k2 = exact_answer('question 1 k2', [r'k\.aaa \s inlineobject\ntabledata?\s*pen?'], text, points=1)
    test1k3 = keyword_and_length('question 1 k3', ['pen', 'change', 'color', 'set'], text,
                                 search_string=r'k\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata\sl', points=1)
    test1l2 = exact_answer('question 1 l2', [r'l\.aaa \s inlineobject\ntabledata?\s*motion?'], text, points=1)
    test1l3 = keyword_and_length('question 1 l3', ['point', 'sprite', 'mouse'], text,
                                 search_string=r'l\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)2', points=1)
    test2a = keyword_and_length('question 2a', ['motion', 'move', 'moving', 'category', 'speed', 'way', 'blocks',
                                                'glide', 'turn', 'go', 'set', 'sprite', 'left', 'right'], text,
                                search_string=r'tabledata\sa\.\swhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'motion\scategory\sdo\?\s+you\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=1)
    test2b = keyword_and_length('question 2b', ['look', 'appear', 'effect', 'talk', 'say', 'disappear',
                                                'category', 'blocks', 'costume',
                                                'set', 'sprite'], text,
                                search_string=r'tabledata\sb\.\swhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'looks\scategory\sdo\?\s+you\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=1)
    test2c = keyword_and_length('question 2c', ['noise', 'sound', 'music', 'effect', 'cat', 'meow',
                                                'category', 'blocks',
                                                'set', 'sprite'], text,
                                search_string=r'tabledata\sc\.\swhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'sound\scategory\sdo\?\s+you\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=1)
    test2d = keyword_and_length('question 2d', ['tools', 'pen', 'thickness', 'color', 'size', 'erase', 'clear', 'draw'
                                                'sprite'], text,
                                search_string=r'tabledata\sd\.\swhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'pen\scategory\sdo\?\s+you\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+)',
                                points=4, min_matches=1)
    tests.extend([test1b2, test1b3, test1c2, test1c3, test1d2, test1d3, test1e2, test1e3, test1f2, test1f3, test1g2,
                  test1g3, test1h2, test1h3, test1i2, test1i3, test1j2, test1j3, test1k2, test1k3, test1l2, test1l3,
                  test2a, test2b, test2c, test2d])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/recon_network_protocols_revisited')
def docs_feedback_recon_network_protocols_revisited():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 27, 'manually_scored': 73, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Ping machine',
                          [r'1a\. .+? tabledata .*? pinging .*? 1b\.',
                           r'1a\. .+? tabledata .*? reply .*? 1b\.'], text, points=5)
    test1b = exact_answer('1b. Ping africa.mit.edu',
                          [r'1b\. .+? tabledata .*? pinging .*? tracert',
                           r'1b\. .+? tabledata .*? request \s time \s out .*? tracert'], text, points=5)
    test2a = exact_answer('2a. tracert',
                          [r'2a\. .+? tabledata .+? hops .+? 4b\.',
                           r'2a\. .+? tabledata .+? ms .+? 4b\.',
                           r'2a\. .+? tabledata .+? tracing .+? 4b\.',
                           ],
                          text, points=5, required=3)
    test2b = keyword_and_length('2b. Explain the tracert?', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+?) 2c\.', min_length=10, points=1)
    test2c = keyword_and_length('2c. tracert on local machine?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) tcp \s and', min_length=7, points=1)
    test3a = keyword_and_length('3a. UDP/TCP table? Must be table.', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata .* tabledata (.+?)  3b\.', min_length=1, points=1)
    test3b = keyword_and_length('3b. explain handshake?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) ports', min_length=8, points=1)
    test4a = exact_answer('4a. http port',
                          [r'4a\. .+? tabledata .*? 80 .*? tabledata .*? 4b\.',], text, points=2)
    test4b = keyword_and_length('4b. http use?', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) tabledata .+? 5a\.', min_length=2, points=1)
    test5a = exact_answer('5a. https port',
                          [r'5a\. .+? tabledata .*? 443 .*? tabledata .*? 5b\.', ], text, points=2)
    test5b = keyword_and_length('5b. https use?', [r'[a-zA-Z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) tabledata .+? 6a\.', min_length=2, points=1)
    test6a = exact_answer('6a. http port',
                          [r'6a\. .+? tabledata .*? 53 .*? tabledata .*? 6b\.', ], text, points=2)
    test6b = keyword_and_length('6b. DNS use?', [r'[a-zA-Z]+'], text,
                                search_string=r'6b\. .+? tabledata (.+?) tabledata .+? 7a\.', min_length=2, points=1)
    test7a = exact_answer('7a. http port',
                          [r'7a\. .+? tabledata .*? 67 .*? tabledata .*? 7b\.', ], text, points=2)
    test7b = keyword_and_length('7b. DHCP use?', [r'[a-zA-Z]+'], text,
                                search_string=r'7b\. .+? tabledata (.+?) tabledata .+? 8a\.', min_length=2, points=1)
    test8a = exact_answer('8a. http port',
                          [r'8a\. .+? tabledata .*? 3389 .*? tabledata .*? 8b\.', ], text, points=2)
    test8b = keyword_and_length('8b. RDP use?', [r'[a-zA-Z]+'], text,
                                search_string=r'8b\. .+? tabledata (.+?) netstat', min_length=2, points=1)
    test9a = exact_answer('9a. netstat',
                          [r'9a\. .+? tabledata .+? tcp .+? 9b\.',
                           r'9a\. .+? tabledata .+? established .+? 9b\.',
                           r'9a\. .+? tabledata .+? udp .+? 9b\.',
                           r'9a\. .+? tabledata .+? connections .+? 9b\.',
                           ],
                          text, points=15, required=3)
    test9b = keyword_and_length('9b. Ports and their use??', [r'[a-zA-Z]+'], text,
                                search_string=r'9b\. .+? tabledata (.+?) autograder', min_length=10, points=1)

    tests.extend([test1a, test1b, test2a, test2b, test2c, test3a, test3b, test4a, test4b, test5a, test5b,
                  test6a, test6b, test7a, test7b, test8a, test8b, test9a, test9b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/networking_cable_management')
def docs_feedback_networking_cable_management():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 33, 'manually_scored': 42, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. IDF definition?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=7, points=1)
    test1b = keyword_and_length('1b. MDF definition?', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) 1c\.', min_length=7, points=1)
    test1c = keyword_and_length('1c. Demarc definition?', [r'[a-zA-Z]+'], text,
                                search_string=r'1c\. .+? tabledata (.+?) server \s racking', min_length=7, points=1)
    test2a = exact_answer('2a. How many servers? 42U rack 1U servers',
                          [r'2a\. .+? tabledata .*? 42  .*? 2b\.', ], text, points=5)
    test2b = keyword_and_length('2b. Show work for 2a?', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+?) 2c\.', min_length=7, points=1)
    test2c = exact_answer('2c. How many servers? 42U rack 1U servers + PDUs',
                          [r'2c\. .+? tabledata .*? 36  .*? 2d\.', ], text, points=5)
    test2d = keyword_and_length('2d. Show work for 2c?', [r'[a-zA-Z]+'], text,
                                search_string=r'2d\. .+? tabledata (.+?) 2e\.', min_length=7, points=1)
    test2e = exact_answer('2e. How many servers? 42U rack 1U servers + PDUs + switches',
                          [r'2e\. .+? tabledata .*? 28  .*? 2f\.', ], text, points=5)
    test2f = keyword_and_length('2f. Show work for 2c?', [r'[a-zA-Z]+'], text,
                                search_string=r'2f\. .+? tabledata (.+?) the \s importance \s of', min_length=7,
                                points=1)
    test3a = keyword_and_length('3a. Label machine', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=1, points=5)
    test3b = keyword_and_length('3b. Label wires', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) mdf \/ idf.', min_length=1, points=5)
    test4a = keyword_and_length('4a. Good about design', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 4b\.', min_length=7, points=1)
    test4b = keyword_and_length('4b. Bad about design', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) check \s your \s work', min_length=10,
                                points=1)
    tests.extend(
        [test1a, test1b, test1c, test2a, test2b, test2c, test2d, test2e, test2f, test3a, test3b,
         test4a, test4b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/networking_internet_connections')
def docs_feedback_networking_internet_connections():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 33, 'manually_scored': 41, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Drawback of dialup?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=7, points=1)
    test1b = keyword_and_length('1b. Drawback of cable modem?', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) 1c\.', min_length=7, points=1)
    test1c = keyword_and_length('1c. Drawback of dialup?', [r'[a-zA-Z]+'], text,
                                search_string=r'1c\. .+? tabledata (.+?) use \s this \ website', min_length=7, points=1)
    test2a = exact_answer('2a. Area coverage, fiber/cable Adak',
                          [r'2a\. .+? tabledata .*? low  .*? 2b\.', ], text, points=3)
    test2b = exact_answer('2b. Area coverage, fiber/cable Cambridge',
                          [r'2b\. .+? tabledata .*? high  .*? 2c\.', ], text, points=3)
    test2c = exact_answer('2c. Bandwidth, fiber/cable Adak',
                          [r'2c\. .+? tabledata .*? low  .*? 2d\.', ], text, points=3)
    test2d = exact_answer('2d. Bandwidth, fiber/cable Cambridge',
                          [r'2d\. .+? tabledata .*? high  .*? 2e\.', ], text, points=3)
    test2e = exact_answer('2e. Area coverage, satellite Adak',
                          [r'2e\. .+? tabledata .*? high  .*? 2f\.', ], text, points=3)
    test2f = exact_answer('2f. Area coverage, satellite Cambridge',
                          [r'2f\. .+? tabledata .*? high  .*? 2g\.', ], text, points=3)
    test2g = exact_answer('2g. Bandwidth, satellite Adak',
                          [r'2g\. .+? tabledata .*? low  .*? 2h\.', ], text, points=3)
    test2h = exact_answer('2h. Bandwidth, satellite Cambridge',
                          [r'2h\. .+? tabledata .*? high  .*? 2i\.', ], text, points=3)
    test2i = keyword_and_length('2i. Put it all together', [r'[a-zA-Z]+'], text,
                                search_string=r'2i\. .+? tabledata (.+?) quick \s definitions\.', min_length=7,
                                points=1)
    test3a = keyword_and_length('3a. Line of sight', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=7, points=1)
    test3b = keyword_and_length('3b. SLA', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c\.', min_length=7, points=1)
    test3c = keyword_and_length('3c. 3G vs 4G vs 5G', [r'[a-zA-Z]+'], text,
                                search_string=r'3c\. .+? tabledata (.+?) 3d\.', min_length=7, points=1)
    test3d = keyword_and_length('3d. 3G vs 4G vs 5G', [r'[a-zA-Z]+'], text,
                                search_string=r'3d\. .+? tabledata (.+?) 3e\.', min_length=7, points=1)
    test3e = keyword_and_length('3e. 3G vs 4G vs 5G', [r'[a-zA-Z]+'], text,
                                search_string=r'3e\. .+? tabledata (.+?) check \s your \s work', min_length=7, points=1)

    tests.extend(
        [test1a, test1b, test1c, test2a, test2b, test2c, test2d, test2e, test2f, test2g, test2h, test2i, test3a, test3b,
         test3c,
         test3d, test3e])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/networking_network_media')
def docs_feedback_networking_network_media():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 25, 'manually_scored': 75, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Connecting CRLS desktops, type?',
                          [r'1a\. .+? tabledata .*? copper .*? 1b\.', r'1a\. .+? tabledata .*? non .*? 1b\.',
                           r'1a\. .+? tabledata .*? utp .*? 1b\.', ], text, points=2, required=3)
    test1b = keyword_and_length('1b. 1a Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) 1c\.', min_length=7, points=1)
    test1c = exact_answer('1c. Connecting Google computers under floor (<100m), type?',
                          [r'1c\. .+? tabledata .*? copper .*? 1d\.',
                           r'1c\. .+? tabledata .*? plenum .*? 1d\.',
                           r'1c\. .+? tabledata .*? utp .*? 1d\.', ], text, points=2, required=3)
    test1d = keyword_and_length('1d. 1c Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'1d\. .+? tabledata (.+?) 1e\.', min_length=7, points=1)
    test1e = exact_answer('1e. Connecting machines on floor of NYSE (<100m), type?',
                          [r'1e\. .+? tabledata .*? copper .*? 1f\.',
                           r'1e\. .+? tabledata .*? non .*? 1f\.',
                           r'1e\. .+? tabledata .*? stp .*? 1f\.', ], text, points=2, required=3)
    test1f = keyword_and_length('1f. 1e Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'1f\. .+? tabledata (.+?) 1g\.', min_length=7, points=1)
    test1g = exact_answer('1g. Connecting machines in NSA (>100 m)?',
                          [r'1g\. .+? tabledata .*? fibre .*? 1h\.',
                           r'1g\. .+? tabledata .*? plenum .*? 1h\.', ], text, points=2, required=2)
    test1h = keyword_and_length('1h. 1g Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'1h\. .+? tabledata (.+?) 1i\.', min_length=7, points=1)
    test1i = exact_answer('1i. Connecting machines across ocean?',
                          [r'1i\. .+? tabledata .*? fibre .*? 1j\.', ], text, points=2)
    test1j = keyword_and_length('1j. 1i Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'1j\. .+? tabledata (.+?) 1k\.', min_length=7, points=1)
    test1k = exact_answer('1k. Connecting machines between CRLS and library?',
                          [r'1k\. .+? tabledata .*? fibre .*? 1l\.', ], text, points=2, required=1)
    test1l = keyword_and_length('1l. 1k Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'1l\. .+? tabledata (.+?) connectors .*? for \s each \s', min_length=7,
                                points=1)
    test2a = exact_answer('2a. LC-LC',
                          [r'2a\. .+? tabledata .*? aaa \s inlineobject .*? 2b\.', ], text, points=1)
    test2b = exact_answer('2b. SC-LC',
                          [r'2b\. .+? tabledata .*? aaa \s inlineobject .*? 2c\.',], text, points=1)
    test2c = exact_answer('2c. RJ11',
                          [r'2c\. .+? tabledata .*? aaa \s inlineobject .*? 2d\.',], text, points=1)
    test2d = exact_answer('2d. RJ45',
                          [r'2d\. .+? tabledata .*? aaa \s inlineobject .*? troubleshooting',], text, points=1)
    test3a = keyword_and_length('3a. Wired connection is flaky', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=7, points=1)
    test3b = keyword_and_length('3b. Connect two machines via cable no connection', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c\.', min_length=7, points=1)
    test3c = keyword_and_length('3c. 4 floors apard', [r'[a-zA-Z]+'], text,
                                search_string=r'3c\. .+? tabledata (.+?) hardware .*? you \s should', min_length=7, points=1)

    
    tests.extend(
        [test1a, test1b, test1c, test1d, test1e, test1f, test1g, test1h, test1i, test1j, test1k, test1l,
         test2a, test2b, test2c, test2d, test3a, test3b, test3c ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/networking_network_monitoring')
def docs_feedback_networking_network_monitoring():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 21, 'manually_scored': 24, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Explain how network monitoring generated?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=7, points=1)
    test1b = exact_answer('1b. Screenshot network graph',
                          [r'1b\. .+? tabledata .*? aaa \s inlineobject .*? 1c\.',], text, points=1)
    test1c = keyword_and_length('1c. Explain network monitoring graph', [r'[a-zA-Z]+'], text,
                                search_string=r'1c\. .+? tabledata (.+?) analyzing \s data', min_length=7, points=1)
    test2a = exact_answer('2a. Webserver problem??',
                          [r'2a\. .+? tabledata .*? no .*? 2b\.',], text, points=5)
    test2b = keyword_and_length('2b. Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+?) 2c\.', min_length=8, points=1)
    test2c = exact_answer('2c. Victim or cause?',
                          [r'2c\. .+? tabledata .*? cause .*? 2d\.',], text, points=5)
    test2d = keyword_and_length('2d. Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'2d\. .+? tabledata (.+?) 2e\.', min_length=8, points=1)
    test2e = exact_answer('2e. Who is right?',
                          [r'2e\. .+? tabledata .*? wu .*? 2f\.',], text, points=5)

    test2f = keyword_and_length('2f. Why?', [r'[a-zA-Z]+'], text,
                                search_string=r'2f\. .+? tabledata (.+?) check \s that \s you', min_length=8, points=1)
    tests.extend(
        [test1a, test1b, test1c, test2a, test2b, test2c, test2d, test2e, test2f ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/networking_wireless_1')
def docs_feedback_networking_wireless_1():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 66, 'manually_scored': 9, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. 3 latest wireless protocols',
                          [r'1a\. .+? tabledata .*? 802\.11ac .*? 802.11n .*? 802.11g .*? 1b\.', ], text, points=5)
    test1b = exact_answer('1b. 802.11ac max speed Mbps include units,',
                          [r'1b\. .+? tabledata .*? 1300 .*? mb .*? s .*? 1c\.',
                           r'1b\. .+? tabledata .*? 6933 .*? mb .*? s .*? 1c\.'], text, points=5, required=1)
    test1c = exact_answer('1c. 802.11n max speed Mbps, include units,',
                          [r'1c\. .+? tabledata .*? 450 .*? mb .*? s .*? 1d\.',
                           '1c\. .+? tabledata .*? 600 .*? mb .*? s .*? 1d\.',], text, points=5, required=1)
    test1d = exact_answer('1d. 802.11ac max range in feet',
                          [r'1d\. .+? tabledata .*? 115 .*? f .*? 1e\.', ], text, points=5)
    test1e = exact_answer('1e. 802.11n max range in feet',
                          [r'1e\. .+? tabledata .*? 230 .*? f .*? 1f\.', ], text, points=5)
    test1f = exact_answer('1f. 802.11ac frequency',
                          [r'1f\. .+? tabledata .*? 5 .*? ghz .*? 1g\.', ], text, points=5)
    test1g = exact_answer('1g. 802.11n frequency',
                          [r'1g\. .+? tabledata .*? either .*? selecting \s encryption', ], text, points=5)
    test2a = exact_answer('2a. which encryption to use?',
                          [r'2a\. .+? tabledata .*? wpa2 .*? 2b\.', ], text, points=5)
    test2b = exact_answer('2b. AES or TKIP?',
                          [r'2b\. .+? tabledata .*? aes .*? troubleshooting', ], text, points=5)
    test3a = exact_answer('3a. Public Starbucks',
                          [r'3a\. .+? tabledata .*? 1 .*? 6 .*? 3b\.', ], text, points=5)
    test3b = exact_answer('3b. Private Starbucks',
                          [r'3b\. .+? tabledata .*? 1 .*? 3 .*? 5 .*? 6 .*?  3c\.', ], text, points=5)
    test3c = exact_answer('3c. Xfinity',
                          [r'3c\. .+? tabledata .*? 2 .*? 4 .*?  3d\.', ], text, points=5)

    test3d = exact_answer('3d. Chilling',
                          [r'3d\. .+? tabledata .*? 1 .*? 3 .*? 5  .*? 6.*?  services', ], text, points=5)
    test4a = keyword_and_length('4a. Why services off?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) autograder', min_length=8, points=1)

    tests.extend(
        [test1a, test1b, test1c, test1d, test1e, test1f, test1g, test2a, test2b, test3a, test3b, test3c, test3d, test4a,])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/recon_nmap_2')
def docs_feedback_recon_nmap_2():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 73, 'manually_scored': 27, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Explain scan efficient not complete.', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=10, points=1)
    test1b = keyword_and_length('1b. Scenarios where scan could miss machines?', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) nmap \s scanning', min_length=7, points=1)
    test2a = exact_answer('2a. 20 random IP scan, Nmap',
                          [r'2a\. .+? tabledata .*? 20 \s ip \s addresses .*? scanned .*? networks',], text, points=15)
    test3a = exact_answer('3a. IP addresses',
                          [r'3a\. .+? tabledata .*? 172\.25\.233\. .*?  3b\.',], text, points=5)
    test3b = exact_answer('3b. Network address',
                          [r'3b\. .+? tabledata .*? 172\.25\.233\.0 .*?  3c\.',], text, points=5)
    test3c = exact_answer('3c. Range of usable addresses',
                          [r'3c\. .+? tabledata .+? 172\.25\.233\.1 .+? 3d\.',
                           r'3c\. .+? tabledata .+? 172\.25\.233\.254 .+? 3d\.',
                           ],
                          text, points=5, required=2)
    test3d = exact_answer('3d. How many up?',
                          [r'3d\. .+? tabledata .*? 256 \s ip \s addresses .*? hosts \s up .*? 3e\.', ], text, points=19)
    test3e = exact_answer('3e. How many up?',
                          [r'3e\. .+? tabledata .*? 1[0-9][0-9] .*?  3f\.', ], text, points=5)
    test3f = keyword_and_length('3f. Describe services.', [r'[a-zA-Z]+'], text,
                                search_string=r'3f\. .+? tabledata (.+?) more \s networking', min_length=10, points=1)

#  256 IP addresses (256 hosts up)  
    test4a = exact_answer('4a. 10.10.5.2/24 Network address',
                          [r'4a\. .+? tabledata .*? 10\.10\.5\.0 .*? 4b\.', ], text, points=2)
    test4b = exact_answer('4b. 10.10.5.2/24 Usable hosts',
                          [r'4b\. .+? tabledata .*? 254 .*? 4c\.',], text, points=2)
    test4c = exact_answer('4c. 192.168.3.22 / 255.255.240.0 Network address',
                          [r'4c\. .+? tabledata .*? 192\.168\.3\.16 .*? 4d\.', ], text, points=2)
    test4d = exact_answer('4d. 192.168.3.22 / 255.255.240.0 Usable hosts',
                          [r'4d\. .+? tabledata .*? 14 .*? 4e\.',], text, points=2)
    test4e = exact_answer('4e. 172.25.244.9 / 255.255.192.0 Network address',
                          [r'4e\. .+? tabledata .*? 172\.25\.192\.0 .*? 4f\.', ], text, points=2)
    test4f = exact_answer('4f. 172.25.244.9 / 255.255.192.0 Usable hosts',
                          [r'4f\. .+? tabledata .*? 16 ,* 382 .*? 4g\.', ], text, points=2)
    test4g = exact_answer('4g. 2.3.4.5 / 255.0.0.0 Network address',
                          [r'4g\. .+? tabledata .*? 2\.0\.0\.0 .*? 4h\.', ], text, points=2)
    test4h = exact_answer('4h. 2.3.4.5 / 255.0.0.0 Usable hosts',
                          [r'4h\. .+? tabledata .*? 16,*777,*214 .*? autograder', ], text, points=2)

    tests.extend([test1a, test1b, test2a, test3a, test3b, test3c, test3d, test3e, test3f, test4a, test4b,
                  test4c, test4d, test4e, test4f,
                  test4g, test4h])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/recon_nmap_3')
def docs_feedback_recon_nmap_3():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 74, 'manually_scored': 26, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. -sS',
                          [r'1a\. .+? tabledata .*? tcp .*? 1b\.', r'1a\. .+? tabledata .*? syn .*? 1b\.',], text, points=2, required=1)
    test1b = exact_answer('1b. -sU',
                          [r'1b\. .+? tabledata .*? udp .*? 1c\.',], text, points=2, required=1)
    test1c = exact_answer('1c. -v',
                          [r'1c\. .+? tabledata .*? verbose .*? 1d\.',], text, points=2, required=1)
    test1d = exact_answer('1d. --top-ports 1500',
                          [r'1d\. .+? tabledata .*? common .*? 1e\.', '1d\. .+? tabledata .*? popular .*? 1e\.',], text, points=2, required=1)
    test1e = exact_answer('1e. Screenshot of scan',
                          [r'1e\. .+? tabledata .*? starting \s nmap .*? 1f\.',
                           r'1e\. .+? tabledata .*? host \s is \s up .*? 1f\.',
                           r'1e\. .+? tabledata .*? nmap \s done.*? 1f\.'], text, points=5, required=3)
    
    test1f = exact_answer('1f. TCP or UDP longer?',
                          [r'1f\. .+? tabledata .*? udp .*? 1g\.', ], text, points=2, required=1)
    test1g = keyword_and_length('1g. Why UDP or TCP longer?', [r'[a-zA-Z]+'], text,
                                search_string=r'1g\. .+? tabledata (.+?) from \s the', min_length=7, points=1)

    test2a = exact_answer('2a. auth scan, MySQL vulnerability',
                          [r'2a\. .+? tabledata .*? root \s account \s has \s empty \s password .*? 2b\. ', ], text,
                          points=10)
    test2b = exact_answer('2b. auth scan, FTP vulnerability',
                          [r'2b\. .+? tabledata .*? anonymous \s ftp \s login \s allowed .*? 2c\. ', ], text, points=10)
    test2c = keyword_and_length('2c. Why FTP vulnerability bad?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) 2d\.', min_length=7, points=1)
    test2d = exact_answer('2d. What CVE stands for',
                          [r'2d\. .+? tabledata .*? common .*? 2e\.', r'2d\. .+? tabledata .*? vulnerab.*? 2e\.',
                           r'2d\. .+? tabledata .*? exposure .*? 2e\.', ], text, points=5, required=3)
    test2e = exact_answer('2e. 5 vulnerabilities',
                          [r'2e\. .+? tabledata .*? CVE-2011-2523 .*? 2f\.',
                           r'2e\. .+? tabledata .*? CVE-2014-3566 .*? 2f\.',
                           r'2e\. .+? tabledata .*? CVE-2007-6750 .*? 2f\.', ], text, points=10, required=3)
    test2f = keyword_and_length('2f. Research a vulnerability', [r'[a-zA-Z]+'], text,
                                search_string=r'2f\. .+? tabledata (.+?) nmap \s vs', min_length=10, points=1)
    test3a = exact_answer('3a. Firewall up and incoming blocked',
                          [r'3a\. .+? tabledata .*? aaa \s inlineobject .*? 3b\.', ], text, points=5)
    test3b = exact_answer('3b. Firewall logging',
                          [r'3b\. .+? tabledata .*? aaa \s inlineobject .*? 3c\.', ], text, points=5)
    test3c = exact_answer('3c. Verify scan shows in logs',
                          [r'3c\. .+? tabledata .+? drop .+? 3d\.',
                           r'3c\. .+? tabledata .+? udp .+? 3d\.',
                           r'3c\. .+? tabledata .+? tcp .+? 3d\.',
                           r'3c\. .+? tabledata .+? 445 .+? 3d\.',
                           r'3c\. .+? tabledata .+? 172\.25\.233\.[0-9]+ .+? 3d\.',
                          ],
                          text, points=5, required=2)
    test3d = exact_answer('3d. Verify decoy scan shows in logs',
                          [r'3d\. .+? tabledata .+? drop .+? 3e\.',
                           r'3d\. .+? tabledata .+? udp .+? 3e\.',
                           r'3d\. .+? tabledata .+? tcp .+? 3e\.',
                           r'3d\. .+? tabledata .+? 445 .+? 3e\.',
                           r'3d\. .+? tabledata .+? 172\.25\.233\.1 .+? 3e\.',
                          ],
                          text, points=5, required=2)
    test3e = keyword_and_length('3e. What should I look for in logs', [r'[a-zA-Z]+'], text,
                                search_string=r'3e\. .+? tabledata (.+?) check \s your \s work', min_length=10, points=1)

    tests.extend([test1a, test1b, test1c, test1d, test1e, test1f, test1g,  test2a, test2b, test2c, test2d, test2e, test2f,
                  test3a, test3b, test3c, test3d, test3e, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/recon_passive_recon')
def docs_feedback_recon_passive_recon():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 50, 'manually_scored': 50, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Advantage/disadvantage of passive recon', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=10, points=1)
    test1b = keyword_and_length('1b. Contact info exploited by bad entities', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) google', min_length=7, points=1)
    test2a = keyword_and_length('2a. Google as passive recon', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+?) whois', min_length=10, points=1)
    test3a = keyword_and_length('3a. whois as passive recon', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) netcraft', min_length=10, points=1)
    test4a = keyword_and_length('4a. whois as passive recon', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) censys\.io', min_length=10, points=1)
    test5a = keyword_and_length('5a. What is heartbleed', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) 5b.', min_length=7, points=1)
    test5b = exact_answer('5b. screenshot censys.io heartbleed',
                          [r'5b\. .+? tabledata \s aaa \s inlineobject .+? 5c\.'], text, points=5)
    test5c = exact_answer('5c. Fix heartbleed, how?',
                          [r'5c\. .+? tabledata .+? update .+? 5d\.',
                           r'5c\. .+? tabledata .+? patch .+? 5d\.',
                           r'5c\. .+? tabledata .+? ssl .+? 5d\.',
                           ],
                          text, points=5, required=1)
    test5a = keyword_and_length('5a. What is heartbleed', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) 5b.', min_length=7, points=1)
    test5b = exact_answer('5b. screenshot censys.io heartbleed',
                          [r'5b\. .+? tabledata \s aaa \s inlineobject .+? 5c\.'], text, points=5)
    test5c = keyword_and_length('5c. Fix heartbleed, how?', [r'update', r'patch', r'ssl', ], text,
                                search_string=r'5c\. .+? tabledata (.+?) 5d.', min_length=7, points=5, min_matches=1)
    test5d = keyword_and_length('5d. What is heartbleed', [r'[a-zA-Z]+'], text,
                                search_string=r'5d\. .+? tabledata (.+?) 5e.', min_length=7, points=1)
    test5e = exact_answer('5e. screenshot censys.io heartbleed',
                          [r'5e\. .+? tabledata \s aaa \s inlineobject .+? 5f\.'], text, points=5)
    test5f = keyword_and_length('5f. Fix FREAK, how?', [r'update', r'patch', r'disable', ], text,
                                search_string=r'5f\. .+? tabledata (.+?) autograder', min_length=10, points=5,
                                min_matches=1)
    tests.extend([test1a, test1b, test2a, test3a, test4a, test5a, test5b, test5c, test5d, test5e, test5f, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/recon_shodan')
def docs_feedback_recon_shodan():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 5, 'manually_scored': 95, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    test1a = keyword_and_length('1a. What is shodan.io?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 2a\.', min_length=10, points=1)
    test2a = exact_answer('2a. screenshot shodan webcams',
                          [r'2a\. .+? tabledata \s aaa \s inlineobject .+? 3a\.'], text, points=1)
    test3a = exact_answer('3a. screenshot shodan routers',
                          [r'3a\. .+? tabledata \s aaa \s inlineobject .+? 4a\.'], text, points=1)
    test4a = keyword_and_length('4a. Security by obscurity?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 5a\.', min_length=10, points=1)
    test5a = keyword_and_length('5a. Security by obscurity compared to 30 years ago', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) autograder', min_length=10, points=1)

    tests.extend([test1a, test2a, test3a, test4a, test5a,])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/search_sort')
def docs_feedback_search_sort():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 24, 'manually_scored': 86, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Good algorithm?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=10, points=1)
    test2a = keyword_and_length('2a. Efficiency of merge vs. bubble, small sets??', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 2b\.', min_length=7, points=1)
    test2b = keyword_and_length('2b. Efficiency of merge vs. bubble, large sets??', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+) 3a\.', min_length=7, points=1)
    test3a = exact_answer('3a. binary always faster?',
                          [r'3a\. .+? tabledata \s* no \s*  3b\.'], text, points=1)
    test3b = keyword_and_length('3b. Explain 3a', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+) 3c\.', min_length=7, points=1)
    test3c = exact_answer('3c. Before binary search must?',
                          [r'3c\. .+? tabledata .+? sort .+?  3d\.'], text, points=3)
    test3d = exact_answer('3d. Must sort for linear search?',
                          [r'3a\. .+? tabledata \s* no \s*  3b\.'], text, points=3)
    test4a = keyword_and_length('4a. Put numbers on it', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+) 5a\.', min_length=12, points=1)
    test5a = keyword_and_length('5a. Why sort?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+) 6a\.', min_length=10, points=1)
    test6a = keyword_and_length('6a. Example of time want to sort?', [r'[a-zA-Z]+'], text,
                                search_string=r'6a\. .+? tabledata (.+) 7a\.', min_length=10, points=1)
    test7a = exact_answer('7a. n^2 reasonable?',
                          [r'7a\. .+? tabledata .+? yes .+?  7b\.'], text, points=5)
    test7b = exact_answer('7b. n! reasonable?',
                          [r'7b\. .+? tabledata .+? no .+?  in \s the \s real'], text, points=5)

    tests.extend([test1a, test2a, test2b, test3a, test3b, test3c, test3d, test4a, test5a, test6a, test7a,
                  test7b])

    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/two_factor_authentication')
def docs_feedback_two_factor_authentication():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 7, 'manually_scored': 93, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Two factor good?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=10, points=1)
    test2a = keyword_and_length('2a. Two factor bad?', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 3\.', min_length=10, points=1)
    test3a = exact_answer('3a. Screenshot of two-factor',
                          [r'3a\. .+? tabledata \s* aaa \s* inlineobject \s*  3b\.'], text, points=1)
    test3b = keyword_and_length('3b. Authentications more secure than before??', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c\.', min_length=10, points=1)
    test3c = keyword_and_length('3c. Authentications when you lose phone?', [r'[a-zA-Z]+'], text,
                                search_string=r'3c\. .+? tabledata (.+?) 3d\.', min_length=10, points=1)
    test3d = keyword_and_length('3c. What happens when cancel two-factor??', [r'[a-zA-Z]+'], text,
                                search_string=r'3d\. .+? tabledata (.+?) 4a\.', min_length=10, points=1)
    test4a = keyword_and_length('4a. Celeb hack, what you think??', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) check', min_length=10, points=1)

    tests.extend([test1a, test2a, test3a, test3b, test3c, test3d, test4a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/visualization_exploring_trends')
def docs_feedback_visualization_exploring_trends():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 13, 'manually_scored': 37, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Where data comes from', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2a\.', min_length=7, points=1)
    test2a = keyword_and_length('2a. How data adjusted', [r'[a-zA-Z]+'], text,
                                search_string=r'2a\. .+? tabledata (.+) 2b\.', min_length=7, points=1)
    test2b = keyword_and_length('2b. Value of 100?', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+) 3a\.', min_length=7, points=1)
    test3a = keyword_and_length('3a. Digital divide?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=10, points=1)
    test3b = keyword_and_length('3b. Digital divide affect result?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) exploring', min_length=10, points=1)
    test4a = exact_answer('4a. screenshot', [r'4a\. .+? tabledata \s* aaa \s* inlineobject \s*  5a\.'], text, points=5)
    test5a = keyword_and_length('5a. Describe terms?', [r'[a-zA-Z]+'], text,
                               search_string=r'5a\. .+? tabledata (.+)  6a\.', min_length=10, points=1)
    test6a = keyword_and_length('6a. Describe charts?', [r'[a-zA-Z]+'], text,
                               search_string=r'6a\. .+? tabledata (.+)  7a\.', min_length=10, points=1)
    test7a = keyword_and_length('7a. Plausible story?', [r'[a-zA-Z]+'], text,
                                search_string=r'7a\. .+? tabledata (.+)  $', min_length=15, points=1)

    tests.extend([test1a, test2a, test2b, test3a, test3b, test4a, test5a, test6a, test7a, ])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/docs/visualization_worksheet')
def docs_feedback_visualization_worksheet():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 18, 'manually_scored': 32, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. GPA, what is wrong?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+) 2\.', min_length=10, points=1)
    test2a = exact_answer('2a. screenshot', [r'2a\. .+? tabledata \s* aaa \s* inlineobject \s*  2b\.'], text, points=5)
    test2b = keyword_and_length('2b. Describe what you see', [r'[a-zA-Z]+'], text,
                                search_string=r'2b\. .+? tabledata (.+?) 2c\.', min_length=7, points=1)
    test2c = keyword_and_length('2c. Tricks?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) 3\.', min_length=10, points=1)

    test3a = keyword_and_length('3a. Correlation does not imply causation?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=10, points=1)
    test3b = keyword_and_length('3b. Dismissing correlation.', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 4\.', min_length=10, points=1)
    test4a = exact_answer('4a. screenshot', [r'4a\. .+? tabledata \s* aaa \s* inlineobject \s*  4b\.'], text, points=1)
    test4b = keyword_and_length('4b. Explain what showing, explain why good', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) 5\.', min_length=10, points=1)
    test5a = exact_answer('5a. screenshot', [r'5a\. .+? tabledata \s* aaa \s* inlineobject \s*  5b\.'], text, points=1)
    test5b = keyword_and_length('5b. Explain why bad', [r'[a-zA-Z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) 5c\.', min_length=10, points=1)
    test5c = exact_answer('5c. screenshot', [r'5c\. .+? tabledata \s* aaa \s* inlineobject \s*  5d\.'], text, points=1)
    test5d = keyword_and_length('5d. Explain why bad', [r'[a-zA-Z]+'], text,
                                search_string=r'5d\. .+? tabledata (.+?) 5e\.', min_length=10, points=1)
    test5e = exact_answer('5e. screenshot', [r'5e\. .+? tabledata \s* aaa \s* inlineobject \s*  5f\.'], text, points=1)
    test5f = keyword_and_length('5f. Explain why bad', [r'[a-zA-Z]+'], text,
                                search_string=r'5f\. .+? tabledata (.+?) $', min_length=10, points=1)

    tests.extend([test1a, test2a, test2b, test2c, test3a, test3b, test4a, test4b, test5a, test5b, test5c, test5d,
                  test5e, test5f])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)

@app.route('/docs/wireless_attacks_deauth')
def docs_feedback_wireless_attacks_deauth():
    from app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 38, 'manually_scored': 12, 'finished_scoring': True}

    link = request.args['link']
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. What is a MAC address?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a\. .+? tabledata (.+?) 1b\.', min_length=7, points=1)
    test1b = keyword_and_length('1b. MAC address same and different than IP address??', [r'[a-zA-Z]+'], text,
                                search_string=r'1b\. .+? tabledata (.+?) monitoring', min_length=10, points=1)
    test2a = exact_answer('2a. Monitoring mode',
                          [r'2a\. .+? tabledata .+? [a-zA-Z0-9] .+? deauthentication'], text, points=15)
    test3a = exact_answer('3a. Deauth',
                          [r'3a\. .+? tabledata .+? [a-zA-Z0-9] .+? 3b\.'], text, points=20)
    test3b = keyword_and_length('3b. How is deauth bad??', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) check \s your \s work', min_length=7, points=1)

    tests.extend([test1a, test1b, test2a, test3a, test3b])
    for test in tests:
        if test['pass']:
            score_info['score'] += test['points']
    return render_template('feedback.html', user=user, tests=tests, filename=link, score_info=score_info)


@app.route('/feedback_1040')
def feedback_1040():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_questions
    from app.python_labs.io_test import io_test
    from app.python_labs.python_1_040 import statement_variables
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'manually_scored': 5.5, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '1.040')
    tests.append(test_filename)

    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there are 3 input questions
        test_find_three_questions = find_questions(filename_data, 3, 5)
        test_find_three_questions['name'] += " Checking that Genie asks at least 3 questions. <br> " + \
                                             " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_three_questions)
        if not test_find_three_questions['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # io test 1- a b c
            test_io_1 = io_test(filename, r'.+ a1 .+ a2 .+ a3 ', 1, points=5)
            test_io_1['name'] += "Check things are in correct order - wishing for a, b, c " +\
                                 " should print 'your wishes are a, b, and c.' <br>" \
                                 "You must have at least 1 character of some sort between your wishes.<br>"
            test_io_1['fail_message'] += '<br>Did you put at least one character of some sort between your wishes?<br>' \
                                         'wish1 + wish2 + wish3 will fail because there is no space between wishes<br>'
            tests.append(test_io_1)

            # Check that there are 6 total questions (3 part 1, 3 part 2)
            test_find_six_questions = find_questions(filename_data, 6, 5)
            test_find_six_questions['name'] += " Checking that Genie asks at least 6 questions (you need 3 for" \
                                               " part 1 and 3 for part 2 (5 points)). <br>"
            tests.append(test_find_six_questions)

            # Check that repeated questions put into variables.
            test_input_variable = statement_variables(filename_data, 5)
            tests.append(test_input_variable)

            # io test 2 - a b c, b2, b3, b1
            test_io_2 = io_test(filename, r'.+ a1 .+ a2 .+ a3 .+ b2 .+ b3 .+ b1 ', 1, points=5)
            test_io_2['name'] += "Check things are in correct order - wishing for a, b, c, d, e, f " + \
                                 " should print 'your wishes are a, b, and c' <br>" +\
                                 " and 'your wishes are e, f, and d' <br>" \
                                 "You must have at least 1 character of some sort between your wishes.<br>"
            tests.append(test_io_2)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_1060')
def feedback_1060():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_questions, find_string
    from app.python_labs.io_test import io_test_find_all, io_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '1.060')
    tests.append(test_filename)

    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)
        # Check that there are 5 input questions
        test_find_five_questions = find_questions(filename_data, 5, 5)
        test_find_five_questions['name'] += " Checking for at least 5 questions. <br> " + \
                                            " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_five_questions)
        if not test_find_five_questions['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check that inputs are named after part of speech
            test_find_parts_of_speech = find_string(filename_data,
                                                    r'(verb|noun|name|adjective|adverb|preposition|place) _* [0-9]* \s* = '
                                                    r'\s* input\(',
                                                    5, points=5)
            test_find_parts_of_speech['name'] += "Testing that variables are named after parts of speech. <br>"\
                                                 "If this test fails, rename variables to parts of speech " \
                                                 "per instructions.<br>" \
                                                 "Also note, Python variable name convention is LOWERCASE, so this " \
                                                 "test will flunk variables like 'Noun1' or 'Verb2'<br>"
            tests.append(test_find_parts_of_speech)

            # Check for at least 1 print statement
            test_find_print = find_string(filename_data, r'print \s* \(', 1, points=5)
            test_find_print['name'] += "Testing for at least one print statement. <br>"
            tests.append(test_find_print)

            # Check for less than 3 print statements
            test_find_three_print = find_string(filename_data, r'print \s \(', 3, points=5, minmax='max')
            test_find_three_print['name'] += "Testing for at maximum of three print statements. <br>"
            tests.append(test_find_three_print)

            # answer 5 questions, they should all show up in printout
            test_io_five_inputs = io_test_find_all(filename, [r'a1', r'a2', r'a3', r'b1', r'b2'], 1, points=15)
            test_io_five_inputs['name'] += 'Testing for first 5 things you answered questions to show in output.<br>' \
                                           'For example, if you typed in noun1, verb1, noun2, verb2, and adjective' \
                                           '<br> noun1, verb1, noun2, verb2, and adjective should all appear ' \
                                           'in the printout. <br>'
            tests.append(test_io_five_inputs)

            # Check for 3 punctuations
            test_puncts = io_test(filename, r'(\? | ! | \.) ', 1, points=5, occurrences=3)
            test_puncts['name'] += "Testing for at least 3 punctuations.<br>"
            tests.append(test_puncts)

            # Test second 4 inputs for correct spacing
            test_io_spacing = io_test_find_all(filename, [r'(\^ | \s+ ) a2 (\s+ | \? | \. | , | ! | \n)',
                                                          r'(\^ | \s+ ) a3 (\s+ | \? | \. | , | ! | \n)',
                                                          r'(\^ | \s+ ) b1 (\s+ | \? | \. | , | ! | \n)',
                                                          r'(\^ | \s+ ) b2 (\s+ | \? | \. | , | ! | \n)'],
                                               1, points=10)
            test_io_spacing['name'] += 'Testing for spacing.  Things you enter should have spaces or punctuations<br>' \
                                       'after them and spaces before them in the printout. <br>'
            tests.append(test_io_spacing)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2020')
def feedback_2020():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.io_test import io_test, io_test_find_all
    from app.python_labs.find_items import find_questions, find_string
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 55, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.020')
    tests.append(test_filename)

    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there is 1 input questions
        test_find_question = find_questions(filename_data, 1, 5)
        test_find_question['name'] += " Checking for at least 1 question. <br> " + \
                                      " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_question)
        if not test_find_question['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Test for casting of any sort
            test_find_casting = find_string(filename_data, r'( int\( | float\( )', 1, points=5)
            test_find_casting['name'] += 'Checking that there is some casting of any sort to either integer or float.'
            tests.append(test_find_casting)

            # Test for casting of initial value to float.  Will crash with unknown errors later if casted to int.
            test_find_casting_2 = find_string(filename_data, r'float\( ', 1)
            test_find_casting_2['name'] += 'Test your program by manually running it and typing in 55.5 for your ' \
                                           'number. <br> If you  get an error<br>' \
                                           'ValueError: invalid literal for int() with base 10:<br>' \
                                           'This error means you are trying to convert a string that looks like' \
                                           ' a float into an integer.  ' \
                                           '<br> If you really want an integer you have to cast the string' \
                                           ' to a float first. <br> Or else if you are OK with float, cast to float ' \
                                           'instead of integer.<br> '
            tests.append(test_find_casting_2)
            if not test_find_casting_2['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that input1 is good (input / 2) 99 / 2 = 49.5
                test_io_1 = io_test(filename, '49.5', 1, points=10)
                test_io_1['name'] += "Checks that the number divides by 2 and prints out.  Input 99, " \
                                     "expected 49.5 and 49 in output. <br>"
                tests.append(test_io_1)

                # Check input2 is good (int(input / 2))
                test_io_2 = io_test(filename, '49$', 1, points=10)
                test_io_2['name'] += "Checks that the number divides by 2 and prints out the INTEGER only answer. " \
                                     " Input 99, expected 49 in output. <br>"
                tests.append(test_io_2)

                # Check input2 is good (int(input / 2))
                test_io_3 = io_test_find_all(filename, ['49.75', '49$'], 2, points=6)
                test_io_3['name'] += "Checks that the program works for non-whole inputs. " \
                                     " Input 99.5, expected 49.75 and 49 in output. <br>"
                tests.append(test_io_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                score_info['finished_scoring'] = True
                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_2021')
def feedback_2021():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.io_test import io_test, io_test_find_all
    from app.python_labs.find_items import find_questions, find_string
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()

    score_info = {'score': 0, 'max_score': 55, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.021')
    tests.append(test_filename)

    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check that there is 1 input questions
        test_find_question = find_questions(filename_data, 1, 5)
        test_find_question['name'] += " Checking for at least 1 question. <br> " + \
                                      " Autograder will not continue if this test fails. <br>"
        tests.append(test_find_question)
        if not test_find_question['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Test for casting of any sort
            test_find_casting = find_string(filename_data, r'( int\( | float\( )', 1, points=5)
            test_find_casting['name'] += 'Checking that there is some casting of any sort to either integer or float.'
            tests.append(test_find_casting)
            test_io_1 = io_test(filename, r'3\.14', 1, points=5)
            test_io_1['name'] += "case 1: Checks that circumference is calculated.  Input 1, " \
                                 "expected 3.14 in output. <br>"
            tests.append(test_io_1)
            test_io_2 = io_test(filename, r'[^0-9]3$', 1, points=5)
            test_io_2['name'] += "case 1: Checks that circumference is calculated, rounded.  Input 1, " \
                                 "expected 3 in output. <br>"
            tests.append(test_io_2)
            test_io_3 = io_test(filename, r'5\.34', 2, points=5)
            test_io_3['name'] += "case2: Checks that circumference is calculated.  Input 1.7, " \
                                 "expected 5.34 in output (be sure pi has enough digits) <br>"
            tests.append(test_io_3)
            test_io_4 = io_test(filename, r'[^0-9]5$', 2, points=5)
            test_io_4['name'] += "case2: Checks that circumference is calculated, rounded.  Input 1.7, " \
                                 "expected 5 in output. <br>"
            tests.append(test_io_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                   score_info=score_info)


@app.route('/feedback_2032a')
def feedback_2032a():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_if
    from app.python_labs.python_2_03x import python_2_032a
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 26.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.032a')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check for ifs
        test_ifs = find_if(filename_data, 0, 5, minmax='max')
        test_ifs['name'] += 'Testing for ifs.  There should be zero ifs in the code. <br>' \
                            'For example, print(1==1) NOT if (1 == 1): print("True") <br>' \
                            ''
        tests.append(test_ifs)

        if not test_ifs['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            debug_statement = 'Program asks for DC/Marvel, age, and power in that order. <br>' \
                              'DC must be capitalized.<br>'
            test_runs = python_2_032a(filename, filename_data, debug_statement=debug_statement)
            tests.append(test_runs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            score_info['finished_scoring'] = True
            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2032b')
def feedback_2032b():

    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_if
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_03x import python_2_032b
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 26.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.032b')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Check for ifs
        test_ifs = find_if(filename_data, 0, 5, minmax='max')
        test_ifs['name'] += 'Testing for ifs.  There should be zero ifs in the code. <br>' \
                            'For example, print(1==1) NOT if (1 == 1): print("True") <br>' \
                            'If you think this should pass, control-F and search for "if" in your code'
        tests.append(test_ifs)

        # test all 8 cases
        debug_statement = 'Program asks for if you are Yuka Kinoshita, your stomach size, and money in that order <br>'\
                          'If you are failing 2 tests, read example 8 from the presentation.'
        test_runs = python_2_032b(filename, filename_data, debug_statement=debug_statement)
        tests.append(test_runs)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2040')
def feedback_2040():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_all_strings, find_questions, find_if, find_elif, find_else
    from app.python_labs.python_2_040 import python_2_040
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 61, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.040')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # Test for prize variables
        test_prizes = find_all_strings(filename_data, [r'prize1 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize2 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize3 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+',
                                                       r'prize4 \s* = \s* (\'|\")[a-zA-Z0-9!-\.\s]+', ], 6)
        test_prizes['name'] += "Testing for 4 variables names prize1, prize2, prize3, prize4 (not prize_1, prize_2..." \
                               " <br>"
        tests.append(test_prizes)
        if not test_prizes['pass']:
            test_prizes['fail_message'] += 'Be sure you have 4 variables called  prize1, prize2, prize3, prize4. <br>' \
                                           'Be sure to set their values to be prizes'
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            test_question = find_questions(filename_data, 1, 6)
            tests.append(test_question)
            if not test_question['pass']:
                test_question['fail_message'] += "You need to ask the user a question about which door to pick. <br>"
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # test if, check for at least 1 if statement
                test_ifs = find_if(filename_data, 1, 6)
                tests.append(test_ifs)

                # test else check for at least 1 else statement
                test_else = find_else(filename_data, 1, 6)
                tests.append(test_else)

                # look for 3 elifs
                test_elif = find_elif(filename_data, 3, 6)
                tests.append(test_elif)

                test_correct_prizes = python_2_040(filename, filename_data)
                if not test_correct_prizes['pass']:
                    test_correct_prizes['fail_message'] += test_correct_prizes['debug']
                tests.append(test_correct_prizes)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests,
                                       filename=filename, score_info=score_info)


@app.route('/feedback_2051a')
def feedback_2051a():

    from app.python_labs.find_items import find_string, find_questions, find_all_strings
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_05x import python_2_051a
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 32.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.051a')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 4 items
        test_prizes = find_string(filename_data, r'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]', 1, points=5)
        test_prizes['name'] += "Testing that there is a variable prizes.  Prizes is a list with exactly 4 items.<br>" \
                               "Prizes is a named exactly 'prizes' and not something else."
        tests.append(test_prizes)
        if not test_prizes['pass']:
            test_prizes['fail_message'] += r"Looking for variable prizes that is a list with 4 items.  We name lists " \
                                           r"plural to help keep track of what is what.<br>  " \
                                           r"Looked for 'prizes \s* = \s* \[ .+ , .+ , .+ , .+ \]' " \
                                           r"in this string: <br>" + filename_data
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check for question
            test_find_input = find_questions(filename_data, 1, 5)
            tests.append(test_find_input)

            # Test input gives output
            test_runs = python_2_051a(filename, filename_data)
            tests.append(test_runs)

            # Test efficiency
            test_efficiency = find_all_strings(filename_data, [r'prizes\[0\]', r'prizes\[1\]',
                                                               r'prizes\[2\]', r'prizes\[3\]'], 5)
            test_efficiency['name'] += "Testing efficiency.  Do NOT want to have a big if/elif/else.<br>" \
                                       "If you have a variable x which is a number of item in list," \
                                       " list[x-1] will get you the correct item.<br>" \
                                       "<br>  This technique saves a lot of lines of code over a big if/elif  " \
                                       "and scales to big numbers.  " \
                                       "<br>That is, a list with 10,000 items will need " \
                                       "just one line to print out the list item whereas with a big if/else, " \
                                       "you will need 20,000 lines of code.<br>" \
                                       " If this does not make sense, ask a neighbor or the teacher."
            if test_efficiency['pass']:
                test_efficiency['pass'] = False
                test_efficiency['points'] = 0
                test_efficiency['fail_message'] += "You want to use a variable for the list index of prizes."
            else:
                test_efficiency['pass'] = True
                test_efficiency['pass_message'] += "(actually, did NOT find prizes[0], prizes[1] prizes[2] prizes[3]"
                test_efficiency['points'] = 5
            tests.append(test_efficiency)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_2051b')
def feedback_2051b():

    from app.python_labs.find_items import find_if, find_questions, find_list, find_elif, find_else
    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.python_2_05x import python_2_051b_1, python_2_051b_2
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 32.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '2.051b')
    tests.append(test_filename)
    if not test_filename['pass'] is True:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 4 items
        test_lcs = find_list(filename_data, num_items=4, list_name='learning_communities', points=3)
        tests.append(test_lcs)
        if not test_lcs['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Read in the python file to filename_data
            filename_data = read_file_contents(filename)

            test_scores = find_list(filename_data, num_items=4, list_name='scores', points=3)
            test_scores['name'] += "All items should be initially all zero (which we do not check right now).<br>"
            tests.append(test_scores)
            if not test_scores['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                test_question = find_questions(filename_data, 1, 1)
                if not test_question['pass']:
                    test_question['fail_message'] += "You need to ask the user a question about which " \
                                                     "LC to vote for. <br>"
                tests.append(test_question)

                # test if, check for at least 1 if statement
                test_if = find_if(filename_data, 1, 1)
                tests.append(test_if)

                # test else check for at least 1 else statement
                test_else = find_else(filename_data, 1, 4)
                tests.append(test_else)

                # test elif check for at least 3
                test_elif = find_elif(filename_data, 3, 1)
                tests.append(test_elif)

                # Try C C R L S, should get 2, 1, 1, 1
                test_1_io = python_2_051b_1(filename, 5)
                tests.append(test_1_io)

                # Try C R L S blah blah blah, should get 1, 1, 1, 1
                test_2_io = python_2_051b_2(filename, 5)
                tests.append(test_2_io)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_3011')
def feedback_3011():

    from app.python_labs.read_file_contents import read_file_contents
    from app.python_labs.find_items import find_questions, find_list, find_random, find_print
    from app.python_labs.python_3_011 import python_3_011_2, python_3_011_1
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 64, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.011')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        filename_data = read_file_contents(filename)

        # test for a list being created with 6 items
        test_houses = find_list(filename_data, num_items=6, list_name='houses', points=10)
        tests.append(test_houses)
        if not test_houses['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Asks a question, but that is ignore
            test_question = find_questions(filename_data, 1, 5)
            if not test_question['pass']:
                test_question['fail_message'] += "You need to ask the user a question to try to influence the hat. <br>"
            tests.append(test_question)

            # test for importing random
            test_random = find_random(filename_data, 5)
            tests.append(test_random)
            if not test_random['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # test for importing randint
                test_randint = find_random(filename_data, 5, randint=True)
                tests.append(test_randint)

                # Check for at least 1 print statement
                test_find_print = find_print(filename_data, 1, 5)
                tests.append(test_find_print)

                # Test efficiency
                test_efficiency = python_3_011_1(filename_data, 5)
                tests.append(test_efficiency)

                test_runs = python_3_011_2(filename, filename_data, 10)
                tests.append(test_runs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_3020')
def feedback_3020():

    from app.python_labs.find_items import find_function, function_called, find_list
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, extract_single_function, run_unit_test, \
        create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_3_020 import ten_runs, check_random

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.020')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        test_find_function_1 = find_function(filename, 'birthday_song', 1, points=4)
        tests.append(test_find_function_1)

        # Only continue if you have a birthday_song_function
        if not test_find_function_1['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Check that function is called once
            test_birthday_song_run = function_called(filename, 'birthday_song', 1, points=4)
            tests.append(test_birthday_song_run)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('3.020', 1, 4)
            test_function_1['name'] += " (prints out 'birthday' somewhere) "
            tests.append(test_function_1)

            # function test 2
            test_function_2 = run_unit_test('3.020', 2, 5)
            test_function_2['name'] += " (prints out input parameter somewhere) "
            tests.append(test_function_2)

            # function test 3
            test_function_3 = run_unit_test('3.020', 3, 8)
            test_function_3['name'] += " (output looks good) "
            tests.append(test_function_3)

            test_find_function_2 = find_function(filename, 'pick_card', 0, points=4)
            tests.append(test_find_function_2)

            # Only continue if you have a birthday_song_function
            if not test_find_function_2['pass']:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:

                cards_function = extract_single_function(filename, 'pick_card')

                test_find_cards = find_list(cards_function, num_items=4, list_name='cards', points=2)
                test_find_cards['fail_message'] += '"<h5 style=\"color:purple;\">'\
                                                   'List must be INSIDE function. Autograder extracts function to test it' \
                                                   '(which tests the reusability of the function)</h5>'                 
                tests.append(test_find_cards)

                test_find_suits = find_list(cards_function, num_items=4, list_name='suits', points=2)
                test_find_suits['fail_message'] += '"<h5 style=\"color:purple;\">'\
                                                   'List must be INSIDE function. Autograder extracts function to test it' \
                                                   '(which tests the reusability of the function)</h5>'
                tests.append(test_find_suits)

                # function test 4
                test_function_4 = run_unit_test('3.020', 4, 5)
                test_function_4['name'] += " (function picks 1 card) "
                tests.append(test_function_4)

                # Check that function is called once
                test_pick_card_run = function_called(filename, 'pick_card', 1, points=4)
                tests.append(test_pick_card_run)

                # Check that random is random
                test_random = check_random(filename)
                tests.append(test_random)

                # check that pick_card prints out 10 cards (looks for 'of' 10x)
                test_run_ten_cards = ten_runs(filename)
                tests.append(test_run_ten_cards)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_3026')
def feedback_3026():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_string, find_function, function_called, find_loop
    from app.python_labs.function_test import run_unit_test, create_testing_file, extract_all_functions, \
        extract_single_function
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 44.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '3.026')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function return_min
        test_find_function = find_function(filename, 'return_min', 1, points=5)
        tests.append(test_find_function)

        # Only continue if you have a return_min_function
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            extract_all_functions(filename)
            create_testing_file(filename)

            return_min_function = extract_single_function(filename, 'return_min')

            # Check that function is called 1x
            test_function_run = function_called(filename, 'return_min', 1, points=5)
            tests.append(test_function_run)

            # find string return (return in the function)
            test_return = find_string(return_min_function, r'return \s .+', 1, points=2.5)
            test_return["name"] += " (There is a return in the function)"
            test_return["fail_message"] += " (There is a return in the function)"
            tests.append(test_return)

            # find loop in function
            test_loop = find_loop(return_min_function, 2.5)
            test_loop["name"] += " (There is a loop in the code)"
            test_loop["fail_message"] += " (There is a loop in the function)"
            tests.append(test_loop)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('3.026', 1, 5)
            test_function_1['name'] += " (return_min with list [-1, 3, 5, 99] returns -1) "
            tests.append(test_function_1)

            # function test 2
            test_function_2 = run_unit_test('3.026', 2, 5)
            test_function_2['name'] += " (return_min with list [-1, 3, 5, -99] returns -99) "
            tests.append(test_function_2)

            # function test 3
            test_function_3 = run_unit_test('3.026', 3, 5)
            test_function_3['name'] += " (return_min with list [5] returns 5) "
            tests.append(test_function_3)

            # function test 4
            test_function_4 = run_unit_test('3.026', 4, 5)
            test_function_4['name'] += " (return_min with list [5, 4, 99, -11, 44, -241, -444, -999, 888, -2] " \
                                       "returns -444) "
            tests.append(test_function_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4011')
def feedback_4011():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_loop, function_called, find_if
    from app.python_labs.function_test import run_unit_test, extract_single_function,\
        extract_all_functions, create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.011')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function
        test_find_function = find_function(filename, 'could_it_be_a_martian_word', 1, points=5)
        tests.append(test_find_function)

        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'could_it_be_a_martian_word')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 5)
            test_loop['name'] += "Testing there is a loop in the could_it_be_a_martian_word function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'could_it_be_a_martian_word', 3, points=5)
                tests.append(test_function_run)

                test_function_1 = run_unit_test('4.011', 1, 10)
                test_function_1['name'] += " (could_it_be_a_martian_word with 'bcdefgijnpqrstuvwxyz' returns []) "
                tests.append(test_function_1)

                test_function_2 = run_unit_test('4.011', 2, 10)
                test_function_2['name'] += " (could_it_be_a_martian_word with 'ba' returns ['a']) "
                tests.append(test_function_2)

                test_function_3 = run_unit_test('4.011', 3, 10)
                test_function_3['name'] += " (could_it_be_a_martian_word with 'baa' returns ['a']) "
                tests.append(test_function_3)

                test_ifs = find_if(function_data, 3, 5, minmax='max')
                tests.append(test_ifs)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_4012')
def feedback_4012():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_loop, function_called, find_if
    from app.python_labs.function_test import run_unit_test, extract_single_function,\
        extract_all_functions, create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.012')
    tests.append(test_filename)
    flash("got here")
    print("got here")
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function
        test_find_function = find_function(filename, 'samuel_l_algorithm', 1, points=5)
        tests.append(test_find_function)

        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'samuel_l_algorithm')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 5)
            test_loop['name'] += "Testing there is a loop in the samuel_l_algorithm function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'samuel_l_algorithm', 3, points=5)
                tests.append(test_function_run)

                test_ifs = find_if(function_data, 3, 5, minmax='max')
                tests.append(test_ifs)

                test_function_1 = run_unit_test('4.012', 1, 10)
                test_function_1['name'] += " (samuel_l_algorithm with 'Birdman or (The Unexpected Virtue of Ignorance)'" \
                                           " returns 'bad') <br>Note: this is a single movie with a super long pretentious title."
                tests.append(test_function_1)

                test_function_2 = run_unit_test('4.012', 2, 10)
                test_function_2['name'] += " (samuel_l_algorithm with 'Snakes on a plane' returns 'good') "
                tests.append(test_function_2)

                test_function_3 = run_unit_test('4.012', 3, 10)
                test_function_3['name'] += " (samuel_l_algorithm with 'aladdin' returns 'maybe') "
                tests.append(test_function_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 14)
                tests.append(test_pep8)
                test_help = helps(filename, 5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_4021')
def feedback_4021():
    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import run_unit_test, extract_all_functions, extract_single_function, \
        create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 37,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function the_rock_says
        test_find_function = find_function(filename, 'the_rock_says', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)
            function_data = extract_single_function(filename, 'the_rock_says')

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 2.5)
            test_loop['name'] += "Testing there is a loop in the the_rock_says function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'the_rock_says', 3, points=5)

                tests.append(test_function_run)

                # test1 for the_rock_says
                test_function_1 = run_unit_test('4.021', 1, 5)
                test_function_1['name'] += " (Testing calling the_rock_says with list ['eggs', 'apple'] returns a " \
                                           "list ['The Rock says eggs', 'The Rock says apple']) (caps unimportant)"
                tests.append(test_function_1)

                # test2 for the_rock_says
                test_function_2 = run_unit_test('4.021', 2, 5)
                test_function_2['name'] += " (Testing calling the_rock_says with list ['eggs', 'smell'] returns " \
                                           "['The Rock says eggs', 'Do you smell what The Rock is cooking'] (caps unimportant) <br>"
                tests.append(test_function_2)

                # test3 for the_rock_says
                test_function_3 = run_unit_test('4.021', 3, 5)
                test_function_3['name'] += " (Testing calling the_rock_says with list " \
                                           "['eggs', 'what should I think'] returns ['The Rock says eggs', 'It doesn't matter what you think' (caps unimportant) "
                tests.append(test_function_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']

                score_info['finished_scoring'] = True
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)


@app.route('/feedback_4022')
def feedback_4022():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.function_test import run_unit_test, extract_all_functions, \
        extract_single_function, create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 37,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.022')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for function
        test_find_function = find_function(filename, 'bad_lossy_compression', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            function_data = extract_single_function(filename, 'bad_lossy_compression')
            create_testing_file(filename)

            # Check for a loop of some sort (for or while)
            test_loop = find_loop(function_data, 2.5)
            test_loop['name'] += "Testing there is a loop in the bad_lossy_compression function.<br>"
            tests.append(test_loop)

            if test_loop['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:
                # Check that function is called 3x
                test_function_run = function_called(filename, 'bad_lossy_compression', 3, points=5)
                tests.append(test_function_run)

                # test1
                test_function_1 = run_unit_test('4.022', 1, 5)
                test_function_1['name'] += " (Testing calling bad_lossy_compression with 'The rain in spain falls " \
                                           "mainly in the plain' returns 'The ain n spin flls ainl in he pain') "
                tests.append(test_function_1)

                # test2 for the_rock_says
                test_function_2 = run_unit_test('4.022', 2, 5)
                test_function_2['name'] += " (Testing calling bad_lossy_compression with " \
                                           "'I am sick and tired of these darned snakes on this darned plane'" \
                                           " returns 'I a sik ad tredof hes danedsnaes n tis arnd pane' <br> "
                tests.append(test_function_2)

                # test3 for the_rock_says
                test_function_3 = run_unit_test('4.022', 3, 5)
                test_function_3['name'] += "Testing calling bad_lossy_compression with 'Madness?!?!?!?!" \
                                           " THIS IS SPARTA!!!!'" \
                                           " returns 'Madess!?!!?!THI ISSPATA!!!' <br> "
                tests.append(test_function_3)

                # Find number of PEP8 errors and helps
                test_pep8 = pep8(filename, 7)
                tests.append(test_pep8)
                test_help = helps(filename, 2.5)
                tests.append(test_help)

                for test in tests:
                    if test['pass']:
                        score_info['score'] += test['points']
                score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4023')
def feedback_4023():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, function_called, find_loop
    from app.python_labs.function_test import run_unit_test, extract_all_functions, \
        extract_single_function, create_testing_file
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.023')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:


        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)
        
        test_function_1 = run_unit_test('4.023', 1, 5)
        tests.append(test_function_1)
        test_function_2 = run_unit_test('4.023', 2, 2.5)
        tests.append(test_function_2)
        test_function_3 = run_unit_test('4.023', 3, 2.5)
        tests.append(test_function_3)
        test_function_4 = run_unit_test('4.023', 4, 2.5)
        tests.append(test_function_4)
        test_function_5 = run_unit_test('4.023', 5, 2.5)
        tests.append(test_function_5)
        test_function_6 = run_unit_test('4.023', 6, 2.5)
        tests.append(test_function_6)
        test_function_7 = run_unit_test('4.023', 7, 2.5)
        tests.append(test_function_7)
        test_function_8 = run_unit_test('4.023', 8, 2.5)
        tests.append(test_function_8)
        test_function_9 = run_unit_test('4.023', 9, 2.5)
        tests.append(test_function_9)


        
        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)
        
        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']
                score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

        
@app.route('/feedback_4025')
def feedback_4025():

    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_loop, find_string
    from app.python_labs.function_test import extract_all_functions, create_testing_file, extract_single_function, \
        run_unit_test
    from app.python_labs.python_4_025 import win_all, win_most

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 129,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.025')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)
        play_tournament_function = extract_single_function(filename, 'play_tournament')

        test_function_1 = run_unit_test('4.025', 1, 10)
        test_function_1['name'] += " Testing game function - 10000 runs with 90% win" \
                                   " should give between 8850 and 9150 wins " \
                                   "(10 points) "
        tests.append(test_function_1)

        test_game_2 = run_unit_test('4.025', 2, 5)
        tests.append(test_game_2)
        test_game_3 = run_unit_test('4.025', 3, 5)
        tests.append(test_game_3)
        test_game_2['name'] += " Testing game function - 10000 runs with 0% win should give 0 wins (5 points) "
        test_game_3['name'] += " Testing game function - 10000 runs with 100% win should give 10000 wins (5 points) "


        if test_function_1['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            test_loop = find_loop(play_tournament_function, 5)
            test_loop['name'] += " Testing for loop in play_tournament function.<br>"
            tests.append(test_loop)

            test_function_4 = run_unit_test('4.025', 4, 5)
            test_function_4['name'] += " Testing play_tournament function.  If I call play_tournament with " \
                                       "input parameters (0.75, 'Wimbledon'), play_tournament  should " \
                                       "print 'Wimbledon' somewhere (2.5 points).<br>"
            tests.append(test_function_4)

            test_function_5 = run_unit_test('4.025', 5, 5)
            test_function_5['name'] += " Testing play_tournament function.  If I call play_tournament with " \
                                       "input parameters (1.0, 'Wimbledon'), Serena should win this tournament" \
                                       "(5 points).<br>"
            tests.append(test_function_5)

            test_function_6 = run_unit_test('4.025', 6, 10)
            test_function_6['name'] += " Testing play_season function.  If I call play_season enough times," \
                                       "Serena should win US open most, followed by Wimbledon, followed by French " \
                                       "open (10 points).<br>"
            tests.append(test_function_6)

            test_function_7 = run_unit_test('4.025', 7, 10)
            test_function_7['name'] += " Testing data_analysis function, looking to see if correct percentages are " \
                                       "printed (10 points).<br>"
            tests.append(test_function_7)

            run_simulation_function = extract_single_function(filename, 'run_simulation')
            test_run_sim = find_loop(run_simulation_function, 5)
            test_run_sim['name'] = "Looking for loop in the run_simulation function (5 points).<br>"
            tests.append(test_run_sim)

            test_run_sim_data_analysis = find_string(run_simulation_function, r'\s*data_analysis\(', 1, points=5)
            test_run_sim_data_analysis['name'] = "Checking that run_simulation calls data_analysis (5 points).<br>"
            tests.append(test_run_sim_data_analysis)

            test_function_8 = run_unit_test('4.025', 8, 5)
            test_function_8['name'] = " Testing run_simulation function, verifying that if you call it with " \
                                      "p_num_simulations = 13, the printout has the exact phrase ' of 13 simulations'.. <br>" \
                                      " Requires a working data_analysis (5 points).<br>"
            tests.append(test_function_8)


            # IO tests
            test_io_1 = win_all(filename)
            tests.append(test_io_1)


            test_io_2 = win_most(filename)
            tests.append(test_io_2)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4026')
def feedback_4026():

    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_loop, find_string
    from app.python_labs.function_test import extract_all_functions, create_testing_file, extract_single_function, \
        run_unit_test
    from app.python_labs.python_4_026 import case_1, case_2, case_3, case_4

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 134,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.026')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)
        play_tournament_function = extract_single_function(filename, 'play_tournament')

        test_function_1 = run_unit_test('4.026', 1, 15)
        test_function_1['name'] += "Testing animate_dead function.  " \
                                   "2000 runs should give between 18000 and 21000 raised dead "
        tests.append(test_function_1)

        if test_function_1['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            print("trying 2")
            test_function_2 = run_unit_test('4.026', 2, 10)
            test_function_2['name'] += "Testing raise_army function.  " \
                                       "100 runs of raise_army should print out how many Atwood raises in each cemetary<br>" \
                                       "For each cemetary, Atwood will either 'raises and control' or else " \
                                       "'raises but loses control' <br>" \
                                       "See test output for debugging info.  IF YOU ARE PERIOD 1 2019 S1 APCSP, "\
                                       " LOOK AT ANNOUNCEMENT IN GOOGLE CLASSROOM FOR CORRECTION OF WHAT IT SHOULD PRINT <br>"
            tests.append(test_function_2)

            test_function_3 = run_unit_test('4.026', 3, 10)
            test_function_3['name'] += "Testing raise_army function.  " \
                                       "5 runs of raise_army should give correct undead_data."
            tests.append(test_function_3)

            test_function_4 = run_unit_test('4.026', 4, 15)
            test_function_4['name'] += "Testing dance function.  500 runs of dance should print out correct info AND" \
                                       "should also return correct p_sim." \
                                       "  <br>" \
                                       "Check instructions in the '4 possible outcomes' section to " \
                                       "see what it should print.<br>"
            tests.append(test_function_4)

            test_function_5 = run_unit_test('4.026', 5, 10)
            test_function_5['name'] += "Testing data analysis. Give it a list [25, 50, 75, 3] and 200 simulations.<br>" \
                                       "  Spacing matters (i.e. 50.0% not 50.0 %).  This test ist mostly checking" \
                                       "that you can do math. "
            tests.append(test_function_5)


            run_simulation_function = extract_single_function(filename, 'run_simulation')
            test_run_sim = find_loop(run_simulation_function, 5)
            test_run_sim['name'] = "Looking for loop in the run_simulation function (5 points).<br>"
            tests.append(test_run_sim)

            test_run_sim_data_analysis = find_string(run_simulation_function, r'\s*data_analysis\(', 1, points=5)
            test_run_sim_data_analysis['name'] = "Checking that run_simulation calls data_analysis (5 points).<br>"
            tests.append(test_run_sim_data_analysis)

            test_function_6 = run_unit_test('4.026', 6, 5)
            test_function_6['name'] = " Testing data_analysis through run_simulation function.  Verifying that if you call it with" \
                                      "p_num_simulations of 13, the printout shows 13 runs. <br>" \
                                      "Program looks for the string 'out of 13 simulations' (assuming you ran 13 sims)." \
                                      "Requires a working data_analysis that prints out how many simulations you ran (5 points).<br>"
            tests.append(test_function_6)

            # IO tests
            test_io_1 = case_1(filename)
            tests.append(test_io_1)
            test_io_2 = case_2(filename)
            tests.append(test_io_2)
            test_io_3 = case_3(filename)
            tests.append(test_io_3)
            test_io_4 = case_4(filename)
            tests.append(test_io_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_011')
def feedback_6011():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_elif, find_dictionary
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.011')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        test_find_function = find_function(filename, 'bob_kraft_translator', 2, points=5)
        tests.append(test_find_function)
        if not test_find_function['pass']:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Test for dictionary with 3+ items
            filename_data = read_file_contents(filename)

            test_dictionary = find_dictionary(filename_data, num_items=3, points=10)
            tests.append(test_dictionary)

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            test_function_1 = run_unit_test('6.011', 1, 10)
            test_function_1['name'] += " (Sent in dictionary  {'wth': 'What the heck'}, search for 'wth', " \
                                       "returned 'what the heck') <br>"
            tests.append(test_function_1)

            test_function_2 = run_unit_test('6.011', 2, 10)
            test_function_2['name'] += " (Sent in dictionary  {'wth': 'What the heck', 'aymm': 'Ay yo my man',}, " \
                                       "looking for aymm, should receive 'Ay yo my man'. <br>"
            tests.append(test_function_2)

            test_function_3 = run_unit_test('6.011', 3, 10)
            test_function_3['name'] += " (Sent in dictionary  {'wth': 'What the heck','aymm': 'Ay yo my man',}, " \
                                       "asdfasdf, received something with 'do not know''. <br>"
            tests.append(test_function_3)

            # Check for 3 ifs on different lines
            test_elifs = find_elif(filename_data, 3, 5, minmax='max')
            tests.append(test_elifs)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_021')
def feedback_6021():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, function_called, find_dictionary
    from app.python_labs.function_test import extract_all_functions, extract_single_function, \
        create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        extract_all_functions(filename)
        create_testing_file(filename)

        test_find_function = find_function(filename, 'martinez_dictionary', 1, points=5)
        tests.append(test_find_function)

        # Check that function is called 3x
        test_function_run = function_called(filename, 'martinez_dictionary', 3, points=5)
        tests.append(test_function_run)

        # extract martinez_dictionary functions and look for dictionary
        martinez_function = extract_single_function(filename, 'martinez_dictionary')
        test_dictionary = find_dictionary(martinez_function, num_items=0, points=5)
        tests.append(test_dictionary)

        # Martinez test 1
        test_function_1 = run_unit_test('6.021', 1, 10)
        tests.append(test_function_1)

        # Martinez test 2
        test_function_2 = run_unit_test('6.021', 2, 10)
        tests.append(test_function_2)

        test_find_function = find_function(filename, 'data_generator', 2, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # Martinez test 3
            test_function_3 = run_unit_test('6.021', 3, 5)
            tests.append(test_function_3)

            # Martinez test 4
            test_function_4 = run_unit_test('6.021', 4, 5)
            tests.append(test_function_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']
                flash(test['name'])
                flash(score_info['score'])

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_022')
def feedback_6022():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, function_called, find_dictionary
    from app.python_labs.function_test import extract_all_functions, extract_single_function, \
        create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.022')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Read in the python file to filename_data
        extract_all_functions(filename)
        create_testing_file(filename)

        test_find_function = find_function(filename, 'dr_lam_workout_counter', 1, points=10)
        tests.append(test_find_function)

        # Check that function is called 3x
        test_function_run = function_called(filename, 'dr_lam_workout_counter', 3, points=10)
        tests.append(test_function_run)

        # extract dr_lam_workout_counter functions and look for dictionary
        martinez_function = extract_single_function(filename, 'dr_lam_workout_counter')
        test_dictionary = find_dictionary(martinez_function, num_items=0, points=10)
        tests.append(test_dictionary)

        # Martinez test 1
        test_function_1 = run_unit_test('6.022', 1, 10)
        tests.append(test_function_1)

        # Martinez test 2
        test_function_2 = run_unit_test('6.022', 2, 10)
        tests.append(test_function_2)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 14)
        tests.append(test_pep8)
        test_help = helps(filename, 5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']
            flash(test['name'])
            flash(score_info['score'])

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_031')
def feedback_6031():
    from app.python_labs.function_test import extract_all_functions, run_unit_test, create_testing_file
    from app.python_labs.find_items import find_function, find_loop, find_dictionary
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.031')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        test_dictionary = find_dictionary(filename_data, num_items=0, points=5)
        tests.append(test_dictionary)
        if test_dictionary['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # Check for function add with 3 inputs
            test_find_function = find_function(filename, 'add', 3, points=5)
            tests.append(test_find_function)
            if test_find_function['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:

                extract_all_functions(filename)
                create_testing_file(filename)

                # function test 1
                test_function_1 = run_unit_test('6.031', 1, 5)
                tests.append(test_function_1)

                # function test 2
                test_function_2 = run_unit_test('6.031', 2, 10)
                tests.append(test_function_2)

                # Check for function add with 2 inputs
                test_find_function = find_function(filename, 'get', 2, points=5)
                tests.append(test_find_function)
                if test_find_function['pass'] is False:
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)
                else:
                    # function test 3
                    test_function_3 = run_unit_test('6.031', 3, 5)
                    tests.append(test_function_3)

                    # function test 3
                    test_function_4 = run_unit_test('6.031', 4, 10)
                    tests.append(test_function_4)

                    # Check for a loop of some sort (for or while)
                    test_loop = find_loop(filename_data, 5)
                    tests.append(test_loop)

                    # Find number of PEP8 errors and helps
                    test_pep8 = pep8(filename, 14)
                    tests.append(test_pep8)
                    test_help = helps(filename, 5)
                    tests.append(test_help)

                    for test in tests:
                        if test['pass']:
                            score_info['score'] += test['points']

                    score_info['finished_scoring'] = True
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)


@app.route('/feedback_6_032')
def feedback_6032():
    from app.python_labs.function_test import extract_all_functions, run_unit_test, create_testing_file
    from app.python_labs.find_items import find_function, find_loop, find_dictionary
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test
    from app.python_labs.read_file_contents import read_file_contents
    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 74, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.032')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        test_dictionary = find_dictionary(filename_data, num_items=0, points=5)
        tests.append(test_dictionary)
        if test_dictionary['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            test_find_function = find_function(filename, 'add_assignment', 3, points=5)
            tests.append(test_find_function)
            if test_find_function['pass'] is False:
                return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                       score_info=score_info)
            else:

                extract_all_functions(filename)
                create_testing_file(filename)

                # function test 1
                test_function_1 = run_unit_test('6.032', 1, 5)
                tests.append(test_function_1)

                # function test 2
                test_function_2 = run_unit_test('6.032', 2, 5)
                tests.append(test_function_2)

                # function test 3
                test_function_3 = run_unit_test('6.032', 3, 5)
                tests.append(test_function_3)

                # function test 4
                test_function_4 = run_unit_test('6.032', 4, 5)
                tests.append(test_function_4)

                # Check for function add with 2 inputs
                test_find_function = find_function(filename, 'calculate_grade', 1, points=5)
                tests.append(test_find_function)
                if test_find_function['pass'] is False:
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)
                else:
                    # function test 4
                    test_function_5 = run_unit_test('6.032', 5, 5)
                    tests.append(test_function_5)

                    test_function_6 = run_unit_test('6.032', 6, 5)
                    tests.append(test_function_6)

                    test_function_7 = run_unit_test('6.032', 7, 5)
                    tests.append(test_function_7)

                    test_loop = find_loop(filename_data, 5)
                    tests.append(test_loop)

                    # Find number of PEP8 errors and helps
                    test_pep8 = pep8(filename, 14)
                    tests.append(test_pep8)
                    test_help = helps(filename, 5)
                    tests.append(test_help)

                    for test in tests:
                        if test['pass']:
                            score_info['score'] += test['points']

                    score_info['finished_scoring'] = True
                    return render_template('feedback.html', user=user, tests=tests, filename=filename,
                                           score_info=score_info)


@app.route('/feedback_6_041')
def feedback_6041():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_string
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_6_041 import five_loop
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.041')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        # Check for function add with 1 inputs
        test_find_function = find_function(filename, 'item_list_to_dictionary', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 1
            test_function_1 = run_unit_test('6.041', 1, 10)
            tests.append(test_function_1)

            # Check for function 1 inputs
            test_find_function_2 = find_function(filename, 'min_item', 1, points=5)
            tests.append(test_find_function_2)

            # unit test 2
            test_function_2 = run_unit_test('6.041', 2, 20)
            tests.append(test_function_2)

            # Check that removes, just look for del or pop
            test_removal = find_string(filename_data, r"\.pop\( | del", 1, points=5)
            tests.append(test_removal)

            # Check that it's run 5x
            test_five_times = five_loop(filename_data)
            tests.append(test_five_times)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_6_042')
def feedback_6042():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.find_items import find_function, find_loop, find_dictionary, function_called
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test, \
        extract_single_function
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_6_041 import five_loop
    from app.python_labs.read_file_contents import read_file_contents

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '6.042')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        filename_data = read_file_contents(filename)

        # Check for function add with 1 inputs
        test_find_function = find_function(filename, 'worst_hit', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # unit tests
            test_function_1 = run_unit_test('6.042', 1, 5)
            tests.append(test_function_1)
            test_function_2 = run_unit_test('6.042', 2, 5)
            tests.append(test_function_2)

            # Check for function 2 inputs
            test_find_function_2 = find_function(filename, 'top_hits', 1, points=5)
            tests.append(test_find_function_2)

            run_simulation_function = extract_single_function(filename, 'top_hits')
            test_run_sim = find_loop(run_simulation_function, 5)
            test_run_sim['name'] = "Looking for loop in the run_simulation function (5 points).<br>"
            tests.append(test_run_sim)

            # unit tests
            test_function_3 = run_unit_test('6.042', 3, 5)
            tests.append(test_function_3)
            test_function_4 = run_unit_test('6.042', 4, 5)
            tests.append(test_function_4)

            test_dictionary = find_dictionary(filename_data, num_items=6, points=5)
            tests.append(test_dictionary)
            test_function_run = function_called(filename, 'worst_hit', 3, points=5)
            tests.append(test_function_run)
            test_function_run = function_called(filename, 'top_hits', 3, points=5)
            tests.append(test_function_run)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_021')
def feedback_7021():
    from app.python_labs.find_items import find_class, find_function, function_called, object_created
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 69, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.021')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for class Collectible
        test_class = find_class(filename, 'Collectible', 'object', points=5)
        tests.append(test_class)

        if test_class['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:

            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)

            # function test 2
            test_function_1 = run_unit_test('7.021', 1, 15)
            tests.append(test_function_1)

            # Check for function existence
            test_find_function = find_function(filename, 'collectible_printer', 1, points=5)
            tests.append(test_find_function)

            # test 2
            test_function_2 = run_unit_test('7.021', 2, 5)
            tests.append(test_function_2)

            # test 3
            test_function_3 = run_unit_test('7.021', 3, 10)
            tests.append(test_function_3)

            # Check for all objects
            test_objects = object_created(filename, 'Collectible', 3, points=5)
            tests.append(test_objects)

            # Check that function is called
            test_function_run = function_called(filename, 'collectible_printer', 1, points=5)
            tests.append(test_function_run)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True

            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_031')
def feedback_7031():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.031')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        test_function_1 = run_unit_test('7.031', 1, 5)
        tests.append(test_function_1)

        # unit test 2
        test_function_2 = run_unit_test('7.031', 2, 10)
        tests.append(test_function_2)

        # unit test 3
        test_function_3 = run_unit_test('7.031', 3, 10)
        tests.append(test_function_3)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_7_034')
def feedback_7034():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 34.5,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.034')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = run_unit_test('7.034', 1, 5)
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = run_unit_test('7.034', 2, 5)
        tests.append(unit_test_2)

        # unit test 3
        unit_test_3 = run_unit_test('7.034', 3, 5)
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = run_unit_test('7.034', 4, 5)
        tests.append(unit_test_4)

        # unit test 5
        unit_test_5 = run_unit_test('7.034', 5, 5)
        tests.append(unit_test_5)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 7)
        tests.append(test_pep8)
        test_help = helps(filename, 2.5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)    


@app.route('/feedback_7_036')
def feedback_7036():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.find_items import find_class

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 44.5,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '7.036')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # Check for class Collectible
        test_class = find_class(filename, 'Contraband', 'object', points=5)
        tests.append(test_class)
   ##     test_class = {}
     #   test_class['pass'] = False
        if test_class['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            # extract functions and create python test file
            extract_all_functions(filename)
            create_testing_file(filename)
            #
            # Unit tests
            unit_test_1 = run_unit_test('7.036', 1, 5)
            tests.append(unit_test_1)

            # # Check for class Collectible
            test_class2 = find_class(filename, 'Ship', 'object', points=5)
            tests.append(test_class2)

            # unit tests
            unit_test_2 = run_unit_test('7.036', 2, 5)
            tests.append(unit_test_2)
            unit_test_3 = run_unit_test('7.036', 3, 5)
            tests.append(unit_test_3)
            unit_test_4 = run_unit_test('7.036', 4, 5)
            tests.append(unit_test_4)
            unit_test_5 = run_unit_test('7.036', 5, 5)
            tests.append(unit_test_5)
            #
            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 7)
            tests.append(test_pep8)
            test_help = helps(filename, 2.5)
            tests.append(test_help)

            for test in tests:
                if test['pass']:
                    score_info['score'] += test['points']

            score_info['finished_scoring'] = True
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4031')
def feedback_4031():
    from app.python_labs.filename_test import filename_test
    from app.python_labs.function_test import create_testing_file, extract_all_functions, run_unit_test
    from app.python_labs.helps import helps
    from app.python_labs.pep8 import pep8
    from app.python_labs.python_4_03x import python_4_031_double_loops, python_4_031_good_prints

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 74, 'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.031')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = run_unit_test('4.031', 1, 2.5)
        tests.append(unit_test_1)

        # unit test 2
        unit_test_2 = run_unit_test('4.031', 2, 2.5)
        tests.append(unit_test_2)

        # unit test 3
        unit_test_3 = run_unit_test('4.031', 3, 2.5)
        tests.append(unit_test_3)

        # unit test 4
        unit_test_4 = run_unit_test('4.031', 4, 5)
        tests.append(unit_test_4)

        # unit test 5
        unit_test_5 = run_unit_test('4.031', 5, 5)
        tests.append(unit_test_5)

        # unit test 6
        unit_test_6 = run_unit_test('4.031', 6, 5)
        tests.append(unit_test_6)

        # unit test 7
        unit_test_7 = run_unit_test('4.031', 7, 5)
        tests.append(unit_test_7)

        # unit test 8
        unit_test_8 = run_unit_test('4.031', 8, 7.5)
        tests.append(unit_test_8)

        # Check for double loops
        test_loop = python_4_031_double_loops(filename)
        tests.append(test_loop)

        # Check for double loops
        test_prints = python_4_031_good_prints(filename)
        tests.append(test_prints)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 14)
        tests.append(test_pep8)
        test_help = helps(filename, 5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

    
@app.route('/feedback_4036')
def feedback_4036():
    from app.python_labs.find_items import find_function
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 89,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.036')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:

        # Check for function existence
        test_find_function = find_function(filename, 'fried_chicken_problem_1', 2, points=5)
        tests.append(test_find_function)

        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1
        unit_test_1 = run_unit_test('4.036', 1, 10)
        tests.append(unit_test_1)
        unit_test_2 = run_unit_test('4.036', 2, 10)
        tests.append(unit_test_2)

        # Check for function existence
        test_find_function = find_function(filename, 'fried_chicken_problem_2', 2, points=5)
        tests.append(test_find_function)

        # unit test 3
        unit_test_3 = run_unit_test('4.036', 3, 10)
        tests.append(unit_test_3)
        unit_test_4 = run_unit_test('4.036', 4, 10)
        tests.append(unit_test_4)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 14)
        tests.append(test_pep8)
        test_help = helps(filename, 5)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)


@app.route('/feedback_4037')
def feedback_4037():
    import re
    from app.python_labs.find_items import find_function, find_loop
    from app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test, \
        extract_single_function
    from app.python_labs.python_4_037 import linear_looks_linear, binary_looks_binary
    from app.python_labs.pep8 import pep8
    from app.python_labs.helps import helps
    from app.python_labs.filename_test import filename_test

    user = {'username': 'CRLS Scholar'}
    tests = list()
    score_info = {'score': 0, 'max_score': 144,  'manually_scored': 11, 'finished_scoring': False}

    # Test 1: file name
    filename = request.args['filename']
    filename = '/tmp/' + filename
    test_filename = filename_test(filename, '4.037')
    tests.append(test_filename)
    if not test_filename['pass']:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)

        # unit test 1 and 2
        unit_test_1 = run_unit_test('4.037', 1, 10)
        unit_test_1['name'] += 'Testing monthly_payment_calculation function with arguments principal 1000,' \
                               'DPR 0.0027 and payment 100.'
        tests.append(unit_test_1)
        unit_test_2 = run_unit_test('4.037', 2, 10)
        unit_test_2['name'] += 'Testing monthly_payment_calculation function with arguments principal 10000, ' \
                               'DPR 127 and payment 200.'
        tests.append(unit_test_2)

        function_2 = extract_single_function(filename, 'loan_life_calculation')
        test_function_2_loop = find_loop(function_2, 10)
        test_function_2_loop['name'] += 'Looking for loop in loan_life_calculation function'
        tests.append(test_function_2_loop)
        
        unit_test_3 = run_unit_test('4.037', 3, 10)
        unit_test_3['name'] += 'Testing loan_life_calculation with arguments  principal 1000, ' \
                               'DPR = 100/36.25/100, payment = 50, life of loan=2. '
        tests.append(unit_test_3)

        function_3 = extract_single_function(filename, 'linear_search')
        test_function_3_loop = find_loop(function_3, 5)
        test_function_3_loop['name'] += 'Testing for loop in function linear_search'
        tests.append(test_function_3_loop)

        test_looks_linear = linear_looks_linear(function_3, 5)
        tests.append(test_looks_linear)

        unit_test_4 = run_unit_test('4.037', 4, 10)
        unit_test_4['name'] += 'Testing linear_search with arguments principal = 1000, DPR = 100/36.25/100,' \
                               ' p_life_of_loan = 1'
        tests.append(unit_test_4)
        unit_test_5 = run_unit_test('4.037', 5, 10)
        unit_test_5['name'] += 'Testing linear_search with arguments principal = 35000, DPR = 2.7/36.25/100,' \
                               ' p_life_of_loan = 5'

        tests.append(unit_test_5)

        function_4 = extract_single_function(filename, 'binary_search')
        test_function_4_loop = find_loop(function_4, 5)
        test_function_4_loop['name'] += 'Testing for loop in function binary_search'
        tests.append(test_function_4_loop)
        test_looks_binary = binary_looks_binary(function_4, 5)
        tests.append(test_looks_binary)
        #
        unit_test_6 = run_unit_test('4.037', 6, 10)
        unit_test_6['name'] += 'Testing binary_search with principal 1000, DPR = 100/36.25/100, life of loan = 1 ' \
                               'Expected 134.15 +/- 0.05<br>'
        tests.append(unit_test_6)

        unit_test_7 = run_unit_test('4.037', 7, 10)
        unit_test_7['name'] += 'Timed binary_search with principal 1000, DPR = 100/36.25/100, life of loan = 1 ' \
                               'and linear search with the same.  Binary search should be faster for this case.<br>'
        tests.append(unit_test_7)

        unit_test_8 = run_unit_test('4.037', 8, 10)
        unit_test_8['name'] += 'Testing print_report output, test 1'
        tests.append(unit_test_8)
        unit_test_9 = run_unit_test('4.037', 9, 10)
        tests.append(unit_test_9)

        # Find number of PEP8 errors and helps
        test_pep8 = pep8(filename, 14)
        tests.append(test_pep8)
        test_help = helps(filename, 10)
        tests.append(test_help)

        for test in tests:
            if test['pass']:
                score_info['score'] += test['points']

        score_info['finished_scoring'] = True
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)

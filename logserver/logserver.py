from flask import Flask, jsonify, render_template, request, url_for, redirect
import serial, time
import socket
import sys
import json, os
import re
import threading
import zipfile
import shutil
import hashlib
import getpass
from pathlib import Path

global gUsername
global gPassword
# timeout = 1
# socket.setdefaulttimeout(timeout)


app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Welcome %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


@app.route('/')
@app.route('/<name>')
def indexx(name=None):
    # return redirect(url_for('login'))
    # return render_template("index.html", gUsername="testname")
    return redirect(url_for('log_page'))


@app.route('/log')
def log_page(gUsername=None):
    username = getpass.getuser()
    return render_template("log.html", gUsername=username)


'''
@app.route('/main', methods=['POST'])
def main_page():
    return render_template("main.html", error='*Wrong username or password!')
'''


@app.route('/signin', methods=['GET'])
def signin_form(error):
    return render_template("user.html", error=error)


@app.route('/login', methods=['GET'])
def login(error=''):
    return render_template("user.html", error=error)


@app.route('/login', methods=['POST'])
def signin(name=None):
    try:
        global gUsername
        global gPassword
        gUsername = request.form['username']
        gPassword = request.form['password']
    except:
        print('request.form[username] error')
        pass
    if request.form['username'] == 'service' and request.form['password'] == 'service':
        return render_template("main.html", gUsername=gUsername)
    elif request.form['username'] == 'admin' and request.form['password'] == 'admin':
        return render_template("log.html", gUsername=gUsername)
    #	return redirect(url_for("main", gUsername=gUsername))
    # return login('*Wrong username or password!')
    return render_template("user.html", error='*Wrong username or password!')


@app.route('/<filename>')
def download_log(filename):
    return ""


basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/upload_update_zip', methods=['post'])
def upload_update_zip():
    uzip = request.files.get('update_zip')
    username = request.form.get("name")
    path = basedir + "/static/"
    file_path = path + uzip.filename
    uzip.save(file_path)
    #    print ('上传头像成功，上传的用户是：'+username)
    print('upload has been successed by ' + username)
    #    return render_template('main.html')
    return build_response(200, None, None)


def build_response(code, msg, data):
    res = {
        "code": code
    }
    if code != 200:
        res["msg"] = msg
    else:
        res["data"] = data
    return jsonify(res)


@app.route('/download/<filename>', methods=["GET"])
def download_report(filename):
    try:
        dir_path = os.path.join("/home/jude/", 'app')
        #        file_name = "jq.js"
        return send_from_directory(dir_path, file_name, as_attachment=True)
    except Exception as e:
        return build_response(500, "Server error", None)
    return build_response(200, None, None)


@app.route('/up_file', methods=['GET', 'POST'])
def up_file():
    if request.method == "POST":
        file = request.files['file']

        filename = file.filename
        flist = filename.split('_')
        fmd5 = flist[len(flist) - 1].split('.')[0]
        if len(fmd5) != 32:
            return "Upgrade failed: Invalid file md5."
        unzippath = "/opt/frontier/run/"
        rc = unzippath + "frontier/scripts/skeleton/etc/rc.local"
        savepath = unzippath + filename
        try:
            file.save(savepath)
        except:
            return "Error:Save file failed!"
        # smd5 = GetFileMd5(savepath)
        smd5 = CalcMD5(savepath)
        if fmd5 == smd5:
            un_zip(savepath, unzippath)
            return "Upload succeed!"
        else:
            os.remove(savepath)
            return "Upgrade failed: Invalid check md5."


@app.route('/upload_log', methods=['GET', 'POST'])
def upload_log():
    if request.method == "POST":
        file = request.files['logname']
        print(str(file))
        filename = file.filename
        print(os.getcwd())
        log_dir = "log/"
        log_path = Path(log_dir)
        if log_path.is_dir():
            pass
        else:
            print("Create path log/ ")
            os.mkdir(log_dir)
        filename = log_dir + filename
        '''
        filePath = Path(filename)
        print (filename)
        print (filePath)
        if filePath.exists():
            os.remove(filePath)
            print ("log file is exist, remove it.")'''
        try:
            # file.save(filePath)
            file.save(filename)
        except:
            return "Error:Save log failed!"
        return "Upload success!"


if __name__ == "__main__":
    #    t = threading.Thread(name="seriali-"+COM232,target=serial_for_ip,daemon=False)
    #    t.start()
    print('web server start!!!')
    app.run(host="0.0.0.0", port=5000, debug=True)

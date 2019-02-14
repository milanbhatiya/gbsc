from project import app
from flask import Flask, render_template, request, url_for, session,redirect,flash


@app.route('/viewUsers')
def viewUsers():
    try:
        if session['sessionloginDict']['loginRole'] == 'admin':
            return render_template('admin/viewUsers.html')
        else:
            flash('Plese Login First ! ', 'danger')
            return redirect(url_for('loadLogin'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('loadLogin'))
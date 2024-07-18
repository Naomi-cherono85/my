from flask import Blueprint, render_template, render_template, request, redirect, url_for, flash


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/fitness')
def fitness():
    return render_template('fitness.html')

@bp.route('/fitness/<section>')
def fitness_section(section):
    # Assuming 'section' can be 'cardio', 'strength', 'flexibility', 'balance', 'core', etc.
    return render_template('fitness.html', section=section)


@bp.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/about/<section>')
def about_section(section):
    # Assuming 'section' can be 'our_mission', 'founders_story', etc.
    return render_template('about.html', section=section)

@bp.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@bp.route('/contact')
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Handle form submission
        flash('Thank you for your message! We will get back to you soon.')
        return redirect(url_for('main.contact'))
    return render_template('contact.html')
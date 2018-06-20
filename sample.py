

@users_blueprint.route('/signup', methods=["GET", "POST"])
def signup():
    form = UserForm()
    if request.method == "POST":
        if form.validate():
            try:
                new_user = User(
                    username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
                if form.image_url.data:
                    new_user.image_url = form.image_url.data
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
            except IntegrityError as e:
                flash({'text': "Username already taken", 'status': 'danger'})
                return render_template('users/signup.html', form=form)
            return redirect(url_for('root'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods=["GET", "POST"])
    def login():
        if current_user:
            return redirect(url_for('root'))
        form = LoginForm()
        if request.method == "POST":
            if form.validate():
                found_user = User.authenticate(form.username.data,
                form.password.data)
        if found_user:
            login_user(found_user)
            flash({
                'text': f"Hello, {found_user.username}!",
                'status': 'success'
            })
        return redirect(url_for('root'))
        flash({ 'text': "Invalid credentials.", 'status': 'danger' })
        return render_template('users/login.html', form = form)
        return render_template('users/login.html', form = form)
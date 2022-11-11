exports.postSignup = async (req, res) => {
    let username = req.body.username;
    let email = req.body.email;
    let password = req.body.password;
    let existingUser = await UserSchema.findOne({ email });
    if (existingUser == true) {
        let err = new Error(
            `${email} A user with that email has already registered.`,
        );

        err.status = 400;
        console.log(err);
        res.render('signup', {
            errorMessage: `${email} already taken. A user with that email has already registered.`,
        });
        return;
    }

    const user = new UserSchema({
        username: username,
        email: email,
        password: password,
    });
    user.save();

    res.redirect('/');
};
passport.use(new LocalStrategy(
function(username, password, done) {
User.findOne({username: username}, function(err, user) {
if (err) {return done(err); }
if (!user) {return done(null, false); }
if (!user.verifyPassword(password)) {return done(null, false); }
return done(null, user); }); }
));
done(null, user.id);
});
passport.deserializeUser(function(id, done) {
User.findById(id, function(err, user) {
done(err, user); });
});

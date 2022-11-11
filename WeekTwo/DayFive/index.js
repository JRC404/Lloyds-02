// npm i express-handlebars
const express = require('express');
const hbs = require('express-handlebars');
const path = require('path'); //TODO ADD THIS LINE!
const app = express();

app.use(express.static(path.join(__dirname, 'public')));
// use the public folder when accessing any files for the site

app.engine('.hbs', hbs.engine({
    defaultLayout: 'layout', // template file
    extname: 'hbs' // layout.hbs
}))

app.set('view engine', '.hbs');

app.get('/', async (req, res) => {
    res.render('index');
})

app.get('/about', async(req, res) => {
    res.render('about'); // display about.hbs
})

app.listen(3000, () => {
    console.log("I am listening. Always listening. Badwolf.")
})
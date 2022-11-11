# HTTP Methods

* Get, Post, Put / Patch, Delete make up the four CRUD operations
* CRUD:
    * Create
    * Read
    * Update
    * Delete

## Get - Read

* In our example, we used get to ask the server to retrieve data for us
    * We asked the server: app.get('/about')
    * This is asking the server at the location /about to do something for us
    * We asked our server to display about.hbs with the following code:
```js
app.get('/about', async(req, res) => {
    res.render('about'); // display about.hbs
})
```

## Post - Create

* Sends information to the server to be checked
* Think about a login form for a website:
    * We send the username 
    * We send the password
* The server then checks the information and does something with it
    * If the user information is correct, load profile
    * If the user information is incorrect, reload the signin form or go to signup

## Put / Patch - Update

* Update method is a way to update records on a server / database
* Jehcub == Andrew

* Treat update with caution as it doesn't have a safety check, it will just update without someone else's approval

## Delete

* Delete request that should be treated with absolute caution
* Delete, by default, doesn't have verification / validation of what you're trying to do:
    * If you are trying to delete 10,000 records, it won't check if you are sure... it will just do it!
# Git

* Version Control
* Repository access for multiple users / developers / engineers

## Github

* Lloyds use Github Enterprise for their Git access
* Gitlabs, Github, Bitbucket, Azure Devops, AWS Dev and many more...

* GHE (Github Enterprise) uses a secure, controlled location created by Github and maintained by Lloyds
* Only people at Lloyds can access your area / space

## Uploading to a blank repository on GHE

* If you have just created a repository without a readme (Try not to create one...) then we have the following instructions:
    0. Create a folder in your documents / desktop and create a file of your choice - Only do this if you don't alreday have a folder you want to upload!
    1. Open the folder in Integrated terminal / bash and run the following commands:
    ```
    git status -> fatal not a git repository
    git init -> initialized empty repository
    git status -> On branch main: No commits yet

    ```
    2. We need to tell Git which files we want to upload. 'git add .' will get all files ready to be uploaded 
    ```
    git add .
    OR
    git add index.js index.html readme.md
    THEN
    git status
    ```
    3. We now need to write a message for our commit
    ```
    git commit -m "My first commit"
    ```


## Notes for Repositories

* Don't put spaces in your repository names!
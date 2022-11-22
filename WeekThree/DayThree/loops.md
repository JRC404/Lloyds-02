# JavaScript Loops

* While Loop
* Do-while Loop
* For Loop
* For of Loop

## For Loop

* A for loop requires 3 things:
    * Initialisation
    ```js
    let i = 0;
    ```
    * Condition
    ```js
    i < artists.length;
    ```
    * Iteration
    ```js
    i++;
    ```

### Example of For Loop
```js
let artists = ["Lady Gaga", "James Blunt", "Miley Cyrus", "Adele"];

for(let i = 0; i < artists.length; i++) {
    console.log(artists[i]);
}
```
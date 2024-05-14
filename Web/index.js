// First JS code
// console.log('Hello world!');

/* let name = 'String';
console.log(name);

let firstName = 'Bhogaraju'; // Camel notation
let lastName = 'SSK' */

/* let interestRate = 0.3;
interestRate = 1;

console.log(interestRate); */

/* const interestRate = 0.3;
interestRate = 1;

'const' cannot be redefinded
'let' can be redefined

console.log(interestRate); */

/* let name = 'Elon Musk'; // String Literal
let age = 19; // Number Literal
let isAssigned = true; // Boolean Literal
let firstName; // Undefined Literal
let selectColor = null; // NULL Literal */

/* let person = {
    name: 'Krish',
    age: 19
};

// Dot notation
person.name = 'Mosh';

// Bracket Notation
let selection = 'name';
person[selection] = 'Mosh2';

console.log(person['name']); */

/* let selectColor = [];
selectColor = ['blue', 'red'];

selectColor[2] = 'green';

console.log(selectColor); */

/* // Performing a task
function greet(firstName, lastName) {
    console.log('Hello ' + firstName + ' ' + lastName);
}

// Calculating a value
function getSquare(number){
    return number * number;
}

// greet('Shanmukha', 'Sri Krishna');
// greet('Ram');

let sq = getSquare(2);
console.log(sq); */

// let userName = window.prompt("What's your name? ");
// console.log(userName);

/* let userName;

document.getElementById('mySubmit').onclick = function(){
    userName = document.getElementById('myText').value;
    // console.log(userName);
    document.getElementById('myH1').textContent = `Hello ${userName}`;
} */



// This part is only needed for OELP
function myTest(){
    let userName = document.getElementById('myText');
    let message = document.getElementById('message');

    message.innerHTML = 'Test lol ' + userName.value;
}
const prompt = require("prompt-sync")();

function main(){
    var upperChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var lowerChars = "abcdefghijklmnopqrstuvwxyz";
    var digits = "1234567890";
    var symbols = "!@#$%^&*()-=+,./<>?";

    var possibleChars = upperChars + lowerChars + digits + symbols;
    var length = parseInt(prompt("Please enter how long you want the password to be: "));
    
    var password = "";
    while(0!=length){
        password += possibleChars[Math.floor(Math.random() * possibleChars.length)];
        length -= 1;
    }

    console.log(`Generated Password is: ${password}`);
}
main()
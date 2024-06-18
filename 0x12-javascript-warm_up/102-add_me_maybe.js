#!/usr/bin/node
// function that increment and calls a function

function addMeMaybe(number, theFunction){
	number++;
	return theFunction(number);

}

module.exports = {
   addMeMaybe: addMeMaybe
};

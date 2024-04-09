#!/usr/bin/node
//  function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((acc, curr) => {
    return (curr === searchElement) ? ++acc : acc;
  }, 0);
  return count;
};

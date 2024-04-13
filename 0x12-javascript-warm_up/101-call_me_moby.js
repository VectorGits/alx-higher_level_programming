#!/usr/bin/node

exports.callMeMoby = function (a, theFunction) {
	for (let x = 0; x < a; x++) {
		theFunction();
	}
}

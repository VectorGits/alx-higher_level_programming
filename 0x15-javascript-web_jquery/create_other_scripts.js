const fs = require('fs');

for (let x = 2; x <= 9; x++) {
	const filename = `${x}-script.js`;
	fs.writeFile(filename, `console.log('Javascript is amazing');`, (err) => {
		if (err) {
			console.log(err);
		} else {
			console.log(`File ${filename} was created`);
		}
	});
}
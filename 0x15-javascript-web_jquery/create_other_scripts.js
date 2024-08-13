const fs = require('fs');

for (let x = 3; x <= 9; x++) {
	const filename = `${x}-main.html`;
	fs.writeFile(filename, `console.log('Javascript is amazing');`, (err) => {
		if (err) {
			console.log(err);
		} else {
			console.log(`File ${filename} was created`);
		}
	});
}
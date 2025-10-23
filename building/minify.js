import { transform, bundle } from 'lightningcss';
import fs from 'fs-extra';
import path from 'path';

let inputDir = 'src/css'
let outputDir = 'dist/css'

{
	let inputFile = inputDir + '/style.css';
	let outputFile = outputDir + '/style.css';

	// const content = await fs.readFile(inputFile, 'utf8');

	let { code, map } = bundle({
		filename: inputFile,
		// filename: 'style.css',
		// code: Buffer.from(content),
		minify: true,
		targets: {
			chrome: 95,
		},
		sourceMap: false,
	});

	// Ensure the destination directory exists
	await fs.ensureDir(path.dirname(outputFile));

	// Write the bundle content to the output file
	await fs.writeFile(outputFile, code, 'utf8');
	console.log(`Minified CSS created successfully at ${outputFile}`);

}

{
	let inputFile = inputDir + '/pages/homepage.css';
	let outputFile = outputDir + '/pages/homepage.css';

	// const content = await fs.readFile(inputFile, 'utf8');

	let { code, map } = bundle({
		filename: inputFile,
		// code: Buffer.from(content),
		minify: true,
		targets: {
			chrome: 95,
		},
		sourceMap: false,
	});

	// Ensure the destination directory exists
	await fs.ensureDir(path.dirname(outputFile));

	// Write the bundle content to the output file
	await fs.writeFile(outputFile, code, 'utf8');
	console.log(`Minified CSS created successfully at ${outputFile}`);

}

{
	let inputFile = inputDir + '/header-v3.css';
	let outputFile = outputDir + '/header-v3.css';

	// const content = await fs.readFile(inputFile, 'utf8');

	let { code, map } = bundle({
		filename: inputFile,
		// code: Buffer.from(content),
		minify: true,
		targets: {
			chrome: 95,
		},
		sourceMap: false,
	});

	// Ensure the destination directory exists
	await fs.ensureDir(path.dirname(outputFile));

	// Write the bundle content to the output file
	await fs.writeFile(outputFile, code, 'utf8');
	console.log(`Minified CSS created successfully at ${outputFile}`);

}

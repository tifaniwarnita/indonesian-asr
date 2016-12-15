var child_process = require('child_process');

// exec: spawns a shell.
child_process.exec('ping google.com', function(error, stdout, stderr){
	console.log(stdout);
});

// execFile: executes a file with the specified arguments
child_process.execFile('ls', ['-lah', '/tmp'], function(error, stdout, stderr){
	console.log(stdout);
});
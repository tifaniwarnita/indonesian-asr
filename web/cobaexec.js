var child_process = require('child_process');

// exec: spawns a shell.
child_process.exec('julius -input rawfile -filelist file.txt -C decoder-conf-trifon', function(error, stdout, stderr){
	console.log(stdout);
});

// execFile: executes a file with the specified arguments
/*child_process.execFile('ls', ['-lah', '/tmp'], function(error, stdout, stderr){
	console.log(stdout);
});*/

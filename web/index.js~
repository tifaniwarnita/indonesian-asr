var express = require('express');
var BinaryServer = require('binaryjs').BinaryServer;
var fs = require('fs');
var wav = require('wav');
var child_process = require('child_process');

var port = 8800;
var outFile = 'demo.wav';
var app = express();

app.set('views', __dirname + '/template');
app.set('view engine', 'jade');
app.engine('jade', require('jade').__express);
app.use(express.static(__dirname + '/public'))

app.get('/', function(req, res){
  res.render('index', {output: req.params.output});
});

app.listen(port);

console.log('server open on port ' + port);

binaryServer = BinaryServer({port: 9001});

binaryServer.on('connection', function(client) {
  console.log('new connection');

  var fileWriter = new wav.FileWriter(outFile, {
    channels: 1,
    sampleRate: 48000,
    bitDepth: 16
  });

  client.on('stream', function(stream, meta) {
    console.log('new stream');
    stream.pipe(fileWriter);

    stream.on('end', function() {
      fileWriter.end();
      console.log('wrote to file ' + outFile);
	child_process.exec('julius -input rawfile -filelist file.txt -C decoder-conf-trifon', function(error, stdout, stderr){
	console.log(stdout);
	var out= stdout.substr(stdout.indexOf("phseq1")+7);
	var out1 = out.substr(0,out.indexOf("cmscore1"));
	var output = out1.replace(/ /g, '').replace(/@/g, "e").replace(new RegExp('sil','g'), " ").replace(/\|/g, " ");
	stream.write(output);
      });
    });
	
  });
});

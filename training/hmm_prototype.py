"""
HMM Training: #1 Creating Prototype
The first step in HMM training is to define a prototype model.
Please look at HTKBook chapter 3.2.1

References: https://github.com/syhw/timit_tools
"""

import sys, util, subprocess

USAGE = """
Usage:
	python hmm_prototype.py [$script_folder] [--debug]

Example:
	python hmm_prototype.py files

What You Need:
	$script_folder/train.scp
"""

header = "~o <VecSize> 39 <"
body = """
~h "proto"
  <BeginHMM>
    <NumStates> 5
    <State> 2
      <Mean> 39
        0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
      <Variance> 39
        1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
    <State> 3
      <Mean> 39
        0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
      <Variance> 39
        1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
    <State> 4
      <Mean> 39
        0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
      <Variance> 39
        1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0
    <TransP> 5
        0.0 1.0 0.0 0.0 0.0
        0.0 0.6 0.4 0.0 0.0
        0.0 0.0 0.6 0.4 0.0
        0.0 0.0 0.0 0.7 0.3
        0.0 0.0 0.0 0.0 0.0
  <EndHMM>
"""

if len(sys.argv) > 1:
	if '--help' in sys.argv:
		print util.GROUP_NAME
		print USAGE
		sys.exit(0)

	l = filter(lambda x: not '--' in x[0:2], sys.argv)
	if len(l) > 1:
		script_folder = l[1].rstrip('/')
		with open(script_folder + '/train.scp') as f:
			process = subprocess.Popen(['HList', '-t', f.readline().strip('\n')], stdout=subprocess.PIPE)
			for line in process.stdout:
				if "Sample Kind:" in line:
					header += line.rstrip('\n').split(':')[-1].strip() + '>'
			with open(script_folder + '/proto.hmm', 'w') as wf:
				wf.write(header + '\n')
				wf.write(body)
else:
	print 'Add --help for help'
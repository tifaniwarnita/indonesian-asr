# Indonesian Automatic Speech Recognition

1. Create MFCC files
  
  `python feature_extraction.py dataset/train`

2. Create Monophone Model
  1. Prototype
  
    `python hmm_prototype.py files`
    
  2. Wordlist 
    
    `HDMan -m -w wordlist/wlist -n monophones1 -l dlog dict wordlist/lexicon.txt` (GAUSAH LAGI)
    
    `HLEd -l * -d wordlist/dict -i wordlist/phones0.mlf wordlist/mkphones0.led wordlist/words_sanitize.mlf` (INI IYA)

  3. HMM0-Init
    `HCompV -C config/conf-train -f 0.01 -m -S files/train.scp -M hmm0 files/proto.hmm`
   
  4. HMM-0 - HMM-7    
    `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm0/macros -H hmm0/hmmdefs -M hmm1 wordlist/monophones0`
    
    `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm1/macros -H hmm1/hmmdefs -M hmm2 wordlist/monophones0`
    
    `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm2/macros -H hmm2/hmmdefs -M hmm3 wordlist/monophones0`
    
    `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm3/macros -H hmm3/hmmdefs -M hmm4 wordlist/monophones0`
    
    `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm4/macros -H hmm4/hmmdefs -M hmm5 wordlist/monophones0`
    
    `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm5/macros -H hmm5/hmmdefs -M hmm6 wordlist/monophones0`
    
    `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm6/macros -H hmm6/hmmdefs -M hmm7 wordlist/monophones0`

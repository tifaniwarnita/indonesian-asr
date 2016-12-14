# Indonesian Automatic Speech Recognition

`cd training`

1. Create MFCC files
  
  `python feature_extraction.py dataset/train`

2. Create Monophone Model
  1. Prototype
  
    `python hmm_prototype.py files`
    
  2. Wordlist 
    
    `HDMan -m -w wordlist/wlist -n monophones1 -l dlog dict wordlist/lexicon.txt` (GAUSAH LAGI)
    
    `HLEd -l * -d wordlist/dict -i wordlist/phones0.mlf wordlist/mkphones0.led wordlist/words_sanitize.mlf` (INI IYA)

  3. HMM0-Init
  
    `mkdir hmm0`
    
    `HCompV -C config/conf-train -f 0.01 -m -S files/train.scp -M hmm0 files/proto.hmm`
   
  4. Create Model
  
      1. HMM-1
        
        `mkdir hmm1`
        
        `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm0/macros -H hmm0/hmmdefs -M hmm1 wordlist/monophones0`
    
      2. HMM-2
        
        `mkdir hmm2`
    
        `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm1/macros -H hmm1/hmmdefs -M hmm2 wordlist/monophones0`
    
      3. HMM-3
      
        `mkdir hmm3`

        `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm2/macros -H hmm2/hmmdefs -M hmm3 wordlist/monophones0`
    
      4. HMM-4
      
        `mkdir hmm4`
        
        `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm3/macros -H hmm3/hmmdefs -M hmm4 wordlist/monophones0`
    
      5. HMM-5
      
        `mkdir hmm5`
        
        `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm4/macros -H hmm4/hmmdefs -M hmm5 wordlist/monophones0`
    
      6. HMM-6
        
        `mkdir hmm6`

        `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm5/macros -H hmm5/hmmdefs -M hmm6 wordlist/monophones0`
    
      7. HMM-7
      
        `mkdir hmm7`
        
        `HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 1000.0 -S files/train_sanitize.scp -H hmm6/macros -H hmm6/hmmdefs -M hmm7 wordlist/monophones0`
        
        
    
    5. Silence
    
       1. Copy directory hmm7 to hmm8
          
          `xcopy hmm7 hmm8`
             
       2. Add `~h "sp"` and change `<TRANSP> 5` to 
          
       2. HHed
       
          `mkdir hmm10`
          
          `HHEd -H hmm9/macros -H hmm9/hmmdefs -M hmm10 wordlist/sil.hed wordlist/monophones1`

    
    --- disini adalagi tapi lupa ---
    
    HERest -A -D -T 1 -C config/conf-train -I wordlist/phones0.mlf -t 250.0 150.0 3000.0 -S files/train_sanitize.scp -H hmm9/macros -H hmm9/hmmdefs -M hmm10 wordlist/monophones1

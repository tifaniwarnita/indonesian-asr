# Indonesian Automatic Speech Recognition

1. Create MFCC files
  
  `python feature_extraction.py dataset/train`

2. Create Monophone Model
  1. Prototype
  
    `python hmm_prototype.py files`
    
    `HCompV -C config/conf-train -f 0.01 -m -S files/train.scp -M hmm0 files/proto.hmm`
    
    `HERest -C config/conf-train -I phones0.mlf -t 250.0 150.0 1000.0 -S files/train.scp -H hmm0/macros -H hmm0/hmmdefs -M hmm1 monophones0`
    

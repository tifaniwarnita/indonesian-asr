# Indonesian Automatic Speech Recognition

`cd training`

1. Create MFCC files
  
  `python feature_extraction.py dataset/train`

2. Create Monophone Model
  1. Prototype
  
    `python hmm_prototype.py files` (SEKIP AJA GAPAPA SIH)
    
  2. Wordlist 
    
    `HDMan -m -w wordlist/wlist -n monophones1 -l dlog dict wordlist/indonesian.lex`

    Edit "dict" by adding
    SENT-END    sil
    SENT-START  sil
    silence     sil

    at the correct position (remain sorted)

    Jalankan `python mlf.py`

    Create following edit script "mkphones0.led" containing:
    EX
    IS sil sil
    DE sp
    
    Window: `HLEd -l * -d wordlist/dict -i wordlist/phones0.mlf wordlist/mkphones0.led wordlist/words_sanitize.mlf` (INI IYA)
    
    Ubuntu: `HLEd -l '*' -d wordlist/dict -i wordlist/phones0.mlf wordlist/mkphones0.led wordlist/words_sanitize.mlf` (INI IYA)

    (disini bakal kobam dan ketahuan mana aja kata-kata yang ga ada di wlist dan dict, jadi harus crosscheck sampe bener)
    (ERROR [+6550]  LoadHTKLabels: Junk at end of HTK transcription -> jangan lupa hapus spasi doang 1 line, hapus dengan regex `^\n` )
    (ERROR [+6550]  LoadHTKList: Label Name Expected -> ini karena ada yang angka)
    (ERROR [+1232]  NumParts: Cannot find word %s in dictionary -> mangat nguli)

    beres semua error diatas,
    `python sanitizer.py`
    buat ngebersihin si mlf dan scp dari suara yang samsek ga ada di dict
    bakal ngeluarin scp dan mlf yang _sanitize

  3. HMM0-Init
  
    `mkdir hmm0`
    
    `HCompV -C config/conf-train -f 0.01 -m -S files/train_sanitize.scp -M hmm0 files/proto.hmm`

    Create monophones0 dengan menggunakan monophones1 tanpa menggunakan entri 'sp'
    Lalu bikin file hmmdefs dan macros
   
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
             
       2. Copy and paste the “sil” model and rename the new one “sp”(don't delete your old "sil" model, you will need it - just make a copy of it)
       
          Remove state 2 and 4 from new “sp” model (i.e. keep 'centre state' of old “sil” model in new “sp” model)
          
          change <NUMSTATES> to 3
          
          change <STATE> to 2
          
          change <TRANSP> to 3
          
          change matrix in <TRANSP> to 3 by 3 array
          
          change numbers in matrix as follows:
           `0.0 1.0 0.0
           0.0 0.9 0.1
           0.0 0.0 0.0`
          
       2. HHed
           Create the "sil.hed" script containing:
            `AT 2 4 0.2 {sil.transP}
            AT 4 2 0.2 {sil.transP}
            AT 1 3 0.3 {sp.transP}
            TI silst {sil.state[3],sp.state[2]}`
       
          `mkdir hmm9`
          
          `HHEd -H hmm8/macros -H hmm8/hmmdefs -M hmm9 wordlist/sil.hed wordlist/monophones1`
          
       3. HRest 2x
       
          Windows: `HLEd -l * -d wordlist/dict -i wordlist/phones1.mlf wordlist/mkphones1.led wordlist/words_sanitize.mlf`
          
          Ubuntu: `HLEd -l '*' -d wordlist/dict -i wordlist/phones1.mlf wordlist/mkphones1.led wordlist/words_sanitize.mlf`
          
          `mkdir hmm10`
          
          `HERest -A -D -T 1 -C config/conf-train  -I wordlist/phones1.mlf -t 250.0 150.0 3000.0 -S files/train_sanitize.scp -H hmm9/macros -H  hmm9/hmmdefs -M hmm10 wordlist/monophones1`
          
          `mkdir hmm11`
          
          `HERest -A -D -T 1 -C config/conf-train  -I wordlist/phones1.mlf -t 250.0 150.0 3000.0 -S files/train_sanitize.scp -H hmm10/macros -H  hmm10/hmmdefs -M hmm11 wordlist/monophones1`
          
    6. Realigning the data
       
       1. HVite
        
          Bagian ini kata voxforge `1000.0` tapi kalau segitu maupun `3000.0` ada label yang hilang, jadi aku ubah `5000.0`.
          
          Windows: `HVite -A -D -T 1 -l * -o SWT -b SENT-END -C config/conf-train -H hmm11/macros -H hmm11/hmmdefs -i wordlist/aligned.mlf -m -t 250.0 150.0 5000.0 -y lab -a -I wordlist/words_sanitize.mlf -S files/train_sanitize.scp wordlist/dict wordlist/monophones1> HVite_log`
          
          Ubuntu: `HVite -A -D -T 1 -l '*' -o SWT -b SENT-END -C config/conf-train -H hmm11/macros -H hmm11/hmmdefs -i wordlist/aligned.mlf -m -t 250.0 150.0 5000.0 -y lab -a -I wordlist/words_sanitize.mlf -S files/train_sanitize.scp wordlist/dict wordlist/monophones1> HVite_log`

       2. HRest 999999x :'(
       
          `mkdir hmm12`
          
          `HERest -A -D -T 1 -C config/conf-train  -I wordlist/aligned.mlf -t 250.0 150.0 3000.0 -S files/train_sanitize.scp -H hmm11/macros -H  hmm11/hmmdefs -M hmm12 wordlist/monophones1`
          
          `mkdir hmm13`
          
          `HERest -A -D -T 1 -C config/conf-train  -I wordlist/aligned.mlf -t 250.0 150.0 3000.0 -S files/train_sanitize.scp -H hmm12/macros -H  hmm12/hmmdefs -M hmm13 wordlist/monophones1`
        
        
`cd ..`

`mkdir decoder`

`cd decoder` (`indonesian-asr/decoder`)

    7. Recognizer evaluation
    
       1. Install Julius (http://julius.osdn.jp/en_index.php)
       2. Download SLRIM (http://www.speech.sri.com/projects/srilm/)
       3. Buat LM:
       4. Buat AM: `mkbinhmm -htkconf ../training/config/conf-train ../training/hmm12/hmmdefs julius.am`
    
        Install HDecode: `nmake /f htk_hdecode_nt.mkf all`
       
        `mkdir result`
        
        `HDecode -A -D -T 1 -H hmm13/macros -H hmm13/hmmdefs -C config/conf-test -S files/test_sanitize.scp -l * -i result/recout.mlf -w lm/lm.arpa -p 0.0 -s 5.0 wordlist/dict wordlist/monophones1`
        
        Windows: `HVite -H hmm13/macros -H hmm13/hmmdefs -S files/test_sanitize.scp -l * -i result/recout.mlf -w ../lm/lm.arpa -p 0.0 -s 5.0 wordlist/dict wordlist/monophones1`

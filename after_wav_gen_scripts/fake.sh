#工作事故，伪造 speak 结构 ABC12_123.wav
#

spkid=0
uttid=0
for f in CA/*.wav; do

    trn=$f.trn

    if [ $uttid -gt 999 ]
    then
      spkid=$[spkid + 1]
      uttid=0
    fi


    printf -v n_wav "Z%d_%d.wav" $spkid $uttid
    n_trn=$n_wav.trn
    echo $n_wav
    echo $n_trn

    cp $f CA_fake/$n_wav
    cp $trn CA_fake/$n_trn


    uttid=$[uttid + 1]
done

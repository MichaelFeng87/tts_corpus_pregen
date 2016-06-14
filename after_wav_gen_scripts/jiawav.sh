#工作事故，thchs30的格式是 xxxx.wav   xxxx.wav.trn，所以把 ca 的 trn之前加 wav.

for f in CA/*.trn; do

    trn=${f%.trn}.wav.trn
    echo $trn
    mv $f $trn

done
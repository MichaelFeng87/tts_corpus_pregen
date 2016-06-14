rm -rf ca_dev
rm -rf ca_test
rm -rf ca_train
mkdir ca_dev
mkdir ca_test
mkdir ca_train
for f in CA_fake/*.wav; do

    trn=$f.trn
    echo $trn
    va=$[$RANDOM%100]
    if [ $va -lt 80 ]
    then
        cp $f ca_train/
        cp $trn ca_train/

    elif [ $va -lt 95 ]
    then
        cp $f ca_test/
        cp $trn ca_test/

    else
        cp $f ca_dev/
        cp $trn ca_dev/
    fi

done

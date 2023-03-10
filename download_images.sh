for FILE in image-links/*;
do
        mkdir "/home/ubuntu/dataset/$FILE"
        cd "/home/ubuntu/dataset/$FILE"
        echo "|||||||||>>>>>>>>>> Downloading: $FILE"
        aria2c -x 10 -i "/root/$FILE"
        echo "|||||||||>>>>>>>>>> Downloading: $FILE COMPLETE <<<<<<<<<<<<<<<<<"
        cd
done
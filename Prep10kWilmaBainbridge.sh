
# Open and unload 10kfacesWilmaBainbridge dataset
# need 10kfacesWilmaBainbridge dataset to be in the same file
unzip 10kfacesWilmaBainbridge.zip
mv "10k US Adult Faces Database" wBainbridge
cd wBainbridge
rm *.txt
pwd
mv "/Users/Alex/Google Drive/2017Fall/IW/wBainbridge/Face Images" ..
cd ..
mv "Face Images" wBainbridgeGTruth
rm -r wBainbridge
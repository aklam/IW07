#download data and decompress it
wget https://s3.us-east-2.amazonaws.com/iw07alexlamfacesdataset/data.zip
unzip data.zip
rm data.zip

wget https://s3.us-east-2.amazonaws.com/iw07alexlamfacesdataset/faces96.zip
unzip faces96.zip
rm faces96.zip
mv faces96 EssexFaces


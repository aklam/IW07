#move ec2setup directory to root
cp -r ec2setup ~

#download data and decompress it
wget https://s3.us-east-2.amazonaws.com/iw07alexlamfacesdataset/data.zip

bash Prep10kWilmaBainbridge.sh
bash PrepsomeData.sh

#wget https://s3.us-east-2.amazonaws.com/iw07alexlamfacesdataset/faces96.zip
#unzip faces96.zip
#rm faces96.zip
#mv faces96 EssexFaces


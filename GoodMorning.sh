#move ec2setup directory to root
#cp -r ec2setup ~

#download data and decompress it
wget https://s3.us-east-2.amazonaws.com/iw07alexlamfacesdataset/data.zip


bash PrepsomeData.sh


#### FOR SCALING ####
#bash Prep10kWilmaBainbridge.sh

####combine directories into All_Images
#mkdir All_images
#mv -v data_images/* All_images/
#xargs -0 mv -v WB_images/* All_images/


python ExposeImages.py data_images


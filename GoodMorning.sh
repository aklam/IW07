#download data and decompress it
wget https://s3.us-east-2.amazonaws.com/iw07alexlamfacesdataset/data.zip
unzip data.zip
rm data.zip


#copy images from african directory
cd data/african/imgs
cp *.png ../../
cd ../../

#copy images from flickr directory
cd flickr2/imgs
cp *.png ../../
cd ../../

##copy images from martin
cd martin/imgs
cp *.png ../../
cd ../../

echo "done copying"
rm -r african eyes flickr2 kelco martin mit2 platon samples

((i=0))
for d in * ; do 
	newname="data${i}.png"
	mv $d $newname
	(( i++ ))
done



#wget https://s3.us-east-2.amazonaws.com/iw07alexlamfacesdataset/faces96.zip
#unzip faces96.zip
#rm faces96.zip
#mv faces96 EssexFaces


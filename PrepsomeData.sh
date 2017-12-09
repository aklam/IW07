#Must have data.zip in same directory

unzip data.zip

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

rm data122.png

cd ../
mv data data_images
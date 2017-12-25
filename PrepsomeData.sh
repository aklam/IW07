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

rm data10.png
rm data34.png
rm data44.png
rm data55.png
rm data56.png
rm data57.png
rm data63.png
rm data81.png
rm data98.png
rm data115.png
rm data122.png
rm data131.png
rm data134.png
rm data135.png
rm data138.png
rm data140.png
rm data141.png

cd ../
mv data data_images
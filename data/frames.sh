# echo "Enter URL":
# read URL
# echo "Enter dir name":
# read DIRNAME
# echo "Enter start time":
# read START
# echo "Enter end time (0 if not wanted)":
# read END

URL=$1
DIRNAME=$2
START=$3
END=$4

mkdir $DIRNAME
cd $DIRNAME

yt-dlp -o "VOD.%(ext)s" $URL

FILENAME=$( ls | grep VOD )

mkdir frames

if START == null || END == null
then
    ffmpeg -i $FILENAME -r 0.2 frames/frame%04d.jpg
else
    if END==0
    then
        ffmpeg -ss $START -i $FILENAME -r 0.2 frames/frame%04d.jpg
    else
        ffmpeg -ss $START -to $END -i $FILENAME -r 0.2 frames/frame%04d.jpg
    fi
fi
rm $FILENAME

python3 ../masking.py
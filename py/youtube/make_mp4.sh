ffmpeg \
	-r 30 \
	-pattern_type glob -i "frame*.jpg" \
	-c:v libx264 -crf 30 -pix_fmt yuv420p  \
	out.mp4

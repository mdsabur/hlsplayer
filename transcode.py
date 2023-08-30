import os
from pyffmpeg import FFmpeg

# Input video file
input_file = 'sample.mp4'

# Output directory for segmented video files
output_dir = 'output_hls'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Command for FFmpeg to generate adaptive HLS
ffmpeg_command = (
    f'ffmpeg -i {input_file} '
    f'-c:v libx264 -c:a aac -strict -2 '
    f'-hls_list_size 0 '
    f'{output_dir}/playlist.m3u8'
)

# Run the FFmpeg command
os.system(ffmpeg_command)

print("Adaptive streaming files generated in:", output_dir)

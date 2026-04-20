#!/bin/bash
# Compress videos to web-friendly MP4 (H.264, max 720p height, CRF 28, AAC 96k)
set -e
IN="/c/Users/shaha/Downloads"
OUT="C:/Users/shaha/OneDrive/מסמכים/GitHub/JARVIS/workspace/freshbiz/videos"

declare -A MAP
MAP["IMG_2623.MOV"]="t-yuval-peretz.mp4"
MAP["IMG_2622.MOV"]="t-yoad-kachal.mp4"
MAP["IMG_2547.MP4"]="t-roei-ovadia.mp4"
MAP["IMG_2544.MP4"]="t-yuval-tsarfati.mp4"
MAP["IMG_2549.MOV"]="t-tamir-damri.mp4"
MAP["IMG_7468.MOV"]="atmosphere.mp4"
MAP["IMG_0292.MP4"]="explainer.mp4"

for src in "${!MAP[@]}"; do
  dst="${MAP[$src]}"
  infile="$IN/$src"
  outfile="$OUT/$dst"
  if [ ! -f "$infile" ]; then
    echo "MISS: $infile"
    continue
  fi
  if [ -f "$outfile" ]; then
    echo "skip existing: $dst"
    continue
  fi
  echo "=== $src -> $dst ==="
  ffmpeg -y -i "$infile" \
    -vf "scale=-2:'min(720,ih)'" \
    -c:v libx264 -preset medium -crf 28 \
    -c:a aac -b:a 96k \
    -movflags +faststart \
    -hide_banner -loglevel warning \
    "$outfile" 2>&1 | tail -5
done

echo "--- done ---"
ls -lh "$OUT"

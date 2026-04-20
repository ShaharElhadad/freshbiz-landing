#!/bin/bash
set -e
V="C:/Users/shaha/OneDrive/מסמכים/GitHub/JARVIS/workspace/freshbiz/videos"
P="C:/Users/shaha/OneDrive/מסמכים/GitHub/JARVIS/workspace/freshbiz/images/posters"
mkdir -p "$P"

for f in "$V"/*.mp4; do
  name=$(basename "$f" .mp4)
  out="$P/$name.jpg"
  ffmpeg -y -ss 00:00:00.5 -i "$f" -frames:v 1 -q:v 3 -hide_banner -loglevel warning "$out" 2>&1 | tail -2
  echo "poster: $name.jpg"
done

ls -lh "$P"

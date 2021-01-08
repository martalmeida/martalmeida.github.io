
im=$1
convert $im -thumbnail 150x75   -unsharp 0x.5  thumb_${im}
convert $im -thumbnail 150x45   -unsharp 0x.5  sthumb_${im}

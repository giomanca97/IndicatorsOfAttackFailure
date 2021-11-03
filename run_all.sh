for MODEL in 0 13
do
    echo "Computing indicators for model $MODEL"
    python -m src.ioaf_demo --model $MODEL --samples 2
done
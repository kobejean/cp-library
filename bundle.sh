for file in test/*; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        oj-bundle "$file" > "output/${file}"
    fi
done
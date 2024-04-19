#!/bin/sh

rename_folders() {
    local search_dir="$1"

    for entry in "$search_dir"/*; do
        if [ -d "$entry" ]; then
            folder_name=$(basename "$entry")
            if [[ "$folder_name" == *" "* ]]; then
                new_folder_name=$(echo "$folder_name" | tr ' ' '-')
                mv "$entry" "$search_dir/$new_folder_name"
                echo "Renamed folder: $entry -> $search_dir/$new_folder_name"
            fi
            rename_folders "$entry"
        fi
    done
}

rename_folders .

echo "Folder renaming completed."
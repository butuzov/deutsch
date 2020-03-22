DEUTSCH_DIR="$(pwd)"

if [[ $PATH != *$DEUTSCH_DIR* ]]; then
    echo "Deutsch Aktiviert"

    PATH="$DEUTSCH_DIR/bin:$PATH"
    export PATH
    source .de/bin/activate
else
    echo "Deutsch Deaktiviert"
    deactivate

    PATH="${PATH/$DEUTSCH_DIR\/bin:/}"
    export PATH
fi





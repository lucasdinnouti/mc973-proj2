FOLDER="$1"
for FILE in $FOLDER/*
do
	riscv64-unknown-elf-objcopy -O binary -j .text -j .rodata $FILE $FILE.bin
	python3 main.py $FILE.bin
done
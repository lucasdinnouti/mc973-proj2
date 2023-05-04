FOLDER="$1"
for FILE in $FOLDER/*.riscv
do
	riscv64-linux-gnu-objcopy -O binary -j .text -j .rodata $FILE $FILE.bin
	python3 main.py $FILE.bin
done
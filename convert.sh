for FILE in ./test/*.riscv
do
	riscv64-linux-gnu-objcopy -O binary -j .text -j .rodata $FILE $FILE.bin
done